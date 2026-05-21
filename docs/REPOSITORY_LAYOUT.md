# Nexus-APCP Repository Layout

Nexus-APCP keeps primary protocol templates at the repository root on purpose. The root files are the public install surface used by raw GitHub fetches, profile installs, adapter files, and context gathering.

## Root Files

Root-level Markdown files should be limited to:

- primary Nexus-APCP protocol templates;
- short AI adapter files such as `AGENTS.md`, `CODEX.md`, `CLAUDE.md`, `CURSOR.md`, `GEMINI.md`, and `COPILOT.md`;
- public project documents such as `README.md`, `CHANGELOG.md`, `SECURITY.md`, `SUPPORT.md`, and `CONTRIBUTING.md`;
- the master prompt and setup guide when they are part of first-run onboarding.

## Docs Directory

Use `docs/` for repository maintenance guidance, SEO checklists, release process, layout policy, and other documents that are not copied into downstream projects by default.

## Examples Directory

Use `examples/` for sanitized project starter kits and task-specific prompt references. One-off prompt guides should not live at the repository root.

## Refactor Rule

Before moving a primary protocol file out of the root, update:

- `scripts/apcp_core_files.py`;
- `README.md`;
- `SETUP_GUIDE.md`;
- local exclude installers;
- validation checks;
- examples and adapter references.

Run full validation before committing any layout change.
