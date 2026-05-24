# Nexus-APCP CodeGraph Integration Protocol
## Local code knowledge graph workflow for AI-assisted development

This protocol adds optional CodeGraph-compatible code intelligence to Nexus-APCP. The goal is to let AI agents answer codebase navigation questions from a local semantic index before spending tokens on broad file scans.

## Source and Attribution

This document was created after reviewing the public CodeGraph repository:

- Source: <https://github.com/colbymchenry/codegraph>
- Reviewed date: 2026-05-20
- Observed license: MIT

Nexus-APCP does not copy upstream instructions, tool schemas, benchmark tables, generated config, or implementation code. This file converts the public idea into Nexus-APCP operating guidance: local-first graph indexing, safe adapter setup, and public/private publishing hygiene.

If a future maintainer copies upstream content directly, they must first review the upstream license, attribution requirements, and whether the copied material belongs in a public MIT-licensed protocol kit.

## Purpose

Large repositories are expensive for AI agents to explore with repeated `rg`, `find`, `ls`, and file reads. A local code knowledge graph can reduce that discovery cost by indexing symbols, call relationships, routes, and related code structure before the agent starts work.

Use this protocol when:

- A codebase is large enough that repeated search and file reads waste time or tokens.
- The user asks for faster architecture discovery, call tracing, impact analysis, or route-to-handler navigation.
- The project already has a local CodeGraph index such as `.codegraph/`.
- A team wants AI agents to prefer local semantic code intelligence without exposing source or generated indexes publicly.

Do not use this protocol as a replacement for tests, source review, security review, or human approval. The graph helps discovery; it does not prove behavior.

## Public and Private Boundary

CodeGraph-style indexes are local operating artifacts. They may contain derived structure, paths, symbol names, and source-adjacent data from the project being indexed.

Keep these local by default:

- `.codegraph/`
- CodeGraph SQLite databases or generated index files.
- Agent-specific generated config that reveals local paths, private project names, or private tool settings.
- Any exported graph, call trace, or impact report that includes private architecture or code excerpts.

Commit only sanitized instructions or templates that do not reveal private implementation details.

## Setup Workflow

For a downstream project:

1. Confirm Node.js and package-manager policy with the user or repo docs.
2. Install CodeGraph using the official upstream package or documented project-approved method.
3. Initialize the project index locally.
4. Confirm `.codegraph/` and generated index artifacts are ignored or locally excluded before any public push.
5. Restart or reload the AI tool if its MCP or local-tool configuration requires it.
6. Run the project's normal validation after using graph-derived findings for edits.

Public-safe example commands:

```bash
npx @colbymchenry/codegraph
codegraph init -i
```

If an AI agent wants to run installer commands, it should first explain what files may be written and whether the setup is global or project-local. In public repositories, prefer local excludes or private global excludes for generated graph artifacts.

## Agent Usage Rules

When a local graph is available:

- Use graph search for symbol, class, function, route, and module discovery before broad text scans.
- Use callers, callees, and impact queries before changing shared interfaces.
- Use route or handler queries before editing web entry points.
- Use graph results as a map, then inspect the exact source files that will be edited.
- Fall back to `rg`, direct file reads, tests, and runtime checks when graph results are missing, stale, ambiguous, or conflict with source.
- Rebuild or refresh the graph after major file moves, generated code changes, dependency updates, or branch switches.

For main-session context hygiene:

- Keep graph queries targeted.
- Avoid dumping large source sections into the main AI response.
- Summarize graph results by symbol, path, relationship, and confidence.
- Use exploration sub-agents only when the tool and user workflow allow delegation.

## Task Fit Matrix

| Task | Recommended graph use | Verification |
| :--- | :--- | :--- |
| Architecture orientation | Find entry points, modules, and high-degree symbols. | Read selected docs and source files. |
| Bug diagnosis | Trace callers, callees, and related symbols around the failing behavior. | Reproduce failure and run regression test. |
| Refactor planning | Check impact radius before changing public interfaces. | Run tests, type checks, and targeted search for references. |
| Route changes | Map URL patterns or route files to handlers. | Run framework route tests or request-level checks. |
| Security-sensitive change | Use graph only for navigation. | Follow private reporting and security verification paths. |
| Documentation update | Use graph to identify accurate names and boundaries. | Verify against source and public-safe docs. |

## Adapter Compatibility Notes

When adding CodeGraph guidance to tool adapter files:

- Keep adapter files short and point back to this protocol.
- Do not paste full upstream generated instructions into public adapter files.
- Do not commit private MCP endpoint details, local absolute paths, or generated allowlists.
- Record only durable behavior: when a graph exists, prefer graph discovery before broad scans; verify edits with source and tests.
- Update `AI_TOOL_ADAPTER_COMPATIBILITY_PROTOCOL.md` when a tool's MCP setup, permissions, or local configuration behavior changes.

## Staleness and Trust Rules

A code graph is stale when:

- The current branch changed since indexing.
- Dependencies generated or removed code.
- Files were moved or renamed.
- The graph reports symbols that no longer exist.
- Test or runtime behavior conflicts with graph-derived expectations.

When stale:

1. Refresh the graph.
2. Repeat the narrow query.
3. Inspect source before editing.
4. Note any graph limitation in the handoff or task notes if it affected the work.

## Nexus-APCP Integration Rules

- Include this protocol in context bundles when code intelligence is part of the project workflow.
- Keep `.codegraph/` and generated graph artifacts out of public commits.
- Use `CONTEXT_OPTIMIZATION.md` to decide whether graph results should replace broad context loading.
- Use `AI_AGENT_SKILLS_PROTOCOL.md` for diagnosis, architecture, and handoff workflows that rely on graph discovery.
- Update `TASK_PROGRESS.yaml` when adding or completing visible code intelligence setup work.
- Update README and SEO metadata when local code graph support is part of public positioning.

## Review Checklist

Before finishing CodeGraph-related changes:

- `.codegraph/` and generated graph artifacts are ignored or locally excluded.
- No private source excerpts, indexes, local paths, or generated MCP configs were committed.
- Adapter guidance is summarized, not copied wholesale from upstream generated output.
- Graph-derived conclusions were verified against source, tests, or docs before edits.
- `python scripts/validate-repo.py` passes.
