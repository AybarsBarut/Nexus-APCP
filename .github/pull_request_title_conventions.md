# Pull Request Title Conventions

Nexus-APCP uses simple conventional titles so changelogs, releases, and repository history stay readable.

## Format

```text
type(optional-scope): Summary in imperative present tense
```

Examples:

```text
docs(readme): Clarify AI Project Context Protocol positioning
feat(examples): Add backend API context kit
fix(script): Handle Unicode output on Windows
chore(metadata): Refresh repository SEO topics
```

## Types

| Type | Use for |
| :--- | :--- |
| `feat` | New protocol capabilities, example kits, or user-facing assets. |
| `fix` | Corrections to broken links, scripts, incorrect guidance, or unsafe defaults. |
| `docs` | Documentation-only changes. |
| `prompt` | Prompt templates, AI instructions, or agent guidance. |
| `security` | Safe-publishing guidance, private-context handling, or vulnerability-reporting process. |
| `ci` | GitHub Actions or repository validation automation. |
| `chore` | Metadata, maintenance, cleanup, or non-user-facing updates. |

## Scopes

Common scopes include `readme`, `protocol`, `prompts`, `security`, `seo`, `examples`, `scripts`, `github`, and `agents`.

## Rules

- Use the imperative present tense: `Add`, `Clarify`, `Fix`, `Update`.
- Capitalize the first word after the colon.
- Do not end the title with a period.
- Do not include secrets, private project names, customer names, or vulnerability details.
- For breaking protocol changes, add `!` before the colon and describe the migration path in the PR body.
