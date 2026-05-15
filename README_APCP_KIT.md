# 📦 AI PROJECT CONTEXT PROTOCOL (APCP) KIT v1.0

**A complete system for efficient development with AI models**

---

## 📂 KIT CONTENTS (4 Files)

This kit consists of 4 core files. You should use them all together:

### 1️⃣ **AI_PROJECT_CONTEXT.md** (Main Documentation)
- **Size**: ~20 KB
- **Purpose**: To fully define the project
- **Usage**: Load at the beginning of each AI session
- **Refresh Frequency**: Monthly or upon significant changes
- **Contents**:
  - Project identity and goals
  - File hierarchy
  - Import/module structures
  - Security rules
  - Git workflow
  - Design patterns
  - Documentation and resources
  - Best practices

### 2️⃣ **TASK_PROGRESS.yaml** (Task Tracking)
- **Size**: ~5-10 KB
- **Purpose**: To track tasks
- **Usage**: Update at the start/end of each task
- **Refresh Frequency**: Daily (session-dependent)
- **Contents**:
  - Task list (status, priority, effort)
  - Subtasks and dependencies
  - Sprint tracking
  - Velocity metrics
  - Retrospective notes

### 3️⃣ **AI_ASSISTANT_PROMPT_TEMPLATES.md** (Quick Start)
- **Size**: ~15 KB
- **Purpose**: Ready-to-use prompts for 15 different scenarios
- **Usage**: Select, copy, and paste the scenario that fits your situation
- **Refresh Frequency**: Rarely (when needed)
- **Contents**:
  - Scenarios 1-15: Prompts for different tasks
  - Best practices
  - Token efficiency tips
  - Model-specific guidance

### 4️⃣ **SETUP_GUIDE.md** (Setup and Routine)
- **Size**: ~12 KB
- **Purpose**: To set up and run APCP
- **Usage**: Initial setup + weekly routine
- **Refresh Frequency**: Only if processes change
- **Contents**:
  - Step-by-step setup
  - Helper scripts
  - Weekly routine
  - Troubleshooting
  - Best practices

### 🌟 **ADVANCED FEATURES (Professional Pack)**
- **DECISION_LOG_PROTOCOL.md**: Architecture Decision Records (ADR) to track technical intent.
- **CONTEXT_OPTIMIZATION.md**: Strategies for handling large-scale codebases and token limits.
- **WORKSPACE_SPECIFIC_DELIVERY_PROTOCOLS.md**: Workspace-specific release gates for Unity/game engines, web apps, backend services, AI/LLM products, penetration testing, packaging, and scalability.
- **DOMAIN_SPECIFIC_GITIGNORE_PROTOCOLS.md**: Domain-specific `.gitignore` templates and prompts for games, web apps, banking/fintech, AI/RAG systems, data/ML, mobile, and DevOps.
- **scripts/apcp-gather.py**: Automation tool to pack your context for the AI.

---

## 🚀 QUICK START (5 STEPS)

### Step 1: Copy Files to the Project (1 min)

```bash
# Copy the 4 files to your project root:
cp AI_PROJECT_CONTEXT.md /your/project/
cp TASK_PROGRESS.yaml /your/project/
cp AI_ASSISTANT_PROMPT_TEMPLATES.md /your/project/docs/
cp SETUP_GUIDE.md /your/project/docs/
```

### Step 2: Customize APCP (30 min)

```bash
# 1. Open AI_PROJECT_CONTEXT.md
nano AI_PROJECT_CONTEXT.md

# Fill in the UPPER_CASE sections:
# - [PROJECT_NAME]
# - [https://github.com/...]
# - Adapt the folder structure to your project
# - Organize imports according to your modules
# - Add external services
# - Add team information

# 2. Initialize TASK_PROGRESS.yaml
nano TASK_PROGRESS.yaml
# Add your first 5-10 tasks (sprint planning)
```

Security rule: the filled `AI_PROJECT_CONTEXT.md` for a real project is private by default. It can expose backend structure, internal architecture, database internals, deployment topology, admin flows, private prompts, and security assumptions. Keep it local or in an approved private knowledge base unless you create a sanitized public version.

### Step 3: Create Helper Scripts (5 min)

```bash
# Follow "Step 3" in SETUP_GUIDE.md
# Create these scripts:
# - scripts/checkpoint.sh (pre-commit checks)
# - scripts/update-apcp.sh (timestamp updates)
# - scripts/apcp-gather.py (context automation)

chmod +x scripts/*.sh
git add scripts/
git commit -m "chore: add APCP helper scripts"
```

### Step 4: Commit to Git (2 min)

```bash
# Commit sanitized templates/docs only. Keep filled AI_PROJECT_CONTEXT.md local/private by default.
git add .gitignore
git add docs/AI_ASSISTANT_PROMPT_TEMPLATES.md
git add docs/SETUP_GUIDE.md
git add docs/AI_PROJECT_CONTEXT_TEMPLATE.md  # optional sanitized template, not the filled private context
git commit -m "docs: initialize APCP system for AI-assisted development"
git push
```

