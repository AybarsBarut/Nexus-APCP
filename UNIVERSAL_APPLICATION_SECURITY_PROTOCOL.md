# Universal Application Security Protection Protocol
## SQL güvenliği, veri koruma, kimlik, yetki, tedarik zinciri ve dağıtım savunmaları için savunma odaklı rehber

Version: 1.0
Owner: Project team and AI assistants
Status: Recommended protocol layer for every project that stores data, accepts user input, exposes a network surface, ships client code, calls third-party APIs, or handles AI/model workflows.
Scope: Static websites, full-stack web apps, backend APIs, SaaS products, mobile apps, desktop apps, CLI tools, ecommerce systems, AI/RAG products, game backends, data dashboards, internal tools, plugins, automation scripts, and cloud/serverless workloads.

---

## 0. Safety Boundary

This file is defensive. It explains how to prevent, detect, limit, and recover from common software security failures. It intentionally avoids exploit payloads, step-by-step attack paths, private infrastructure examples, and sensitive operational details.

Use this protocol as a checklist before release, before connecting a database, before exposing an API, and before asking an AI coding assistant to modify security-sensitive code.

---

## 1. Core Rule

Every project should assume:

> All external input is untrusted. All secrets leak if placed on the client. All authorization must be checked on the server. All dependencies can become risk. All logs can become sensitive data.

Security is not one library or one firewall. It is a layered system:

1. Secure design.
2. Safe implementation.
3. Least privilege runtime.
4. Automated verification.
5. Monitoring and incident recovery.

---

## 2. Project Type Matrix

| Project type | Main risks | Minimum protection baseline |
| --- | --- | --- |
| Static site / portfolio | Exposed secrets, unsafe forms, third-party scripts, supply-chain drift | No secrets in frontend, strict form provider/serverless relay, dependency pinning, security headers, minimal analytics |
| Marketing / landing page | Lead form abuse, spam, script injection, tracking/privacy issues | Server-side form validation, rate limits, CAPTCHA only when needed, consent-aware analytics, CSP |
| Full-stack web app | Unsafe database access, session risk, broken authorization, XSS/CSRF | Parameterized queries, server-side authz, secure cookies, CSRF controls, output encoding, centralized validation |
| Backend API | Broken object access, weak tokens, overexposed endpoints, abuse traffic | Strong auth, object-level authorization, rate limits, schema validation, audit logs, versioned contracts |
| SaaS / multitenant | Tenant data mixing, privilege escalation, billing abuse, admin misuse | Tenant isolation, scoped queries, RBAC/ABAC, audit trails, billing idempotency, break-glass controls |
| Mobile app | Hardcoded secrets, insecure storage, API abuse, reverse engineering | No embedded private keys, OS secure storage, certificate validation, backend-enforced authorization |
| Desktop app / CLI | Unsafe file paths, command execution, local secrets, update tampering | Safe path handling, no shell string building, signed updates where possible, OS keychain storage |
| Ecommerce | Payment integrity, order manipulation, webhook replay, inventory races | Hosted payment provider, webhook verification, idempotency keys, server-side price calculation |
| AI/RAG app | Prompt/data boundary issues, tool overreach, data leakage, cost abuse | Server-side model calls, tool allowlists, retrieval filtering, prompt/data separation, quotas |
| Game backend | Cheating, replay, inventory/currency manipulation, account theft | Server-authoritative state, anti-replay, transaction logs, rate limits, fraud review |
| Data dashboard | Overbroad data access, unsafe exports, formula/file injection, privacy leaks | Row-level controls, export sanitization, aggregation rules, data minimization |
| Internal admin tool | Excessive privileges, weak review, sensitive logs, lateral movement | MFA/SSO, IP/device controls where possible, least privilege roles, mandatory audit logging |
| Plugin/extension | Overbroad permissions, unsafe content scripts, token leakage | Minimal permissions, isolated storage, explicit host allowlists, reviewable release package |
| Serverless/cloud job | Overprivileged IAM, public buckets, secret sprawl, event replay | Least-privilege IAM, private-by-default resources, secret manager, event validation |

