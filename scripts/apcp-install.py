import argparse
import json
import shutil
import sys
from pathlib import Path

try:
    from apcp_core_files import (
        DEFAULT_PROFILE,
        available_profiles,
        get_install_files,
        normalize_profile,
        profile_description,
    )
except ImportError as exc:
    raise SystemExit(
        "ERROR: scripts/apcp_core_files.py is required next to apcp-install.py."
    ) from exc


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


ROOT = Path(__file__).resolve().parents[1]


def fail(message):
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def copy_file(relative, target_root, overwrite=False, dry_run=False):
    source = ROOT / relative
    destination = target_root / relative
    if not source.is_file():
        raise FileNotFoundError(f"Source file missing: {relative}")

    if destination.exists() and not overwrite:
        print(f"Skipping existing: {relative}")
        return "skipped"

    print(f"{'Would copy' if dry_run else 'Copying'}: {relative}")
    if not dry_run:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    return "copied"


def write_profile_config(target_root, profile, overwrite=False, dry_run=False):
    destination = target_root / "apcp-profile.json"
    if destination.exists() and not overwrite:
        print("Skipping existing: apcp-profile.json")
        return "skipped"

    data = {
        "profile": profile,
        "include": [],
        "exclude": [],
    }
    print(f"{'Would write' if dry_run else 'Writing'}: apcp-profile.json")
    if not dry_run:
        destination.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return "copied"


def install_profile(
    target,
    profile=DEFAULT_PROFILE,
    overwrite=False,
    dry_run=False,
    write_config=True,
):
    selected_profile = normalize_profile(profile)
    files = get_install_files(selected_profile)
    target_root = Path(target).expanduser().resolve()

    print(f"Installing Nexus-APCP profile: {selected_profile}")
    print(profile_description(selected_profile))
    print(f"Target: {target_root}")

    if not dry_run:
        target_root.mkdir(parents=True, exist_ok=True)

    copied = 0
    skipped = 0
    try:
        for relative in files:
            result = copy_file(
                relative,
                target_root,
                overwrite=overwrite,
                dry_run=dry_run,
            )
            copied += result == "copied"
            skipped += result == "skipped"
        if write_config:
            result = write_profile_config(
                target_root,
                selected_profile,
                overwrite=overwrite,
                dry_run=dry_run,
            )
            copied += result == "copied"
            skipped += result == "skipped"
    except Exception as exc:
        return fail(str(exc))

    action = "Dry run complete" if dry_run else "Install complete"
    print(f"{action}: {copied} copied, {skipped} skipped.")
    return 0


def list_profiles():
    for profile in available_profiles():
        print(f"{profile}: {profile_description(profile)}")


def list_files(profile):
    selected_profile = normalize_profile(profile)
    for relative in get_install_files(selected_profile):
        print(relative)
    print("apcp-profile.json")


def build_parser():
    parser = argparse.ArgumentParser(
        description="Install Nexus-APCP files into a target project by profile."
    )
    parser.add_argument(
        "--target",
        default=".",
        help="Target project root. Defaults to the current directory.",
    )
    parser.add_argument(
        "--profile",
        default=DEFAULT_PROFILE,
        help="Install profile. Use --list-profiles to see available values.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing target files. Default is to skip them.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned actions without writing files.",
    )
    parser.add_argument(
        "--no-config",
        action="store_true",
        help="Do not write apcp-profile.json into the target project.",
    )
    parser.add_argument(
        "--list-profiles",
        action="store_true",
        help="List available profiles and exit.",
    )
    parser.add_argument(
        "--list-files",
        action="store_true",
        help="List files for the selected profile and exit.",
    )
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.list_profiles:
        list_profiles()
        return 0
    if args.list_files:
        list_files(args.profile)
        return 0
    return install_profile(
        target=args.target,
        profile=args.profile,
        overwrite=args.overwrite,
        dry_run=args.dry_run,
        write_config=not args.no_config,
    )


if __name__ == "__main__":
    raise SystemExit(main())
