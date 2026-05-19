# Nexus-APCP AI Assistant Prompt Templates
## Ready-to-use prompts for AI-assisted development scenarios

---

## SCENARIO 0: Initializing the "Second Brain" (NotebookLM / Obsidian Sync)
**Objective:** Transform structured APCP context into a high-density Knowledge Base optimized for RAG-based tools (NotebookLM) or linked-note systems (Obsidian). This is critical for team onboarding and multi-model synchronization.

**Prompt to send to AI:**
```text
I want to establish a "Second Brain" Knowledge Base for this project to support team onboarding and multi-AI coordination.

Using the current APCP documents (Context Protocol, Task Progress, and Decision Log), please generate a "Project Wisdom Center" export. 

The output should be a structured Markdown document optimized for NotebookLM (RAG) and Obsidian Vault, covering:
1. Strategic Roadmap: The project's "North Star" and core tech stack rationale.
2. Architectural DNA: Logical summary of the folder structure and data flow patterns.
3. Decision Archive: Summary of key technical decisions (ADRs) and "rejected paths" to avoid refactor loops.
4. Onboarding Guide: Top 3 rules a new developer must know and "low-hanging fruit" tasks for immediate contribution.

Format the output to be instructive and mentor-like, ensuring all technical terms and file paths are explicitly linked for better AI retrieval.
```

---

## SCENARIO 1: Starting a Project for the First Time (Recommended)

Copy and send to the AI in the same session:

```
I'm starting to work on a new project and want to use an AI-assisted workflow.

I've prepared:
1. AI_PROJECT_CONTEXT_PROTOCOL.md - A comprehensive protocol for you to understand the project
2. TASK_PROGRESS.yaml - Task tracking and project status

Please:
1. **Carefully read** both files in order
2. Summarize what you understand:
   - Project name, goals, and scope
   - Folder structure and key modules
   - Current tasks and their status
   - Any blockers or dependencies
3. Ask me clarifying questions about:
   - Technology stack (frameworks, databases, etc.)
   - Development environment setup
   - Any missing details
4. Propose a first task/step we should take

Let's make sure we're on the same page before diving into code.
```

---

## SCENARIO 2: Continuing with the Same Model

If you are close to the token limit and continuing with the same model:

```
Continuing work on [PROJECT_NAME].

Here are the latest project documents:

[PASTE: AI_PROJECT_CONTEXT_PROTOCOL.md]

[PASTE: TASK_PROGRESS.yaml - Only current sprint section]

What I need you to do:
1. Identify the last completed task
2. Check for any blockers on the next task
3. Tell me: "Next step: [Task], starting with: [Subtask]"
4. Ready to implement

Let's go!
```

---

## SCENARIO 3: Switching to a New Model

If you are changing models or have reached the token limit:

```
I'm switching to a new AI model on [PROJECT_NAME].

This is the complete project context and status:

[PASTE: AI_PROJECT_CONTEXT_PROTOCOL.md - FULL]

[PASTE: TASK_PROGRESS.yaml - FULL]

Here's what I need:
1. Review and acknowledge you understand the project architecture
2. Identify the current status:
   - Last completed task: _______
   - Current blockers: _______
   - Next immediate action: _______
3. List any clarifications you need

We'll continue exactly where we left off.
```

---

## SCENARIO 4: Code Review Session

To review existing code:

```
I need a comprehensive code review for [PROJECT_NAME] before we merge.

Here's the project context:

[PASTE: AI_PROJECT_CONTEXT_PROTOCOL.md - SECTIONS 2, 3, 5 only]

Here's the code I want reviewed:

[PASTE: Modified files or PR diff]

Please review against:
1. Section 5 (Code Structure and Design Patterns)
2. Section 3 (Common Functions and Imports)
3. Section 14 (Best Practices)
4. Section 15 (Code Review Checklist)

Give me:
- What looks good
- Issues/concerns
- Suggested improvements
- Before you approve, I'll:
```

---

## SCENARIO 5: Editing Documentation

When documentation needs updating:

```
Help me update/create documentation for [PROJECT_NAME].

Current project structure:

[PASTE: AI_PROJECT_CONTEXT_PROTOCOL.md - SECTION 8 only]

I need to create/update: [docs/API.md / docs/ARCHITECTURE.md / docs/SETUP.md]

Here's what should be documented:
1. [Feature/System/Component Description]
2. [Technical details]
3. [Code examples]

Use the templates from AI_PROJECT_CONTEXT_PROTOCOL.md Section 8 and make sure it's:
- Clear for new developers
- Includes code examples
- Links to relevant internal docs
- Follows existing documentation style

Draft the documentation for me.
```

---

## SCENARIO 6: Bug Fix / Hotfix

When an urgent bug fix is needed:

```
Quick fix needed for [PROJECT_NAME]:

Bug: [Description]
Impact: [Severity]
Affected Component: [src/api/ | src/services/ | etc]

Context:
[PASTE: AI_PROJECT_CONTEXT_PROTOCOL.md - SECTIONS 2, 3, 5 (minimal)]
[PASTE: Relevant code snippet]

Steps:
1. Find root cause
2. Propose fix (code + tests)
3. Run checkpoint (Section 6.4)
4. Generate commit message (Section 6.2 format)

Let's move fast but safe.
```

---

## SCENARIO 7: Architecture Decision

When an architectural decision or refactoring is needed:

```
I need help with an architecture decision for [PROJECT_NAME].

Current architecture:

[PASTE: AI_PROJECT_CONTEXT_PROTOCOL.md - SECTIONS 2, 5]

[PASTE: docs/ARCHITECTURE.md - if exists]

Question/Problem:
[Your architecture question]

Please:
1. Analyze current architecture constraints
2. Propose 2-3 solutions with pros/cons
3. Recommend one approach
4. Show how it fits with existing code structure

Let's think this through before we code.
```

---

## SCENARIO 8: Performance Optimization

When performance improvement is needed:

```
Help me optimize [PROJECT_NAME] for performance.

Current bottleneck: [Description]
Metrics:
- Current: [X]ms response time / [Y]% CPU usage / [Z]MB memory
- Target: [X']ms / [Y']% / [Z']MB

Relevant code:
[PASTE: Slow code section]

Context:
[PASTE: AI_PROJECT_CONTEXT_PROTOCOL.md - Section 5 (Code Patterns)]

Please:
1. Identify the root cause
2. Suggest optimization strategies
3. Show before/after code
4. Estimate performance improvement
5. Provide benchmarking code

Let's make it faster.
```

---

## SCENARIO 9: Dependency/Library Update

When updating a library or adding a new dependency:

```
I want to update/add a dependency in [PROJECT_NAME].

Current dependency:
[Library name and version]

Reason for update:
[Security patch / New features / Performance / etc]

Questions:
1. Is it safe to update to [new version]?
2. Are there breaking changes?
3. Do we need to update our code?
4. Impact assessment?

Context:
[PASTE: AI_PROJECT_CONTEXT_PROTOCOL.md - Section 9.4 (Libraries)]

Help me make this update safely.
```

---

## SCENARIO 10: Task Not Started Yet

Time to start a new task:

```
Starting TASK-XXX: [Task Title]

Task details:

[PASTE: AI_PROJECT_CONTEXT_PROTOCOL.md - Section 7 (Task Management)]

[PASTE: TASK_PROGRESS.yaml - Just the TASK-XXX section]

Here's what I want you to do:

1. Break down the subtasks into concrete steps
2. Identify any dependencies or blockers
3. Suggest the tech/approach (with Section 5 patterns)
4. Show me a simple implementation plan

Then:
- Start with the first subtask
- Write code with full tests
- Provide commit message

Let's build this feature!
```

---

## SCENARIO 11: External Service Integration

Integrating an external service/API:

```
I need to integrate an external service into [PROJECT_NAME].

Service Details:
- Name: [Service name]
- Purpose: [What it does]
- API Docs: [URL]
- Authentication: [API key / OAuth / etc]
- Rate limits: [X] req/sec

Integration point:
[Where in the app should this fit?]

Context:
[PASTE: AI_PROJECT_CONTEXT_PROTOCOL.md - Sections 2, 3, 9.3]
[PASTE: Relevant service code if exists]

Steps:
1. Where should this live in our architecture?
2. Design the integration (service layer)
3. Handle errors and rate limits
4. Provide tests
5. Document in docs/

Let's integrate this safely.
```

