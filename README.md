# Nexus-APCP: AI Project Context Protocol for AI-Assisted Development

![Nexus-APCP social preview](./assets/nexus-apcp-social-preview.svg)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![AI Workflow](https://img.shields.io/badge/Workflow-AI--assisted-blue)](#quick-start)
[![Context Engineering](https://img.shields.io/badge/Context-Engineering-green)](#what-nexus-apcp-solves)
[![Token Optimized](https://img.shields.io/badge/Token-Optimized-brightgreen)](#token-optimization-with-caveman-mode)

**Nexus-APCP** is an open-source **AI Project Context Protocol** for developers who work with AI coding assistants, AI agents, and large language models. It gives every AI session the same project memory, architecture rules, task state, decision history, and token-efficient operating style.

Use Nexus-APCP with **Claude Code, Cursor, ChatGPT, Gemini, GitHub Copilot, local LLMs, and multi-agent development workflows** to reduce context loss, repeated explanations, inconsistent code suggestions, and prompt bloat.

> Security note: protocol templates may be public, but filled project-context files, backend maps, internal architecture diagrams, deployment maps, database internals, private threat models, and security runbooks should stay local/private unless sanitized and explicitly approved.

## What Nexus-APCP Solves

AI-assisted software development gets slower when every new model, chat, IDE agent, or pull request review starts from zero. Nexus-APCP creates a durable context layer for the repository so the AI can understand the project before it suggests code.

- **Persistent AI project context**: architecture, folder structure, conventions, security rules, and delivery gates stay in one reusable protocol.
- **Token optimization**: Caveman Mode keeps responses compact while preserving technical depth.
- **Decision memory**: architecture decision records explain why choices were made and reduce refactor loops.
- **Task continuity**: `TASK_PROGRESS.yaml` tracks active work, sprint goals, checkpoints, and quality gates.
- **Model portability**: move between Claude, Cursor, ChatGPT, Gemini, Copilot, and local agents without rebuilding context.
- **Safer publishing**: domain-specific `.gitignore` guidance helps prevent secrets, internal maps, customer data, and generated context from leaking.

## Core Features

| Feature | What it does |
| :--- | :--- |
| AI Project Context Protocol | Keeps project identity, architecture, workflows, and constraints available to every AI session. |
| Caveman Compression | Reduces verbose AI output with short, high-signal technical language. |
| ADR-style Decision Log | Records technical intent so agents do not undo settled architecture. |
| Task Progress YAML | Gives humans and agents a shared source of truth for status, priorities, and checkpoints. |
| Prompt Templates | Provides ready-to-use prompts for implementation, review, debugging, refactoring, and handoff. |
| Delivery Protocols | Adds release gates for web apps, backend services, AI/LLM products, games, mobile apps, DevOps, and security work. |
| GitHub Safety Rules | Includes broad `.gitignore` patterns for AI artifacts, secrets, generated files, domain data, and private docs. |

## Quick Start

Clone the repository:

```bash
git clone https://github.com/AybarsBarut/Nexus-APCP.git
cd Nexus-APCP
```

Copy the protocol into your project:

```bash
cp AI_PROJECT_CONTEXT_PROTOCOL.md /your/project/
cp TASK_PROGRESS.yaml /your/project/
cp DECISION_LOG_PROTOCOL.md /your/project/
cp CAVEMAN_RULES.md /your/project/
mkdir -p /your/project/scripts
cp scripts/apcp-gather.py /your/project/scripts/
```

Generate an AI-ready context package:

```bash
python scripts/apcp-gather.py --caveman
```

Paste the generated `PROMPT_READY.txt` into your AI assistant, or start with the ready-made prompt in [`MASTER_PROMPT.md`](./MASTER_PROMPT.md).

## Repository Contents

| File | Purpose |
| :--- | :--- |
| [`AI_PROJECT_CONTEXT_PROTOCOL.md`](./AI_PROJECT_CONTEXT_PROTOCOL.md) | Main project context template and operating rules. |
| [`AI_MAIN.md`](./AI_MAIN.md) | Execution orchestrator for AI sessions and workflow gates. |
| [`TASK_PROGRESS.yaml`](./TASK_PROGRESS.yaml) | Task tracking, sprint status, checkpoints, and velocity metrics. |
| [`DECISION_LOG_PROTOCOL.md`](./DECISION_LOG_PROTOCOL.md) | Architecture decision record protocol for intent preservation. |
| [`CONTEXT_OPTIMIZATION.md`](./CONTEXT_OPTIMIZATION.md) | Strategies for large codebases, context windows, and token limits. |
| [`CAVEMAN_RULES.md`](./CAVEMAN_RULES.md) | Token-efficient communication rules for concise AI output. |
| [`AI_ASSISTANT_PROMPT_TEMPLATES.md`](./AI_ASSISTANT_PROMPT_TEMPLATES.md) | Prompt templates for common AI-assisted development scenarios. |
| [`WORKSPACE_SPECIFIC_DELIVERY_PROTOCOLS.md`](./WORKSPACE_SPECIFIC_DELIVERY_PROTOCOLS.md) | Delivery gates by workspace type and product domain. |
| [`DOMAIN_SPECIFIC_GITIGNORE_PROTOCOLS.md`](./DOMAIN_SPECIFIC_GITIGNORE_PROTOCOLS.md) | Safe publishing patterns for different technical domains. |
| [`SETUP_GUIDE.md`](./SETUP_GUIDE.md) | Step-by-step setup instructions. |
| [`scripts/apcp-gather.py`](./scripts/apcp-gather.py) | Context packer that generates `PROMPT_READY.txt`. |
| [`VISUAL_CONTEXT_MERMAID.md`](./VISUAL_CONTEXT_MERMAID.md) | Standardized Mermaid.js flowchart protocol for architecture and logic visualization. |
| [`AGENTS.md`](./AGENTS.md) | Repository instructions for AI coding assistants and automation agents. |
| [`examples/`](./examples/README.md) | Sanitized starter kits for web apps, backend APIs, and AI/RAG systems. |

## How Nexus-APCP Works

1. **Capture project truth** in `AI_PROJECT_CONTEXT_PROTOCOL.md`: architecture, modules, conventions, security boundaries, tooling, and delivery rules.
2. **Track execution state** in `TASK_PROGRESS.yaml`: active tasks, priorities, estimates, dependencies, and quality gates.
3. **Preserve decisions** in `DECISION_LOG_PROTOCOL.md`: accepted tradeoffs, rejected paths, and architectural intent.
4. **Package context** with `scripts/apcp-gather.py`: combine the core protocol files into one prompt-ready bundle.
5. **Run compact AI sessions** with Caveman Mode: lower token usage, fewer repeated explanations, and cleaner handoffs.

## Ideal Use Cases

- AI-assisted software development teams using Claude Code, Cursor, ChatGPT, Gemini, Copilot, or local LLMs.
- Solo developers who want a reusable AI memory layer across projects.
- Agencies and freelancers who switch between many client repositories.
- AI agent workflows that need stable instructions, delivery gates, and handoff state.
- Open-source maintainers who want contributors and AI assistants to follow the same architecture rules.
- Teams practicing context engineering, prompt engineering, ADRs, and token-optimized development.

## Token Optimization With Caveman Mode

Nexus-APCP includes the Caveman Protocol: short, direct, fragment-based technical communication for lower token cost and faster AI collaboration.

Normal AI style:

> I reviewed the authentication middleware and noticed a potential security flaw in the token validation logic. I recommend adding a null check before accessing the user property.

Caveman Mode:

> Auth middleware bug. Token validation lacks user null guard. Fix: add guard clause before access.

Same technical meaning, fewer tokens, easier scanning.

## Recommended GitHub Topics

For better GitHub discovery, use these repository topics:

`ai`, `ai-assisted-development`, `ai-agents`, `context-engineering`, `prompt-engineering`, `llm`, `claude-code`, `cursor-ai`, `chatgpt`, `gemini`, `github-copilot`, `developer-productivity`, `token-optimization`, `architecture-decision-records`, `adr`, `documentation`, `software-development`, `devtools`, `open-source`, `workflow-automation`

See [`docs/SEO_CHECKLIST.md`](./docs/SEO_CHECKLIST.md) for the full repository SEO checklist and metadata source of truth.

## Community and Maintenance

Nexus-APCP includes the repository hygiene expected from a serious open-source protocol kit:

- [`CONTRIBUTING.md`](./CONTRIBUTING.md): contribution rules and public-safety checklist.
- [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md): community standards.
- [`SECURITY.md`](./SECURITY.md): private-context and vulnerability-reporting policy.
- [`SUPPORT.md`](./SUPPORT.md): where to ask for help and what to keep private.
- [`.github/pull_request_template.md`](./.github/pull_request_template.md): PR checklist for docs, protocol, security, and metadata changes.
- [`.github/ISSUE_TEMPLATE/`](./.github/ISSUE_TEMPLATE/): structured issue forms for bugs, docs, protocol suggestions, and security-sensitive process notes.
- [`.github/workflows/validate.yml`](./.github/workflows/validate.yml): repository validation for required files, metadata, links, SVG, and context gathering.

## FAQ

### Is Nexus-APCP a prompt template or a protocol?

It is a protocol kit. Prompt templates are included, but the main value is the shared project context, task state, decision history, safety rules, and repeatable AI handoff workflow.

### Does it work with any AI coding assistant?

Yes. Nexus-APCP is model-agnostic and works with hosted assistants, IDE agents, CLI agents, local LLMs, and multi-agent workflows.

### Is filled project context safe to publish?

Usually no. Filled project context can expose internal architecture, deployment topology, database internals, secrets, private prompts, or security assumptions. Publish sanitized templates, not private implementation maps.

### Why use YAML for task tracking?

YAML is easy for humans to read, easy for AI models to update, and structured enough to keep task status consistent across sessions.

## Related Keywords

AI project context protocol, context engineering, AI-assisted development, AI coding assistant workflow, prompt engineering, LLM project memory, AI agent handoff, token optimization, architecture decision records, ADR protocol, Claude Code workflow, Cursor AI workflow, ChatGPT coding workflow, Gemini coding workflow, GitHub Copilot workflow, developer productivity toolkit.

## License

Distributed under the MIT License. See [`LICENSE`](./LICENSE) for details.

**Nexus-APCP: stable project memory for AI-native software engineering.**
