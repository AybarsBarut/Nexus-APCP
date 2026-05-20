param(
    [string]$Message = "Routine checkpoint",
    [switch]$Stage,
    [switch]$Commit
)

$ErrorActionPreference = "Stop"

$blockedPatterns = @(
    "PROMPT_READY.txt",
    "PROMPT_READY.tmp",
    "PROMPT_READY*.txt",
    "PROMPT_READY*.tmp",
    ".env",
    ".env.*",
    "*.local",
    ".apcp-cache/*",
    ".codegraph/*",
    "codegraph.db",
    "codegraph.sqlite",
    "*.codegraph.db",
    "*.codegraph.sqlite",
    "*.apcp.tmp",
    "*.prompt.local",
    "*.context.local"
)

function Get-StatusPath {
    param([string]$StatusLine)

    $path = $StatusLine.Substring(3)
    if ($path -like "* -> *") {
        return ($path -split " -> ", 2)[1]
    }
    return $path
}

function Test-BlockedPath {
    param([string]$Path)

    $normalized = $Path -replace "\\", "/"
    $leaf = Split-Path -Leaf $normalized
    foreach ($pattern in $blockedPatterns) {
        if (($normalized -like $pattern) -or ($leaf -like $pattern)) {
            return $true
        }
    }
    if ($normalized -like "*/.apcp-cache/*") {
        return $true
    }
    if ($normalized -like "*/.codegraph/*") {
        return $true
    }
    return $false
}

Write-Host "[INFO] Starting checkpoint review..." -ForegroundColor Cyan

$statusLines = @(git status --porcelain)
if (-not $statusLines) {
    Write-Host "[OK] No changes to checkpoint." -ForegroundColor Green
    exit 0
}

Write-Host "[INFO] Current working tree changes:" -ForegroundColor Yellow
git status --short

$blocked = @()
$stageable = @()

foreach ($line in $statusLines) {
    if ($line.Length -lt 4) {
        continue
    }
    $path = Get-StatusPath -StatusLine $line
    if (Test-BlockedPath -Path $path) {
        $blocked += $path
    } else {
        $stageable += $path
    }
}

if ($blocked.Count -gt 0) {
    Write-Host "[WARN] Blocked from staging by checkpoint safety rules:" -ForegroundColor Yellow
    $blocked | ForEach-Object { Write-Host "  $_" }
}

if (-not $Stage -and -not $Commit) {
    Write-Host "[INFO] Review mode only. No files were staged or committed." -ForegroundColor Cyan
    Write-Host "[INFO] Re-run with -Stage to stage safe paths, or -Commit to stage and commit."
    exit 0
}

if ($stageable.Count -eq 0) {
    Write-Host "[OK] No safe paths to stage." -ForegroundColor Green
    exit 0
}

Write-Host "[INFO] Staging safe paths only..." -ForegroundColor Cyan
foreach ($path in $stageable) {
    git add -- "$path"
}

Write-Host "[INFO] Staged changes:" -ForegroundColor Yellow
git diff --cached --name-status

if (-not $Commit) {
    Write-Host "[OK] Safe paths staged. Review before committing." -ForegroundColor Green
    exit 0
}

$staged = @(git diff --cached --name-only)
if (-not $staged) {
    Write-Host "[OK] No staged changes to commit." -ForegroundColor Green
    exit 0
}

Write-Host "[INFO] Creating checkpoint commit..." -ForegroundColor Cyan
git commit -m "CHECKPOINT: $Message"

Write-Host "[OK] Checkpoint created: $Message" -ForegroundColor Green
