# AI Architecture Decision Log (ADL) Protocol

## Purpose
To prevent the "Cycle of Refactoring." AI assistants often suggest changing code that was written in a specific way for a reason (performance, legacy compatibility, etc.). This log stores the **intent** behind the code.

## ADR Template (Architecture Decision Record)

When a significant decision is made, the AI must propose adding a record in `docs/ADR/` using this format:

```markdown
### ADR-[000X]: [Title]
- **Date**: YYYY-MM-DD
- **Status**: [Proposed | Accepted | Superseded]
- **Context**: What was the problem we were solving?
- **Decision**: What did we do?
- **Rationale**: Why did we do it this way? (Why not alternatives?)
- **Consequences**: What are the trade-offs? (e.g., "Makes tests slower but API safer")
```

## AI Instructions
1. **Check Before Changing**: Before refactoring a core module, search the `docs/ADR/` directory for relevant logs.
2. **Propose Logs**: After completing a complex task, if you made a non-obvious technical choice, ask the user: *"Should I document this decision in an ADR?"*
3. **Consistency**: Ensure all new ADRs follow the numbering sequence (ADR-0001, ADR-0002, etc.).
