# Nexus-APCP Agent Guide

This file gives AI coding assistants and automation agents the repository-specific rules for working on Nexus-APCP. Treat it as the first file to read before changing docs, prompts, scripts, metadata, or examples.

## Project Overview

Nexus-APCP is an open-source AI Project Context Protocol. The repository is a documentation and workflow kit, not a runtime application. Its purpose is to help developers give AI coding assistants stable project memory, task state, decision history, safety rules, and token-efficient communication patterns.

The public repository should remain safe to share. Real project context files, private architecture maps, secrets, generated prompt bundles, customer data, and security runbooks must not be committed unless they are sanitized templates.

## Primary Files

| Path | Role |
| :--- | :--- |
| `README.md` | Public product page, quick start, SEO surface, and first-time user orientation. |
| `AI_PROJECT_CONTEXT_PROTOCOL.md` | Main protocol template for project identity, architecture, rules, and context. |
| `AI_MAIN.md` | AI execution orchestrator and session checkpoint flow. |
| `TASK_PROGRESS.yaml` | Current task state, sprint status, and repository maintenance progress. |
| `DECISION_LOG_PROTOCOL.md` | Decision history and architecture intent protocol. |
| `CONTEXT_OPTIMIZATION.md` | Strategies for handling large-scale codebases and context window limits. |
| `CAVEMAN_RULES.md` | Token-efficient communication rules. |
| `EMOJI_POLICY.md` | Repository-wide and AI-wide emoji usage ban with a narrow user-approved temporary button icon exception. |
| `VISUAL_CONTEXT_MERMAID.md` | Mermaid README flowchart and visual context protocol. |
| `AI_AGENT_SKILLS_PROTOCOL.md` | Skill-based AI agent workflows for diagnosis, TDD, triage, PRDs, handoff, architecture improvement, and prototyping. |
| `FILE_STRUCTURE_REFACTOR_PROTOCOL.md` | Safe iterative file and folder restructuring protocol for existing projects. |
| `AI_ASSISTANT_PROMPT_TEMPLATES.md` | Reusable prompts for common AI-assisted development scenarios. |
| `WORKSPACE_SPECIFIC_DELIVERY_PROTOCOLS.md` | Domain-specific delivery gates and release expectations. |
| `DOMAIN_SPECIFIC_GITIGNORE_PROTOCOLS.md` | Safe publishing patterns for different project domains. |
| `MACP_IMPLEMENTATION_GUIDE.md` | Multi-AI Coordination Protocol for parallel model workflows. |
| `SETUP_GUIDE.md` | Step-by-step setup instructions and routine maintenance. |
| `scripts/apcp-gather.py` | Generates an AI-ready context bundle from core protocol files. |
| `scripts/validate-repo.py` | Repository integrity, metadata, and link validation script. |
| `docs/SEO_CHECKLIST.md` | Repository SEO metadata and keyword source of truth. |

## Essential Commands

Run these from the repository root.

```bash
python scripts/apcp-gather.py --caveman
python scripts/validate-repo.py
```

On Windows, the PowerShell checkpoint can also be used:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/checkpoint.ps1
```

## Working Rules

- Keep changes scoped to the requested protocol, documentation, metadata, or script behavior.
- Preserve the public/private boundary. Public templates are welcome; filled private project context is not.
- Prefer durable wording over model-version-specific wording.
- Keep repository-facing terminology consistent: `Nexus-APCP`, `AI Project Context Protocol`, `context engineering`, `AI-assisted development`, and `token optimization`.
- When adding or changing reusable agent workflows, keep them aligned with `AI_AGENT_SKILLS_PROTOCOL.md`.
- Follow `EMOJI_POLICY.md`: do not add emoji to README files, Markdown, code, comments, scripts, metadata, examples, generated output, commits, PR text, or AI responses. For a missing button icon, ask the user before using a temporary emoji placeholder.
- Update `TASK_PROGRESS.yaml` when completing a visible repository maintenance task.
- Update `docs/SEO_CHECKLIST.md`, `codemeta.json`, or `.github/repository-metadata.yml` when changing search-facing positioning.
- Use concise comments only when they explain non-obvious validation, safety, or release behavior.

## Security Publishing Hygiene

This is a public repository. When working on security-related docs or fixes:

- Do not expose exploit paths, attack names, private infrastructure, or sensitive project identifiers in branch names, commit messages, PR titles, test names, or comments.
- Use neutral functional wording, such as `improve input validation`, instead of naming the vulnerability class.
- Keep vulnerability details in private reporting channels.
- Never commit `PROMPT_READY.txt` generated from a private project.
- Do not weaken `.gitignore`, security guidance, or private-context warnings without a clear replacement.

## Documentation Style

- First-time users should understand what the protocol does within the first screen of the README.
- Prefer examples that are easy to adapt across Claude Code, Cursor, ChatGPT, Gemini, GitHub Copilot, local LLMs, and other agents.
- Avoid claims that require live proof unless the repository provides the evidence.
- Use tables for file maps, checklists for setup/review flows, and short code blocks for commands.
- Keep public examples realistic but sanitized.

## Review Checklist

Before finishing a change, verify:

- Required public files still exist.
- Markdown links added by the change are valid or intentionally external.
- JSON files parse.
- SVG assets parse as XML.
- `scripts/apcp-gather.py --caveman` runs successfully.
- The change does not add private context, secrets, generated prompt bundles, or sensitive security details.

## AI Adapter Files

Adapter files such as `CLAUDE.md`, `GEMINI.md`, `CURSOR.md`, `COPILOT.md`, and `CODEX.md` should stay short. They should point back to this file and mention only tool-specific startup behavior when necessary.
