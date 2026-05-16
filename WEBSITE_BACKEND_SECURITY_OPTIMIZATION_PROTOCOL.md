# Website Backend Security and Optimization Protocol
## Minimal backend, private API handling, performance gates, and authorized penetration testing for website projects

Version: 1.0
Owner: Project team and AI assistants
Status: Mandatory protocol layer when a website project touches backend logic, APIs, forms, auth, data storage, serverless functions, or deployment security.
Scope: Portfolio sites, landing pages, brochure sites, blogs, dashboards, ecommerce sites, SaaS frontends, admin panels, API-backed websites, serverless websites, and static sites with third-party integrations.

---

## 0. Purpose

This protocol helps AI assistants and developers choose the smallest secure backend that satisfies a website request.

The default rule is:

> Static first. Backend only when needed. Database only when there is real dynamic state. Secrets never ship to the browser.

Many website projects become slower and less secure because they add a database, login system, server, or API proxy before the product needs one. A portfolio site, for example, usually does not need SQL, user accounts, sessions, migrations, or a long-running backend. It may need only static files, a CDN, a contact form relay, analytics with privacy controls, and a deployment checklist.

This protocol keeps that decision flexible. If the user later asks for comments, a CMS, private dashboard, payment flow, membership area, search, admin editing, or integrations, the backend can grow deliberately with security and performance gates.

---

## 1. Website Backend Classification

Before building or changing a website backend, classify the requested website type.

| Website type | Default backend | Default database | Notes |
| --- | --- | --- | --- |
| Portfolio/resume | None or static hosting | None | Use static pages, CDN, optimized media, optional serverless contact form. SQL is not justified unless the user asks for dynamic content management, private submissions, or analytics storage. |
| Landing page/marketing | None or static hosting | None | Forms should use a trusted form service, serverless relay, or CRM integration with rate limits and spam controls. |
| Brochure/company site | Static or headless CMS | Usually none | Use static generation for public pages. Add CMS only when non-developers need content editing. |
| Blog/docs | Static generator or CMS | Usually none | Prefer Markdown, Git-backed content, static CMS, or managed CMS. Database only for dynamic comments, memberships, or editorial workflows. |
| Contact/lead site | Static plus form endpoint | Optional managed storage | Store only required fields. Add CAPTCHA or rate limits. Avoid direct SMTP/API secrets in the browser. |
| Ecommerce | Backend required | Required | Payment, inventory, orders, webhooks, and admin actions require strong auth, idempotency, audit logs, and PCI-aware design. |
| SaaS/dashboard | Backend required | Required | Requires auth, authorization, tenancy boundaries, audit logs, backup/restore, and scale planning. |
| Community/UGC | Backend required | Required | Requires moderation, abuse controls, rate limits, upload safety, and privacy rules. |
| AI-backed website | Backend usually required | Optional | Model/provider keys stay server-side. Add quotas, cost controls, prompt injection defenses, and logging without sensitive content. |
| Internal/admin portal | Backend required | Required or existing | Require least-privilege access, MFA, network restrictions where possible, and audit trails. |

If the classification is uncertain, choose the simpler option and document which user request would justify adding backend or storage.

---

## 2. Backend Necessity Decision Gate

Do not add a backend until at least one of these is true:

- The site must write or read private data.
- The site needs authenticated user accounts.
- The site needs role-based, tenant-based, or object-level authorization.
- The site must call a third-party service with a private credential.
- The site must receive or verify webhooks.
- The site needs dynamic content editing that cannot be solved with static content or a managed CMS.
- The site needs protected admin tools.
- The site needs server-side rendering for private data or protected personalization.
- The site needs file uploads, payment flows, AI calls, email sending, search indexing, background jobs, or scheduled tasks.
- The site has legal, retention, audit, compliance, or reporting requirements.

If none are true, prefer:

- Static HTML/CSS/JS or static-site generation.
- CDN hosting.
- Public assets with cache headers.
- A managed form provider or narrowly scoped serverless form endpoint.
- Static content stored in Markdown, JSON, or a CMS export that contains no secrets.

Stop condition:

- A database, server, authentication system, or admin panel is being added only because it is familiar, not because the user request requires it.

---

## 3. Database Selection Rules

### 3.1 No Database

Use no database when:

- Content is public and changes rarely.
- The user only needs a portfolio, resume, product page, event page, gallery, docs site, or landing page.
- Form submissions can go to email, CRM, a form provider, or a small serverless endpoint.
- Search can be static or client-side over public content.
- Analytics can be privacy-preserving and aggregated by a provider.

Rules:

- Do not add SQL to a portfolio site unless the user explicitly needs dynamic records, private admin editing, search over large mutable data, or stored submissions.
- Do not store personal data just because a form exists. If email delivery is enough, do not keep a copy.
- Do not create an admin login for content that can be updated through Git, Markdown, or a static CMS workflow.

