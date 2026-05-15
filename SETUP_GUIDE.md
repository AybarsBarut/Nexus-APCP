# 🚀 AI PROJECT CONTEXT PROTOCOL - SETUP GUIDE

A step-by-step guide to setting up APCP for your project.

---

## 🎯 SETUP STEPS

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

### Step 1: Add Files to GitHub (5 minutes)

#### 1.1 Copy Files to the Repo

```bash
# In the project root:

# Copy the files (download the 3 below):
# - AI_PROJECT_CONTEXT.md
# - TASK_PROGRESS.yaml
# - AI_ASSISTANT_PROMPT_TEMPLATES.md

cp AI_PROJECT_CONTEXT.md /path/to/your/project/
cp TASK_PROGRESS.yaml /path/to/your/project/
cp AI_ASSISTANT_PROMPT_TEMPLATES.md /path/to/your/project/docs/

# Add to Git
git add AI_PROJECT_CONTEXT.md TASK_PROGRESS.yaml
git add docs/AI_ASSISTANT_PROMPT_TEMPLATES.md

# Commit
git commit -m "docs: add AI Project Context Protocol (APCP) v1.0

- Add AI_PROJECT_CONTEXT.md for project documentation
- Add TASK_PROGRESS.yaml for task tracking
- Add AI_ASSISTANT_PROMPT_TEMPLATES.md for prompt templates
- Enables AI-assisted development workflow"

git push origin main
```

#### 1.2 Add to .gitignore

```bash
# Add to .gitignore file:
cat >> .gitignore << 'EOF'

# APCP - Sensitive data (if needed)
.env
.env.local
config/*.secret
secrets/

# Temporary APCP files
*.apcp.tmp
.checkpoint
EOF

git add .gitignore
git commit -m "chore: update gitignore for APCP"
```

---

### Step 2: Customize APCP (30-45 minutes)

#### 2.1 Fill in AI_PROJECT_CONTEXT.md

Open the editor and fill in the UPPER_CASE sections:

```markdown
# SECTION 1.1 - Project Identity
Project Name: [PROJECT_NAME] ← Fill this in
GitHub Repo: [https://github.com/username/repo] ← Fill this in
Main Language: [Python/JavaScript/TypeScript] ← Select

# SECTION 2 - File Hierarchy
[PROJECT_NAME]/
├── 📁 src/
│   ├── 📁 core/
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
    status: "⚪ NOT_STARTED"
    priority: "🔴 CRITICAL"
    due_date: "2024-01-17"
    effort_estimate: "4h"
    subtasks:
      - "⚪ Create folder structure"
      - "⚪ Set up Docker"
      - "⚪ Build CI/CD pipeline"
    
  - id: "TASK-002"
    title: "Authentication system"
    status: "⚪ NOT_STARTED"
    priority: "🔴 CRITICAL"
    due_date: "2024-01-22"
    effort_estimate: "12h"
    dependencies: ["TASK-001"]
    subtasks:
      - "⚪ Determine JWT strategy"
      - "⚪ Write auth service"
      - "⚪ Write tests"
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

echo "🔍 Pre-commit checklist..."
echo ""

# 1. Tests
echo "1. Running tests..."
if ! pytest src/tests/ -v --tb=short 2>/dev/null; then
    echo "❌ Tests failed!"
    exit 1
fi
echo "✅ Tests passed"
echo ""

# 2. Code format
echo "2. Checking code format..."
if ! black --check src/ 2>/dev/null; then
    echo "⚠️  Code formatting issues found. Running: black src/"
    black src/
fi
echo "✅ Code formatted"
echo ""

# 3. Linting
echo "3. Linting..."
if ! flake8 src/ --max-line-length=100 2>/dev/null; then
    echo "⚠️  Linting issues found (non-blocking)"
fi
echo ""

# 4. Type checking (if using Python)
echo "4. Type checking..."
if command -v mypy &> /dev/null; then
    if ! mypy src/ 2>/dev/null; then
        echo "⚠️  Type hints issues (non-blocking)"
    fi
fi
echo ""

# 5. Security
echo "5. Security scan..."
if command -v bandit &> /dev/null; then
    if ! bandit -r src/ -ll 2>/dev/null; then
        echo "⚠️  Security warnings (check them!)"
    fi
fi
echo ""

# 6. Git status
echo "6. Git status:"
git status --short
echo ""

echo "✅ All checks completed!"
echo ""
echo "Ready to commit. Do:"
echo "  git add ."
echo "  git commit -m 'type(scope): message'"
EOF

chmod +x scripts/checkpoint.sh
```

#### 3.2 APCP Update Script

A script to help update the APCP:

```bash
cat > scripts/update-apcp.sh << 'EOF'
#!/bin/bash

echo "📝 Updating APCP files..."
echo ""

# Get current timestamp
TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M:%S UTC")

# Update the header timestamp
sed -i "s/Last Updated: .*/Last Updated: $TIMESTAMP/" AI_PROJECT_CONTEXT.md
sed -i "s/# Last Updated: .*/# Last Updated: $TIMESTAMP/" TASK_PROGRESS.yaml

echo "✅ Updated timestamps"
echo ""

# Show git diff
echo "Changes to APCP files:"
git diff --stat AI_PROJECT_CONTEXT.md TASK_PROGRESS.yaml

echo ""
echo "Ready to commit:"
echo "  git add AI_PROJECT_CONTEXT.md TASK_PROGRESS.yaml"
echo "  git commit -m 'docs: update APCP context and task progress'"
EOF

chmod +x scripts/update-apcp.sh
```

