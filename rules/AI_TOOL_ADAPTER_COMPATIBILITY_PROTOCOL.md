# Nexus-APCP AI Tool Adapter Compatibility Protocol
## Safe compatibility checks for AI coding assistants, models, tools, and prompt surfaces

This protocol helps a project work consistently across AI coding assistants without copying vendor system prompts, leaked prompt text, private tool schemas, or model-specific internals into a public repository.

## Source Review Boundary

This file was created after reviewing the repository structure, license, and public framing of:

- Source: <https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools>
- Reviewed date: 2026-05-19
- Observed license: GPL-3.0

No upstream system prompt text, tool schema, model transcript, proprietary instruction block, or prompt-extraction detail is copied or paraphrased here. Nexus-APCP uses the review only as a signal that AI coding tools differ in operating modes, tool access, context loading behavior, and safety boundaries.

If a future maintainer wants to copy any upstream material directly, they must first check license compatibility, attribution requirements, and whether the content is appropriate for a public MIT-licensed protocol kit.

## Purpose

AI tools do not behave the same way. One assistant may default to planning, another may edit files immediately, another may require explicit browser verification, and another may hide tool behavior behind an IDE workflow. This protocol gives teams a safe adapter layer so those differences are documented without importing private prompts.

Use this protocol when:

- Adding support guidance for Claude Code, Cursor, ChatGPT, Gemini, Copilot, local LLMs, IDE agents, or CLI agents.
- Updating short adapter files such as `CLAUDE.md`, `CURSOR.md`, `CODEX.md`, `GEMINI.md`, or `COPILOT.md`.
- Comparing AI tools for a project workflow.
- Debugging repeated AI behavior differences across tools.
- Preparing a model switch or multi-agent workflow.
- Reviewing public prompt archives, tool manifests, or model-behavior notes for lessons that can be converted into safe project rules.

## Compatibility Inventory

For each AI tool used by the project, record behavior at the level a maintainer can verify without relying on leaked internals.

| Field | What to capture | Public-safe example |
| :--- | :--- | :--- |
| Adapter file | Which local file gives startup guidance. | `CODEX.md` points to `AGENTS.md` and tool-specific startup notes. |
| Primary mode | How the tool usually starts work. | Planning-first, chat-first, edit-first, review-first, or issue-first. |
| Execution tools | What the assistant can operate. | Shell, file edit, browser, tests, package manager, issue tracker, or MCP connector. |
| Context loading | How it should read Nexus-APCP. | Start with `AGENTS.md`, then selected protocol files, then task state. |
| Local code graph | Whether CodeGraph-compatible tools or `.codegraph/` indexes are available. | Prefer graph lookup for symbol discovery, caller/callee tracing, route mapping, and impact checks. |
| Verification path | How it proves work. | Run tests, render docs, open browser, validate links, or inspect generated files. |
| Output style | What response format works best. | Short status updates, findings-first review, patch summary, or handoff note. |
| Git behavior | What the tool may do. | Inspect diffs freely; stage, commit, push, or branch only when requested. |
| Known drift risk | What changes over time. | Model naming, context windows, tool availability, IDE permissions, or browsing access. |
| Last verified | Date and evidence. | `2026-05-19`, tested with local validation script. |

## Adapter File Rules

Adapter files should stay short. They should not become full prompt mirrors.

Good adapter files:

- Point back to `AGENTS.md` and the relevant Nexus-APCP protocol files.
- Name only tool-specific startup behavior that helps the assistant operate correctly.
- Avoid repeating the full project context.
- Avoid hardcoding model versions unless the behavior truly depends on that version.
- Keep public/private boundaries visible.
- Tell the tool which local validation commands matter.
- Point to `CODEGRAPH_INTEGRATION_PROTOCOL.md` when the project uses local code graph discovery.

Do not add:

- Vendor system prompts or extracted internal policy blocks.
- Full tool schemas copied from a proprietary assistant.
- Prompt injection bypass text, jailbreak patterns, or prompt-extraction recipes.
- Private model routing notes, customer prompts, hidden chain-of-thought requests, or internal evaluation data.
- Secrets, local credentials, private MCP endpoints, customer data, or generated prompt bundles.
- Generated CodeGraph configs, `.codegraph/` indexes, local database paths, or private MCP allowlists.