---

## SCENARIO 12: Deployment Preparation

Before production deployment:

```
Preparing [PROJECT_NAME] for deployment to [staging/production].

Checklist:

[PASTE: AI_PROJECT_CONTEXT_PROTOCOL.md - Section 6 (Git Flow & Checkpoints)]

Pre-deployment tasks:
1. All tests passing? 
2. Documentation updated?
3. Environment variables configured?
4. Database migrations ready?
5. Security scans clean?
6. Performance tested?
7. Backups configured?

Please:
1. Run full pre-deploy checklist
2. Generate deployment commands
3. Provide rollback plan
4. List verification steps (post-deploy)

Ready to deploy?
```

---

## SCENARIO 13: Emergency / Urgent Issue

Solving an emergency:

```
 EMERGENCY FIX NEEDED 

Issue: [Description]
Severity: [Critical / High / Medium]
Impact: [X users affected / System down / Data loss risk / etc]

What's happening:
[Error message / Symptoms / When it started]

Affected code:
[PASTE: Relevant error stack trace or code]

Quick context:
[PASTE: AI_PROJECT_CONTEXT_PROTOCOL.md - SECTIONS 2, 3 only - MINIMAL]

PRIORITY ORDER:
1. Identify root cause (1 min)
2. Propose emergency fix (2 min)
3. Provide safe rollback plan (1 min)
4. After emergency: full investigation

Let's fix this NOW.
```

---

## SCENARIO 14: Retrospective & Planning

Retrospective and planning at the end of a sprint:

```
Sprint [X] ending. Time for retrospective and planning.

Sprint Status:

[PASTE: TASK_PROGRESS.yaml - Full current sprint]

[PASTE: AI_PROJECT_CONTEXT_PROTOCOL.md - Section 13 (Metrics)]

Please analyze:

1. **Completed Tasks**: What went well?
2. **Incomplete Tasks**: Why? What blocked us?
3. **Velocity**: Is our estimation accurate?
4. **Risks**: Any technical debt?
5. **Learnings**: What did we discover?

Then:

1. Summarize retrospective
2. List action items for next sprint
3. Review and adjust estimation process
4. Update TASK_PROGRESS.yaml with Sprint_Retrospective

Ready for next sprint planning.
```

---

## SCENARIO 15: Token/Session Ending

If you are approaching the end of the session:

```
Getting close to token limit. Need to prepare handover.

Remaining tokens: [X] / [Y]

Current session summary:
- Completed: [TASK-XXX]
- In progress: [TASK-YYY] ([%]% done)
- Blockers: [List any]
- Files changed: [List]

Please:

1. Generate commit with current state:
   bash
   git add .
   git commit -m "[Commit message]"
   git push origin feature/branch
   

2. Update TASK_PROGRESS.yaml:
   - Mark completed tasks as 
   - Update in-progress percentages
   - Note blockers for next session

3. Create a "Handover Note":
   
   Next model should:
   - [ ] Continue from TASK-XXX ([Y]% done)
   - [ ] Watch out for: [Blocker]
   - [ ] Test these: [Test points]
   - [ ] Reference: [Relevant docs/code]

Save everything and ready to switch models.

---

## SCENARIO 16: Caveman Mode (Token Saver) 

Use this to reduce output token usage by 65%+:

```
From now on, speak like caveman. 

Rules:
1. Use fragments. No filler words (a, the, is).
2. No politeness. Only substance.
3. Keep technical accuracy 100%. 
4. Keep code blocks perfect.

Current Task: [Task]

Why use many token when few token do trick?
```
```

---

## SCENARIO 17: User-Requested Update System

Use this only when the user asks for an updater, version checker, auto-update flow, GitHub sync, or launcher that updates before app start.