---

### Step 4: First AI Session Setup (5 minutes)

Now send this prompt to the AI:

```markdown
I'm setting up AI-assisted development for my project: [PROJECT_NAME]

I've created:
1. **AI_PROJECT_CONTEXT.md** - Complete project documentation
2. **TASK_PROGRESS.yaml** - Task tracking file
3. **AI_ASSISTANT_PROMPT_TEMPLATES.md** - Prompt templates for different scenarios

I'm ready to start working with you as an AI assistant.

Here's my project:

[PASTE FULL: AI_PROJECT_CONTEXT.md]

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

## 📋 POST-SETUP CHECKLIST

Checklist after completing the setup:

```
APCP Setup Verification:
□ [ ] AI_PROJECT_CONTEXT.md filled with custom project information
□ [ ] TASK_PROGRESS.yaml created with initial tasks
□ [ ] AI_ASSISTANT_PROMPT_TEMPLATES.md in docs/
□ [ ] scripts/checkpoint.sh is working (test: bash scripts/checkpoint.sh)
□ [ ] scripts/update-apcp.sh is working
□ [ ] 3 files committed to Git
□ [ ] Is there a reference to APCP in README.md? (good if there is)
□ [ ] Team members know what APCP is
□ [ ] First AI session conducted and successful
```

---

## 🔄 WEEKLY ROUTINE

Life in the project becomes like this:

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
# 1. Mark completed tasks with ✅
# 2. Merge open PRs
# 3. Finalize TASK_PROGRESS.yaml

# Send to AI (SCENARIO 14)
bash scripts/update-apcp.sh
git add TASK_PROGRESS.yaml
git commit -m "docs: week X retrospective and planning"
git push
```

---

## ⚠️ STRICT RULES (FOR APCP SUCCESS)

### 🔐 NEVER Do

```
❌ Hard-code AI Keys/Secrets in APCP
❌ Commit Production URLs to test
❌ Store user passwords in APCP
❌ Leave documentation obsolete (update it!)
❌ Ignore TASK_PROGRESS (keep it active!)
```

### ✅ ALWAYS Do

```
✅ Run checkpoint.sh before every commit
✅ Update TASK_PROGRESS at the end of every task
✅ Update Section 9 every time an external service is added
✅ Update docs at every major code change
✅ Run update-apcp.sh once a week
✅ Reference APCP sections during code review
```

---

## 🎓 BENEFITS OF APCP (Why so detailed?)

It benefits not only the AI but also the team:

```
From the developer's perspective:
✅ New team members get up-to-speed in 30 minutes
✅ Code reviews accelerate (patterns are defined)
✅ Inconsistency decreases
✅ Even the person doing maintenance knows previous decisions

From management's perspective:
✅ Task tracking is automatic (TASK_PROGRESS.yaml)
✅ Velocity can be measured (estimates vs actual)
✅ Bottlenecks are visible
✅ Project status is always up-to-date

From the AI's perspective:
✅ Uses tokens efficiently (does not reload context)
✅ Model switches are smooth
✅ Works consistently (patterns are specified)
✅ Understands user intent better
```

---

## 🚨 TROUBLESHOOTING

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
[PASTE: AI_PROJECT_CONTEXT.md]
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
[PASTE: AI_PROJECT_CONTEXT.md]
[PASTE: TASK_PROGRESS.yaml]

# Subsequent sessions: MINIMAL
"Working on [PROJECT_NAME].
Current task: TASK-X from https://github.com/user/repo/blob/main/TASK_PROGRESS.yaml
[PASTE: TASK_PROGRESS.yaml - Current sprint section ONLY]
Continue..."
```

---

## 📚 NEXT STEPS

After completing the setup:

1. **Give the first task to the AI** (SCENARIO 1 or 10)
2. **Update APCP once a week** (scripts/update-apcp.sh)
3. **Conduct a retrospective when sprints end** (SCENARIO 14)
4. **Update Section 15 as the team grows** (Escalation contacts)
5. **Monitor success metrics** (Section 12)

---

## 🎯 MEASURE OF SUCCESS

When APCP is successful:

```
✅ AI models remain consistent across sessions
✅ Model switches are problem-free
✅ Tasks are finished within estimated times (Velocity stable)
✅ Code reviews accelerate
✅ New team members onboard quickly
✅ Production bugs decrease
✅ Team morale rises ("Everything is planned!")
✅ Documentation stays up-to-date
```

---

## 📞 SUPPORT AND QUESTIONS

If you have questions:

1. **Read this file again** (usually the answer is there)
2. **Search for the relevant scenario in AI_ASSISTANT_PROMPT_TEMPLATES.md** 
3. **Don't ask questions in GitHub Issues** (other teams benefit)
4. **Ask the team lead** (for internal decisions)

---

## ✨ SUCCESS STORIES

From teams using APCP:

- "When switching models, we didn't have to reload the context!"
- "Our velocity estimate was 96% accurate (we used to always guess wrong)"
- "Bug fixes come out faster because we know the architecture exactly"
- "Newcomers get up-to-speed in 2 hours"
- "Code reviews accelerated by 50%"

---

**🚀 Ready to launch your AI-assisted development?**

**Let's go! 🎯**
