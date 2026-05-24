# Nexus-APCP: AI Project Context Protocol (Session Starter)
## Lightweight Project Context Protocol for AI coding assistants

---

## QUICK START

This file is the **single source of truth** for AI coding assistants to understand the core identity of this project.
For detailed architectural references, codebase patterns, and full workflows, refer to `templates/AI_PROJECT_REFERENCE_PROTOCOL.md`.

### Active Context Profile
Nexus-APCP supports profile-based context loading. Use `apcp-init.py` to choose your stack and generate relevant constraints.

---

## SECTION 1: GENERAL PROJECT INFORMATION

```yaml
Project Name: [PROJECT_NAME]
Description: [PROJECT_DESCRIPTION]
Owner: [OWNER_NAME/ORGANIZATION]
Main Language/Stack: [Python/JS/C++/Unity/etc]
```

### Goals
1. [Goal 1]
2. [Goal 2]

---

## SECTION 2: SECURITY AND RULES

1. **Never Commit Secrets**: .env files, API keys, and database passwords must remain local.
2. **Follow Stack Constraints**: Obey the tech stack chosen during initialization. Do not assume Python/Flask if the stack is Unity/C#.
3. **Keep Context Private**: Do not commit filled context files or internal architecture maps to public repositories unless explicitly sanitized.

---

## SECTION 3: TASK TRACKING

Progress is tracked in `TASK_PROGRESS.yaml`.
- Before starting a task: Read the YAML file, identify dependencies, set status to `IN_PROGRESS`.
- Upon completion: Mark as `COMPLETED`, update actual effort, and write a summary.
- **Sprint Archiving**: Completed sprints are archived in the `archive/` folder (e.g., `archive/sprint-1.yaml`) to prevent file bloat.

---

## SECTION 4: AI PROTOCOLS (CAVEMAN & EMOJI)

- **Emoji Policy**: Do NOT use emojis in code, docs, UI, or AI responses unless explicitly approved as a temporary UI placeholder.
- **Caveman Mode**: When activated, prioritize extreme token efficiency. Use sentence fragments, remove politeness, and skip unnecessary explanations. Provide code directly.

*(Note: See `CONTRIBUTING.md` for full details on these protocols.)*
