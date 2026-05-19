import json
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    "CURSOR.md",
    "COPILOT.md",
    "CODEX.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "CITATION.cff",
    "codemeta.json",
    "AI_PROJECT_CONTEXT_PROTOCOL.md",
    "EMOJI_POLICY.md",
    "VISUAL_CONTEXT_MERMAID.md",
    "AI_AGENT_SKILLS_PROTOCOL.md",
    "FILE_STRUCTURE_REFACTOR_PROTOCOL.md",
    "UPDATE_SYSTEM_RECOMMENDATION_PROTOCOL.md",
    "DEBLOAT_APPLICATION_GUIDE.md",
    "WEBSITE_BACKEND_SECURITY_OPTIMIZATION_PROTOCOL.md",
    "TASK_PROGRESS.yaml",
    "docs/SEO_CHECKLIST.md",
    ".github/CODEOWNERS",
    ".github/pull_request_template.md",
    ".github/pull_request_title_conventions.md",
    ".github/workflows/validate.yml",
    "examples/README.md",
]

YAML_LIKE_FILES = [
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
EMOJI_RE = re.compile(
    "["
    "\U0001F000-\U0001FAFF"
    "\U00002600-\U000027BF"
    "\U0000FE0E-\U0000FE0F"
    "\U0000200D"
    "\U000020E3"
    "]"
)
EMOJI_SCAN_EXTENSIONS = {
    ".cff",
    ".css",
    ".html",
    ".js",
    ".json",
    ".md",
    ".ps1",
    ".py",
    ".svg",
    ".ts",
    ".tsx",
    ".txt",
    ".yaml",
    ".yml",
}


def fail(message):
    print(f"ERROR: {message}")
    return 1


def check_required_files():
    errors = []
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).exists():
            errors.append(f"Missing required file: {relative}")
    return errors


def check_json():
    path = ROOT / "codemeta.json"
    with path.open("r", encoding="utf-8") as handle:
        json.load(handle)
    return []


def check_svg():
    ET.parse(ROOT / "assets" / "nexus-apcp-social-preview.svg")
    return []


def check_yaml_like_files():
    errors = []
    for relative in YAML_LIKE_FILES:
        path = ROOT / relative
        if not path.exists():
            errors.append(f"Missing YAML-like file: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        if "\t" in text:
            errors.append(f"Tabs are not allowed in YAML-like file: {relative}")
        if not text.strip():
            errors.append(f"YAML-like file is empty: {relative}")
    return errors


def check_markdown_links():
    errors = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip()
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            if "://" in target:
                continue
            clean_target = target.split("#", 1)[0]
            if not clean_target:
                continue
            clean_target = clean_target.replace("%20", " ")
            candidate = (path.parent / clean_target).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                errors.append(f"Link escapes repository: {path.relative_to(ROOT)} -> {target}")
                continue
            if not candidate.exists():
                errors.append(f"Broken local link: {path.relative_to(ROOT)} -> {target}")
    return errors


def check_no_emoji():
    errors = []
    skipped_dirs = {".git", "__pycache__"}
    for path in ROOT.rglob("*"):
        if path.is_dir():
            continue
        if any(part in skipped_dirs for part in path.parts):
            continue
        if path.suffix.lower() not in EMOJI_SCAN_EXTENSIONS:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if EMOJI_RE.search(line):
                errors.append(f"Emoji found: {path.relative_to(ROOT)}:{line_number}")
    return errors


def check_context_gatherer():
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    result = subprocess.run(
        [sys.executable, "scripts/apcp-gather.py", "--caveman"],
        cwd=ROOT,
        env=env,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=30,
    )
    if result.returncode != 0:
        return [f"Context gatherer failed:\n{result.stdout}"]
    return []


def main():
    checks = [
        ("required files", check_required_files),
        ("JSON metadata", check_json),
        ("SVG social preview", check_svg),
        ("YAML-like files", check_yaml_like_files),
        ("Markdown links", check_markdown_links),
        ("emoji policy", check_no_emoji),
        ("context gatherer", check_context_gatherer),
    ]

    errors = []
    for label, check in checks:
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
