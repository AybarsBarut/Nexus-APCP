# Nexus-APCP Checkpoint Script (Windows/PowerShell)
# Purpose: Create a development checkpoint by committing current changes.

$message = $args[0]
if (-not $message) {
    $message = "Routine checkpoint"
}

Write-Host "[INFO] Starting Checkpoint Protocol..." -ForegroundColor Cyan

# 1. Check for changes
$status = git status --porcelain
if (-not $status) {
    Write-Host "[OK] No changes to checkpoint." -ForegroundColor Green
    exit
}

# 2. Sync Task Progress (Optional: user can manually update before running)
Write-Host "[INFO] Syncing TASK_PROGRESS.yaml..." -ForegroundColor Yellow
# In a real scenario, we could auto-update the last_updated field here.

# 3. Commit
Write-Host "[INFO] Committing changes..." -ForegroundColor Magenta
git add .
git commit -m "CHECKPOINT: $message"

Write-Host "[OK] Checkpoint created: $message" -ForegroundColor Green
