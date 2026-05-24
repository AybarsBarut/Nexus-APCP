# Update System Recommendation Protocol

## Purpose

This protocol tells AI assistants when to recommend a lightweight update system to the user and when to avoid it. It is based on the public Archura SyncGuard pattern: compare a local SemVer file with a GitHub raw version file, download the repository zip when the remote version is newer, preserve local-only files, back up before sync, and launch the app through a guarded start script.

Reference pattern: https://github.com/AybarsBarut/Archura-SyncGuard

## Default Behavior

Do not add an update system automatically for every project. Recommend it only when the user asks for one of these:

- auto update
- updater
- version checker
- sync from GitHub
- launcher that updates before start
- desktop app update system
- portable app update flow
- Git-free update flow for end users

If the user asks for a general deployment, CI/CD, package release, app store release, or server rollout, use the normal deployment protocols instead.

## Fit Check

Recommend this pattern only when most conditions are true:

| Check | Required fit |
| :--- | :--- |
| Runtime target | Windows desktop, internal tool, portable app, or local project folder |
| Distribution source | Public GitHub repository or another public zip endpoint |
| Versioning | Simple `MAJOR.MINOR.PATCH` SemVer is enough |
| Launch flow | User can start through `start.bat`, `start.ps1`, or an equivalent launcher |
| Update scope | Replacing/synchronizing project files from a zip is acceptable |
| Local data | Local-only files can be listed in an exclude list |
| Safety | Backup before update is enabled |
| Git dependency | End user should not need Git installed |

Do not recommend this pattern when any of these are true:

- The project is SaaS, API-only backend, serverless, mobile app store, browser extension store, or package-manager distributed software.
- The update must support signed installers, delta patches, staged rollout, enterprise policy, or rollback orchestration.
- The source repository is private and the project has no approved token handling design.
- The app stores user databases or critical local state that cannot be safely excluded or migrated.
- Cross-platform update support is required and no platform-specific launcher design exists yet.
- The update would overwrite secrets, local config, generated assets, user data, or private context files.

## Recommendation Response Shape

When the user asks for an update system, the AI should respond with a short fit assessment:

```text
Update system fit: [GOOD FIT / PARTIAL FIT / NOT A FIT]
Reason: [one or two concrete reasons]
Recommended pattern: GitHub raw SemVer check + zip sync + backup + exclude list
Required decisions:
- Repository owner/name/branch
- Version file path
- Files to protect from overwrite
- Launcher command
- Backup and restore behavior
```

If the fit is good, ask only for missing project-specific values. If the values are discoverable from the repository, inspect first and propose defaults.

## Implementation Blueprint

Use this structure for projects where the pattern fits:

```text
ProjectRoot/
  version controller/
    version.md
    version-checker.ps1
    config.json
    update-log.md
    backups/
  start.bat
  start.ps1
```

Required behavior:

- `version.md` contains one SemVer value such as `1.0.0`.
- `config.json` stores repository owner, repository name, branch, version path, download mode, protected files, backup setting, backup folder, restart setting, and start command.
- `version-checker.ps1` reads local version, reads remote GitHub raw version, compares SemVer numerically, downloads a zip only when remote is newer, extracts to a temporary folder, syncs files while respecting excludes, logs the result, and restores from backup when needed.
- `start.bat` and/or `start.ps1` run the checker before launching the app.
- The update process must keep `.git`, backups, logs, `.env`, user data, local settings, generated prompt bundles, and filled private context files protected.

## Public Repository Safety

For public template repositories:

- Do not commit real private repository tokens.
- Do not include private customer data in examples.
- Do not commit generated `PROMPT_READY.txt` from a private project.
- Keep updater config examples sanitized.
- For private repositories, stop and design token storage before adding remote downloads.

## Prompt Template

Use this prompt when asking an AI assistant to add the update system to a compatible project:

```text
I want a lightweight update system for this project.

Please first check whether the Archura SyncGuard style pattern fits:
- Windows or portable local app
- public GitHub source
- SemVer version file
- launcher can run before app start
- local-only files can be excluded
- backup before sync is acceptable

If it fits, add:
- version controller/version.md
- version controller/config.json
- version controller/version-checker.ps1
- start.bat or start.ps1 integration
- update-log.md handling
- backup and restore behavior

Protect local-only files such as .env, user data, settings.local.json, generated prompt bundles, backups, logs, and private context files.

If it does not fit, explain why and recommend the correct release/update strategy instead.
```
