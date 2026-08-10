import argparse
import datetime
import json
import sys
from pathlib import Path

try:
    from apcp_core_files import (
        CORE_FILES,
        DEFAULT_PROFILE,
        available_profiles,
        get_profile_files,
        normalize_profile,
        profile_description,
        unique_files,
    )
except ImportError as exc:
    raise SystemExit(
        "ERROR: scripts/apcp_core_files.py is required next to apcp-gather.py."
    ) from exc


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


ROOT = Path(__file__).resolve().parents[1]
CONFIG_FILENAMES = ("apcp-profile.json", ".apcp-profile.json")


def fail(message):
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def safe_relative_path(relative):
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Path must stay inside the project root: {relative}")
    return path.as_posix()


def find_config(root, config_path=None):
    if config_path:
        path = Path(config_path)
        if not path.is_absolute():
            path = root / path
        return path

    for filename in CONFIG_FILENAMES:
        candidate = root / filename
        if candidate.exists():
            return candidate
    return None


def load_profile_config(root, config_path=None):
    path = find_config(root, config_path)
    if path is None:
        return {}, None
    if not path.exists():
        raise FileNotFoundError(f"Profile config not found: {path}")

    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("Profile config must be a JSON object.")
    return data, path


def read_list_field(config, key):
    value = config.get(key, [])
    if value is None:
        return []
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"Config field '{key}' must be a list of file paths.")
    return [safe_relative_path(item) for item in value]


def resolve_context_files(profile=None, config=None):
    config = config or {}
    selected_profile = normalize_profile(profile or config.get("profile") or DEFAULT_PROFILE)
    files = get_profile_files(selected_profile)

    known_files = set(CORE_FILES)
    include_files = read_list_field(config, "include")
    exclude_files = set(read_list_field(config, "exclude"))

    unknown = [item for item in [*include_files, *exclude_files] if item not in known_files]
    if unknown:
        raise ValueError(
            "Config include/exclude entries must be known Nexus-APCP protocol files: "
            + ", ".join(unknown)
        )

    files = unique_files([*files, *include_files])
    files = [item for item in files if item not in exclude_files]
    ponytail_mode = (config.get("ponytail") or "full").strip().lower()
    if ponytail_mode == "off":
        files = [f for f in files if "PONYTAIL" not in Path(f).name.upper()]
    if not files:
        raise ValueError("Selected APCP profile produced no context files.")
    return selected_profile, files


def validate_files_exist(root, files):
    missing = [relative for relative in files if not (root / relative).is_file()]
    if missing:
        raise FileNotFoundError("Missing required context file(s): " + ", ".join(missing))


def compact_markdown_content(text):
    """Apply lossless whitespace compaction for prompt bundles."""
    compacted = []
    previous_blank = False
    for line in text.splitlines():
        stripped_line = line.rstrip()
        is_blank = stripped_line == ""
        if is_blank and previous_blank:
            continue
        compacted.append(stripped_line)
        previous_blank = is_blank
    return "\n".join(compacted).strip() + "\n"


def read_context_file(path, caveman_mode):
    text = path.read_text(encoding="utf-8")
    if caveman_mode:
        return compact_markdown_content(text)
    return text


