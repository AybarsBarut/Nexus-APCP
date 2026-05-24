# Nexus-APCP AI Agent Skills Protocol
## Skill-based workflows for AI-assisted development

This protocol adds a model-agnostic skill layer to Nexus-APCP. A skill is a compact, named workflow that an AI agent can invoke when the user asks for a specific kind of work: diagnosis, TDD, triage, PRD creation, handoff, architecture review, prototyping, or token-compressed communication.

## Source and Attribution

This document adapts public ideas from Matt Pocock's `skills` repository:

- Source: <https://github.com/mattpocock/skills>
- Reviewed snapshot: `67bce91c80cd1020a4f068ced32d0281656842ad`
- Snapshot date: 2026-05-18
- License: MIT
- Copyright notice in upstream source: Copyright (c) 2026 Matt Pocock

This file is a Nexus-APCP synthesis, not a verbatim mirror. If a project copies original upstream skill text, scripts, or templates substantially, include the upstream MIT license notice with that copied material.

## Purpose

Agent skills solve a different problem than full project context. APCP tells the agent what the project is. Skills tell the agent how to behave for a repeated kind of task.

Use this protocol when:

- The same AI workflow repeats often enough to deserve a name.
- The workflow has a clear trigger, inputs, steps, and output.
- The task benefits from strict sequencing or quality gates.
- The agent should avoid improvising a process from scratch.
- Multiple AI tools should share the same operating pattern.

## Core Principles

- Keep skills small, composable, and easy to adapt.
- Prefer skill descriptions that tell the agent exactly when to load the skill.
- Separate hard dependencies from soft dependencies.
- Use project vocabulary from `AI_PROJECT_CONTEXT_PROTOCOL.md`, `CONTEXT.md`, or `CONTEXT-MAP.md`.
- Record durable decisions in `DECISION_LOG_PROTOCOL.md` or `docs/adr/`.
- Prefer feedback loops over speculation.
- Break work into vertical slices that can be verified independently.
- Write issues, briefs, PRDs, and handoffs as durable behavior contracts, not path-by-path instructions.
- Use prototypes to answer a question, then delete or absorb them.
- Keep public repositories sanitized: no private context, secrets, customer data, internal security details, or generated prompt bundles.

## Skill Buckets

| Bucket | Role | Nexus-APCP treatment |
| :--- | :--- | :--- |
| Engineering | Daily code work such as diagnosis, TDD, triage, PRDs, architecture improvement, prototyping, and zoom-out explanations. | Promote as reusable operating protocols. |
| Productivity | Communication and session-flow helpers such as Caveman Mode, grilling, handoff, and skill writing. | Promote where they improve context quality and token use. |
| Misc | Optional repo hygiene or niche migrations. | Include as optional recipes, not core requirements. |
| Personal | Workflows tied to one maintainer's local setup. | Do not copy as-is; extract only generic ideas. |
| In progress | Draft workflows that may change. | Treat as experimental patterns. |
| Deprecated | Older workflows replaced by better patterns. | Do not install by default; mine only the lesson learned. |

## Skill Registry

Use this registry as a model-agnostic equivalent of slash commands. Agents can invoke the skill by name when the user request matches the trigger.

