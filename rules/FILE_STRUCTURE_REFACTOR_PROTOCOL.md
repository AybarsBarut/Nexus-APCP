# File Structure Refactor Protocol

## Purpose

This protocol gives AI agents and maintainers a safe way to reorganize files in an existing project after Nexus-APCP has already been added. The goal is to improve repository readability without breaking code that was written before the new structure existed.

Use this protocol when a project needs:
- A clearer folder layout.
- Separation between app, domain, infrastructure, tests, docs, and scripts.
- Migration from a flat repository into a maintainable architecture.
- Cleanup after rapid prototyping.
- Iterative restructuring while active development continues.
- Import, path, asset, test, or build updates after files move.

Do not use this protocol to hide private context, rename security-sensitive material for public release, or move generated prompt bundles into tracked source control. Keep the public/private boundary defined in `AGENTS.md`, `EMOJI_POLICY.md`, and the main project protocol.

## Core Rule

A file structure refactor is not complete when files have moved. It is complete only when the moved code can still be imported, built, tested, and run from its new location.

Every iteration must preserve or restore:
- Runtime entry points.
- Imports and module resolution.
- Test discovery.
- Build and packaging configuration.
- Asset and template paths.
- CLI, script, and deployment commands.
- Documentation links.
- Existing public APIs unless a breaking change is explicitly approved.

## Preflight Inventory

Before moving files, inspect the repository and write a short migration inventory.

Minimum inventory:

```markdown
## File Structure Inventory

### Current Entry Points
- App start command:
- CLI commands:
- Worker commands:
- Test command:
- Build command:
- Deployment command:

### Current File Groups
- Source:
- Tests:
- Config:
- Scripts:
- Docs:
- Assets:
- Generated files:

### Known Path Coupling
- Relative imports:
- Absolute imports or aliases:
- Asset paths:
- Template paths:
- Test fixture paths:
- Docker or CI paths:
- Package exports:

### Private or Generated Files That Must Not Move Into Public Source
- `.env` files:
- local settings:
- generated context bundles:
- customer or production data:
- private architecture maps:
```

If a command, entry point, or coupling point is unknown, discover it before moving files. Do not guess when the project has real runtime behavior.

## Target Structure Plan

Create a target structure before editing. Keep it boring, explicit, and aligned with the project type.

Recommended structure template:

```text
project-root/
├── README.md
├── AI_PROJECT_CONTEXT_PROTOCOL.md
├── TASK_PROGRESS.yaml
├── docs/
│   ├── ARCHITECTURE.md
│   ├── SETUP.md
│   └── DECISIONS.md
├── src/
│   ├── app/
│   ├── domain/
│   ├── infrastructure/
│   └── shared/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── scripts/
├── config/
└── assets/
```

Adapt the structure to the stack. Do not force every project into the same layout.

Common adaptations:
- Frontend apps may use `src/components`, `src/routes`, `src/lib`, `public`, and `tests`.
- Backend APIs may use `src/api`, `src/services`, `src/models`, `src/repositories`, and `src/workers`.
- Python packages may use `src/package_name`, `tests`, and `pyproject.toml`.
- Node packages may use `src`, `test` or `tests`, `dist`, and `package.json` exports.
- AI or RAG projects may use `src/prompts`, `src/retrieval`, `src/evals`, and `data/samples`.
- Documentation kits may use root protocol files, `docs`, `examples`, `scripts`, and `assets`.

## Iterative Migration Loop

Move files in small, verified iterations. One iteration should have a clear theme and a small blast radius.

```text
1. Select one file group.
2. Record current references.
3. Move files with history-preserving commands when possible.
4. Update imports, paths, configs, tests, and docs.
5. Add temporary compatibility shims if existing entry points depend on old paths.
6. Run targeted verification.
7. Run broader verification.
8. Update task state and migration notes.
9. Continue with the next file group.
```

Good iteration examples:
- Move tests into `tests/unit` and update test discovery.
- Move reusable code into `src/shared` and update imports.
- Move scripts into `scripts` and update README commands.
- Move UI components into `src/components` and update route imports.
- Move database code into `src/infrastructure/database` and update service imports.

Avoid moving source, tests, scripts, config, and docs in one large pass unless the project is tiny and verification is trivial.

## Move Safety Rules

- Prefer `git mv` when the repository is under Git and the user has allowed Git operations.
- If Git operations are restricted, use normal filesystem moves but document the old path and new path.
- Never move ignored secrets, local environment files, production data, or generated private context into tracked directories.
- Do not rename public APIs while moving files unless the user approved a breaking change.
- Keep old entry points working with compatibility wrappers when users or scripts may still call them.
- Update imports with parser-aware or framework-aware tooling when available.
- Update path aliases in config files instead of adding fragile relative import chains.
- Keep file names consistent with the target language and framework conventions.
- After a move, search for old paths and old module names.
- Do not delete the old path until replacement behavior has been verified or a shim is in place.

## Compatibility Patterns

Use temporary compatibility only when it reduces breakage risk. Remove it later through a planned cleanup task.

### Re-export Module

Use when code imports from an old module path.

```python
# old_module.py
from new_package.module import *
```

```ts
// old-module.ts
export * from "./new-location/module";
```

### Entrypoint Wrapper

Use when scripts, docs, or deployment commands still call an old path.

```python
# old_entrypoint.py
from new_package.cli import main

if __name__ == "__main__":
    main()
```

### Package Export Alias