## Tool Mode Matrix

Use this matrix when deciding whether a project needs a specific adapter note.

| Mode | What to document | APCP rule |
| :--- | :--- | :--- |
| Chat mode | How the user provides context and asks questions. | Load only the relevant protocol sections and task state. |
| Agent mode | Whether the tool can edit files, run commands, or browse. | Require scoped edits, verification, and task progress updates. |
| Plan mode | Whether the tool should ask before implementation. | Use when the user explicitly requests planning or decisions are risky. |
| Spec mode | Whether the tool writes requirements before code. | Link to PRD, issue, waterfall, or delivery protocol guidance. |
| Review mode | Whether the tool prioritizes findings. | Use findings-first code-review output with file and line references. |
| Prototype mode | Whether throwaway experiments are allowed. | Mark prototypes as disposable and capture the answer before cleanup. |
| Multi-agent mode | Whether parallel workers can act safely. | Split ownership by files or modules and prevent overlapping edits. |
| Local graph mode | Whether the assistant can query a local code knowledge graph. | Use graph lookup for navigation, then verify source and tests before editing. |

## Safe Prompt Archive Review

Public prompt archives can still be useful if they are treated as research signals, not as content to vendor.

Allowed:

- Identify broad categories such as plan mode, tool calling, browser verification, file editing, handoff, or safety checks.
- Convert common patterns into original project rules.
- Cite the reviewed repository as inspiration or input when appropriate.
- Prefer official documentation when claiming how a current tool works.
- Keep summaries at the level of workflow design, not prompt reconstruction.

Not allowed:

- Copying or lightly rewriting full system prompts.
- Importing exact proprietary tool definitions.
- Adding instructions that help extract hidden prompts from live services.
- Describing exploit paths or bypasses in public docs.
- Treating unofficial prompt dumps as current product documentation.

## Model and Tool Drift Protocol

AI tools change quickly. Update adapter compatibility notes when:

- A tool gains or loses file edit, shell, browser, connector, or automation access.
- A model family changes context window, tool-use behavior, or response policy in a way that affects APCP.
- A short adapter file starts conflicting with `AGENTS.md`.
- A recurring assistant failure traces back to ambiguous startup instructions.
- Official docs or release notes change a workflow that the project depends on.

Update record:

```yaml
adapter_compatibility_update:
  date: "YYYY-MM-DD"
  tool: "[assistant or IDE agent]"
  observed_change: "[short behavior change]"
  project_impact: "[what must change in APCP or adapter files]"
  files_updated:
    - "[path]"
  verification:
    - "[command or manual check]"
```

## Sanitized Compatibility Matrix Template

Copy this into private project docs when a team wants a tool-by-tool view.

```markdown
| Tool | Adapter file | Mode default | Tools available | Context entry | Verification | Last verified |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [Tool name] | `[FILE].md` | [chat/agent/plan/review] | [shell/files/browser/etc.] | `AGENTS.md` plus [files] | [commands] | [date] |
```

Keep the matrix behavior-focused. Do not include secret project prompts, private provider instructions, or copied system prompt text.

## Nexus-APCP Integration Rules

- Read this protocol when adding or revising AI tool adapter files.
- Use it before importing ideas from prompt archives, model dumps, or unofficial tool manifests.
- Keep adapter notes model-agnostic unless a version-specific rule is necessary and verified.
- Prefer official documentation for current product behavior; use public prompt archives only as historical or comparative input.
- Update `TASK_PROGRESS.yaml` when completing a visible adapter compatibility task.
- Update README and SEO metadata when adapter compatibility becomes part of the public positioning.
- Keep generated `PROMPT_READY.txt`, private prompts, and filled project context out of public commits.

## Review Checklist

Before finishing adapter compatibility changes:

- No copied vendor system prompt text.
- No prompt-extraction, bypass, or jailbreak instructions.
- No private tool schemas, secrets, customer data, local endpoints, or generated prompt bundles.
- Adapter files stay short and point back to canonical Nexus-APCP files.
- `scripts/apcp-gather.py --caveman` includes this protocol when compatibility guidance is core to the project.
- `scripts/validate-repo.py` passes.