---

## 3. Universal Security Lifecycle

### 3.1 Design Gate

Before implementation, document:

- What data is stored, where it lives, and who can access it.
- Which inputs are accepted from users, browsers, webhooks, files, queues, or AI tools.
- Which operations require authentication.
- Which operations require authorization beyond authentication.
- Which secrets exist and where they are stored.
- Which dependencies, APIs, SDKs, and infrastructure services are trusted.
- What should happen if validation, authorization, payment, model calls, or storage fails.

Stop if the design cannot answer:

- "Can one user access another user's data?"
- "Can a frontend caller change server-trusted fields?"
- "Can a low-privilege role trigger admin behavior?"
- "Can a leaked client bundle reveal private credentials?"
- "Can a retry duplicate payment, inventory, email, or destructive state?"

### 3.2 Implementation Gate

Every security-sensitive implementation should include:

- Centralized input validation at trust boundaries.
- Safe database access patterns.
- Server-side authorization checks.
- Structured errors that do not leak internals.
- Tests for allowed and denied paths.
- Logging for security-relevant decisions without storing secrets.
- Dependency and configuration review.

### 3.3 Release Gate

Before release:

- Run the project test suite.
- Run dependency vulnerability checks where available.
- Verify no secrets are committed or bundled.
- Review security headers and CORS policy for web apps.
- Confirm production configuration differs from development configuration.
- Confirm backups, rollback, and incident contact paths.
- Confirm monitoring alerts for authentication, authorization, billing, and error spikes.

---

## 4. Input Handling

### 4.1 Trust Boundaries

Treat these as untrusted:

- HTTP request bodies, query strings, headers, cookies, and route params.
- WebSocket messages.
- GraphQL variables and operation names.
- Uploaded files and filenames.
- Webhook payloads.
- Queue messages and scheduled job payloads.
- Environment variables supplied by deployment systems.
- Browser local storage and client-side state.
- Mobile app state and device identifiers.
- AI model output, tool-call arguments, and retrieved documents.
- CSV, Excel, JSON, XML, YAML, Markdown, PDF, image metadata, and archive contents.

### 4.2 Validation Rules

Use allowlist validation:

- Define expected type, length, range, format, and allowed enum values.
- Reject unknown object fields unless forward compatibility requires them.
- Normalize before validation where appropriate.
- Validate again on the server even if the client already validates.
- Validate file size, MIME type, extension, magic bytes, and post-processing result.
- Validate IDs as references, not as proof of access.

Avoid:

- Blacklist-only filtering.
- Reusing frontend validation as the only gate.
- Treating ORM models, DTOs, or TypeScript types as runtime security controls by themselves.
- Accepting arbitrary JSON objects and passing them directly into queries, filters, commands, templates, or model tools.

### 4.3 Canonicalization

Normalize ambiguous input before security decisions:

- Trim and normalize user identifiers consistently.
- Decode URL/path data once in a controlled layer.
- Resolve filesystem paths and verify they remain inside the intended directory.
- Convert Unicode-sensitive identifiers carefully.
- Store normalized values where uniqueness matters.

---

## 5. Database and Query Safety

### 5.1 Required Pattern

All database access must separate query structure from user-supplied values.

Use:

- Parameterized queries.
- Prepared statements.
- ORM query builders that bind values safely.
- Stored procedures only when they do not build dynamic query strings from untrusted values.

Do not:

- Concatenate user input into query strings.
- Use template strings to build query conditions from request data.
- Pass untrusted values into raw query fragments.
- Trust hidden form fields, client-side filters, or query params as database-safe.

### 5.2 Dynamic Query Construction

If users can sort, filter, select columns, or choose report fields:

- Map user choices to server-defined allowlists.
- Convert `sort=name` into a known column constant, not a raw column string.
- Convert `direction=desc` into a boolean or enum, not raw SQL text.
- Limit filter operators to approved operations.
- Enforce maximum page size and query complexity.
- Apply tenant/user restrictions before user-controlled filters.

### 5.3 ORM Safety

ORMs reduce risk but do not remove it.

Required ORM rules:

- Prefer typed query APIs over raw query APIs.
- Review every raw query manually.
- Do not pass request JSON directly into ORM `where`, `include`, `select`, `update`, or aggregation objects unless schema-validated and allowlisted.
- Use transactions for multi-step state changes.
- Use optimistic locking or database constraints for race-sensitive updates.
- Keep migrations reviewable and reversible.

### 5.4 Least-Privilege Database Accounts

Use separate database roles:

- Read-only role for read replicas and reporting.
- App role with only required table/function permissions.
- Migration role used only by deployment automation.
- Admin role kept outside normal application runtime.

Production applications should not run with unrestricted database owner credentials.

### 5.5 Database Constraints

Use the database as a final integrity layer:

- Primary keys and foreign keys.
- Unique constraints.
- Check constraints for valid ranges/status values.
- Not-null constraints for required fields.
- Cascades only when intentionally reviewed.
- Row-level security where supported and appropriate.

### 5.6 Error Handling

Database errors should:

- Return generic user-facing messages.
- Log structured internal details to protected logs.
- Avoid exposing query text, connection strings, schema internals, table names, or stack traces to users.

---

## 6. Authentication

### 6.1 Password-Based Login

If passwords exist:

- Store passwords only with modern slow hashing algorithms through maintained libraries.
- Use a unique salt per password.
- Add MFA for admin and high-risk users.
- Add rate limits and risk checks to login, signup, password reset, and MFA endpoints.
- Use generic login failure messages.
- Use secure password reset tokens that expire quickly and are single-use.
- Revoke active sessions after password reset where appropriate.

Avoid:

- Plain hashing without password-specific hardening.
- Custom password storage algorithms.
- Passwords in logs, analytics, emails, URLs, or support tickets.

### 6.2 Session Cookies

For browser apps:

- Use `HttpOnly`, `Secure`, and appropriate `SameSite` cookie attributes.
- Rotate session IDs after login and privilege changes.
- Expire inactive and long-lived sessions.
- Store only opaque session identifiers in cookies.
- Keep session state server-side or signed/encrypted with key rotation.

### 6.3 Token-Based Auth

For APIs:

- Validate issuer, audience, expiration, signature, and algorithm.
- Reject unsigned or unexpected algorithms.
- Keep access tokens short-lived.
- Store refresh tokens securely and rotate them.
- Revoke tokens on logout, password reset, account compromise, or role changes when feasible.
- Scope tokens to the minimum required capabilities.

### 6.4 SSO/OAuth/OIDC

When using identity providers:

- Use maintained client libraries.
- Validate redirect URIs strictly.
- Store client secrets server-side only.
- Use state/nonce protections.
- Map external identity claims to internal roles deliberately.
- Do not treat email domain alone as authorization for sensitive actions.

---

## 7. Authorization

### 7.1 Server-Side Checks

Authentication says who the caller is. Authorization says what the caller may do.

Every protected operation must check authorization on the server:

- Read.
- Create.
- Update.
- Delete.
- Export.
- Invite.
- Bill.
- Impersonate.
- Approve.
- Run job.
- Call external provider.
- Trigger AI tool.

Frontend route guards improve UX but are not security controls.

### 7.2 Object-Level Authorization

For every object ID from a request:

- Load the object through a query scoped to the caller's tenant/account/user.
- Return not found or denied consistently.
- Do not load globally and check ownership later unless the check is guaranteed and tested.
- Do not rely on sequential IDs as protection.

### 7.3 Role and Permission Design

Use explicit permissions:

- Prefer named permissions over vague role checks in critical code.
- Keep admin actions separate from normal user actions.
- Require step-up auth for destructive or financial operations.
- Review default roles carefully.
- Make privilege changes auditable.