```
I want an update system for [PROJECT_NAME].

User request:
[Describe the requested update behavior]

Project profile:
- Runtime target: [Windows desktop / portable app / web app / SaaS / mobile / other]
- Distribution source: [public GitHub / private repo / package manager / app store / other]
- Current launch flow: [start.bat / start.ps1 / app.exe / npm script / other]
- Versioning: [SemVer / tags / releases / none]
- Local-only files to protect: [.env, user data, settings, generated files, private context]

Context:
[PASTE: UPDATE_SYSTEM_RECOMMENDATION_PROTOCOL.md]
[PASTE: AI_PROJECT_CONTEXT_PROTOCOL.md - Sections 4, 6, 13 only]

Please:
1. Decide whether the Archura SyncGuard style pattern fits.
2. If it fits, propose the safest implementation plan and required files.
3. If values are missing, inspect the repository first and propose defaults.
4. If it does not fit, recommend the correct release/update strategy instead.
5. Preserve private files, local settings, backups, logs, and generated prompt bundles.
```

---

## SCENARIO 18: Existing Project File Structure Refactor

Use this when Nexus-APCP is added to an existing project and the repository needs a safer, clearer file layout without breaking previously written code.

```
I want to reorganize the file structure for [PROJECT_NAME].

Goal:
[Describe the target organization or readability problem]

Current concern:
- Existing code must keep running after files move.
- Imports, scripts, tests, builds, assets, and docs must be updated.
- Migration should happen iteratively, not as one risky bulk move.

Context:
[PASTE: FILE_STRUCTURE_REFACTOR_PROTOCOL.md]
[PASTE: AI_PROJECT_CONTEXT_PROTOCOL.md - Sections 2, 3, 7, 8, 13 only]
[PASTE: TASK_PROGRESS.yaml - current sprint only]

Please:
1. Inspect the current structure, entry points, scripts, tests, imports, and config before moving files.
2. Propose the target structure and the first migration iteration.
3. Move only one coherent file group at a time.
4. Update imports, path aliases, scripts, tests, docs, and Mermaid diagrams affected by each move.
5. Preserve old entry points with temporary wrappers or re-exports when needed.
6. Run relevant verification after each iteration and stop if verification fails.
7. Update TASK_PROGRESS.yaml when the visible migration task is complete.
```

---

## SCENARIO 19: Reusable AI Agent Skill Workflow

Use this when a repeated AI workflow needs a named process instead of ad hoc prompting: diagnosis, TDD, triage, PRD creation, issue breakdown, handoff, architecture improvement, prototyping, or skill creation.

```
I want to use a reusable AI agent skill workflow for [PROJECT_NAME].

Requested skill:
[diagnose / tdd / triage / to-prd / to-issues / handoff / improve-codebase-architecture / prototype / grill-with-docs / write-a-skill / other]

Goal:
[Describe what we need to accomplish]

Context:
[PASTE: AI_AGENT_SKILLS_PROTOCOL.md]
[PASTE: AI_PROJECT_CONTEXT_PROTOCOL.md - relevant sections]
[PASTE: TASK_PROGRESS.yaml - current sprint only]
[PASTE: DECISION_LOG_PROTOCOL.md or docs/adr/ summaries if relevant]

Please:
1. Confirm which skill workflow applies and why.
2. Identify hard dependencies before acting, especially issue tracker, label, and domain-doc configuration.
3. Use project vocabulary and existing decisions.
4. Follow the skill's sequence without skipping verification gates.
5. Produce the expected skill output: repro loop, failing test, PRD, issue brief, handoff, prototype verdict, or architecture candidate list.
6. Update TASK_PROGRESS.yaml if this completes a visible repository task.
```

---

## SCENARIO 20: AI Tool Adapter Compatibility Review

Use this when adding, comparing, or updating support notes for AI coding tools such as Claude Code, Cursor, ChatGPT, Gemini, GitHub Copilot, local LLMs, IDE agents, CLI agents, or multi-agent systems.

