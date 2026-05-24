# Nexus-APCP Repository Layout

Nexus-APCP utilizes a structured layout to separate core functionality, rules, templates, and archives.

## Root Files

Root-level Markdown files are limited to essential context and public documentation:
- `AI_PROJECT_CONTEXT_PROTOCOL.md` (Lightweight session starter)
- Short AI adapter files (`AGENTS.md`, `CLAUDE.md`, `CURSOR.md`, etc.)
- Public project documents (`README.md`, `CHANGELOG.md`, `SECURITY.md`, `SUPPORT.md`, `CONTRIBUTING.md`)

## Rules Directory (`rules/`)

The `rules/` directory contains standard operating procedures and specific behavioral guidelines for agents. These are loaded conditionally or by default based on the profile.
- e.g., `AI_MAIN.md`, `AI_AGENT_SKILLS_PROTOCOL.md`, `DECISION_LOG_PROTOCOL.md`.

## Templates Directory (`templates/`)

The `templates/` directory holds large reference documents and optional architectural guidelines. These ensure the core root files stay lean and token-efficient.
- e.g., `AI_PROJECT_REFERENCE_PROTOCOL.md`, `WATERFALL_DEVELOPMENT_PROTOCOL.md`.

## Archive Directory (`archive/`)

Used for storing completed sprint data (e.g., `sprint-1.yaml`) to keep `TASK_PROGRESS.yaml` clean and focused on active work.

## Docs Directory (`docs/`)

Use `docs/` for repository maintenance guidance, SEO checklists, release process, layout policy, and other documents that are not copied into downstream projects by default.

## Examples Directory (`examples/`)

Use `examples/` for sanitized project starter kits and task-specific prompt references. One-off prompt guides should not live at the repository root.

## Refactor Rule

Before moving a primary protocol file, update:
- `scripts/apcp_core_files.py`
- `README.md`
- `SETUP_GUIDE.md`
- local exclude installers
- validation checks
- examples and adapter references.

Run full validation before committing any layout change.
