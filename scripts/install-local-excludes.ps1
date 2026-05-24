param(
    [string]$ExcludePath = ".git/info/exclude"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath ".git")) {
    Write-Host "ERROR: run this from the root of a Git working tree." -ForegroundColor Red
    exit 1
}

$patterns = @(
    "# Nexus-APCP local agent operating files",
    "AI_PROJECT_CONTEXT_PROTOCOL.md",
    "rules/AI_MAIN.md",
    "TASK_PROGRESS.yaml",
    "rules/DECISION_LOG_PROTOCOL.md",
    "rules/CONTEXT_OPTIMIZATION.md",
    "rules/VISUAL_CONTEXT_MERMAID.md",
    "rules/AI_AGENT_SKILLS_PROTOCOL.md",
    "rules/AI_TOOL_ADAPTER_COMPATIBILITY_PROTOCOL.md",
    "rules/CODEGRAPH_INTEGRATION_PROTOCOL.md",
    "rules/FILE_STRUCTURE_REFACTOR_PROTOCOL.md",
    "templates/AI_ASSISTANT_PROMPT_TEMPLATES.md",
    "rules/DOMAIN_SPECIFIC_GITIGNORE_PROTOCOLS.md",
    "templates/AI_PROJECT_REFERENCE_PROTOCOL.md",
    "rules/WORKSPACE_SPECIFIC_DELIVERY_PROTOCOLS.md",
    "rules/MACP_IMPLEMENTATION_GUIDE.md",
    "templates/WATERFALL_DEVELOPMENT_PROTOCOL.md",
    "rules/UPDATE_SYSTEM_RECOMMENDATION_PROTOCOL.md",
    "templates/DEBLOAT_APPLICATION_GUIDE.md",
    "templates/WEBSITE_BACKEND_SECURITY_OPTIMIZATION_PROTOCOL.md",
    "templates/DISCOVER_ALGORITHM_DESIGN_GUIDE.md",
    "templates/FRONTEND_APPLICATION_DESIGN_PROTOCOL.md",
    "templates/UNIVERSAL_APPLICATION_SECURITY_PROTOCOL.md",
    "scripts/apcp_core_files.py",
    "scripts/apcp-gather.py",
    "scripts/apcp-install.py",
    "scripts/apcp-init.py",
    "scripts/install-local-excludes.sh",
    "scripts/install-local-excludes.ps1",
    "README_APCP_KIT.md",
    "MASTER_PROMPT.md",
    "ZERO_SETUP_PROMPT.txt",
    "templates/AI_ASSISTANT_PROMPT_TEMPLATES.md",
    "apcp-profile.json",
    ".apcp-profile.json",
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
    ".env",
    ".env.*",
    "*.env.local"
)

$target = Join-Path (Get-Location) $ExcludePath
$directory = Split-Path -Parent $target

if ($directory) {
    New-Item -ItemType Directory -Force -Path $directory | Out-Null
}

if (-not (Test-Path -LiteralPath $target)) {
    New-Item -ItemType File -Path $target | Out-Null
}

$existing = Get-Content -LiteralPath $target -ErrorAction SilentlyContinue
foreach ($pattern in $patterns) {
    if ($existing -notcontains $pattern) {
        Add-Content -LiteralPath $target -Value $pattern
    }
}

Write-Host "Updated local Git excludes: $ExcludePath" -ForegroundColor Green
git status --short
