"""Canonical Nexus-APCP file lists used by scripts and documentation checks."""

CORE_FILES = [
    "AI_PROJECT_CONTEXT_PROTOCOL.md",
    "AI_MAIN.md",
    "TASK_PROGRESS.yaml",
    "DECISION_LOG_PROTOCOL.md",
    "CONTEXT_OPTIMIZATION.md",
    "CAVEMAN_RULES.md",
    "EMOJI_POLICY.md",
    "VISUAL_CONTEXT_MERMAID.md",
    "AI_AGENT_SKILLS_PROTOCOL.md",
    "AI_TOOL_ADAPTER_COMPATIBILITY_PROTOCOL.md",
    "CODEGRAPH_INTEGRATION_PROTOCOL.md",
    "FILE_STRUCTURE_REFACTOR_PROTOCOL.md",
    "AI_ASSISTANT_PROMPT_TEMPLATES.md",
    "WORKSPACE_SPECIFIC_DELIVERY_PROTOCOLS.md",
    "DOMAIN_SPECIFIC_GITIGNORE_PROTOCOLS.md",
    "MACP_IMPLEMENTATION_GUIDE.md",
    "WATERFALL_DEVELOPMENT_PROTOCOL.md",
    "UPDATE_SYSTEM_RECOMMENDATION_PROTOCOL.md",
    "DEBLOAT_APPLICATION_GUIDE.md",
    "WEBSITE_BACKEND_SECURITY_OPTIMIZATION_PROTOCOL.md",
]

INSTALL_SUPPORT_FILES = [
    "scripts/apcp_core_files.py",
    "scripts/apcp-gather.py",
    "scripts/install-local-excludes.sh",
    "scripts/install-local-excludes.ps1",
]

INSTALL_FILES = [
    *CORE_FILES,
    *INSTALL_SUPPORT_FILES,
]

OPTIONAL_LOCAL_CONTEXT_FILES = [
    "DISCOVER_ALGORITHM_DESIGN_GUIDE.md",
    "FRONTEND_APPLICATION_DESIGN_PROTOCOL.md",
    "UNIVERSAL_APPLICATION_SECURITY_PROTOCOL.md",
    "README_APCP_KIT.md",
    "MASTER_PROMPT.md",
    "docs/AI_ASSISTANT_PROMPT_TEMPLATES.md",
]

GENERATED_CONTEXT_PATTERNS = [
    "PROMPT_READY.txt",
    "PROMPT_READY.tmp",
    "PROMPT_READY*.txt",
    "PROMPT_READY*.tmp",
    ".checkpoint",
    ".apcp-cache/",
    ".codegraph/",
    "codegraph.db",
    "codegraph.sqlite",
    "*.codegraph.db",
    "*.codegraph.sqlite",
    "*.apcp.tmp",
    "*.prompt.local",
    "*.context.local",
    "*.local",
]

LOCAL_SECRET_PATTERNS = [
    ".env",
    ".env.*",
    "*.env.local",
]

LOCAL_EXCLUDE_PATTERNS = [
    *INSTALL_FILES,
    *OPTIONAL_LOCAL_CONTEXT_FILES,
    *GENERATED_CONTEXT_PATTERNS,
    *LOCAL_SECRET_PATTERNS,
]

PUBLIC_REQUIRED_FILES = [
    "README.md",
    "CHANGELOG.md",
    ".gitignore",
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    "CURSOR.md",
    "COPILOT.md",
    "CODEX.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "CITATION.cff",
    "codemeta.json",
    *CORE_FILES,
    "MASTER_PROMPT.md",
    "docs/SEO_CHECKLIST.md",
    "scripts/apcp_core_files.py",
    "scripts/apcp-gather.py",
    "scripts/validate-repo.py",
    "scripts/checkpoint.ps1",
    "scripts/install-local-excludes.ps1",
    "scripts/install-local-excludes.sh",
    ".github/CODEOWNERS",
    ".github/pull_request_template.md",
    ".github/pull_request_title_conventions.md",
    ".github/repository-metadata.yml",
    ".github/workflows/validate.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/docs_improvement.yml",
    ".github/ISSUE_TEMPLATE/protocol_suggestion.yml",
    ".github/ISSUE_TEMPLATE/security_private.yml",
    "examples/README.md",
]