| Skill | Use when | Output |
| :--- | :--- | :--- |
| `diagnose` | User reports a bug, failure, broken behavior, or performance regression. | Reproduction loop, ranked hypotheses, targeted instrumentation, fix, regression proof, cleanup notes. |
| `codegraph-explore` | User asks how code is connected, where a symbol lives, who calls what, which routes hit a handler, or what a change impacts. | Targeted local graph query plan, source verification list, and confidence notes. |
| `grill-with-docs` | User wants to stress-test a code or architecture plan against project language and decisions. | One-question-at-a-time interview, updated glossary, optional ADR. |
| `triage` | User wants to classify, clarify, route, or prepare issues. | Issue state recommendation, reporter questions, ready-for-agent brief, or out-of-scope record. |
| `improve-codebase-architecture` | User wants refactoring opportunities, better testability, or less tangled architecture. | Numbered deepening candidates with files, problem, solution, benefits, and test impact. |
| `setup-agent-skills` | A repo needs skill configuration for issue tracker, triage labels, and domain docs. | Agent skills block plus `docs/agents/` configuration files. |
| `tdd` | User wants test-first feature work or bug fixing. | One behavior test at a time, minimal implementation, refactor after green. |
| `to-issues` | User wants a plan, PRD, or spec broken into implementation issues. | Vertical-slice issues with dependencies, AFK/HITL classification, and acceptance criteria. |
| `to-prd` | User wants the current context turned into a PRD. | PRD with problem, solution, user stories, implementation decisions, testing decisions, out of scope, notes. |
| `zoom-out` | User is unfamiliar with code and needs the bigger map. | Higher-level module and caller explanation using project vocabulary. |
| `prototype` | User wants to explore a state model, data model, flow, or UI before committing. | Throwaway runnable prototype plus captured answer. |
| `caveman` | User asks for short, token-light, high-signal communication. | Terse technical responses that preserve exact meaning. |
| `grill-me` | User wants a plan challenged outside a codebase-specific context. | One-question-at-a-time design interview with recommended answers. |
| `handoff` | User wants another agent or session to continue. | Compact handoff document that references existing artifacts instead of duplicating them. |
| `write-a-skill` | User wants to create a new skill. | Skill folder design, trigger description, main instructions, optional references and scripts. |
| `git-guardrails` | User wants to block risky Git operations in an agent tool. | Hook or policy that blocks push, hard reset, clean, destructive branch deletion, and broad restore. |
| `setup-pre-commit` | User wants commit-time formatting, type checking, or tests. | Pre-commit setup adapted to the detected package manager. |
| `migrate-test-assertions` | User wants to replace unsafe TypeScript test assertions with a safer helper. | Test-only migration plan and verification. |
| `scaffold-exercises` | User wants structured exercise folders. | Section/exercise directories, stub readmes, linter-compatible layout. |

## Setup Protocol

Before using issue-writing, triage, PRD, or issue-breakdown skills, configure the repo once.

1. Inspect existing agent docs: `AGENTS.md`, `CLAUDE.md`, `CODEX.md`, `GEMINI.md`, `CURSOR.md`, `COPILOT.md`.
2. Inspect context docs: `AI_PROJECT_CONTEXT_PROTOCOL.md`, `CONTEXT.md`, `CONTEXT-MAP.md`, `DECISION_LOG_PROTOCOL.md`, `docs/adr/`.
3. Inspect issue workflow: GitHub Issues, GitLab Issues, Linear, Jira, local markdown, or other.
4. Ask the user one decision at a time:
   - Where do issues live?
   - What labels or states map to triage roles?
   - Is domain context single-context or multi-context?
5. Write or update `docs/agents/issue-tracker.md`.
6. Write or update `docs/agents/triage-labels.md`.
7. Write or update `docs/agents/domain.md`.
8. Add or update an `Agent skills` block in the adapter file already used by the repo.

Do not create duplicate adapter files. If the repo already uses `AGENTS.md`, update it. If it uses a tool-specific file, update that one and keep it short.

Example block:

```markdown
## Agent skills

### Issue tracker

Issues live in [GitHub Issues / local markdown / other]. See `docs/agents/issue-tracker.md`.

### Triage labels

Triage roles map to existing labels. See `docs/agents/triage-labels.md`.

### Domain docs

This repo uses [single-context / multi-context] domain docs. See `docs/agents/domain.md`.
```

## Dependency Rules

Some skills cannot work correctly without repo configuration.

Hard dependency skills:

- `to-issues`
- `to-prd`
- `triage`

These need issue tracker and label mapping before publishing or modifying issues.

Soft dependency skills:

- `diagnose`
- `tdd`
- `improve-codebase-architecture`
- `zoom-out`
- `prototype`

These should read domain language and ADRs when present, but they can still operate when those docs are missing.

## Domain Language Protocol

Use a project glossary to reduce ambiguity and token cost.

Single-context repo:

```text
/
  CONTEXT.md
  docs/adr/
```

Multi-context repo:

```text
/
  CONTEXT-MAP.md
  docs/adr/
  src/<context>/CONTEXT.md
  src/<context>/docs/adr/
```

`CONTEXT.md` is a glossary, not a spec. It should define domain terms, avoided aliases, relationships, example dialogue, and flagged ambiguities. Keep implementation details in APCP, architecture docs, PRDs, or ADRs.

When a term is resolved during a planning conversation, update the glossary immediately. When a decision is hard to reverse, surprising without context, and based on a real tradeoff, record an ADR or a decision-log entry.

## Grilling Protocol

Use grilling before major implementation when the user has a fuzzy plan.

Rules:

- Ask one question at a time.
- Provide your recommended answer with each question.
- If the answer is discoverable from the codebase, inspect the code instead of asking.
- Challenge overloaded terms against the project glossary.
- Stress-test edge cases with concrete scenarios.
- Update glossary terms as they crystallize.
- Offer ADRs only for durable, surprising tradeoffs.

## Diagnosis Protocol

Use this for bugs and performance regressions.

1. Build a fast pass/fail feedback loop before theorizing.
2. Reproduce the user's exact symptom.
3. Generate 3 to 5 ranked, falsifiable hypotheses.
4. Instrument one prediction at a time.
5. Add a regression test at the correct behavior boundary when possible.
6. Fix the issue and rerun the original loop.
7. Remove temporary instrumentation and prototypes.
8. State what prevented fast diagnosis and whether architecture should improve.

Feedback loops can be tests, HTTP scripts, CLI fixtures, browser automation, captured trace replay, throwaway harnesses, fuzz loops, bisection, differential comparison, or a structured human-in-the-loop script.

For nondeterministic bugs, raise the reproduction rate with loops, stress, seeds, timing controls, or parallel runs until the bug can be reasoned about.

When `CODEGRAPH_INTEGRATION_PROTOCOL.md` is installed and a local `.codegraph/` index exists, use graph discovery to find the affected symbols, callers, callees, and route bindings before broad file scans. Verify graph findings against source and tests before applying the fix.

## TDD Protocol

Use this for test-first implementation.

- Test observable behavior through public interfaces.
- Write one failing behavior test at a time.
- Implement only enough code to pass the current test.
- Do not write all tests first and implementation later.
- Refactor only after the suite is green.
- Mock only system boundaries such as external APIs, time, randomness, filesystem, or external services.
- Prefer test databases or real local seams where practical.
- Design interfaces so dependencies are passed in, results are returned, and surface area stays small.

Good test names describe what the system does. Bad tests overfit private methods, call counts, internal collaborators, line numbers, or database rows that bypass the public interface.

## Architecture Deepening Protocol

Use this when the codebase feels hard to test, hard to navigate, or spread across too many shallow modules.

Vocabulary:

- Module: anything with an interface and implementation.
- Interface: everything a caller must know to use the module.
- Implementation: code hidden behind the interface.
- Depth: leverage provided by a small interface over meaningful behavior.
- Seam: where behavior can be altered without editing callers.
- Adapter: concrete implementation used at a seam.
- Leverage: what callers gain from the module.
- Locality: how much change and knowledge stay in one place.

Process:

1. Read domain language and relevant ADRs.
2. Explore the code organically and note friction.
3. Apply the deletion test: if deleting a module removes complexity, it was probably pass-through; if complexity spreads to callers, it was earning its keep.
4. Present deepening opportunities with files, problem, solution, benefits, and test impact.
5. Let the user choose which opportunity to explore.
6. Grill the interface shape before implementation.
7. Record new terms or rejected durable refactor ideas.

## Issue and PRD Protocol

Use durable issue language.

Write what behavior should exist, not which file or line to edit. File paths and line numbers go stale. Types, public interfaces, contracts, config shapes, current behavior, desired behavior, acceptance criteria, and scope boundaries are more durable.

Vertical slice rules:

- Each slice should deliver a narrow complete path through the system.
- Each slice should be demoable or independently verifiable.
- Prefer many thin slices over a few broad ones.
- Mark slices as AFK when an agent can complete them without human input.
- Mark slices as HITL when decisions, access, design review, or manual judgment are required.

Recommended PRD sections:

- Problem Statement
- Solution
- User Stories
- Implementation Decisions
- Testing Decisions
- Out of Scope
- Further Notes

Recommended agent brief sections:

- Category
- Summary
- Current behavior
- Desired behavior
- Key interfaces
- Acceptance criteria
- Out of scope

## Triage Protocol

Use two role categories:

- `bug`: something is broken.
- `enhancement`: a new feature or improvement.

Use one state role at a time:

- `needs-triage`: maintainer evaluation needed.
- `needs-info`: reporter must answer specific questions.
- `ready-for-agent`: fully specified and AFK-ready.
- `ready-for-human`: requires human judgment or access.
- `wontfix`: will not be actioned.

Map these canonical roles to actual issue labels in `docs/agents/triage-labels.md`.

When posting AI-generated triage notes to an external issue tracker, include a clear AI-generated disclosure and follow the repo's contribution policy.

For rejected enhancements, maintain a durable out-of-scope knowledge base when the project wants one:

```text
.out-of-scope/
  dark-mode.md
  plugin-system.md
```

One file per rejected concept. Include the decision, durable reason, and prior requests. Check this directory during future triage to avoid re-litigating the same scope decision.

## Prototype Protocol

A prototype answers one question.

Use a logic prototype when the question is about state, data flow, rules, or business logic. Use a UI prototype when the question is about screen shape, interaction, layout, or visual alternatives.

Rules:

- Mark prototype code as throwaway from the start.
- Put it close enough to the real code that context is obvious.
- Provide one command to run it.
- Avoid persistence by default.
- Surface relevant state after each action.
- Skip production polish.
- Delete, absorb, or explicitly quarantine it when done.
- Capture the answer in an ADR, issue, note, or commit message.

## Handoff Protocol

Use handoff when another agent or future session will continue the work.

The handoff should:

- State the next session's focus.
- Reference existing PRDs, issues, ADRs, plans, commits, or diffs by path or URL.
- Avoid duplicating content already stored elsewhere.
- List suggested skills for the next session.
- Include current blockers and verification status.

## Skill Writing Protocol

Create a new skill when a workflow repeats and the description can reliably trigger it.

Recommended structure:

```text
skill-name/
  SKILL.md
  REFERENCE.md
  EXAMPLES.md
  scripts/
    helper.js
```

`SKILL.md` should include frontmatter:

```markdown
---
name: skill-name
description: Brief capability. Use when the user asks for specific trigger contexts.
---
```

Description rules:

- Keep it short enough for an agent skill registry.
- First sentence says what the skill does.
- Second sentence says when to use it.
- Include concrete triggers, file types, or phrases.

Split reference files when the main skill grows too long or mixes rare advanced material with common flow. Add scripts when a deterministic task would otherwise be generated repeatedly.

## Optional Hygiene Recipes

Git guardrails:

- Block `git push`, force push, hard reset, clean, destructive branch deletion, and broad checkout/restore unless the user explicitly authorizes the action.
- Merge hooks with existing settings instead of overwriting them.
- Test the hook with a known blocked command before declaring success.

Pre-commit setup:

- Detect the package manager from lockfiles.
- Add formatting for staged files.
- Add typecheck and test commands only if they exist.
- Verify the hook before committing.

Test assertion migration:

- Limit migration helpers to test code.
- Replace unsafe assertions with typed partial or intentionally-any helpers only where they improve clarity.
- Run typecheck after migration.

Exercise scaffolding:

- Use predictable numeric prefixes.
- Keep names dash-case.
- Ensure each problem, solution, or explainer folder has a non-empty readme.
- Run the course or repo linter after scaffolding.

## Experimental and Deprecated Lessons

The upstream repository also contains personal, in-progress, and deprecated skills. Nexus-APCP should not promote those as stable core workflows, but the ideas are useful:

- Two-axis review separates standards conformance from spec fulfillment.
- Writing-fragment workflows capture raw ideas before forcing structure.
- Beat-based writing grows narrative one move at a time.
- Article-shaping workflows treat raw notes as read-only source material and build a separate article.
- Obsidian workflows show how index notes and backlinks can support AI research memory, but local personal paths must not be copied.
- Deprecated QA and refactor-plan skills reinforce the same durable-issue pattern now covered by triage, PRD, and vertical-slice issue workflows.
- Deprecated ubiquitous-language workflow is better represented as `CONTEXT.md` plus glossary updates during grilling.
- Deprecated interface-design workflow is better folded into architecture deepening and TDD interface planning.

## Nexus-APCP Integration Rules

- Read `AI_AGENT_SKILLS_PROTOCOL.md` when the user invokes a named skill, asks for slash-command-like workflow, or requests repeated agent behavior.
- Add this file to context bundles when skill-aware operation is desired.
- Keep adapter files short; point them to this protocol instead of copying the full registry into every adapter.
- Update `TASK_PROGRESS.yaml` when adding, changing, or completing a visible skill-related repository task.
- Update SEO metadata when positioning changes to include agent skills or skill-based workflows.
- Keep all examples public-safe and sanitized.

## Review Checklist

Before completing skill-related changes:

- Required files still exist.
- Skill docs do not include private context or personal local paths unless clearly sanitized examples.
- Issue tracker config does not include private tokens, customer data, or internal security details.
- New markdown links resolve.
- JSON and YAML files parse.
- `python scripts/apcp-gather.py --caveman` passes.
- `python scripts/validate-repo.py` passes.