### Step 5: First AI Session (10 min)

```
Send this message to the AI (e.g., Claude):

I'm setting up an AI-assisted development workflow for [PROJECT_NAME].

Here's my complete project context:

[PASTE FULL: AI_PROJECT_CONTEXT.md]

[PASTE FULL: TASK_PROGRESS.yaml]

Please:
1. Confirm you understand the project
2. Summarize the current status
3. Tell me which task to start with

Let's begin!
```

---

## 📋 FILE ROLES (Who needs what and when?)

| File | Project Setup | Daily Work | Code Review | Model Switch | Sprint End |
|-------|---|---|---|---|---|
| **AI_PROJECT_CONTEXT.md** | ✅ Customize | ✅ Reference | ✅ Check | ✅ **Load** | ⚫ Update |
| **TASK_PROGRESS.yaml** | ✅ Create | ✅ Update | ✅ Check | ⚫ Reload | ✅ **Review** |
| **PROMPT_TEMPLATES.md** | ⚫ - | ✅ Select scenario | ⚫ - | ✅ Reference | ⚫ - |
| **SETUP_GUIDE.md** | ✅ **Follow** | ⚫ - | ⚫ - | ⚫ - | ⚫ Routine check |

Legend: ✅ = High priority, ⚫ = Optional, **Bold** = Very important

---

## 🎯 BENEFITS OF APCP

### Short-term Benefits (1 week)
- ✅ AI provides accurate answers instead of learning the project from scratch
- ✅ Tokens are used more efficiently
- ✅ Code reviews become faster
- ✅ The team knows all the rules

### Mid-term Benefits (1 month)
- ✅ Tasks are completed within estimated times
- ✅ Model switches are seamless
- ✅ Bugs are fixed faster
- ✅ Newcomers get up-to-speed in 2 hours

### Long-term Benefits (3+ months)
- ✅ Velocity is stable and predictable
- ✅ Technical debt decreases
- ✅ Documentation stays up-to-date
- ✅ No knowledge silos (the entire system is in APCP)
- ✅ Management always knows the project status

---

## 🔄 WEEKLY ROUTINE (10 min/day)

```
📅 Monday (30 min)
  ├─ Ask AI: "What's this week's plan?"
  ├─ Review TASK_PROGRESS.yaml
  └─ Plan the week's tasks

📅 Tuesday-Friday (10 min/day)
  ├─ Start the day: AI "What's next?"
  ├─ Work and test
  ├─ bash scripts/checkpoint.sh
  ├─ Commit (Section 6.2 format)
  └─ Update TASK_PROGRESS

📅 Friday End (30 min)
  ├─ Review the week's achievements
  ├─ bash scripts/update-apcp.sh
  ├─ Finalize TASK_PROGRESS
  └─ Note for next week
```

---

## 📊 METRICS (To track)

Check weekly/monthly:

```yaml
Velocity:
  - Tasks completed per sprint: ______
  - Effort estimate accuracy: ____% (Target: 90%+)
  - Average task duration: ______

Quality:
  - Code coverage: ____% (Target: 80%+)
  - Test pass rate: ____% (Target: 100%)
  - Bug fix time: ____h (Target: <4h)

AI Efficiency:
  - Tokens per session: ______ (Target: <80k for Haiku)
  - Context loading time: ______ (Target: 5 min)
  - Model switches smooth: Yes/No

Team:
  - New member onboarding time: ____h (Target: <4h)
  - Documentation freshness: Up-to-date/Stale
  - Team satisfaction: ____/10
```

---

## ⚠️ APCP RULES (CRITICAL)

### 🔐 NEVER DO

```
❌ Write secret keys where [REDACTED] should be
❌ Forget to update APCP
❌ Leave task progress empty
❌ Ignore design patterns
❌ Commit without logging breaking changes
```

### ✅ ALWAYS DO

```
✅ Update TASK_PROGRESS at the end of every task
✅ Run checkpoint.sh before committing
✅ Run update-apcp.sh once a week
✅ Load the full APCP during a model switch
✅ Ask questions when there is uncertainty (don't guess)
```

---

## 🆘 STARTING FROM SCRATCH (Existing Project)

If you already have a project:

```
1. Download these 4 files
2. Customize AI_PROJECT_CONTEXT.md in 30 minutes
   - Run git status, git log, tree src/
   - Use the outputs as reference
3. Add the latest activities to TASK_PROGRESS.yaml
4. Start the first AI session
5. Fix the rest as you go

Total: 1.5 hours setup, then works smoothly
```

---

## 🚀 ANATOMY OF APCP