def write_bundle(root, output_file, files, timestamp, caveman_mode, profile, target="generic", ponytail_mode="full"):
    temp_file = output_file.with_name("PROMPT_READY.tmp")
    with temp_file.open("w", encoding="utf-8", newline="\n") as out:
        out.write("--- APCP CONTEXT PACKAGE ---\n")
        out.write(f"Generated: {timestamp}\n")
        out.write(f"Project Root: {root}\n")
        out.write(f"Profile: {profile}\n")
        out.write(f"Ponytail Mode: {ponytail_mode}\n")
        out.write(f"Included Files: {len(files)}\n")
        if caveman_mode:
            out.write("Mode: CAVEMAN (Token Optimized)\n")
            out.write("Compaction: whitespace-trimmed, repeated blank lines collapsed\n")
        out.write("---------------------------\n\n")

        for relative in files:
            path = root / relative
            print(f"Adding: {relative}")
            content = read_context_file(path, caveman_mode)
            if target == "claude":
                out.write(f'<file name="{relative}">\n')
                out.write(content)
                out.write(f'</file>\n\n')
            elif target == "cursor":
                out.write(f"### {relative} ###\n")
                out.write(content)
                out.write("\n\n")
            else:
                out.write(f"=== START OF FILE: {relative} ===\n")
                out.write(content)
                out.write(f"\n=== END OF FILE: {relative} ===\n\n")

        out.write("\n--- INSTRUCTIONS ---\n")
        if caveman_mode:
            out.write("TALK LIKE CAVEMAN. Follow rules in CAVEMAN_RULES.md.\n")
            out.write("Why use many token when few token do trick?\n")
        else:
            out.write(
                "Please read the context above and confirm you understand "
                "the current task and architecture.\n"
            )

    temp_file.replace(output_file)


def gather_context(
    caveman_mode=False,
    profile=None,
    config_path=None,
    output_path=None,
    target="generic",
    root=ROOT,
):
    """
    Gather selected APCP profile files into PROMPT_READY.txt.
    Run: python scripts/apcp-gather.py [--caveman] [--profile core|web|...]
    """
    root = Path(root).resolve()
    output_file = Path(output_path) if output_path else root / "PROMPT_READY.txt"
    if not output_file.is_absolute():
        output_file = root / output_file
    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%d %H:%M:%S UTC"
    )

    try:
        config, config_file = load_profile_config(root, config_path)
        selected_profile, files = resolve_context_files(profile=profile, config=config)
        validate_files_exist(root, files)
    except Exception as exc:
        return fail(str(exc))

    ponytail_mode = (config.get("ponytail") or "full").strip().lower()

    print(f"Gathering project context at {timestamp}...")
    print(f"Profile: {selected_profile} - {profile_description(selected_profile)}")
    print(f"Ponytail Mode: {ponytail_mode}")
    if config_file:
        print(f"Config: {config_file}")
    if caveman_mode:
        print("CAVEMAN MODE ENABLED")

    try:
        output_file.parent.mkdir(parents=True, exist_ok=True)
        write_bundle(root, output_file, files, timestamp, caveman_mode, selected_profile, target, ponytail_mode=ponytail_mode)
    except Exception as exc:
        return fail(f"Unable to write context bundle: {exc}")

    print(f"\nSuccess! Context gathered in: {output_file}")
    print("Review the generated bundle before sharing it outside the local workspace.")
    return 0


def list_profiles():
    for profile in available_profiles():
        print(f"{profile}: {profile_description(profile)}")


def build_parser():
    parser = argparse.ArgumentParser(
        description="Generate a Nexus-APCP context bundle from a selected profile."
    )
    parser.add_argument("--caveman", action="store_true", help="Enable Caveman Mode.")
    parser.add_argument(
        "--profile",
        help="Context profile to gather. Defaults to apcp-profile.json or core.",
    )
    parser.add_argument(
        "--config",
        help="Path to apcp-profile.json. Defaults to apcp-profile.json or .apcp-profile.json.",
    )
    parser.add_argument(
        "--target",
        choices=["claude", "cursor", "codex", "generic"],
        default="generic",
        help="Target AI tool for optimized output formatting.",
    )
    parser.add_argument(
        "--output",
        default="PROMPT_READY.txt",
        help="Output bundle path. Defaults to PROMPT_READY.txt.",
    )
    parser.add_argument(
        "--list-profiles",
        action="store_true",
        help="List available profiles and exit.",
    )
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.list_profiles:
        list_profiles()
        return 0
    return gather_context(
        caveman_mode=args.caveman,
        profile=args.profile,
        config_path=args.config,
        output_path=args.output,
        target=args.target,
    )


if __name__ == "__main__":
    raise SystemExit(main())