```
I want to review AI tool adapter compatibility for [PROJECT_NAME].

Target tool or adapter:
[Claude Code / Cursor / ChatGPT / Gemini / GitHub Copilot / local LLM / IDE agent / CLI agent / other]

Goal:
[Add adapter file / update startup behavior / compare tools / fix repeated model behavior drift / prepare model switch]

Context:
[PASTE: AI_TOOL_ADAPTER_COMPATIBILITY_PROTOCOL.md]
[PASTE: AGENTS.md or the active adapter file]
[PASTE: AI_PROJECT_CONTEXT_PROTOCOL.md - Sections 4, 8, 13, and 14 only]
[PASTE: TASK_PROGRESS.yaml - current sprint only]

Please:
1. Identify the tool's observable mode, tool access, context loading path, verification path, and drift risks.
2. Recommend the smallest safe adapter-file change.
3. Do not copy vendor system prompts, unofficial prompt dumps, proprietary tool schemas, bypass text, or private prompt bundles.
4. Prefer official documentation for current behavior when a claim depends on live product details.
5. Update TASK_PROGRESS.yaml if this completes a visible repository task.
```

---

## BEST PRACTICES WHEN USING THESE PROMPTS

### DOS

1. **Always copy files in full**:
   Instead of:
   ```
   [PASTE: AI_PROJECT_CONTEXT_PROTOCOL.md - SECTIONS X, Y, Z]
   ```
   Copy the entire file and point to the specific sections.

2. **Keep context minimal** (token efficiency):
   - First session: FULL files
   - Subsequent sessions: Only necessary sections

3. **Be specific** (avoid vague requests):
   ```
    Bad: "Help me with the API"
    Good: "Help me implement GET /users/{id} endpoint with proper error handling"
   ```

4. **Always update TASK_PROGRESS**:
   At the end of the session:
   - Mark completed tasks with 
   - Update in-progress (%)
   - Add actual effort
   - Note blockers

5. **Run the checkpoint**:
   ```bash
   bash scripts/checkpoint.sh
   ```
   Right before committing.

### DON'TS

1. **Don't write manually instead of copy/pasting**:
   - You might write file paths incorrectly
   - Details might be missed

2. **Don't send API keys/secrets**:
   - These should be [REDACTED]
   - Kept in a secure management system

3. **Vague requirements**:
   - Instead of "Fix that", use "login() method in UserService returns 403 error"

4. **Don't forget to update documentation**:
   - Every code change should have a corresponding update in docs

5. **Skip writing tests**:
   - Don't say "we'll write them later"
   - Tests should be part of the git history

---

## PROMPT SELECTION FLOWCHART

```
What do I want to do?

├─ New feature (SCENARIO 10)
├─ Bug fix (SCENARIO 6)
├─ Code review (SCENARIO 4)
├─ Documentation (SCENARIO 5)
├─ Architecture decision (SCENARIO 7)
├─ Performance optimization (SCENARIO 8)
├─ External service integration (SCENARIO 11)
├─ Deployment (SCENARIO 12)
├─ Update system / version sync (SCENARIO 17)
├─ Existing project file structure refactor (SCENARIO 18)
├─ Reusable agent skill workflow (SCENARIO 19)
├─ AI tool adapter compatibility review (SCENARIO 20)
├─ Emergency (SCENARIO 13)
├─ Sprint planning (SCENARIO 14)
├─ Model switching (SCENARIO 3)
├─ Token about to run out (SCENARIO 15)
├─ Token saving mode (SCENARIO 16)
└─ İlk başlama (SCENARIO 1)
```

---

## EXTRA TIPS

### Token Efficiency
- First session: FULL context (3000-4000 tokens spent, saves later)
- Later sessions: Reference existing sections (50-100 tokens for links)
- Calculations: "If the context window is ~100k tokens and APCP uses 3k, about 97k tokens remain for work."

### Model Specific
- **Same model/session**: Use Scenario 2.
- **New model or fresh session**: Use Scenario 3.
- **Planning or retrospective**: Use Scenario 14.

### Continuous Work
```
Session 1: Load full context, work on features
Session 2: Reference APCP, continue where left off
Session 3: Load context, clean up + plan
Session 4: Final push, deploy
```

---

**Created for efficient AI-assisted development**
**Use and adapt for your workflow!**
