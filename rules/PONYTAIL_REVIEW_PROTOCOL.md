# Ponytail Review Protocol

**Purpose**: Consolidates ponytail-review (diff review), ponytail-audit (repo-wide audit), and ponytail-debt (debt tracking) into one unified protocol.
**Attribution**: Based on [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) (MIT License).

## Review Mode (Diffs/PRs)

Format comments as follows:
`L<line>: <tag> <what>. <replacement>.`

**Tags**:
- `delete:`
- `stdlib:`
- `native:`
- `yagni:`
- `shrink:`

**End Summary**:
End the review with either `net: -<N> lines possible.` or `Lean already. Ship.`

**Examples**:
*Bad format*: "I think we could probably use the built-in map function here to save some lines of code."
*Good format*: `L42: stdlib custom loop. Array.map().`

## Audit Mode (Repo-wide)

Uses the same tags as Review Mode.

**Hunt List**:
- Single-implementation interfaces
- Pass-through wrappers
- Hand-rolled stdlib equivalents
- Unused dependencies
- Dead feature flags

**Format**:
`<tag> <what to cut>. <replacement>. [path]`

Rank findings by the biggest cut first.

**End Summary**:
`net: -<N> lines, -<M> deps possible.`

## Debt Ledger Mode

Track deliberate shortcuts and technical debt left by the Ponytail protocol.

**Grep Command**:
`grep -rnE '(#|//) ?ponytail:' .` (skip node_modules, .git, build directories)

**Row Format**:
`<file>:<line>, <what was simplified>. ceiling: <limit>. upgrade: <trigger>.`

Flag markers missing an upgrade path with `no-trigger`.

**End Summary**:
`<N> markers, <M> with no trigger.`

## Scope Boundaries
This protocol targets over-engineering and complexity ONLY. Correctness bugs, security holes, and performance issues are out of scope.

## Cross-references
- `PONYTAIL_LAZY_DEV_PROTOCOL.md`
- `AI_AGENT_SKILLS_PROTOCOL.md`
