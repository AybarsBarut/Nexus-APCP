#!/usr/bin/env bash
set -euo pipefail

exclude_file="${1:-.git/info/exclude}"

if [ ! -d ".git" ]; then
    echo "ERROR: run this from the root of a Git working tree."
    exit 1
fi

mkdir -p "$(dirname "$exclude_file")"
touch "$exclude_file"

add_pattern() {
    local pattern="$1"
    if ! grep -Fxq "$pattern" "$exclude_file"; then
        printf '%s\n' "$pattern" >> "$exclude_file"
    fi
}

add_pattern "# Nexus-APCP local agent operating files"
add_pattern "AI_PROJECT_CONTEXT_PROTOCOL.md"
add_pattern "rules/AI_MAIN.md"
add_pattern "TASK_PROGRESS.yaml"
add_pattern "rules/DECISION_LOG_PROTOCOL.md"
add_pattern "rules/CONTEXT_OPTIMIZATION.md"
add_pattern "rules/VISUAL_CONTEXT_MERMAID.md"
add_pattern "rules/AI_AGENT_SKILLS_PROTOCOL.md"
add_pattern "rules/AI_TOOL_ADAPTER_COMPATIBILITY_PROTOCOL.md"
add_pattern "rules/CODEGRAPH_INTEGRATION_PROTOCOL.md"
add_pattern "rules/FILE_STRUCTURE_REFACTOR_PROTOCOL.md"
add_pattern "templates/AI_ASSISTANT_PROMPT_TEMPLATES.md"
add_pattern "rules/DOMAIN_SPECIFIC_GITIGNORE_PROTOCOLS.md"
add_pattern "templates/AI_PROJECT_REFERENCE_PROTOCOL.md"
add_pattern "rules/WORKSPACE_SPECIFIC_DELIVERY_PROTOCOLS.md"
add_pattern "rules/MACP_IMPLEMENTATION_GUIDE.md"
add_pattern "templates/WATERFALL_DEVELOPMENT_PROTOCOL.md"
add_pattern "rules/UPDATE_SYSTEM_RECOMMENDATION_PROTOCOL.md"
add_pattern "templates/DEBLOAT_APPLICATION_GUIDE.md"
add_pattern "templates/WEBSITE_BACKEND_SECURITY_OPTIMIZATION_PROTOCOL.md"
add_pattern "templates/DISCOVER_ALGORITHM_DESIGN_GUIDE.md"
add_pattern "templates/FRONTEND_APPLICATION_DESIGN_PROTOCOL.md"
add_pattern "templates/UNIVERSAL_APPLICATION_SECURITY_PROTOCOL.md"
add_pattern "scripts/apcp_core_files.py"
add_pattern "scripts/apcp-gather.py"
add_pattern "scripts/apcp-install.py"
add_pattern "scripts/apcp-init.py"
add_pattern "scripts/install-local-excludes.sh"
add_pattern "scripts/install-local-excludes.ps1"
add_pattern "README_APCP_KIT.md"
add_pattern "MASTER_PROMPT.md"
add_pattern "ZERO_SETUP_PROMPT.txt"
add_pattern "templates/AI_ASSISTANT_PROMPT_TEMPLATES.md"
add_pattern "apcp-profile.json"
add_pattern ".apcp-profile.json"
add_pattern "PROMPT_READY.txt"
add_pattern "PROMPT_READY.tmp"
add_pattern "PROMPT_READY*.txt"
add_pattern "PROMPT_READY*.tmp"
add_pattern ".checkpoint"
add_pattern ".apcp-cache/"
add_pattern ".codegraph/"
add_pattern "codegraph.db"
add_pattern "codegraph.sqlite"
add_pattern "*.codegraph.db"
add_pattern "*.codegraph.sqlite"
add_pattern "*.apcp.tmp"
add_pattern "*.prompt.local"
add_pattern "*.context.local"
add_pattern "*.local"
add_pattern ".env"
add_pattern ".env.*"
add_pattern "*.env.local"

echo "Updated local Git excludes: $exclude_file"
git status --short
