"""Canonical Nexus-APCP file inventories, profiles, and install sets."""


def unique_files(items):
    """Return paths in first-seen order without duplicates."""
    seen = set()
    unique = []
    for item in items:
        if item not in seen:
            unique.append(item)
            seen.add(item)
    return unique


DEFAULT_PROFILE = "core"

BASE_CONTEXT_FILES = [
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
    "DOMAIN_SPECIFIC_GITIGNORE_PROTOCOLS.md",
]

SPECIALIZED_CONTEXT_FILES = [
    "WORKSPACE_SPECIFIC_DELIVERY_PROTOCOLS.md",
    "MACP_IMPLEMENTATION_GUIDE.md",
    "WATERFALL_DEVELOPMENT_PROTOCOL.md",
    "UPDATE_SYSTEM_RECOMMENDATION_PROTOCOL.md",
    "DEBLOAT_APPLICATION_GUIDE.md",
    "WEBSITE_BACKEND_SECURITY_OPTIMIZATION_PROTOCOL.md",
    "DISCOVER_ALGORITHM_DESIGN_GUIDE.md",
    "FRONTEND_APPLICATION_DESIGN_PROTOCOL.md",
    "UNIVERSAL_APPLICATION_SECURITY_PROTOCOL.md",
]

# Backward-compatible name used by validation and older helpers.
# This is the complete public protocol inventory, not the default active context.
CORE_FILES = unique_files([*BASE_CONTEXT_FILES, *SPECIALIZED_CONTEXT_FILES])

PROFILE_FILE_ADDITIONS = {
    "core": [],
    "web": [
        "FRONTEND_APPLICATION_DESIGN_PROTOCOL.md",
        "WEBSITE_BACKEND_SECURITY_OPTIMIZATION_PROTOCOL.md",
        "DEBLOAT_APPLICATION_GUIDE.md",
        "UNIVERSAL_APPLICATION_SECURITY_PROTOCOL.md",
        "WORKSPACE_SPECIFIC_DELIVERY_PROTOCOLS.md",
    ],
    "backend-api": [
        "UNIVERSAL_APPLICATION_SECURITY_PROTOCOL.md",
        "WORKSPACE_SPECIFIC_DELIVERY_PROTOCOLS.md",
    ],
    "cli": [
        "WORKSPACE_SPECIFIC_DELIVERY_PROTOCOLS.md",
        "UPDATE_SYSTEM_RECOMMENDATION_PROTOCOL.md",
    ],
    "game": [
        "DISCOVER_ALGORITHM_DESIGN_GUIDE.md",
        "WORKSPACE_SPECIFIC_DELIVERY_PROTOCOLS.md",
    ],
    "ai-rag": [
        "DISCOVER_ALGORITHM_DESIGN_GUIDE.md",
        "UNIVERSAL_APPLICATION_SECURITY_PROTOCOL.md",
        "WORKSPACE_SPECIFIC_DELIVERY_PROTOCOLS.md",
    ],
    "full": SPECIALIZED_CONTEXT_FILES,
}

PROFILE_DESCRIPTIONS = {
    "core": "Project memory, task state, decisions, AI rules, prompts, and safe publishing.",
    "web": "Frontend/web work with static-first backend safety, lean app guidance, and delivery gates.",
    "backend-api": "API or service work with application security and delivery gates.",
    "cli": "Command-line or developer-tool projects with delivery and optional updater fit checks.",
    "game": "Game or simulation projects with algorithm/design discovery and delivery gates.",
    "ai-rag": "AI, RAG, or data-assisted applications with discovery, security, and delivery gates.",
    "full": "Every public Nexus-APCP protocol file. Use only when broad context is intentional.",
}

PROFILE_ALIASES = {
    "all": "full",
    "api": "backend-api",
    "backend": "backend-api",
    "default": DEFAULT_PROFILE,
    "minimal": DEFAULT_PROFILE,
    "rag": "ai-rag",
}

CONTEXT_PROFILE_FILES = {
    profile: unique_files([*BASE_CONTEXT_FILES, *additions])
    for profile, additions in PROFILE_FILE_ADDITIONS.items()
}

INSTALL_SUPPORT_FILES = [
    "scripts/apcp_core_files.py",
    "scripts/apcp-gather.py",
    "scripts/apcp-install.py",
    "scripts/install-local-excludes.sh",
    "scripts/install-local-excludes.ps1",
]

INSTALL_FILES = unique_files([*CORE_FILES, *INSTALL_SUPPORT_FILES])

OPTIONAL_LOCAL_CONTEXT_FILES = [
    "README_APCP_KIT.md",
    "MASTER_PROMPT.md",
    "docs/AI_ASSISTANT_PROMPT_TEMPLATES.md",
]

LOCAL_AGENT_CONFIG_FILES = [
    "apcp-profile.json",
    ".apcp-profile.json",
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
    *LOCAL_AGENT_CONFIG_FILES,
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
    "docs/RELEASE_PROCESS.md",
    "docs/REPOSITORY_LAYOUT.md",
    "scripts/apcp_core_files.py",
    "scripts/apcp-gather.py",
    "scripts/apcp-install.py",
    "scripts/validate-repo.py",
    "scripts/checkpoint.ps1",
    "scripts/install-local-excludes.ps1",
    "scripts/install-local-excludes.sh",
    "tests/test_apcp_tools.py",
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


def normalize_profile(profile):
    selected = (profile or DEFAULT_PROFILE).strip().lower()
    return PROFILE_ALIASES.get(selected, selected)


def available_profiles():
    return list(PROFILE_FILE_ADDITIONS.keys())


def profile_description(profile):
    return PROFILE_DESCRIPTIONS[normalize_profile(profile)]


def get_profile_files(profile=None):
    selected = normalize_profile(profile)
    if selected not in CONTEXT_PROFILE_FILES:
        valid = ", ".join(available_profiles())
        raise ValueError(f"Unknown APCP profile: {profile}. Valid profiles: {valid}")
    return list(CONTEXT_PROFILE_FILES[selected])


def get_install_files(profile=None, include_support=True):
    files = get_profile_files(profile)
    if include_support:
        files = [*files, *INSTALL_SUPPORT_FILES]
    return unique_files(files)
