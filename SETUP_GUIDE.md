# Nexus-APCP: AI Project Context Protocol Setup Guide

A step-by-step guide to setting up Nexus-APCP for AI-assisted development, context engineering, and token-optimized coding workflows.

---

## SETUP STEPS

### Step 0: Prepare Information (15 minutes)

Collect the following information before filling out the APCP file:

```
Project Information:
- [ ] Project name
- [ ] GitHub repo URL
- [ ] Main programming language
- [ ] Frameworks (Flask, FastAPI, Django, etc.)
- [ ] Database (PostgreSQL, MongoDB, etc.)
- [ ] External services (Stripe, SendGrid, etc.)

Team Information:
- [ ] Project Manager name/email
- [ ] Tech Lead name/email
- [ ] Software architect (if any)

Documentation:
- [ ] API documentation URL (if any)
- [ ] Architecture diagram URL (if any)
- [ ] Database schema URL (if any)
```

---

### Step 1: Install Local Agent Context (5 minutes)

#### 1.0 AI-Agent Install Prompt

When installing Nexus-APCP from Codex, Claude, Cursor, ChatGPT, Gemini, or another AI agent, start the agent in your target project root and paste:

```markdown
Set up Nexus-APCP in this repository.

Do not rely on search-index snippets or memory. Use exact source files from:
https://github.com/AybarsBarut/Nexus-APCP

Source priority:
1. If network access is available, fetch files from:
   https://raw.githubusercontent.com/AybarsBarut/Nexus-APCP/master/
2. If raw GitHub access is unavailable, ask me for a local clone/path or pasted files.
3. If neither source is available, create only clearly marked placeholders and list what must be synced later.

Git command rule:
- Do not run `git status`, `git add`, `git commit`, `git push`, or other Git commands during setup unless I explicitly ask.
- Inspect files and folders directly first.
- If Git state is truly needed, explain why and ask before running the command.

Public repository rule:
- Install Nexus-APCP files for local or approved private/cloud agent context by default.
- Before any GitHub push, keep installed APCP files, generated context bundles, private task state, and internal maps out of the public repository unless I explicitly approve sanitized public templates.
- Prefer `.git/info/exclude` or a private global excludes file when the public GitHub repo should not reveal local AI workflow files.

Profile rule:
- Inspect the project type before choosing context.
- Start with `core` unless the project clearly matches `web`, `backend-api`, `cli`, `game`, or `ai-rag`.
- Use `full` only when I explicitly ask for every public Nexus-APCP protocol.
- Keep task-specific protocols inactive unless they match the current project or current request.

Bootstrap files:
- Fetch `scripts/apcp_core_files.py`, `scripts/apcp-install.py`, and `scripts/apcp-gather.py` first when possible.
- Run `python scripts/apcp-install.py --list-profiles` to show supported profiles.
- If a local Nexus-APCP clone or source path is available, install from that source with `python /path/to/Nexus-APCP/scripts/apcp-install.py --target . --profile core`, replacing `core` with the selected profile.
- If only raw GitHub access is available, run `python scripts/apcp-install.py --list-files --profile core` after fetching the bootstrap scripts, then download those selected paths from the raw source and preserve their paths.
- The installer writes `apcp-profile.json`; keep it local/private by default.

Then inspect this project, customize placeholders, preserve secrets/private context, and run:
python scripts/apcp-gather.py --caveman
```

#### 1.1 Install a Project Profile

```bash
# From the Nexus-APCP source repository:
python scripts/apcp-install.py --list-profiles
python scripts/apcp-install.py --target /path/to/your/project --profile core

# Do not add these installed APCP operating files to Git by default.
# Keep them local, or sync them through an approved private/cloud knowledge base.
```

Available profiles:

| Profile | Use when |
| :--- | :--- |
| `core` | Any project needs project memory, tasks, decisions, token rules, prompts, and safe publishing. |
| `web` | Frontend or website projects need UI guidance, static-first backend safety, lean app defaults, and delivery gates. |
| `backend-api` | API or service projects need application security and delivery gates. |
| `cli` | Command-line or developer-tool projects need delivery guidance and optional updater fit checks. |
| `game` | Game or simulation projects need algorithm/design discovery and delivery gates. |
| `ai-rag` | AI, RAG, or data-assisted applications need discovery, security, and delivery gates. |
| `full` | Every public protocol file is intentionally needed. |