```
An AI session works like this:

1. AI STARTING
   ├─ Read AI_PROJECT_CONTEXT.md (3k tokens)
   ├─ Read TASK_PROGRESS.yaml (1k tokens)
   └─ "Ready!" (4k tokens spent, 96k left for work)

2. WORKING
   ├─ Read Task (50 tokens)
   ├─ Write Code (2k tokens)
   ├─ Write Test (1k tokens)
   ├─ Respond (500 tokens)
   └─ (3.5k tokens/request, typical 20 requests/session)

3. CLOSING
   ├─ Summarize work (200 tokens)
   ├─ Update TASK_PROGRESS (50 tokens)
   └─ Provide commit message (100 tokens)

4. MODEL SWITCH (YES, context loss would happen, but it doesn't!)
   ├─ Old model: lost context
   ├─ New model: Load Full APCP (4k tokens)
   ├─ Summarize old session: "We completed TASK-X, now need TASK-Y"
   └─ Continue (seamless!)

RESULT: Token efficiency and consistency!
```

---

## 📈 GROWTH PATH

As you use APCP:

```
Week 1: Setup, first-time use
  - Velocity baseline is determined
  - Team learns the patterns

Week 2-4: Becomes routine
  - Velocity stabilizes
  - Estimation accuracy increases

Month 2-3: Optimization
  - Metrics gain stability
  - Technical debt decreases

Month 3+: Mature (AI-assisted dev best practice)
  - Velocity predictable (90%+ accuracy)
  - Quality high (code coverage, low bug rate)
  - Team happy (everyone knows the rules)
  - Management happy (project status clear)
```

---

## 🔗 FILE LINKS

Depending on your environment:

```
On GitHub:
  AI_PROJECT_CONTEXT_TEMPLATE.md
    ├─ Raw: github.com/user/repo/raw/main/docs/AI_PROJECT_CONTEXT_TEMPLATE.md
    └─ Sanitized template only; never publish filled private context by default

  TASK_PROGRESS.yaml
    ├─ Raw: github.com/user/repo/raw/main/TASK_PROGRESS.yaml
    └─ Link from project board

Local Clone:
  ./AI_PROJECT_CONTEXT.md
  ./TASK_PROGRESS.yaml
  ./docs/AI_ASSISTANT_PROMPT_TEMPLATES.md
  ./docs/SETUP_GUIDE.md
```

---

## 💬 FAQ

**Q: When should the files be updated?**
A: AI_PROJECT_CONTEXT.md: Monthly or major changes. TASK_PROGRESS.yaml: Daily. Others: Rarely.

**Q: Is APCP too big?**
A: Yes, but it's loaded once per first session. Then it's incremental. Result: token gain.

**Q: Is it mandatory to update TASK_PROGRESS for every task?**
A: Yes. Without this, the AI cannot track progress.

**Q: Can the AI forget without a model switch?**
A: Yes, the purpose of APCP is to *prevent* this. Load APCP, and it remembers.

**Q: What happens without such a system?**
A: Every session, the model learns the project from scratch, tokens are exhausted, and it works inconsistently.

**Q: Disadvantage of using APCP?**
A: Setup takes 1-2 hours. But ROI: 4-5 hours gain per session (no Haiku → Sonnet switch issues, no restarts).

---

## 🎓 ADVANCED TOPICS

Next level:

```
1. Custom evaluation metrics (Section 12)
2. Automated testing framework integration
3. APCP validation in CI/CD pipeline
4. Team dashboard (task tracking)
5. Multi-team APCP management
6. Version control for APCP itself (git history)
```

---

## 📞 SUPPORT AND COMMUNITY

- **Questions?** Create an issue on GitHub (others will benefit)
- **New scenario?** Add to AI_ASSISTANT_PROMPT_TEMPLATES.md
- **Bug?** Check the Troubleshooting section of SETUP_GUIDE.md
- **Suggestions?** Add a CONTRIBUTING section to README.md

---

## 📄 LICENSE AND USAGE

**APCP Kit is completely open and free.**

- Use for your own project ✅
- Share with the team ✅
- Write on a blog ✅ (a link would be nice)
- Sell ❌
- Remove copyright ❌

---

## 🎉 ARE YOU READY?

```
To start AI-assisted development with APCP:

1. Download the 4 files ✅
2. Follow SETUP_GUIDE.md ✅
3. Start the first task ✅
4. Maintain the routine ✅

Result: Faster, consistent, reliable development!

Ready to build? 🚀
```

---

## 📝 VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2024-01-15 | Initial release: 4 files, 15 scenarios, full system |

---

## 🌟 KEY NOTES

```
"APCP is like the project talking to the AI.
It's not just a technical spec, it's the project's memory.
Even if the model is switched, the project is remembered."

- Created for productive, sustainable AI-assisted development -
```

---

**Last Updated**: 2024-01-15  
**Maintained By**: AI Development Community  
**Questions?** Create an issue or ask your AI assistant

**Happy coding with AI! 🤖✨**
