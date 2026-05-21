import argparse
import json
import os
import py_compile
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

from apcp_core_files import (
    CORE_FILES,
    DEFAULT_PROFILE,
    GENERATED_CONTEXT_PATTERNS,
    INSTALL_FILES,
    INSTALL_SUPPORT_FILES,
    LOCAL_EXCLUDE_PATTERNS,
    PUBLIC_REQUIRED_FILES,
    available_profiles,
    get_profile_files,
)


ROOT = Path(__file__).resolve().parents[1]
SKIPPED_SCAN_DIRS = {
    ".apcp-cache",
    ".codegraph",
    ".git",
    "__pycache__",
    "tmp",
}

YAML_FILES = [
    "TASK_PROGRESS.yaml",
    "CITATION.cff",
    ".github/repository-metadata.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/docs_improvement.yml",
    ".github/ISSUE_TEMPLATE/protocol_suggestion.yml",
    ".github/ISSUE_TEMPLATE/security_private.yml",
    ".github/workflows/validate.yml",
]

LINK_RE = re.compile(r"!?\[[^\]]*]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
COPY_COMMAND_RE = re.compile(r"^\s*cp\s+([A-Za-z0-9_./-]+)\s+", re.MULTILINE)

EMOJI_RE = re.compile(
    "["
    "\U0001F000-\U0001FAFF"
    "\U00002600-\U000027BF"
    "\U0000FE0E-\U0000FE0F"
    "\U0000200D"
    "\U000020E3"
    "]"
)

TEXT_SCAN_EXTENSIONS = {
    ".cff",
    ".css",
    ".html",
    ".js",
    ".json",
    ".md",
    ".ps1",
    ".py",
    ".sh",
    ".svg",
    ".ts",
    ".tsx",
    ".txt",
    ".yaml",
    ".yml",
}

SECRET_PATTERNS = [
    ("private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("AWS access key", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("GitHub token", re.compile(r"\bgh(?:p|o|u|s|r)_[A-Za-z0-9_]{36,}\b")),
    ("OpenAI API key", re.compile(r"\bsk-[A-Za-z0-9]{20,}\b")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("Stripe live secret key", re.compile(r"\bsk_live_[A-Za-z0-9]{16,}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z\-_]{35}\b")),
]

REQUIRED_GITIGNORE_PATTERNS = [
    "PROMPT_READY.txt",
    "PROMPT_READY.tmp",
    "PROMPT_READY*.txt",
    "PROMPT_READY*.tmp",
    "apcp-profile.json",
    ".apcp-profile.json",
]


def check_required_files():
    errors = []
    for relative in PUBLIC_REQUIRED_FILES:
        if not (ROOT / relative).exists():
            errors.append(f"Missing required file: {relative}")
    return errors


def check_python_syntax():
    errors = []
    for path in sorted(ROOT.rglob("*.py")):
        if any(part in SKIPPED_SCAN_DIRS for part in path.parts):
            continue
        try:
            py_compile.compile(str(path), doraise=True)
        except py_compile.PyCompileError as exc:
            errors.append(f"Python syntax error in {path.relative_to(ROOT)}: {exc.msg}")
    return errors


def check_powershell_syntax():
    errors = []
    executable = shutil.which("pwsh") or shutil.which("powershell")
    if executable is None:
        return ["PowerShell is required to parse .ps1 scripts"]

    for path in sorted(ROOT.rglob("*.ps1")):
        if any(part in SKIPPED_SCAN_DIRS for part in path.parts):
            continue
        escaped = str(path).replace("'", "''")
        command = (
            "$tokens = $null; "
            "$parseErrors = $null; "
            f"[System.Management.Automation.Language.Parser]::ParseFile('{escaped}', "
            "[ref]$tokens, [ref]$parseErrors) | Out-Null; "
            "if ($parseErrors.Count -gt 0) { "
            "$parseErrors | ForEach-Object { Write-Output $_.Message }; exit 1 "
            "}"
        )
        result = subprocess.run(
            [executable, "-NoProfile", "-NonInteractive", "-Command", command],
            cwd=ROOT,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=30,
        )
        if result.returncode != 0:
            errors.append(
                f"PowerShell syntax error in {path.relative_to(ROOT)}:\n"
                f"{result.stdout.strip()}"
            )
    return errors


def check_json():
    path = ROOT / "codemeta.json"
    with path.open("r", encoding="utf-8") as handle:
        json.load(handle)
    return []


def check_metadata_required_fields():
    errors = []
    with (ROOT / "codemeta.json").open("r", encoding="utf-8") as handle:
        codemeta = json.load(handle)
    for field in ["dateCreated", "dateModified", "version"]:
        if not codemeta.get(field):
            errors.append(f"codemeta.json missing required metadata field: {field}")

    if yaml is None:
        return errors + ["PyYAML is required for CITATION.cff metadata checks"]
    citation = yaml.safe_load((ROOT / "CITATION.cff").read_text(encoding="utf-8"))
    for field in ["date-released", "version", "repository-code"]:
        if not citation.get(field):
            errors.append(f"CITATION.cff missing required metadata field: {field}")
    return errors


def check_svg():
    ET.parse(ROOT / "assets" / "nexus-apcp-social-preview.svg")
    return []


def check_yaml_files():
    errors = []
    if yaml is None:
        return ["PyYAML is required for YAML parsing. Install with: python -m pip install PyYAML"]

    for relative in YAML_FILES:
        path = ROOT / relative
        if not path.exists():
            errors.append(f"Missing YAML file: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        if "\t" in text:
            errors.append(f"Tabs are not allowed in YAML file: {relative}")
        if not text.strip():
            errors.append(f"YAML file is empty: {relative}")
            continue
        try:
            yaml.safe_load(text)
        except yaml.YAMLError as exc:
            errors.append(f"YAML parse failed in {relative}: {exc}")
    return errors


def check_task_progress_schema():
    errors = []
    if yaml is None:
        return ["PyYAML is required for TASK_PROGRESS.yaml schema checks"]

    path = ROOT / "TASK_PROGRESS.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return ["TASK_PROGRESS.yaml must contain a mapping at the top level"]

    required_sections = [
        "project",
        "active_sprint",
        "tasks",
        "checkpoints",
        "metrics",
        "handoff",
    ]
    for section in required_sections:
        if section not in data:
            errors.append(f"TASK_PROGRESS.yaml missing section: {section}")

    tasks = data.get("tasks")
    if not isinstance(tasks, list) or not tasks:
        errors.append("TASK_PROGRESS.yaml tasks must be a non-empty list")
        return errors

    required_task_fields = [
        "id",
        "title",
        "status",
        "priority",
        "acceptance_criteria",
    ]
    for index, task in enumerate(tasks, start=1):
        if not isinstance(task, dict):
            errors.append(f"TASK_PROGRESS.yaml task {index} must be a mapping")
            continue
        for field in required_task_fields:
            if field not in task:
                errors.append(f"TASK_PROGRESS.yaml task {index} missing field: {field}")
        criteria = task.get("acceptance_criteria")
        if criteria is not None and not isinstance(criteria, list):
            errors.append(
                f"TASK_PROGRESS.yaml task {index} acceptance_criteria must be a list"
            )
    return errors


def normalize_link_target(target):
    target = target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        match = re.match(r"(.+?)(?:\s+['\"].*['\"])?$", target)
        if match:
            target = match.group(1).strip()
    return target


def github_heading_anchors(text):
    anchors = set()
    counts = {}
    for match in HEADING_RE.finditer(text):
        heading = match.group(2).strip()
        heading = re.sub(r"`([^`]*)`", r"\1", heading)
        heading = re.sub(r"<[^>]+>", "", heading)
        heading = heading.lower()
        heading = re.sub(r"[^\w\s-]", "", heading, flags=re.UNICODE)
        heading = re.sub(r"\s+", "-", heading)
        heading = re.sub(r"-+", "-", heading).strip("-")
        if not heading:
            continue
        count = counts.get(heading, 0)
        counts[heading] = count + 1
        anchors.add(heading if count == 0 else f"{heading}-{count}")
    return anchors


def check_markdown_links():
    errors = []
    anchor_cache = {}
    for path in sorted(ROOT.rglob("*.md")):
        if any(part in SKIPPED_SCAN_DIRS for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in LINK_RE.finditer(text):
            target = normalize_link_target(match.group(1))
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if "://" in target:
                continue

            clean_target, _, fragment = target.partition("#")
            if clean_target:
                clean_target = clean_target.replace("%20", " ")
                candidate = (path.parent / clean_target).resolve()
                try:
                    candidate.relative_to(ROOT)
                except ValueError:
                    errors.append(
                        f"Link escapes repository: {path.relative_to(ROOT)} -> {target}"
                    )
                    continue
                if not candidate.exists():
                    errors.append(
                        f"Broken local link: {path.relative_to(ROOT)} -> {target}"
                    )
                    continue
            else:
                candidate = path

            if fragment and candidate.suffix.lower() == ".md":
                anchors = anchor_cache.get(candidate)
                if anchors is None:
                    anchors = github_heading_anchors(
                        candidate.read_text(encoding="utf-8", errors="replace")
                    )
                    anchor_cache[candidate] = anchors
                if fragment not in anchors:
                    errors.append(
                        f"Broken Markdown anchor: {path.relative_to(ROOT)} -> {target}"
                    )
    return errors


def extract_install_bullet_lists(text):
    lists = []
    anchor = "Install these core files when available:"
    start = 0
    while True:
        index = text.find(anchor, start)
        if index == -1:
            break
        collected = []
        for line in text[index + len(anchor) :].splitlines()[1:]:
            stripped = line.strip()
            if stripped.startswith("- "):
                collected.append(stripped[2:].strip("` "))
                continue
            if not stripped:
                if collected:
                    break
                continue
            break
        lists.append(collected)
        start = index + len(anchor)
    return lists


def check_core_file_consistency():
    errors = []
    if len(CORE_FILES) != len(set(CORE_FILES)):
        errors.append("CORE_FILES contains duplicate entries")
    if len(INSTALL_FILES) != len(set(INSTALL_FILES)):
        errors.append("INSTALL_FILES contains duplicate entries")

    for relative in CORE_FILES:
        if not (ROOT / relative).exists():
            errors.append(f"CORE_FILES entry does not exist: {relative}")

    for profile in available_profiles():
        files = get_profile_files(profile)
        if len(files) != len(set(files)):
            errors.append(f"Profile contains duplicate files: {profile}")
        for relative in files:
            if relative not in CORE_FILES:
                errors.append(f"Profile {profile} references non-canonical file: {relative}")
            if not (ROOT / relative).exists():
                errors.append(f"Profile {profile} entry does not exist: {relative}")

    expected_install = list(INSTALL_FILES)
    for relative in ["README.md", "SETUP_GUIDE.md"]:
        text = (ROOT / relative).read_text(encoding="utf-8")
        bullet_lists = extract_install_bullet_lists(text)
        if bullet_lists:
            errors.append(
                f"{relative} must use scripts/apcp-install.py instead of literal install lists"
            )

        copied_files = {
            match.group(1).replace("\\", "/")
            for match in COPY_COMMAND_RE.finditer(text)
            if match.group(1).replace("\\", "/") in INSTALL_FILES
        }
        if len(copied_files) > len(INSTALL_SUPPORT_FILES):
            errors.append(
                f"{relative} contains broad manual copy commands instead of profile install"
            )
        for fragment in [
            "scripts/apcp-install.py",
            "--profile",
            "--list-profiles",
            "apcp-profile.json",
        ]:
            if fragment not in text:
                errors.append(f"{relative} missing profile setup guidance: {fragment}")

    for relative in ["scripts/install-local-excludes.ps1", "scripts/install-local-excludes.sh"]:
        text = (ROOT / relative).read_text(encoding="utf-8")
        missing_patterns = [
            pattern for pattern in LOCAL_EXCLUDE_PATTERNS if pattern not in text
        ]
        if missing_patterns:
            errors.append(
                f"{relative} missing local exclude patterns: "
                f"{', '.join(missing_patterns)}"
            )
    return errors


def check_public_template_hygiene():
    errors = []

    ai_main = (ROOT / "AI_MAIN.md").read_text(encoding="utf-8")
    if re.search(r"(?m)^\s*(?:[-*]|\d+\.)\s+\[[xX]\]", ai_main):
        errors.append("AI_MAIN.md must not ship with completed checklist items")

    task_progress = (ROOT / "TASK_PROGRESS.yaml").read_text(encoding="utf-8")
    forbidden_fragments = [
        "Antigravity",
        "tasks_completed: 25",
        "total_tasks: 25",
    ]
    for fragment in forbidden_fragments:
        if fragment in task_progress:
            errors.append(f"TASK_PROGRESS.yaml carries stale source state: {fragment}")

    return errors


def check_generated_context_hygiene():
    errors = []
    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    gitignore_lines = {
        line.strip()
        for line in gitignore.splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }

    for pattern in REQUIRED_GITIGNORE_PATTERNS:
        if pattern not in gitignore_lines:
            errors.append(f".gitignore must ignore generated context artifact: {pattern}")

    if (ROOT / ".git").exists():
        result = subprocess.run(
            ["git", "ls-files", "--", *GENERATED_CONTEXT_PATTERNS],
            cwd=ROOT,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=30,
        )
        if result.returncode != 0:
            errors.append(f"Unable to inspect tracked generated context files:\n{result.stdout}")
        else:
            tracked = [line.strip() for line in result.stdout.splitlines() if line.strip()]
            if tracked:
                errors.append(
                    "Generated context artifacts must not be tracked: "
                    + ", ".join(tracked)
                )

    return errors


def iter_text_files():
    for path in sorted(ROOT.rglob("*")):
        if path.is_dir():
            continue
        if any(part in SKIPPED_SCAN_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in TEXT_SCAN_EXTENSIONS:
            yield path


def check_no_emoji():
    errors = []
    for path in iter_text_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if EMOJI_RE.search(line):
                errors.append(f"Emoji found: {path.relative_to(ROOT)}:{line_number}")
    return errors


def check_secret_patterns():
    errors = []
    for path in iter_text_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for label, pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    errors.append(
                        f"Potential secret pattern ({label}): "
                        f"{path.relative_to(ROOT)}:{line_number}"
                    )
    return errors


def check_context_gatherer():
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    runs = [
        (
            "repository root",
            ROOT,
            [sys.executable, "scripts/apcp-gather.py", "--caveman"],
            get_profile_files(DEFAULT_PROFILE),
        ),
        (
            "full profile",
            ROOT,
            [sys.executable, "scripts/apcp-gather.py", "--profile", "full", "--caveman"],
            CORE_FILES,
        ),
        (
            "scripts directory",
            ROOT / "scripts",
            [sys.executable, "apcp-gather.py", "--caveman"],
            get_profile_files(DEFAULT_PROFILE),
        ),
    ]

    bundle = ROOT / "PROMPT_READY.txt"
    original_bundle = bundle.read_bytes() if bundle.exists() else None
    errors = []

    try:
        for label, cwd, command, expected_files in runs:
            result = subprocess.run(
                command,
                cwd=cwd,
                env=env,
                text=True,
                encoding="utf-8",
                errors="replace",
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=30,
            )
            if result.returncode != 0:
                errors.append(f"Context gatherer failed from {label}:\n{result.stdout}")
                continue
            if "Skipped (Not Found)" in result.stdout:
                errors.append(f"Context gatherer skipped files from {label}:\n{result.stdout}")

            if not bundle.exists():
                errors.append(f"Context gatherer did not produce PROMPT_READY.txt from {label}")
                continue
            bundle_text = bundle.read_text(encoding="utf-8", errors="replace")
            for relative in expected_files:
                marker = f"=== START OF FILE: {relative} ==="
                if marker not in bundle_text:
                    errors.append(
                        f"Context gatherer output from {label} missing file: {relative}"
                    )
            if label == "repository root":
                excluded_marker = (
                    "=== START OF FILE: WEBSITE_BACKEND_SECURITY_OPTIMIZATION_PROTOCOL.md ==="
                )
                if excluded_marker in bundle_text:
                    errors.append("Default context gatherer included web-only profile file")
    finally:
        if original_bundle is None:
            bundle.unlink(missing_ok=True)
        else:
            bundle.write_bytes(original_bundle)

    return errors


CHECKS = [
    ("required-files", "required files", check_required_files),
    ("python-syntax", "Python syntax", check_python_syntax),
    ("powershell-syntax", "PowerShell syntax", check_powershell_syntax),
    ("json-metadata", "JSON metadata", check_json),
    ("metadata-required-fields", "metadata required fields", check_metadata_required_fields),
    ("svg-social-preview", "SVG social preview", check_svg),
    ("yaml-files", "YAML files", check_yaml_files),
    ("task-progress-schema", "TASK_PROGRESS schema", check_task_progress_schema),
    ("core-file-consistency", "core file consistency", check_core_file_consistency),
    ("template-hygiene", "template hygiene", check_public_template_hygiene),
    ("generated-context-hygiene", "generated context hygiene", check_generated_context_hygiene),
    ("markdown-links", "Markdown links", check_markdown_links),
    ("emoji-policy", "emoji policy", check_no_emoji),
    ("secret-pattern-scan", "secret pattern scan", check_secret_patterns),
    ("context-gatherer", "context gatherer", check_context_gatherer),
]


def selected_checks(only):
    if not only:
        return CHECKS
    requested = set(only)
    return [check for check in CHECKS if check[0] in requested]


def build_parser():
    parser = argparse.ArgumentParser(description="Validate Nexus-APCP repository health.")
    parser.add_argument(
        "--only",
        action="append",
        choices=[key for key, _, _ in CHECKS],
        help="Run one named validation check. Repeat to run multiple checks.",
    )
    parser.add_argument(
        "--list-checks",
        action="store_true",
        help="List validation check names and exit.",
    )
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.list_checks:
        for key, label, _ in CHECKS:
            print(f"{key}: {label}")
        return 0

    errors = []
    for _, label, check in selected_checks(args.only):
        try:
            check_errors = check()
        except Exception as exc:
            check_errors = [f"{label} check crashed: {exc}"]
        if check_errors:
            errors.extend(check_errors)
        else:
            print(f"OK: {label}")

    if errors:
        print("\nValidation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("\nRepository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
