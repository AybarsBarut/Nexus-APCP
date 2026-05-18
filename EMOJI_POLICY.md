# Emoji Usage Policy

## Purpose

Nexus-APCP forbids emoji usage across repository content and AI-generated output. The rule keeps documentation, prompts, code, logs, examples, metadata, and generated context bundles consistent, professional, accessible, and easy to search.

## Scope

This policy applies to every repository-facing artifact:

- README files, Markdown documentation, protocol templates, prompts, examples, and checklists.
- Source code, comments, scripts, console output, tests, fixtures, and sample data.
- YAML, JSON, XML, SVG, metadata, issue templates, pull request templates, and generated prompt bundles.
- AI assistant responses, commits, branch names, PR titles, review comments, changelogs, and release notes produced for this repository.

## Rule

Do not use emoji.

Use plain words, ASCII labels, or existing icon components instead:

- Use `COMPLETED`, `FAILED`, `WARNING`, `IN_PROGRESS`, `BLOCKED`, and `REVIEW` for status.
- Use UI icon libraries or project-approved vector/icon assets for interface controls.
- Use accessible labels and `aria-label` text for icon-only controls.
- Use simple text in scripts, logs, and generated output.

## Temporary UI Exception

Emoji may be proposed only as a temporary button icon placeholder when all of these conditions are true:

- No suitable project-approved icon, icon-library glyph, SVG, or text label is available at that moment.
- The emoji is only a short-lived replacement marker, not final UI, documentation, or code style.
- The AI assistant asks the user first and receives explicit approval before adding it.
- The follow-up task records that the placeholder must be replaced with a proper icon.

If approval is not explicit, do not use the emoji.

## AI Agent Requirements

AI assistants working in this repository must:

- Read this policy before editing docs, prompts, scripts, UI, examples, or metadata.
- Remove emoji introduced by their own changes before finishing.
- Avoid suggesting emoji-based status systems.
- Prefer durable, text-based conventions that work across Claude Code, Cursor, ChatGPT, Gemini, GitHub Copilot, local LLMs, and other agents.
- Treat emoji in incoming user text as user input, not as permission to reproduce it in repository files.

## Review Gate

Before completing a change, run repository validation. Any emoji found outside explicitly approved temporary UI placeholder work is a policy failure.