### 7.4 Multitenancy

For SaaS:

- Include tenant/account scope in every tenant-owned table.
- Enforce tenant scope in shared query helpers.
- Test cross-tenant denied access.
- Isolate background jobs by tenant.
- Scope caches by tenant and user.
- Scope search indexes and analytics exports.

---

## 8. Web Browser Protections

### 8.1 Output Encoding

When rendering user-controlled data:

- Encode for the exact output context: HTML text, HTML attribute, URL, JavaScript, CSS, JSON, or Markdown.
- Prefer framework auto-escaping.
- Avoid raw HTML rendering unless sanitized by a maintained sanitizer.
- Sanitize rich text on input or output with a clearly chosen policy.

### 8.2 Content Security Policy

Use CSP for browser apps:

- Start with a report-only policy if the app is complex.
- Avoid broad script sources.
- Avoid inline scripts where practical.
- Restrict image, frame, connect, and form destinations.
- Monitor violations before enforcing strict production policy.

### 8.3 CSRF Controls

For cookie-authenticated web apps:

- Use framework CSRF protection for state-changing requests.
- Use `SameSite` cookies as an additional layer.
- Require non-simple request headers or tokens for unsafe methods.
- Do not use GET for state changes.

### 8.4 CORS

CORS is not authentication.

Rules:

- Allow only known origins.
- Avoid wildcard origins with credentials.
- Keep allowed methods and headers minimal.
- Validate auth independently of CORS.
- Do not use CORS to protect server-to-server secrets.

### 8.5 Security Headers

Baseline web headers:

- `Strict-Transport-Security` after HTTPS is confirmed.
- `Content-Security-Policy`.
- `X-Content-Type-Options: nosniff`.
- `Referrer-Policy`.
- `Permissions-Policy`.
- `frame-ancestors` through CSP for clickjacking control.

---

## 9. API Security

### 9.1 Contract Validation

Each API endpoint should define:

- Allowed method.
- Auth requirement.
- Request schema.
- Response schema.
- Authorization rule.
- Rate limit.
- Error shape.
- Logging fields.

### 9.2 Rate Limiting and Abuse Controls

Rate-limit:

- Login and signup.
- Password reset and MFA.
- Search and autocomplete.
- File upload.
- Webhook ingestion.
- Expensive reports.
- AI/model calls.
- Email/SMS sending.
- Payment and checkout actions.

Use per-user, per-IP, per-token, per-tenant, or per-endpoint limits depending on the product.

### 9.3 Idempotency

Use idempotency keys for:

- Payments.
- Orders.
- Subscription changes.
- Inventory updates.
- Email/SMS jobs.
- Webhook processing.
- Background tasks that may retry.

### 9.4 Pagination and Query Cost

Protect read endpoints:

- Set maximum page sizes.
- Avoid unbounded exports.
- Limit nested includes.
- Limit GraphQL depth/complexity.
- Cache carefully with tenant/user scope.

---

## 10. File Upload and File Processing

### 10.1 Upload Rules

For uploaded files:

- Authenticate uploaders unless public upload is explicitly required.
- Enforce size limits before processing.
- Validate extension, MIME type, and file signature.
- Rename files server-side.
- Store outside the web root or in private object storage by default.
- Scan where practical.
- Strip risky metadata when appropriate.
- Use short-lived signed URLs for private downloads.

### 10.2 Archive and Document Processing

For ZIP, Office, PDF, image, and media files:

- Limit decompressed size and file count.
- Prevent path traversal during extraction.
- Process in isolated workers when possible.
- Set CPU/memory/time limits.
- Avoid passing untrusted files to privileged system tools.

### 10.3 Export Safety

For CSV/Excel exports:

- Escape cells that spreadsheet software may interpret as formulas.
- Minimize exported fields.
- Mark exports with owner, time, and filter metadata when useful.
- Log sensitive exports.