The installer skips existing files unless `--overwrite` is passed. Use `--dry-run` to preview file operations. It writes `apcp-profile.json` in the target project; `scripts/apcp-gather.py` reads that profile automatically and accepts `--profile` for one-off overrides.

The canonical install and gather file inventory lives in `scripts/apcp_core_files.py`. The repository validator checks this guide, the README, the gather bundle, installer, local excludes, and validator against that same source.

#### 1.2 Keep APCP Out of Public GitHub by Default

If the public GitHub repository should not show local AI workflow files, use a local Git exclude instead of committing a `.gitignore` rule. `.git/info/exclude` stays inside the local clone and is not pushed.

```bash
# macOS, Linux, Git Bash, or WSL:
bash scripts/install-local-excludes.sh

# Windows PowerShell:
powershell -ExecutionPolicy Bypass -File scripts/install-local-excludes.ps1
```

The helper scripts add the local-only APCP paths, generated bundle names, `.env`-style local files, `.apcp-cache/`, and `.codegraph/` entries to the current clone's exclude file. For teams, repeat this step during onboarding or use an approved private global excludes file or private template repository.

Use a committed `.gitignore` block only when the team accepts that the public repository will show the ignore rule. If any APCP file is already tracked, adding an exclude rule is not enough; remove it from Git tracking with `git rm --cached <path>` after confirming the file should remain local.

#### 1.3 Git Behavior by Phase

During AI-agent setup, agents should install files, inspect the project, and stop before any Git operation unless the user explicitly asks. That rule covers `git status`, `git add`, `git commit`, and `git push`.

During a human-maintained private or internal repo routine, Git commands can be used after review. Prefer path-specific staging such as `git add TASK_PROGRESS.yaml` or `git add AI_PROJECT_CONTEXT_PROTOCOL.md TASK_PROGRESS.yaml`. Do not use `git add .` for APCP maintenance unless the entire working tree has been reviewed and generated/private files are excluded.

#### 1.4 Optional Local Code Graph Setup

For large codebases, install CodeGraph only after confirming the project's Node.js and tool-install policy. CodeGraph builds a local semantic index that can help AI agents answer architecture, symbol, caller, callee, route, and impact questions with fewer broad scans.

```bash
npx @colbymchenry/codegraph
codegraph init -i
```

Before public pushes, confirm `.codegraph/` and any generated graph database files remain untracked. Use `CODEGRAPH_INTEGRATION_PROTOCOL.md` for agent usage rules and staleness checks.

---

### Step 2: Customize APCP (30-45 minutes)

#### 2.1 Fill in AI_PROJECT_CONTEXT_PROTOCOL.md

Open the editor and fill in the UPPER_CASE sections:

```markdown
# SECTION 1.1 - Project Identity
Project Name: [PROJECT_NAME] ← Fill this in
GitHub Repo: [https://github.com/username/repo] ← Fill this in
Main Language: [Python/JavaScript/TypeScript] ← Select

# SECTION 2 - File Hierarchy
[PROJECT_NAME]/
├──  src/
│   ├──  core/
│   │   ├── auth.py
│   │   ├── database.py
│   │   ├── config.py
│   │   └── utils.py
← Does this structure fit your project? 
  If not, customize it
```

**Note**: 
- Section 1: Mandatory (complete)
- Section 2: Reflect your folder structure
- Section 3: Update according to your actual imports
- Section 4: List of your sensitive data
- Section 8: Your documentation files
- Section 9: Your external services

#### 2.2 Initialize TASK_PROGRESS.yaml

