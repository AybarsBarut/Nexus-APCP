# Security Policy

Nexus-APCP is a public protocol kit, but real project context can be sensitive. Treat filled context files, generated AI context packages, and downstream installed APCP operating files as private by default unless sanitized publication is explicitly approved.

## Do Not Publish

- Filled `AI_PROJECT_CONTEXT_PROTOCOL.md` files from real projects, or downstream filled copies such as `AI_PROJECT_CONTEXT.md`.
- Installed Nexus-APCP operating files copied into downstream public product repositories, unless they are intentionally approved sanitized templates.
- Backend maps, deployment maps, database internals, architecture-private docs, threat models, and security runbooks.
- API keys, tokens, credentials, certificates, service-account files, `.env` files, and local config.
- Customer data, logs, production exports, model weights, private prompts, or vector databases.
- `PROMPT_READY.txt` files generated from private repositories.

## Reporting a Security Issue

Do not paste secrets or exploit details into a public issue.

Use GitHub Private Vulnerability Reporting for this repository. Maintainers should keep private vulnerability reporting enabled in the GitHub repository settings so reports can be opened without exposing details publicly.

If the GitHub interface does not show a private reporting option, open only a minimal public issue using the security-sensitive issue template and ask for a private maintainer contact. Do not include technical details, proof material, secrets, infrastructure names, customer data, generated context bundles, or reproduction steps in that public issue.

## Disclosure Expectations

- Give maintainers time to investigate before public disclosure.
- Include only the minimum technical detail needed to reproduce the issue privately.
- Redact tokens, customer data, infrastructure details, and internal project names.

## Supported Versions

The current public protocol files in the default branch are supported.
