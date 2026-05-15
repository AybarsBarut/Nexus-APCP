# Security Policy

Nexus-APCP is a public protocol kit, but real project context can be sensitive. Treat filled context files and generated AI context packages as private by default.

## Do Not Publish

- Filled `AI_PROJECT_CONTEXT.md` files from real projects.
- Backend maps, deployment maps, database internals, architecture-private docs, threat models, and security runbooks.
- API keys, tokens, credentials, certificates, service-account files, `.env` files, and local config.
- Customer data, logs, production exports, model weights, private prompts, or vector databases.
- `PROMPT_READY.txt` files generated from private repositories.

## Reporting a Security Issue

Do not paste secrets or exploit details into a public issue.

If GitHub private vulnerability reporting is enabled for this repository, use it. Otherwise, open a minimal public issue that says you need a private security contact, without including sensitive details.

## Disclosure Expectations

- Give maintainers time to investigate before public disclosure.
- Include only the minimum technical detail needed to reproduce the issue privately.
- Redact tokens, customer data, infrastructure details, and internal project names.

## Supported Versions

The current public protocol files in the default branch are supported.