```bash
# Create the first tasks. Example:

cat > TASK_PROGRESS.yaml << 'EOF'
Project:
  Name: "My Project"
  Sprint: "Sprint 1"
  Period: "2024-01-15 - 2024-01-29"

Tasks:
  - id: "TASK-001"
    title: "Create project structure"
    status: " NOT_STARTED"
    priority: " CRITICAL"
    due_date: "2024-01-17"
    effort_estimate: "4h"
    subtasks:
      - " Create folder structure"
      - " Set up Docker"
      - " Build CI/CD pipeline"
    
  - id: "TASK-002"
    title: "Authentication system"
    status: " NOT_STARTED"
    priority: " CRITICAL"
    due_date: "2024-01-22"
    effort_estimate: "12h"
    dependencies: ["TASK-001"]
    subtasks:
      - " Determine JWT strategy"
      - " Write auth service"
      - " Write tests"
EOF
```

---

### Step 3: Create Helper Scripts (10 minutes)

#### 3.1 Checkpoint Script

A script that catches errors in the code before committing:

```bash
# Create scripts/checkpoint.sh file

cat > scripts/checkpoint.sh << 'EOF'
#!/bin/bash
set -e

echo " Pre-commit checklist..."
echo ""

# 1. Tests
echo "1. Running tests..."
if ! pytest src/tests/ -v --tb=short 2>/dev/null; then
    echo " Tests failed!"
    exit 1
fi
echo " Tests passed"
echo ""

# 2. Code format
echo "2. Checking code format..."
if ! black --check src/ 2>/dev/null; then
    echo "  Code formatting issues found. Running: black src/"
    black src/
fi
echo " Code formatted"
echo ""

# 3. Linting
echo "3. Linting..."
if ! flake8 src/ --max-line-length=100 2>/dev/null; then
    echo "  Linting issues found (non-blocking)"
fi
echo ""

# 4. Type checking (if using Python)
echo "4. Type checking..."
if command -v mypy &> /dev/null; then
    if ! mypy src/ 2>/dev/null; then
        echo "  Type hints issues (non-blocking)"
    fi
fi
echo ""

# 5. Security
echo "5. Security scan..."
if command -v bandit &> /dev/null; then
    if ! bandit -r src/ -ll 2>/dev/null; then
        echo "  Security warnings (check them!)"
    fi
fi
echo ""

# 6. Git status
echo "6. Git status:"
git status --short
echo ""

echo " All checks completed!"
echo ""
echo "Ready to commit. Do:"
echo "  git add <reviewed-file-1> <reviewed-file-2>"
echo "  git commit -m 'type(scope): message'"
echo ""
echo "Before pushing, confirm local APCP operating files are excluded or intentionally sanitized."
EOF

chmod +x scripts/checkpoint.sh
```

#### 3.2 APCP Update Script

A script to help update the APCP:

```bash
cat > scripts/update-apcp.sh << 'EOF'
#!/bin/bash

echo " Updating APCP files..."
echo ""

# Get current timestamp
TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M:%S UTC")

# Update the header timestamp
sed -i "s/Last Updated: .*/Last Updated: $TIMESTAMP/" AI_PROJECT_CONTEXT_PROTOCOL.md
sed -i "s/# Last Updated: .*/# Last Updated: $TIMESTAMP/" TASK_PROGRESS.yaml

echo " Updated timestamps"
echo ""

# Show git diff
echo "Changes to APCP files:"
git diff --stat AI_PROJECT_CONTEXT_PROTOCOL.md TASK_PROGRESS.yaml

echo ""
echo "Local APCP context updated."
echo "Do not commit these operating files unless the user explicitly approves sanitized public templates."
EOF

chmod +x scripts/update-apcp.sh
```

---

### Step 4: First AI Session Setup (5 minutes)

Now send this prompt to the AI:

```markdown
I'm setting up AI-assisted development for my project: [PROJECT_NAME]

I've created:
1. **AI_PROJECT_CONTEXT_PROTOCOL.md** - Complete project documentation
2. **AI_MAIN.md** - AI session orchestration flow
3. **TASK_PROGRESS.yaml** - Task tracking file
4. **DECISION_LOG_PROTOCOL.md** - Decision history protocol
5. **CONTEXT_OPTIMIZATION.md** and **CAVEMAN_RULES.md** - Token and context rules
6. **AI_ASSISTANT_PROMPT_TEMPLATES.md** - Prompt templates for different scenarios
7. **AI_AGENT_SKILLS_PROTOCOL.md** - Reusable skill workflows for repeated agent tasks
8. **AI_TOOL_ADAPTER_COMPATIBILITY_PROTOCOL.md** - Safe AI tool adapter compatibility and prompt-source hygiene
9. **scripts/apcp-gather.py** - Context packaging helper

I'm ready to start working with you as an AI assistant.

Here's my project:

[PASTE FULL: AI_PROJECT_CONTEXT_PROTOCOL.md]

[PASTE FULL: TASK_PROGRESS.yaml]

Please:
1. **Read and understand** the project structure, goals, and first tasks
2. **Summarize what you understand**:
   - Project overview
   - Key files and modules
   - Current status (TASK-001, TASK-002, etc.)
   - Any blockers
3. **Ask clarifying questions** if anything is unclear
4. **Ready to start**: Tell me which task to begin with

Let's go!
```

---

## POST-SETUP CHECKLIST

Checklist after completing the setup:

```
APCP Setup Verification:
□ [ ] AI_PROJECT_CONTEXT_PROTOCOL.md filled with custom project information
□ [ ] AI_MAIN.md installed for AI session orchestration
□ [ ] TASK_PROGRESS.yaml created with initial tasks
□ [ ] DECISION_LOG_PROTOCOL.md, CONTEXT_OPTIMIZATION.md, and CAVEMAN_RULES.md installed
□ [ ] AI_ASSISTANT_PROMPT_TEMPLATES.md installed at the project root
□ [ ] AI_TOOL_ADAPTER_COMPATIBILITY_PROTOCOL.md installed if the project supports multiple AI coding tools
□ [ ] CODEGRAPH_INTEGRATION_PROTOCOL.md installed if the project uses local code graph discovery
□ [ ] apcp-profile.json exists with the selected project profile
□ [ ] scripts/apcp_core_files.py is installed next to scripts/apcp-gather.py
□ [ ] scripts/apcp-install.py is available for future profile updates
□ [ ] scripts/apcp-gather.py is working (test: python scripts/apcp-gather.py --caveman)
□ [ ] scripts/install-local-excludes.sh or scripts/install-local-excludes.ps1 has been run when public repository visibility matters
□ [ ] scripts/checkpoint.sh is working (test: bash scripts/checkpoint.sh)
□ [ ] scripts/update-apcp.sh is working
□ [ ] Installed APCP files are excluded locally or explicitly approved as sanitized public templates
□ [ ] If CodeGraph is used, `.codegraph/` and generated graph databases are untracked
□ [ ] If public repository visibility matters, no APCP operating-file references were added to README.md or committed .gitignore
□ [ ] Team members know what APCP is
□ [ ] First AI session conducted and successful
```

---

## HUMAN-MAINTAINED PRIVATE OR INTERNAL REPO ROUTINE

Use this routine after setup, in a private/internal repo or after a human has reviewed what is safe for a public repository. The setup-phase AI-agent rule still applies unless the user explicitly asks the agent to run Git commands.

### **Monday - Sprint Planning**

```bash
# Open TASK_PROGRESS.yaml
# Review previous sprint results
# Add new tasks
# Update sprint dates

# Send to AI (SCENARIO 14 from templates)
bash scripts/update-apcp.sh
git add TASK_PROGRESS.yaml
git commit -m "docs: plan sprint [X]"
```

### **Tuesday-Friday - Development**

```bash
# Start the day
# Ask AI: "What's next?" (SCENARIO 2 or 10)
# Work on task
# Before committing:
bash scripts/checkpoint.sh
# Commit (Section 6.2 format)
# Update TASK_PROGRESS.yaml
```

### **Friday End - Retrospective**

```bash
# At the end of the week:
# 1. Mark completed tasks in TASK_PROGRESS.yaml
# 2. Merge open PRs
# 3. Finalize TASK_PROGRESS.yaml

# Send to AI (SCENARIO 14)
bash scripts/update-apcp.sh
git add TASK_PROGRESS.yaml
git commit -m "docs: week X retrospective and planning"
git push
```

---

