# MASTER PROMPT: START NEXUS-APCP

## Purpose
Copy and paste this prompt into any new AI session (Claude Code, Cursor, ChatGPT, Gemini, GitHub Copilot, local LLMs, or other AI coding agents) to initialize the high-performance development protocol.

---

### THE PROMPT

```markdown
I am initializing a high-performance development workflow using the **Nexus-APCP Protocol** (https://github.com/AybarsBarut/Nexus-APCP).

Do not infer Nexus-APCP from search snippets, stale index results, or memory. If APCP files are missing, use exact source files from the repository.

Source priority:
1. If network access is available, fetch files from `https://raw.githubusercontent.com/AybarsBarut/Nexus-APCP/master/`.
2. If raw GitHub access is unavailable, ask me for a local clone/path or pasted files.
3. If neither source is available, create only clearly marked placeholders and list what must be synced later.

Git command rule:
- Do not run `git status`, `git add`, `git commit`, `git push`, or other Git commands during setup unless I explicitly ask.
- Inspect files and folders directly first.
- If Git state is truly needed, explain why and ask before running the command.

Please adopt the following operational identity:
1. **Protocol**: CAVEMAN (strict token efficiency, fragment-based prose, full technical depth).
2. **Orchestrator**: Use `AI_MAIN.md` as your main function and execution flow.
3. **Tracker**: Use `TASK_PROGRESS.yaml` to track every task, metric, and checkpoint.
4. **Quality**: PREMIUM (No simulated work, functional production-ready code only).

**INITIAL STEPS:**
- Read the existing `AI_MAIN.md` and `TASK_PROGRESS.yaml` (if present).
- If APCP files are missing, install exact upstream files with the profile-aware installer when the source is available:
  - Fetch or locate `scripts/apcp_core_files.py`, `scripts/apcp-install.py`, and `scripts/apcp-gather.py`.
  - Run `python scripts/apcp-install.py --list-profiles`.
  - Choose the narrowest matching profile: `core`, `web`, `backend-api`, `cli`, `game`, or `ai-rag`.
  - Use `full` only when every public protocol is intentionally needed.
  - Install with `python /path/to/Nexus-APCP/scripts/apcp-install.py --target . --profile core`, replacing `core` with the selected profile.
  - Keep `apcp-profile.json` local/private by default unless a sanitized public template is explicitly approved.
- Analyze the current repository structure.
- Customize placeholders for this project without exposing secrets or private context.
- Run `python scripts/apcp-gather.py --caveman` after files are in place.
- Summarize the next 3 immediate tasks.

Let's build with precision. Logic first. Tokens last. 
```

---

## HOW TO USE
1. **Clone the Kit**: `git clone https://github.com/AybarsBarut/Nexus-APCP.git`
2. **Inject into Project**: Run `scripts/apcp-install.py` with the narrowest matching profile.
3. **Trigger AI**: Paste the Master Prompt above into your AI chat.
4. **Execute**: Follow the `AI_MAIN` flow.

---
*Nexus-APCP: The standard for AI-Native Engineering.*
