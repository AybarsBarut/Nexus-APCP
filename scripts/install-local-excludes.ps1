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
    "scripts/apcp_core_files.py",
    "scripts/apcp-gather.py",
    "scripts/install-local-excludes.sh",
    "scripts/install-local-excludes.ps1",
    "DISCOVER_ALGORITHM_DESIGN_GUIDE.md",
    "FRONTEND_APPLICATION_DESIGN_PROTOCOL.md",
    "UNIVERSAL_APPLICATION_SECURITY_PROTOCOL.md",
    "README_APCP_KIT.md",
    "MASTER_PROMPT.md",
    "docs/AI_ASSISTANT_PROMPT_TEMPLATES.md",
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