Use when consumers import package-level paths.

```json
{
  "exports": {
    ".": "./dist/index.js",
    "./old-path": "./dist/new-path.js"
  }
}
```

### Path Alias

Use when a project supports aliases through its compiler or bundler.

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@app/*": ["src/app/*"],
      "@shared/*": ["src/shared/*"]
    }
  }
}
```

Compatibility shims must be documented with:
- Old path.
- New path.
- Reason for keeping the shim.
- Planned removal condition.

## Reference Update Checklist

After every move, update all relevant references.

Code references:
- Imports and exports.
- Dynamic imports.
- Reflection or plugin discovery paths.
- Package exports.
- Test imports.
- Fixture paths.

Runtime references:
- App start commands.
- CLI commands.
- Worker commands.
- Cron or scheduler commands.
- Docker `COPY`, `CMD`, and `ENTRYPOINT`.
- CI workflow paths.
- Deployment manifests.

Build references:
- `package.json` scripts.
- `tsconfig.json` paths.
- Bundler config.
- `pyproject.toml`, `setup.cfg`, or `setup.py`.
- `pytest.ini` or test runner config.
- Lint and formatter config.
- Static asset config.

Documentation references:
- README commands and links.
- Setup guide commands.
- Architecture diagrams.
- Mermaid flowcharts.
- API docs.
- Changelog or migration notes.
- AI context protocol folder maps.

## Verification Gates

Run the smallest relevant verification after each iteration, then broader verification before finishing.

Minimum verification:

```bash
# Search for old path references
rg "old/path|old_module|old-command"

# Run the most relevant test target
pytest
npm test
pnpm test
go test ./...
dotnet test

# Run build or typecheck when available
npm run build
npm run typecheck
python -m compileall src
```

Project-specific verification:
- Start the app from the documented command.
- Import the moved modules from a clean shell.
- Run one smoke test for each moved entry point.
- Render or build frontend assets.
- Run database migrations in a safe local test environment if migration files moved.
- Run container build if Docker paths changed.
- Run CI validation locally where possible.

For Nexus-APCP repositories, also run:

```bash
python scripts/apcp-gather.py --caveman
python scripts/validate-repo.py
```

## Existing Code Guarantee

When this protocol is applied to an existing project, previously written code must continue working after each accepted iteration unless the user explicitly approves a breaking migration.

The agent must prove this by one of these methods:
- Existing tests pass after imports and paths are updated.
- A smoke command imports or runs the moved code from the new location.
- A compatibility wrapper keeps the old path working while new imports are introduced.
- Build, typecheck, or package validation confirms the moved module is discoverable.

If verification fails:
1. Stop moving new files.
2. Identify whether the failure is an import, path, config, asset, test, or runtime command issue.
3. Fix the reference or add a temporary shim.
4. Re-run the failing verification.
5. Continue only after the iteration is green.

Do not leave a repository in a state where the new folder layout looks cleaner but existing code cannot run.

## Migration Notes Template

Use this note format in `TASK_PROGRESS.yaml`, a migration PR description, or a temporary local planning document.

```markdown
## File Structure Refactor Notes

### Goal
[Describe the readability or maintainability goal.]

### Iteration
[Iteration number and scope.]

### Moves
| Old path | New path | Compatibility needed |
| :--- | :--- | :--- |
| `[old/path]` | `[new/path]` | `[yes/no and reason]` |

### References Updated
- Imports:
- Scripts:
- Tests:
- Build config:
- Docs:

### Verification
- Command:
- Result:
- Remaining risk:

### Next Iteration
[Describe the next file group, or state that migration is complete.]
```

## AI Agent Prompt

Use this prompt when asking an AI assistant to restructure an existing project.

```text
Apply FILE_STRUCTURE_REFACTOR_PROTOCOL.md to this repository.

Goal:
[Describe the desired file organization.]

Rules:
- Inspect the current structure, entry points, scripts, tests, imports, and config before moving files.
- Propose a target structure and migrate in small iterations.
- After each iteration, update imports, path aliases, scripts, tests, docs, and Mermaid diagrams affected by the move.
- Preserve existing behavior unless I explicitly approve a breaking change.
- If old paths are still used, add temporary compatibility wrappers or re-exports and document their removal condition.
- Run the relevant verification commands after each iteration.
- Do not move secrets, generated private context bundles, local environment files, customer data, or private architecture maps into public source.
- Update TASK_PROGRESS.yaml when a visible migration task is completed.

Before editing, report the first iteration scope and the verification commands you will use.
```

## Done Criteria

A file structure refactor is done only when:
- The target folder map is documented.
- All intended files for the current iteration are moved.
- Old references are updated or compatibility wrappers are present.
- Tests, build, typecheck, or smoke checks pass for the moved code.
- README and setup commands still match the working repository.
- Mermaid README flowcharts still match the high-level structure.
- AI context files reflect the new layout.
- Private and generated files remain out of public source.
- `TASK_PROGRESS.yaml` records the completed migration task.

## Failure Signals

Stop and repair the migration if any of these appear:
- Imports only work from the agent's current shell but fail from a clean environment.
- Tests pass because moved code is no longer discovered.
- README commands point to old paths.
- Docker or CI still copies old directories.
- Assets render in development but fail in production builds.
- Package consumers lose an exported module path without approval.
- Compatibility wrappers hide a real path problem indefinitely.
- The folder layout is cleaner but startup, build, or tests are broken.
