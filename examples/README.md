# Nexus-APCP Example Kits

These examples show how to adapt Nexus-APCP for common project types without exposing real private context. Each kit is intentionally small: copy the structure, then replace placeholders with sanitized project-specific information.

## Available Examples

| Example | Use when | Suggested profile |
| :--- | :--- | :--- |
| [`web-app`](./web-app/README.md) | You are building a frontend or full-stack web application with an AI coding assistant. | `web` |
| [`backend-api`](./backend-api/README.md) | You are building an API, service layer, database-backed backend, or integration service. | `backend-api` |
| [`ai-rag`](./ai-rag/README.md) | You are building an AI, RAG, agent, prompt, or LLM-powered product. | `ai-rag` |
| [`security/password-hashing-prompt.md`](./security/password-hashing-prompt.md) | You need a sanitized prompt reference for password hashing design or review. | task-specific reference |

## How To Use An Example

1. Read the example closest to your project.
2. Install the matching Nexus-APCP profile with `scripts/apcp-install.py`.
3. Copy relevant sections into `AI_PROJECT_CONTEXT_PROTOCOL.md`.
4. Add the first few tasks to `TASK_PROGRESS.yaml`.
5. Keep private details local unless they are sanitized.
6. Run:

```bash
python scripts/apcp-gather.py --caveman
```

## Safe Example Rules

- Use placeholder domains, fake IDs, and sample data.
- Never include real credentials, production URLs, customer records, internal diagrams, or generated private context bundles.
- Keep security notes functional and neutral.