### 3.2 Lightweight Storage

Use lightweight storage when the site needs small, low-risk dynamic state:

- Contact submissions with retention limits.
- Newsletter signups.
- Feature flags.
- Small public content lists.
- Rate-limit counters.
- Short-lived tokens.

Acceptable options can include managed form storage, KV storage, object storage, SQLite for low-traffic admin tools, or a managed backend service. Apply encryption, least privilege, retention, and export/delete rules when personal data exists.

### 3.3 Relational Database

Use PostgreSQL, MySQL, SQL Server, or equivalent when the site needs:

- Accounts and roles.
- Orders, invoices, subscriptions, or payments.
- Tenant isolation.
- Complex relationships and transactions.
- Reporting over mutable data.
- Audit trails.
- Data integrity constraints.

Rules:

- Use migrations and rollback plans.
- Use parameterized queries or a safe query builder/ORM.
- Use least-privilege database users.
- Add indexes for new query paths.
- Define backups and restore tests before production use.

### 3.4 NoSQL/Search/Vector Stores

Use only when the data shape or product requirement fits:

- Document store for flexible documents.
- Search index for full-text search.
- KV/cache for fast key lookup or edge state.
- Vector store for retrieval use cases.

Rules:

- Keep authorization checks outside and inside retrieval paths where needed.
- Avoid unbounded public query surfaces.
- Do not store secrets, raw private prompts, or sensitive user data unless there is a clear retention and access policy.

---

## 4. API and Secret Exposure Model

### 4.1 Visibility Classes

Classify every key, token, endpoint, and variable before use.

| Class | Examples | Browser exposure | Rules |
| --- | --- | --- | --- |
| Public identifier | Analytics measurement ID, map public key, publishable payment key | Allowed if intended | Restrict by domain/origin, quota, and provider settings. Treat as public, not secret. |
| Public API endpoint | `/api/contact`, `/api/products`, public CMS feed | Allowed | Enforce rate limits, input validation, caching, and safe errors. Do not leak internals. |
| Server-only secret | Database URL, service role key, OAuth client secret, payment secret, webhook signing secret, SMTP password, AI provider key | Never | Store in server env/secret manager. Never put in client bundles, static JSON, source maps, logs, or docs. |
| User secret | Session cookie, access token, password reset token, magic link | Never in JS-readable storage unless explicitly designed | Prefer HttpOnly Secure SameSite cookies for browser sessions. Keep tokens short-lived and revocable. |
| Internal endpoint | Admin API, metrics, health details, staging services | Never public without protection | Require auth, network restriction, or deployment-level protection. |

Rules:

- Any value exposed to frontend JavaScript is public by design.
- Frontend env prefixes such as `NEXT_PUBLIC_`, `VITE_`, `PUBLIC_`, and similar must contain only intentionally public values.
- Private API keys must be used through a server route, serverless function, edge function, worker, or trusted backend.
- URLs must not contain secrets, tokens, emails, personal data, or reset credentials.
- Logs, analytics events, crash reports, screenshots, static exports, source maps, and generated HTML must not contain secrets or personal data.

### 4.2 API Proxy Rules

Use a backend proxy only when it adds security or product value:

- It hides a server-only credential.
- It enforces authorization.
- It validates and normalizes requests.
- It rate-limits expensive provider calls.
- It signs or verifies webhooks.
- It applies caching, quotas, or cost controls.
- It removes sensitive provider responses before the browser sees them.

Do not use a proxy only to obscure a public endpoint. Obscurity is not access control.

### 4.3 External Service Integration Rules

For each service, document:

- Service name and purpose.
- Public keys versus server-only keys.
- Required environment variables.
- Allowed domains/origins.
- Rate limits and quotas.
- Webhook signing and replay policy.
- Data sent to the provider.
- Retention and deletion behavior.
- Failure behavior and fallback.

Common rules:

- Payment secret keys stay server-side; publishable keys may be public but must be domain-restricted when supported.
- Email/SMTP/API mail keys stay server-side.
- AI/model provider keys stay server-side; add quotas and abuse controls.
- Map/search/public SDK keys may be public only if provider restrictions are configured.
- Webhook handlers must verify signatures, timestamps, replay windows, and idempotency.

---

## 5. Secure Backend Baseline

Every website backend, including serverless functions, must satisfy this baseline before release:

- HTTPS-only deployment with HSTS when production domain and rollback risk allow it.
- Centralized server-side input validation at every trust boundary.
- Context-aware output encoding.
- Parameterized database queries where a database exists.
- Least-privilege credentials for database, storage, email, payment, CMS, and cloud APIs.
- Structured errors that do not expose stack traces, internal hostnames, paths, SQL, tokens, or provider payloads.
- Security headers appropriate for the site: Content-Security-Policy, X-Content-Type-Options, Referrer-Policy, frame-ancestors or X-Frame-Options, and Permissions-Policy.
- Cookie settings for sessions: HttpOnly, Secure, SameSite, scoped path/domain, rotation on privilege changes.
- CSRF protection for cookie-authenticated state-changing requests.
- CORS allowlist for trusted origins only.
- Rate limits on login, signup, password reset, contact forms, search, uploads, AI calls, exports, and payment actions.
- Request body size limits and content-type validation.
- File upload type, size, storage, scanning, and access controls when uploads exist.
- Dependency vulnerability scanning before release.
- Secret scanning before push, deployment, or package handoff.
- No sensitive data in logs, analytics, source maps, or public bundles.

Stop conditions:

- A browser can access a service role key, database credential, AI key, payment secret, or webhook signing secret.
- Authorization exists only in UI code.
- User input reaches SQL, shell, templates, filesystem paths, URLs, or HTML without validation and safe encoding.
- An admin route is protected only by a hidden path.

---

## 6. Optimization Baseline

Optimization starts by removing unnecessary moving parts.

### 6.1 Architecture Optimization

Rules:

- Prefer static generation and CDN caching for public pages.
- Prefer serverless/edge functions for narrow tasks such as contact forms, webhooks, image metadata, and provider proxies.
- Prefer a managed service only when it reduces security and operational burden.
- Avoid persistent servers for low-traffic static websites unless required by the product.
- Keep backend routes small, auditable, and purpose-specific.
- Avoid creating a generic backend API before concrete routes are known.

### 6.2 API Performance

Required checks:

- Cache public GET responses where safe.
- Use pagination or cursors for collections.
- Set request and response size limits.
- Use timeouts for external services.
- Use retries with bounded backoff only for safe operations.
- Move slow tasks to background jobs.
- Add idempotency keys for payment, email, import, export, webhook, and job actions.
- Add connection pooling for database-backed services.
- Review indexes for new filters and joins.
- Avoid N+1 queries and unbounded joins.

### 6.3 Frontend/Backend Boundary

Rules:

- Do not fetch private data during static build unless the generated output is private or access-controlled.
- Do not ship build-time private data into generated HTML or JSON.
- Server components, server routes, and API handlers must not import client-only code that leaks secrets into bundles.
- Public metadata, sitemap, robots.txt, Open Graph data, and static search indexes must not include internal URLs or private content.

### 6.4 Cost and Abuse Controls

Required when using paid APIs or serverless:

- Per-IP and per-user quotas.
- Spending ceilings or alerting.
- Bot/spam controls for public forms.
- CAPTCHA or challenge only where abuse risk justifies user friction.
- Circuit breakers for expensive providers.
- Log sampling or redaction for high-volume paths.

---

## 7. Flexible User Request Handling

When a user asks for a website feature, map it to the smallest secure backend shape.

| User request | Preferred response |
| --- | --- |
| "Make me a portfolio" | Static site, no SQL, no auth, optimized images, optional protected contact form endpoint. |
| "Add contact form" | Serverless form handler or trusted provider; no frontend email/API secret; rate limit and spam controls. |
| "Let me edit projects in a dashboard" | Add auth, role checks, audit logs, and a database or CMS only for editable records. |
| "Add comments" | Use moderated managed comments or build auth, moderation, abuse controls, storage, and deletion rules. |
| "Add newsletter" | Use provider embed or server-side subscription endpoint; protect provider secret and avoid storing extra PII. |
| "Add payments" | Use provider checkout or backend payment routes; verify webhooks and use idempotency. |
| "Add AI chatbot" | Use server-side AI proxy with quotas, content rules, prompt-injection controls, and no provider key in browser. |
| "Add admin stats" | Keep private analytics behind auth; avoid exposing raw logs or user data. |
| "Make it faster" | Measure first; optimize static output, caching, images, bundle size, APIs, and database queries in that order. |

If the user asks for a shortcut that would expose secrets, weaken auth, disable validation, or bypass testing, propose the nearest safe implementation and record the tradeoff.

---

## 8. Cloud and Edge Security Rules

When a website uses Cloudflare or similar edge security tooling, configure rules according to the actual risk profile.

Recommended controls:

- Managed WAF rules for common web attacks.
- Custom rules for admin paths, sensitive endpoints, and country/IP/org restrictions where appropriate.
- Rate limiting rules for forms, auth, search, AI calls, downloads, and expensive API routes.
- API JWT validation or equivalent for protected APIs where the platform supports it.
- Bot or challenge rules for public forms and abuse-heavy paths.
- DDoS protection and cache rules for public assets.
- Separate preview/staging and production access policies.

Rules:

- Edge rules supplement application security; they do not replace server-side validation or authorization.
- Document every blocking rule with its target path, reason, expected false-positive risk, and rollback path.
- Test edge rules against authenticated and unauthenticated flows before production deployment.

---

## 9. End-of-Work Security and Penetration Test Gate

Before calling a website backend task release-ready, perform authorized security testing on local, staging, or explicitly approved owned systems.

Documentation-only changes can use a documented waiver, but application code changes that touch backend, forms, auth, APIs, storage, payments, uploads, AI calls, or deployment security must pass this gate before public deployment or customer handoff.

### 9.1 Minimum Security Checks

Run or document equivalent checks:

- Secret scan of repository and generated build output.
- Dependency vulnerability scan.
- Static analysis for obvious injection, auth, deserialization, SSRF, filesystem, and logging mistakes.
- Public bundle/static export review for private env values, source maps, debug routes, internal URLs, and personal data.
- Security header check.
- CORS and CSRF review.
- Cookie/session review.
- Rate-limit review for abuse-prone routes.
- Authorization tests for protected routes and object access.
- Error handling review for internal data leakage.

### 9.2 Minimum Penetration Test Classes

For the changed scope, test:

- Authentication bypass.
- Authorization bypass and direct object access.
- Cross-tenant access where tenancy exists.
- Input injection into SQL, NoSQL, templates, commands, HTML, URLs, and file paths.
- XSS, CSRF, clickjacking, and unsafe CORS.
- SSRF for any URL-fetching feature.
- File upload bypass, content-type mismatch, large files, and unsafe downloads.
- Password reset, magic link, invitation, and email verification abuse.
- Webhook spoofing and replay.
- Rate-limit bypass, account enumeration, spam, and cost abuse.
- Sensitive data exposure in logs, errors, analytics, source maps, public files, and storage buckets.

### 9.3 Fix and Retest Rule

Release is blocked until:

- Critical and high findings are fixed and retested.
- Medium findings are fixed or explicitly accepted by the owner with a date.
- Low findings are tracked.
- Secret exposure findings are remediated, affected credentials are rotated, and history/artifacts are reviewed.
- The final report states exactly which tests ran and what remains risky.

### 9.4 Evidence Template

```text
Website Backend Security Report
Project:
Date:
Website type:
Backend classification:
Database decision:
Secret handling decision:
Environment tested:
Authorization scope:

Commands/tools:
- Secret scan:
- Dependency scan:
- Static analysis:
- Build/public bundle review:
- DAST/manual tests:
- Performance checks:

Findings:
1. ID:
   Severity:
   Surface:
   Reproduction:
   Fix:
   Retest:
   Status:

Release decision:
- Local review / QA-ready / Release-candidate / Production-ready / Not ready
- Waivers:
- Residual risks:
```

---

## 10. Implementation Prompts for AI Assistants

Use these prompt fragments inside website projects.

### 10.1 Minimal Backend Intake

```text
Classify this website before coding:
- Website type:
- Does it need backend? Why?
- Does it need database? Why?
- Which secrets exist?
- Which values are intentionally public?
- Which user data is collected?
- Which routes are protected?
- What security and performance gates apply?
Choose the smallest secure architecture that satisfies the request.
```

### 10.2 Portfolio Site Rule

```text
This is a portfolio site unless the user states otherwise.
Default: no SQL, no auth, no server-side session, no admin backend.
Use static generation/CDN and optimized assets.
If a contact form is required, use a serverless handler or trusted provider.
Keep mail/API secrets server-side and add spam/rate controls.
```

### 10.3 API Secret Review

```text
Review every env var, API key, endpoint, token, and config value.
Label each as public identifier, public endpoint, server-only secret, user secret, or internal endpoint.
Fail the task if a server-only secret reaches frontend code, static output, logs, source maps, generated docs, or public examples.
```

### 10.4 End-of-Work Gate

```text
Before final delivery, run functional tests, build, secret scan, dependency scan, public bundle review, and authorized penetration tests for changed backend/API/form/auth/storage surfaces.
Fix all confirmed critical/high findings and retest before marking release-ready.
```

---

## 11. References

This protocol is informed by defensive web security guidance from:

- MDN Web Docs, Security on the web: https://developer.mozilla.org/en-US/docs/Web/Security
- Cloudflare Security rules documentation: https://developers.cloudflare.com/security/rules/
- HKUST Information Technology Services Office, Secure Web Application Development Guideline: https://itso.hkust.edu.hk/sites/default/files/site-images/cyber-security/Secure%20Web%20Application%20Development%20Guideline.pdf
- Web Developer Security Checklist: https://github.com/virajkulkarni14/WebDeveloperSecurityChecklist
- OWASP Application Security Verification Standard: https://owasp.org/www-project-application-security-verification-standard/
- OWASP Web Security Testing Guide: https://owasp.org/www-project-web-security-testing-guide/