---

## 11. Secrets and Configuration

### 11.1 Secret Storage

Secrets include:

- API keys.
- Database URLs.
- JWT/session signing keys.
- OAuth client secrets.
- Webhook signing secrets.
- Private certificates.
- Service account files.
- Model provider keys.

Rules:

- Store secrets in a secret manager or protected deployment variables.
- Never ship private secrets in frontend bundles, mobile apps, desktop installers, docs, screenshots, logs, or generated AI context files.
- Rotate secrets after suspected exposure.
- Separate development, staging, and production secrets.
- Use short-lived credentials where available.

### 11.2 Environment Configuration

Production should fail closed:

- Debug mode off.
- Stack traces hidden from users.
- Test credentials rejected.
- HTTPS required.
- Secure cookies required.
- Localhost-only allowances disabled.
- Default admin accounts disabled.

### 11.3 AI Assistant Hygiene

When asking AI tools for help:

- Do not paste production secrets.
- Do not paste private customer data.
- Redact internal hostnames and tokens.
- Provide sanitized schemas and representative examples.
- Keep generated prompt bundles out of public commits unless reviewed and sanitized.

---

## 12. Dependency and Supply-Chain Security

### 12.1 Dependency Intake

Before adding a dependency:

- Confirm it is maintained.
- Check license compatibility.
- Prefer small, focused libraries.
- Avoid packages with broad install scripts unless necessary.
- Avoid abandoned packages for security-sensitive code.
- Document why the dependency is needed.

### 12.2 Lockfiles and Reproducibility

Use:

- Lockfiles for app dependencies.
- Pinned action/plugin versions in CI.
- Reproducible builds where practical.
- Separate production and development dependencies.

### 12.3 Automated Checks

Run available tooling:

- Dependency vulnerability scan.
- Static analysis.
- Secret scanning.
- License checks where required.
- Container image scan for deployed images.

Do not blindly upgrade security-sensitive dependencies without reading breaking changes and running tests.

---

## 13. Infrastructure and Deployment

### 13.1 Network Exposure

Expose only what is needed:

- Public web/API ingress.
- Private databases.
- Private queues and caches.
- Admin interfaces behind SSO/VPN/IP allowlists where appropriate.
- No direct production database access from developer laptops unless explicitly controlled.

### 13.2 Cloud IAM

Use least privilege:

- Separate deploy roles from runtime roles.
- Separate read/write/admin permissions.
- Scope service accounts to specific resources.
- Avoid long-lived broad cloud keys.
- Review wildcard permissions.

### 13.3 TLS and Transport

Require encrypted transport:

- HTTPS for web traffic.
- TLS for database and service connections where supported.
- Secure webhook endpoints.
- HSTS for mature HTTPS web apps.

### 13.4 Backups and Recovery

Backups are a security control.

Required:

- Automated backups for critical data.
- Restore testing.
- Retention policy.
- Encryption at rest where supported.
- Access controls on backups.
- Incident rollback plan.

---

## 14. Logging, Monitoring, and Privacy

### 14.1 What to Log

Log security-relevant events:

- Login success/failure.
- Password reset request and completion.
- MFA changes.
- Role and permission changes.
- Sensitive data export.
- Billing/payment state changes.
- Admin actions.
- Webhook verification failures.
- Rate-limit triggers.
- Authorization denials.
- Secret/configuration changes.

### 14.2 What Not to Log

Avoid logging:

- Passwords.
- Session tokens.
- API keys.
- Full payment details.
- Private model prompts containing sensitive data.
- Full customer records unless required and protected.
- Raw uploaded files.
- Excessive request/response bodies.

### 14.3 Monitoring Alerts

Create alerts for:

- Error spikes.
- Authentication failure spikes.
- Authorization denial spikes.
- Unusual admin activity.
- Cost spikes for AI, SMS, email, search, or cloud services.
- Sudden traffic spikes.
- Queue backlog growth.
- Backup failures.

---

