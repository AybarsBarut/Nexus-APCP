# AI_MAIN: EXECUTION ORCHESTRATOR

## Purpose
Main function for AI workflow. Sequential logic. Strict execution. No fluff.

This file is a copy-safe starter template. After copying Nexus-APCP into a project, keep all checklist items unchecked until the current project verifies them. Do not carry Nexus-APCP source-repository completion history into downstream projects.

---

## SYSTEM_INIT
- **Protocol**: CAVEMAN optional. Activate only when requested or when `PROMPT_READY.txt` says `Mode: CAVEMAN`.
- **Quality**: production-ready, verified, no simulated work.
- **Safety**: DRY, SOLID, secure, public/private boundary respected.
- **Checkpoints**: mandatory validation at each gate.

---

## EXECUTION_FLOW

1. [ ] **LOAD_CONTEXT**: Read `AI_PROJECT_CONTEXT_PROTOCOL.md`, `TASK_PROGRESS.yaml`, `DECISION_LOG_PROTOCOL.md`, and task-relevant protocol files.
2. [ ] **TASK_ANALYSIS**: Identify user goal, current state, constraints, risks, and expected deliverables.
3. [ ] **MODEL_DISPATCH**: Choose the best available model, tool mode, or agent role for the task.
4. [ ] **IMPLEMENTATION_PLAN**: Define the smallest safe change path and verification evidence.
5. [ ] **IMPLEMENTATION**: Make scoped changes without exposing private context or secrets.
6. [ ] **QUALITY_GATE**: Run required tests, validation scripts, link checks, builds, or manual verification.
7. [ ] **CHECKPOINT_SAVE**: Update `TASK_PROGRESS.yaml` and decision notes only with current project state.
8. [ ] **DELIVERY**: Summarize completed work, verification results, residual risks, and next action.

---

## MODEL_DISTRIBUTION

| Task Type | Recommended Model | Responsibility |
| :--- | :--- | :--- |
| **Logic/Architecture** | strongest reasoning model available | deep reasoning, complex refactors, architecture review |
| **Boilerplate/Style** | fast implementation model | repetitive edits, formatting, straightforward docs |
| **Testing/Security** | strongest review model available | bug hunting, edge cases, security and privacy checks |
| **Coordination** | agent manager or current assistant | handoff, state sync, multi-agent conflict control |

---

## ACTIVE_TASK_LIST

> [!IMPORTANT]
> Mark `[x]` only when the current project has verified the task. Replace placeholder tasks before the first real session.

- [ ] TASK-001: [FIRST_TASK_TITLE]
- [ ] TASK-002: [SECOND_TASK_TITLE]
- [ ] TASK-003: [THIRD_TASK_TITLE]

---

## CHECKPOINTS

- [ ] **CP1_CONTEXT_SYNC**: Required project context loaded.
- [ ] **CP2_PLAN_READY**: Implementation path and risks understood.
- [ ] **CP3_VERIFICATION**: Tests, validation, or manual checks passed.
- [ ] **CP4_STATE_UPDATE**: `TASK_PROGRESS.yaml` reflects only current project state.
- [ ] **CP5_DELIVERY**: User-facing summary prepared.

---

## OPERATING_RULES

- Preserve the public/private boundary from `AI_PROJECT_CONTEXT_PROTOCOL.md` and `DOMAIN_SPECIFIC_GITIGNORE_PROTOCOLS.md`.
- Keep generated prompt bundles such as `PROMPT_READY.txt` out of public commits.
- Prefer current project evidence over copied template state.
- If context is stale or contradictory, stop and reconcile before implementation.

---

*Nexus-APCP: logic first, tokens last.*