## STRICT RULES (FOR APCP SUCCESS)

### NEVER Do

```
 Hard-code AI Keys/Secrets in APCP
 Commit Production URLs to test
 Store user passwords in APCP
 Leave documentation obsolete (update it!)
 Ignore TASK_PROGRESS (keep it active!)
```

### ALWAYS Do

```
 Run checkpoint.sh before every commit
 Update TASK_PROGRESS at the end of every task
 Update Section 9 every time an external service is added
 Update docs at every major code change
 Run update-apcp.sh once a week
 Reference APCP sections during code review
```

---

## BENEFITS OF APCP (Why so detailed?)

It benefits not only the AI but also the team:

```
From the developer's perspective:
 New team members get up-to-speed in 30 minutes
 Code reviews accelerate (patterns are defined)
 Inconsistency decreases
 Even the person doing maintenance knows previous decisions

From management's perspective:
 Task tracking is automatic (TASK_PROGRESS.yaml)
 Velocity can be measured (estimates vs actual)
 Bottlenecks are visible
 Project status is always up-to-date

From the AI's perspective:
 Uses tokens efficiently (does not reload context)
 Model switches are smooth
 Works consistently (patterns are specified)
 Understands user intent better
```

---

## TROUBLESHOOTING

### Problem: "checkpoint.sh: command not found"

```bash
# Solution:
chmod +x scripts/checkpoint.sh
# And when running:
bash scripts/checkpoint.sh  # (instead of ./scripts/checkpoint.sh)
```

### Problem: "I forgot the context when the AI model version changed"

```bash
# Never forget! At the beginning of every session:

# Start session
# Immediately paste:
[PASTE: AI_PROJECT_CONTEXT_PROTOCOL.md]
[PASTE: TASK_PROGRESS.yaml]

# Then ask your question
```

### Problem: "I forgot to update the progress in the afternoon"

```bash
# At the end of the session:
# Do this automatically:

git add TASK_PROGRESS.yaml
git commit -m "docs: update task progress - TASK-X marked complete"
git push
```

### Problem: "The APCP file got too large, tokens are running out"

```bash
# Solution: Switch to MINIMAL mode

# In the first session: FULL load
[PASTE: AI_PROJECT_CONTEXT_PROTOCOL.md]
[PASTE: TASK_PROGRESS.yaml]

# Subsequent sessions: MINIMAL
"Working on [PROJECT_NAME].
Current task: TASK-X from https://github.com/user/repo/blob/main/TASK_PROGRESS.yaml
[PASTE: TASK_PROGRESS.yaml - Current sprint section ONLY]
Continue..."
```

---

## NEXT STEPS

After completing the setup:

1. **Give the first task to the AI** (SCENARIO 1 or 10)
2. **Update APCP once a week** (scripts/update-apcp.sh)
3. **Conduct a retrospective when sprints end** (SCENARIO 14)
4. **Update Section 15 as the team grows** (Escalation contacts)
5. **Monitor success metrics** (Section 12)

---

## MEASURE OF SUCCESS

When APCP is successful:

```
 AI models remain consistent across sessions
 Model switches are problem-free
 Tasks are finished within estimated times (Velocity stable)
 Code reviews accelerate
 New team members onboard quickly
 Production bugs decrease
 Team morale rises ("Everything is planned!")
 Documentation stays up-to-date
```

---

## SUPPORT AND QUESTIONS

If you have questions:

1. **Read this file again** (usually the answer is there)
2. **Search for the relevant scenario in AI_ASSISTANT_PROMPT_TEMPLATES.md** 
3. **Ask reusable questions in GitHub Issues** (other teams benefit)
4. **Ask the team lead** (for internal decisions)

---

## EXAMPLE OUTCOMES

Typical intended outcomes when a team keeps the protocol current:

- Model switches require less context rebuilding.
- Bug-fix sessions start with clearer architecture and decision history.
- New contributors can inspect project rules and task state before asking for help.
- Code reviews have a shared reference for conventions, safety gates, and delivery expectations.

---

**Ready to launch your AI-assisted development?**

Use the setup checklist, generate the context bundle, and start with the first task.