## 15. AI/RAG and Agentic System Security

### 15.1 Model Boundary

Treat model output as untrusted:

- Validate tool-call arguments before execution.
- Require allowlisted tools.
- Keep tools least-privileged.
- Do not let model text become shell commands, database queries, file paths, or policy decisions without validation.
- Separate system/developer instructions from retrieved/user content.

### 15.2 Retrieval Safety

For RAG:

- Filter documents by user and tenant before retrieval.
- Do not retrieve private documents into sessions that lack access.
- Label retrieved content as data, not instructions.
- Log document IDs used in answers when privacy rules allow.
- Avoid embedding secrets, credentials, and private runbooks in public indexes.

### 15.3 Tool and Automation Safety

For AI agents:

- Require approval for destructive actions.
- Scope filesystem, network, cloud, and database permissions.
- Prefer dry-run previews for migrations and bulk changes.
- Prevent hidden instruction text from overriding project safety rules.
- Keep audit logs for automated changes.

---

## 16. Language and Framework Checklists

### 16.1 Node.js / TypeScript

- Validate runtime input with a schema library.
- Use parameterized ORM/query builder APIs.
- Avoid `eval`, dynamic function construction, and shell string execution.
- Store secrets in server-only environment variables.
- Keep frontend `NEXT_PUBLIC`/public env variables non-secret.
- Use secure cookie/session settings.
- Add rate limits to auth and expensive endpoints.

### 16.2 Python

- Validate request payloads with framework/schema tools.
- Use parameterized DB drivers or safe ORM APIs.
- Avoid unsafe deserialization.
- Avoid shell execution with user-controlled strings.
- Use virtual environments and pinned dependencies.
- Keep debug mode disabled in production.
- Sanitize template rendering and file paths.

### 16.3 PHP

- Use PDO or framework query builders with bound parameters.
- Disable verbose errors in production.
- Keep upload directories non-executable.
- Use built-in password hashing APIs.
- Protect session cookies.
- Keep CMS/plugins/themes updated.
- Remove unused admin panels and default files.

### 16.4 Java / Kotlin

- Use prepared statements or safe ORM parameter binding.
- Validate DTOs at controller/service boundaries.
- Avoid unsafe expression/template evaluation.
- Use framework CSRF protection for browser apps.
- Keep dependency scanning in CI.
- Separate service and admin permissions.

### 16.5 .NET

- Use parameterized queries or Entity Framework safely.
- Validate models server-side.
- Configure secure authentication middleware.
- Use anti-forgery tokens for cookie-auth web apps.
- Protect secrets with managed configuration providers.
- Disable detailed errors in production.

### 16.6 Ruby / Rails

- Prefer ActiveRecord query APIs over raw SQL.
- Use strong parameters.
- Keep CSRF protection enabled.
- Avoid unsafe constantization or dynamic dispatch from request params.
- Configure secure cookies and session expiry.
- Keep gems updated and audited.

### 16.7 Go

- Use parameterized database APIs.
- Validate request structs explicitly.
- Avoid building shell commands from request data.
- Use context timeouts for external calls.
- Set secure HTTP server timeouts.
- Keep error messages generic for clients.

### 16.8 Rust

- Use typed query libraries or parameterized DB calls.
- Keep unsafe blocks rare and reviewed.
- Validate deserialized input before business logic.
- Avoid panics for user-controlled errors.
- Use secure secret handling in configuration.
- Audit crates used in security-sensitive code.

---

## 17. Testing Strategy

### 17.1 Security Unit Tests

Add tests for:

- Validation accepts good input and rejects bad input.
- Authorization denies cross-user and cross-tenant access.
- Role changes affect permissions correctly.
- Query builders bind user values safely.
- File uploads reject disallowed types and oversize files.
- Webhook signatures and timestamps are verified.
- Idempotency prevents duplicate state changes.

### 17.2 Integration Tests

Cover:

- Login/logout/session expiry.
- Password reset lifecycle.
- MFA setup and recovery if used.
- Admin-only endpoints.
- Export and import flows.
- Payment/webhook flows.
- Background job retry behavior.
- API pagination and rate limits.

### 17.3 Review Tests Before Shipping

For every sensitive change, ask:

- Did we test the denied path, not only the happy path?
- Did we test a user trying another user's object ID?
- Did we test stale sessions or changed roles?
- Did we test missing, malformed, and oversized input?
- Did we test retries and duplicate events?

---

## 18. Code Review Checklist

Reviewers should look for:

- Raw query fragments.
- Request data passed directly into database filters.
- Missing authorization after authentication.
- Admin checks only in frontend code.
- Sensitive data in logs.
- Secrets in config files, docs, screenshots, tests, or generated prompt bundles.
- Unsafe file path joins.
- Unbounded pagination or exports.
- Missing rate limits on expensive operations.
- Webhook handlers without signature verification.
- Payment amounts, roles, ownership, or tenant IDs trusted from the client.
- Debug mode or verbose errors in production config.
- Broad cloud IAM permissions.
- Dependency additions without justification.

---

## 19. Incident Response Mini-Protocol

If a security issue is suspected:

1. Preserve evidence without exposing secrets publicly.
2. Rotate affected credentials.
3. Disable or limit the affected feature if needed.
4. Identify impacted users, tenants, data, and time window.
5. Patch root cause.
6. Add regression tests.
7. Review logs for abuse indicators.
8. Notify through approved private channels if required.
9. Document the decision and remediation in a private security record.
10. Update public docs only with sanitized, defensive wording.

Do not publish exploit details, customer data, private infrastructure names, or sensitive timelines in public issues, branch names, commits, PR titles, or generated AI context files.

---

## 20. AI Assistant Prompt Template

Use this prompt when asking an AI coding assistant to implement or review security-sensitive code:

```markdown
You are working on a security-sensitive change. Follow the repository security protocol.

Task:
- [Describe the feature/fix]

Security requirements:
- Validate all external input at the boundary.
- Use parameterized database access; do not build query strings from user input.
- Enforce server-side authorization for every object and action.
- Keep secrets server-side and out of generated files.
- Add denied-path tests, not only happy-path tests.
- Do not include exploit payloads, private infrastructure, or sensitive details in comments, branch names, commits, PR titles, or public docs.

Before finishing:
- Summarize changed files.
- List validation commands run.
- Call out any remaining security assumptions.
```

---

## 21. Minimum Baseline Checklist

Every non-trivial project should satisfy:

- [ ] All external input has runtime validation.
- [ ] Database queries use safe binding or safe ORM APIs.
- [ ] Authorization is server-side and tested.
- [ ] Secrets are not in client code, repo files, logs, or generated prompts.
- [ ] Auth/session cookies or tokens are configured securely.
- [ ] CSRF is handled for cookie-authenticated browser state changes.
- [ ] CORS allows only required origins.
- [ ] File uploads are size/type/path controlled.
- [ ] Rate limits protect auth, upload, email, payment, search, and AI endpoints.
- [ ] Dependencies are pinned and scanned.
- [ ] Production debug output is disabled.
- [ ] Logs avoid secrets and sensitive payloads.
- [ ] Backups exist and restore has been tested.
- [ ] Admin actions are audited.
- [ ] Incident response contact/process exists.

---

## 22. Official Reference Baseline

Use these as the primary public references for defensive controls:

- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [OWASP Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html)
- [OWASP Database Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html)
- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- [NIST Secure Software Development Framework SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final)
- [CISA Secure by Design](https://www.cisa.gov/securebydesign)

---

## 23. Final Principle

Security work is successful when safe behavior is the default:

- The easiest database call is parameterized.
- The easiest route includes authorization.
- The easiest config keeps secrets server-side.
- The easiest deployment is private by default.
- The easiest review catches risky changes before production.
- The easiest AI prompt protects the project instead of leaking it.

