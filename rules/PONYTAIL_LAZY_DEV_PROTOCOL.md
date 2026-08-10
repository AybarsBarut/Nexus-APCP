# Ponytail Lazy Development Protocol

**Purpose**: Integrates the Ponytail "lazy-senior-dev" logic into the Nexus-APCP rule architecture.
**Attribution**: Based on [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) (MIT License).

## Core Philosophy
The best code is the code you never wrote.

## The Decision Ladder
Evaluate all feature requests and implementations against this ladder, progressing downwards only if necessary:

| Rung | Question | Action |
| --- | --- | --- |
| 1. YAGNI | Does it need to exist? | Delete or reject if unneeded. |
| 2. Codebase Reuse | Is it already in the project? | Reuse existing functions or components. |
| 3. Stdlib | Does the standard library cover it? | Use built-in features. |
| 4. Native Platform | Is it a browser/OS feature? | Use native APIs (e.g., HTML5 validation). |
| 5. Existing Dependency | Is there a package already installed? | Leverage existing dependencies. |
| 6. One-liner | Can it be one line? | Write the shortest possible expression. |
| 7. Minimal Implementation | Only then: minimum code | Write the absolute minimum custom logic. |

## Intensity Levels

Configured via `apcp-profile.json` under `"ponytail"`. Valid values:

| Level | Behavior |
| --- | --- |
| `off` | Protocol disabled. |
| `lite` | Build what is asked, but name the lazier alternative in comments or output. |
| `full` | (Default) Decision Ladder enforced strictly. Minimal implementation always preferred. |
| `ultra` | YAGNI extremist. Deletion must occur before addition. |

## Safety Invariants ("Lazy, Not Negligent")
The following must NEVER be simplified away:
- Input validation
- Error handling
- Security (authentication/authorization)
- Accessibility (a11y)
- Data loss prevention

## Bug Fix Rule
Address the root cause over the symptom. Always `grep` callers first to understand the context and prevent patching over architectural flaws.

## Rules
- No unrequested abstractions.
- No boilerplate for potential future use.
- Deletion over addition.
- Boring over clever.
- Fewest files, shortest diff.

## ponytail: Comment Convention
Mark deliberate shortcuts with a `ponytail:` comment. These must name the ceiling (when it will break/need update) and the upgrade path.
Format: `// ponytail: [shortcut description]. ceiling: [limit]. upgrade: [trigger/path]`

## Output Format
Deliver code first, followed by a maximum of 3 lines of explanation.
Pattern:
`[code] -> skipped: [X], add when [Y]`

## Testing Rule
Non-trivial logic gets ONE runnable check (assert-based self-check or small test). No testing frameworks, no fixtures. Trivial one-liners need no tests.

## Cross-references
- `DEBLOAT_APPLICATION_GUIDE.md`
- `CONTEXT_OPTIMIZATION.md`
- `AI_AGENT_SKILLS_PROTOCOL.md`
