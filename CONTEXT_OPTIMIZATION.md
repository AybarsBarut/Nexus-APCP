# 📉 Nexus-APCP Context Window Optimization Strategy

## 🎯 The Problem
As a software project grows, the codebase and documentation eventually exceed the context window (token limit) of AI coding assistants, AI agents, and LLMs. This results in the AI "forgetting" critical rules or making inconsistent decisions.

## 🧩 Modular Context Strategy

### Level 1: Standard (Bootstrap Mode)
**Usage**: When starting a new session or a new project.
- **Files**: Full `AI_PROJECT_CONTEXT_PROTOCOL.md` + Full `TASK_PROGRESS.yaml`.
- **Token Impact**: ~3,000 - 5,000 tokens.

### Level 2: Focused (Deep Work Mode)
**Usage**: When working on a specific module for an extended period.
- **Rules**: `AI_PROJECT_CONTEXT_PROTOCOL.md` (Sections 1-6 only: Identity, Hierarchy, Imports, Security, Patterns, Git).
- **Module Context**: Only the specific documentation for the current module (e.g., `docs/USER_SERVICE.md`).
- **History**: The last 3 entries from the `docs/ADR/` (Decision Logs).
- **Token Impact**: ~2,000 tokens.

### Level 3: Minimal (Fix/Maintenance Mode)
**Usage**: Small bug fixes or minor updates.
- **Identity**: `AI_PROJECT_CONTEXT_PROTOCOL.md` (Section 1 and 2 only).
- **Task**: Only the specific `TASK-XXX` block from `TASK_PROGRESS.yaml`.
- **Current File**: The content of the file being fixed.
- **Token Impact**: ~1,000 tokens.

## 📦 Context Archiving
When `TASK_PROGRESS.yaml` becomes too large:
1. Move completed tasks from the previous month to `docs/archive/TASKS_2024_Q1.yaml`.
2. Keep only the "Sprint Summary" and "Current Sprint" in the active file.

## 🤖 AI Instructions
If you detect that the context is getting too large (e.g., truncated responses or confusion), suggest switching to **Level 2** or **Level 3** context.
