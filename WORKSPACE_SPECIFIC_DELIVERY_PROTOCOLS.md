# Workspace-Specific Delivery Protocols (WSDP)
## Mandatory work methods, security gates, AI evaluation gates, and scalability gates for AI-assisted software delivery

Version: 1.0
Owner: Project team and AI assistants
Status: Mandatory protocol layer for APCP/MACP projects
Scope: Game engines, web applications, backend/API systems, mobile/desktop apps, AI/LLM systems, data products, DevOps/infrastructure, and mixed projects.

---

## 0. Prime Directive

No AI assistant, developer, agent, automation, or model may mark work as "done", push it to GitHub, package it for a customer, deploy it, or hand it off as production-ready until the applicable workspace-specific protocol gates have been executed or explicitly waived by the human owner.

If a gate cannot be executed, the AI must say so before delivery and must provide:

- The skipped gate name.
- The exact reason it could not be run.
- The risk created by skipping it.
- The safest next action.
- Whether the artifact is safe only for local review, staging, internal QA, or production.

Passing functional tests is not enough. A delivery candidate must also pass security, secret-exposure, privacy, AI behavior, scalability, packaging, and user-notification checks appropriate to its workspace.

---

## 1. Universal Work Intake Protocol

Every AI-assisted work session starts by classifying the workspace. A project may match more than one category; when it does, all relevant protocols apply.

### 1.1 Workspace Classification

The AI must identify and write down the active workspace type before making meaningful changes:

| Workspace | Examples | Mandatory protocol sections |
| --- | --- | --- |
| Game engine | Unity, Unreal, Godot, custom engine | Section 3, Section 8, Section 10 |
| Web frontend | React, Next.js, Vue, Svelte, static site | Section 4, Section 7, Section 8, Section 10 |
| Backend/API | Node, Python, Go, .NET, Java, GraphQL, REST | Section 5, Section 7, Section 8, Section 10 |
| Full-stack SaaS | Web UI + API + DB + auth + billing | Section 4, Section 5, Section 7, Section 8, Section 10 |
| AI/LLM/RAG/agent | Chatbot, copilot, model router, agent, vector search | Section 6, Section 7, Section 8, Section 9, Section 10 |
| Mobile/desktop | Android, iOS, Flutter, React Native, Electron, Tauri | Section 11, Section 7, Section 8, Section 10 |
| Data/ML | ETL, analytics, training pipeline, dashboards | Section 12, Section 7, Section 8, Section 10 |
| Infrastructure/DevOps | CI/CD, Docker, Kubernetes, Terraform, cloud | Section 13, Section 7, Section 8, Section 10 |

### 1.2 Required Initial Snapshot

Before implementing, the AI must gather enough project context to avoid blind edits:

- Repository status: branch, dirty files, ignored generated files, untracked secrets risk.
- Runtime stack: language, framework, engine version, package manager, lockfiles, build system.
- Entry points: app start command, test command, build command, deploy/package command.
- Architecture map: major modules, data flow, state boundaries, external services.
- Security map: authentication, authorization, secrets, user data, admin paths, payment paths, file upload paths, network calls.
- Public exposure map: what ships to browsers, app stores, game clients, CDN buckets, public GitHub, logs, analytics, downloadable packages.
- Scale target: expected users, peak concurrency, request rate, data volume, latency targets, availability expectations.
- AI surface map when relevant: prompts, tools, retrieval sources, memory, model providers, model fallbacks, agent permissions.

### 1.3 Definition of Done Levels

The AI must label completion with one of these levels:

| Level | Meaning | Allowed handoff |
| --- | --- | --- |
| Local-only | Runs on developer machine; not hardened | Demo to owner only |
| QA-ready | Functional tests pass; known risks listed | Internal QA/staging |
| Release-candidate | Functional, security, AI, and scale gates pass for agreed scope | Customer acceptance testing |
| Production-ready | Release-candidate plus deployment, observability, rollback, privacy, compliance, and incident playbooks complete | Production or public release |

An AI must not call something production-ready merely because the feature works.

---

## 2. Universal Delivery Gate Sequence

All projects use this gate order. Workspace-specific sections add extra requirements.

### Gate 0: Scope and Safety Confirmation

Required checks:

- Confirm the requested change and the files/modules likely affected.
- Identify whether the work touches auth, payments, secrets, user data, infrastructure, AI tools, model prompts, or public/client-side code.
- Identify legal/authorization limits for security testing. Penetration testing must only be performed on systems owned by the project or explicitly authorized in writing.
- Confirm whether the delivery target is local review, GitHub branch, staging, production, app store, game build, or customer package.

Stop conditions:

- The work requires credentials the AI does not have.
- The user asks to attack a third-party system without authorization.
- The AI detects secrets in files that would be committed or packaged.
- The requested action would expose private code, private assets, user data, keys, certificates, or internal prompts.

### Gate 1: Implementation Hygiene

Required checks:

- Follow the existing architecture and style.
- Keep changes scoped to the request.
- Update tests with the change when behavior changes.
- Update docs, examples, migrations, env templates, and configuration samples when contracts change.
- Avoid introducing new dependencies unless they are justified, maintained, licensed appropriately, and security-reviewed.
- Ensure generated files, build artifacts, local editor files, private logs, and credentials stay out of commits.

### Gate 2: Functional Verification

Required checks:

- Unit tests for changed logic.
- Integration tests for cross-module behavior.
- End-to-end tests for user-facing workflows.
- Regression tests for previously broken behavior.
- Build/package test for release candidates.
- Manual smoke test for the main user journey.

Evidence required:

- Commands executed.
- Pass/fail summary.
- New or changed test files.
- Known gaps.

### Gate 3: Security and Secret Exposure Verification

Required checks:

- Secret scan for repository and package artifacts.
- Static analysis for common vulnerability patterns.
- Dependency vulnerability scan.
- Authentication and authorization review.
- Input validation review.
- Output encoding and injection review.
- File upload, deserialization, SSRF, command execution, path traversal, and template injection review when applicable.
- Secure headers, cookies, CORS, CSRF, rate limits, and session handling when web-facing.
- Logging review to ensure secrets and personal data are not logged.
- Public build review to ensure no private env vars, source maps, debug endpoints, admin panels, model system prompts, internal URLs, private assets, or credentials are exposed.

Minimum recommended tooling, adapted to stack:

- Secrets: gitleaks, trufflehog, GitHub secret scanning and push protection.
- Dependencies: npm audit, pnpm audit, yarn npm audit, pip-audit, safety, cargo audit, govulncheck, osv-scanner, Dependabot.
- SAST: CodeQL, Semgrep, Bandit, ESLint security plugins, Roslyn analyzers, gosec.
- Containers/IaC: Trivy, Grype, Checkov, tfsec, kube-score, kube-linter.
- DAST: OWASP ZAP, Burp Suite, stack-specific scanners, authenticated route probes.

Stop conditions:

- Any committed or packaged secret.
- Any critical/high vulnerability with an exploitable path.
- Any broken authorization boundary.
- Any customer/user data exposure.
- Any AI tool path that can execute sensitive actions without policy checks.

### Gate 4: Penetration Test Gate

Penetration testing is mandatory before public deployment, customer package delivery, production release, or GitHub push/release of application code. Documentation-only or explicitly WIP/internal branches may use a documented waiver, but the artifact must not be labeled release-ready.

Required scope:

- Only owned/local/staging systems or explicitly authorized targets.
- Include authenticated and unauthenticated views.
- Include normal user, admin, tenant boundary, and abuse-case roles.
- Include API endpoints, web UI, file uploads, background jobs, webhooks, admin tools, CI/CD, and package artifacts.

Minimum manual test classes:

- Authentication bypass.
- Authorization bypass and insecure direct object references.
- Cross-tenant data access.
- SQL/NoSQL/LDAP/template/command injection.
- XSS, CSRF, clickjacking, CORS abuse.
- SSRF and internal network access.
- File upload and malware/polyglot payload handling.
- Path traversal and unsafe archive extraction.
- Business logic abuse.
- Payment, subscription, refund, coupon, and quota abuse.
- Rate limit bypass and account enumeration.
- Password reset, email verification, invitation, and magic-link abuse.
- Webhook spoofing and replay.
- Sensitive data in logs, errors, analytics, crash reports, source maps, public bundles, and storage buckets.

Required output:

- Findings grouped by severity.
- Reproduction steps for each confirmed issue.
- Fix applied or explicit owner waiver.
- Retest result after fixes.

### Gate 5: AI/Model Behavior Gate

Mandatory for any feature that uses AI, LLMs, RAG, agents, classifiers, recommendation systems, moderation, transcription, OCR, embeddings, or model routing.

Required checks:

- Hallucination and factuality tests.
- Prompt injection tests.
- System prompt leakage tests.
- Tool misuse tests.
- Retrieval poisoning tests.
- Sensitive data exfiltration tests.
- Refusal and safety behavior tests.
- Multi-turn memory corruption tests.
- Model fallback consistency tests.
- Cross-model comparison if more than one model is available.

No AI system is release-ready until this gate is documented.

### Gate 6: Scalability and Reliability Gate

Every application must be evaluated as if it may need to serve far more than the first one or two users. For production-oriented software, the default mental model is: "Could this survive a path toward 100,000+ concurrent or active users if the business suddenly succeeds?"

Required checks:

- Workload model: active users, concurrent users, requests per second, jobs per minute, storage growth, model calls, token consumption, bandwidth, and file sizes.
- Performance baseline: p50, p95, p99 latency, throughput, memory, CPU, database query time, queue depth, error rate.
- Bottleneck map: database, cache, network, model provider rate limits, file storage, third-party APIs, single-threaded workers, locks, hot partitions.
- Load test: normal expected traffic.
- Stress test: beyond expected traffic until bottleneck is visible.
- Spike test: sudden traffic burst.
- Soak test: long-running stability, memory leaks, queue buildup, rate-limit behavior.
- Failure test: dependency outage, slow database, unavailable model provider, expired token, invalid cache, rollback path.
- Cost test: approximate cost under normal, peak, and abuse conditions.

Stop conditions:

- No backpressure or rate limits on expensive paths.
- No timeout/retry/circuit-breaker strategy for external services.
- Database queries that obviously degrade with user growth.
- Single server/process/stateful memory dependency where horizontal scaling is expected.
- No observability on a critical path.
- No graceful degradation for AI/model/provider failure.

### Gate 7: Packaging and Release Candidate Gate

Required checks:

- Build from a clean checkout.
- Install dependencies from lockfiles.
- Run tests in the same mode used by CI or release packaging.
- Verify generated artifact contents.
- Verify no secret files, local configs, debug symbols, private assets, dev-only endpoints, test data, crash dumps, prompt files, or logs are included.
- Generate release notes and known-risk list.
- Generate rollback instructions for deployable services.
- Generate install/run instructions for customer packages.
- Include license notices and third-party attributions.
- Include version, commit SHA, build timestamp, and checksum for binaries/packages.

### Gate 8: User Notification Before GitHub Push or Customer Handoff

Before pushing to GitHub, publishing, packaging, sending to a customer, or calling work finished, the AI must tell the user:

```text
Delivery gate required before release:
- Workspace type:
- Target: GitHub push / customer package / staging deploy / production deploy
- Functional tests to run:
- Security and penetration tests to run:
- AI/model tests to run:
- Scalability tests to run:
- Packaging checks to run:
- Expected time/cost:
- Risks if skipped:
Proceeding only after these checks pass or are explicitly waived.
```

If the user waives a gate, the AI must record the waiver in the final report and must not label the artifact as production-ready unless the waiver is acceptable for the release level.

---

## 3. Unity and Game Engine Protocol

Use this protocol for Unity, Unreal, Godot, custom engines, and any interactive game/simulation project. The Unity-specific checklist is mandatory when Unity is detected.

### 3.1 Game Project Intake

The AI must identify:

- Engine and exact version.
- Render pipeline: Built-in, URP, HDRP, custom.
- Target platforms: Windows, macOS, Linux, WebGL, Android, iOS, console, VR/AR.
- Package manager dependencies.
- Input system: legacy input, new Input System, custom.
- Networking model: offline, local multiplayer, peer-to-peer, server authoritative, relay, dedicated server.
- Save system: local files, cloud save, encrypted save, player prefs, database.
- Asset pipeline: Resources, Addressables, AssetBundles, StreamingAssets, remote CDN.
- Scene list and build index.
- Critical prefabs and ScriptableObjects.
- Project Settings that affect runtime behavior.
- CI/build automation path.
- Monetization, ads, analytics, login, cloud services, or payment SDKs.

### 3.2 Scene Structure Protocol

The AI must inspect or document:

- All scenes in the build.
- Scene purpose: boot, menu, gameplay, loading, test, debug, additive scene, addressable scene.
- Root GameObjects and persistent managers.
- Objects using DontDestroyOnLoad.
- Scene references to prefabs, materials, shaders, audio, timelines, animations, cameras, lights, canvases, event systems, and post-processing volumes.
- Singletons and global state.
- Objects with Update, FixedUpdate, LateUpdate, OnGUI, coroutines, async tasks, event subscriptions, and physics callbacks.
- Serialized field references that may break after prefab rename, asset move, or addressable change.
- Layer, tag, sorting layer, physics matrix, and collision dependencies.
- UI canvases, safe area handling, scaling mode, localization, and controller/keyboard/touch navigation.

Rules:

- Do not change a scene blindly. If scene serialization is touched, explain why.
- Do not move scene-critical managers without checking execution order and references.
- Prefer prefab variants and ScriptableObjects over duplicating scene-only configuration.
- Keep debug/test scenes out of release build settings unless intentionally included.
- Avoid hard-coded object lookup chains when serialized references, dependency injection, event channels, or registries are safer.

### 3.3 Unity Script Protocol

Required checks for scripts:

- MonoBehaviour lifecycle dependencies: Awake, OnEnable, Start, Update, FixedUpdate, LateUpdate, OnDisable, OnDestroy.
- Script execution order dependencies. If order matters, document it and prefer explicit initialization flow where possible.
- Serialized fields: required references, null handling, tooltip/range validation, prefab override behavior.
- Runtime allocations: per-frame LINQ, string concatenation, boxing, closures, GetComponent loops, Instantiate/Destroy loops.
- Event subscriptions: every subscription must have a matching unsubscribe path.
- Coroutines and async tasks: cancellation on scene unload/destroy.
- Physics code: FixedUpdate for physics mutation, Update for input capture, interpolation settings.
- Save/load code: versioning, migration, corruption handling, tamper assumptions.
- Multiplayer code: client authority, server validation, replay protection, rate limits, desync handling.
- Mobile code: pause/resume, backgrounding, low-memory events, permissions.
- WebGL code: threading/filesystem/network limitations.

Rules:

- Do not rely on an AI guess about Unity event ordering. Check the engine version and project settings.
- Use object pooling for frequent spawn/despawn paths.
- Avoid Resources for large or sensitive runtime content; prefer Addressables or explicit bundles where appropriate.
- Never place secrets, backend admin endpoints, signing keys, API keys, service account files, or payment secrets in client builds.
- Treat every game client as hostile. Competitive, economy, inventory, rank, payment, and anti-cheat decisions must be server-authoritative.

### 3.4 Unity Project Settings Protocol

Review when gameplay, performance, builds, input, networking, or platform behavior changes:

- Player Settings: company/product name, bundle ID, versioning, scripting backend, API compatibility, stripping, managed code stripping, architecture.
- Quality Settings: target frame rate, v-sync, shadows, texture quality, LOD, anti-aliasing.
- Graphics Settings: render pipeline asset, shader variants, always-included shaders.
- Physics and Physics2D: layer collision matrix, solver iterations, gravity, queries hit triggers.
- Time: fixed timestep, maximum allowed timestep, time scale assumptions.
- Tags and Layers: dependency validation.
- Input System settings and generated actions.
- Addressables groups, profiles, catalogs, remote/local build path, content update strategy.
- Build Settings: scene order, target platform, compression, development build flag.
- Package versions and lockfiles.

### 3.5 Unity Functional and Regression Tests

Required tests:

- EditMode tests for pure logic.
- PlayMode tests for scene/prefab behavior.
- Build smoke test for each target platform.
- Scene load/unload test.
- Save/load migration test.
- Input path test for supported devices.
- UI navigation and resolution test.
- Localization and font fallback test when localized.
- Multiplayer connection and authority tests when networked.
- Addressables content build test when addressables are used.

Recommended commands:

```bash
Unity -batchmode -quit -projectPath . -runTests -testPlatform EditMode -testResults TestResults/EditMode.xml
Unity -batchmode -quit -projectPath . -runTests -testPlatform PlayMode -testResults TestResults/PlayMode.xml
Unity -batchmode -quit -projectPath . -executeMethod BuildScript.PerformBuild
```

### 3.6 Unity Performance and Scale Gate

Performance budgets must be defined per target:

- Target FPS and frame time: 60 FPS = 16.67 ms, 30 FPS = 33.33 ms.
- CPU main thread budget.
- Render thread/GPU budget.
- Memory ceiling.
- GC allocations per frame.
- Scene load time.
- Asset download size.
- Save/load time.
- Network tick rate, bandwidth, packet loss tolerance.

Required profiling:

- Unity Profiler capture for core gameplay.
- Memory profiler capture for scene transition and long session.
- Frame debugger/render analysis for expensive draw paths.
- Asset size report.
- Build size report.
- Soak test for long session stability.
- Stress test for maximum AI agents/NPCs/projectiles/entities.

Stop conditions:

- Per-frame allocations on hot gameplay paths without justification.
- Unbounded object spawning.
- Scene load spikes that break target UX.
- Asset bundles/addressables not built or not validated for release.
- Debug/development build accidentally packaged.
- Client-side economy/authority decisions in online games.

### 3.7 Unity Release Gate

Before GitHub push, build packaging, or customer handoff:

- All target scenes are included and ordered correctly.
- Debug scenes, test objects, debug UI, cheats, and dev menus are removed or gated.
- Release build is not a Development Build unless explicitly intended.
- Platform permissions are minimal.
- Crash reporting and analytics do not expose personal data.
- Save files and local caches do not store secrets.
- Addressables/bundles are built for the correct platform/profile.
- Builds are smoke-tested on actual target devices or documented as not tested.
- Version, changelog, known issues, and rollback/rebuild instructions are included.

---

## 4. Web Frontend and Website Protocol

Use this protocol for websites, dashboards, SaaS frontends, landing pages with forms, admin panels, browser tools, static sites, and browser-delivered applications.

### 4.1 Web Stack Intake

The AI must identify:

- Framework: React, Next.js, Vue, Nuxt, SvelteKit, Angular, Astro, vanilla, etc.
- Rendering mode: static, CSR, SSR, ISR, edge rendering, hybrid.
- Runtime: Node, Bun, Deno, serverless, edge workers.
- Package manager and lockfile.
- Routing model and protected route mechanism.
- API/data source.
- Auth/session provider.
- Styling system.
- Build output directory and hosting platform.
- Environment variable exposure model.
- Analytics, ads, chat widgets, payment scripts, maps, and third-party embeds.

### 4.2 Tech Stack Rules

Rules:

- Do not change framework, package manager, router, state manager, styling system, or auth library unless the task requires it.
- Use the existing component patterns and design system.
- Keep public runtime configuration separate from private server-only configuration.
- Never place private environment variables in frontend-exposed names such as NEXT_PUBLIC_*, VITE_*, PUBLIC_*, EXPO_PUBLIC_*, or equivalent unless the value is intentionally public.
- Use typed API contracts when available.
- Keep server-only code out of client bundles.
- Avoid adding client-side dependencies that expose large attack surface or unnecessary tracking.
- Do not disable linting, type checks, hydration checks, CSP, or security middleware to make a build pass.

### 4.3 Public Exposure Protection

The AI must verify that public builds do not expose:

- API keys that grant privileged access.
- Service role keys.
- Database URLs.
- JWT secrets.
- Webhook signing secrets.
- OAuth client secrets.
- Private S3/bucket paths.
- Admin endpoints.
- Internal IPs or hostnames.
- Source maps in production unless access-controlled.
- Debug flags.
- Test accounts.
- Error stack traces.
- Private prompt templates or model instructions.
- Hidden routes that rely only on obscurity.
- Customer data in static JSON, generated HTML, logs, screenshots, or analytics payloads.

Required checks:

- Inspect built assets for sensitive strings.
- Confirm .env files are ignored.
- Confirm .env.example contains placeholders only.
- Confirm client-visible env variables are intentionally public.
- Confirm robots.txt, sitemap, Open Graph images, and metadata do not leak private URLs.
- Confirm storage buckets and CDN paths are not listable unless intentionally public.

### 4.4 Web Functional Testing

Required tests:

- Unit tests for changed components and utilities.
- Integration tests for data fetching and forms.
- E2E tests for primary flows.
- Responsive layout check: mobile, tablet, desktop, wide desktop.
- Accessibility check: keyboard navigation, focus states, labels, contrast, ARIA only when needed.
- Browser compatibility check for supported browsers.
- Form validation and error state tests.
- Authenticated and unauthenticated route tests.
- Empty, loading, success, error, and permission-denied states.
- Build test from clean install.

Recommended tools:

- Playwright or Cypress for E2E.
- Testing Library for components.
- axe-core or equivalent for accessibility.
- Lighthouse for performance and common web hygiene.

### 4.5 Web Security Protocol

Required checks:

- Authentication: secure session creation, refresh, logout, password reset, MFA when applicable.
- Authorization: route-level and object-level checks on the server, not only UI hiding.
- CSRF protection for cookie-authenticated state-changing requests.
- XSS prevention: contextual output encoding, no unsafe HTML injection without sanitization.
- SQL/NoSQL injection prevention: parameterized queries and schema validation.
- SSRF prevention for URL fetchers, webhook testers, image importers, PDF generators, and metadata scrapers.
- File upload safety: type sniffing, size limits, malware scanning when needed, storage isolation, signed URLs.
- CORS: least-privilege origins and methods.
- Cookies: HttpOnly, Secure, SameSite, path/domain scoping.
- Security headers: CSP, HSTS, X-Content-Type-Options, Referrer-Policy, frame-ancestors or X-Frame-Options.
- Rate limits and abuse controls on login, signup, password reset, search, AI calls, export, and payment paths.
- Webhook verification and replay protection.
- Error handling: no stack traces or sensitive data in production.
- Audit logs for admin/security-sensitive actions.

### 4.6 Web Performance and Scale Gate

Required checks:

- Bundle size budgets.
- Image/video optimization.
- CDN caching strategy.
- API caching and invalidation.
- Database query and index review for pages/API routes.
- Server-side rendering latency budget.
- Serverless cold start review.
- Connection pooling.
- Rate limits for expensive routes.
- Background job offloading for slow work.
- Pagination, streaming, or cursoring for large lists.
- Load test for top routes and APIs.

Stop conditions:

- Unbounded list rendering or unpaginated API queries.
- N+1 database queries on hot paths.
- Expensive AI/model calls triggered automatically per page view without caching or limits.
- User-controlled URLs fetched server-side without SSRF defenses.
- Public forms without spam/rate controls.

### 4.7 Web Release Gate

Before GitHub push, deployment, or customer delivery:

- Production build passes.
- All tests for changed surfaces pass.
- Public bundle secret scan passes.
- DAST or manual web pen test completed for release candidates.
- Error pages, 404, 500, auth failure, permission failure states verified.
- Analytics/monitoring configured without leaking personal data.
- Rollback path documented.
- Environment variable list reviewed.
- Source maps policy documented.

---

## 5. Backend, API, and SaaS Core Protocol

Use this protocol for APIs, workers, services, databases, queues, cron jobs, webhooks, SaaS backends, and internal platforms.

### 5.1 Backend Intake

The AI must identify:

- Language/runtime and framework.
- API style: REST, GraphQL, gRPC, WebSocket, event-driven.
- Database type and migration tool.
- Cache layer.
- Queue/job system.
- Auth/session/token strategy.
- Authorization model: RBAC, ABAC, tenant isolation, ownership checks.
- External services.
- Deployment topology.
- Observability stack.
- Data retention and backup policy.
- Rate limits and quotas.

### 5.2 API Contract Protocol

Rules:

- Any API behavior change must update OpenAPI/GraphQL/protobuf/contracts and client expectations.
- All inputs must be validated at trust boundaries.
- All state-changing operations must enforce authz on the server.
- All idempotent operations must be safe to retry.
- Payment, email, webhook, job, import/export, and AI actions must be idempotent or have duplicate protection.
- Errors must be structured and must not leak internals.
- Pagination must be used for large collections.
- Timeouts must exist for external calls.
- Retries must use backoff and must not multiply load catastrophically.
- Long-running work must move to jobs/queues where appropriate.

### 5.3 Database Protocol

Required checks:

- Schema migration and rollback path.
- Indexes for new query patterns.
- Transaction boundaries.
- Tenant isolation.
- PII fields and encryption requirements.
- Soft delete/data retention behavior.
- Backup/restore impact.
- Connection pool sizing.
- Lock/contention risk.
- Migration safety under production data volume.

Stop conditions:

- Destructive migration without backup/rollback.
- Authorization dependent only on client-provided filters.
- Unbounded queries on user-controlled filters.
- Secrets or tokens stored in plaintext.
- Missing audit path for security-sensitive changes.

### 5.4 Backend Security Protocol

Required checks:

- Auth bypass attempts.
- Authorization matrix tests.
- Tenant boundary tests.
- Input validation and injection tests.
- SSRF tests for URL-capable features.
- Deserialization and parser abuse tests.
- File import/export safety.
- Webhook signature tests.
- Rate-limit and brute-force tests.
- Replay protection where applicable.
- Secrets in logs and traces.
- Admin-only operation protection.
- Dependency and container vulnerability scan.

### 5.5 Backend Scale Protocol

Required checks:

- Horizontal scaling assumptions.
- Statelessness or explicit state management.
- Queue throughput and dead-letter handling.
- Cache invalidation and stampede protection.
- Database connection pool under peak.
- Hot key/hot partition review.
- Read/write splitting or replicas when relevant.
- Backpressure for workers.
- Bulkhead isolation for expensive dependencies.
- Circuit breakers for third-party outages.
- Load, stress, spike, and soak tests.

Example scale evidence:

```text
Endpoint: POST /api/search
Expected peak: 2,000 RPS
Observed p95: 180 ms at 2,000 RPS
Error rate: 0.03%
Bottleneck: database CPU at 72%
Mitigation: covering index added, result cache 60s, rate limit 30/min/user
Status: pass for current release target
```

---

## 6. AI, LLM, RAG, and Agent Protocol

Use this protocol for any system that calls AI models, routes among models, stores prompts, retrieves context, generates code/content, uses tools, acts as an agent, or makes decisions based on model output.

### 6.1 AI System Intake

The AI must produce an inventory:

- Model providers and model names.
- Model purposes.
- System prompts and developer prompts.
- User input sources.
- Retrieval sources and vector stores.
- Tool/function list.
- Permissions for each tool.
- External data sources.
- Memory/session storage.
- Logging and telemetry.
- Human approval points.
- Fallback models and routing rules.
- Safety filters and output validators.
- Data retention and training/usage policy.

### 6.2 AI Threat Model

Required threats to consider:

- Direct prompt injection.
- Indirect prompt injection from websites, documents, emails, tickets, files, images, code comments, metadata, and retrieved chunks.
- Multimodal prompt injection.
- System prompt leakage.
- Tool abuse and excessive agency.
- Sensitive data exfiltration.
- Retrieval poisoning.
- Vector store cross-tenant leakage.
- Model denial of service through long/expensive prompts.
- Hallucinated citations, commands, files, laws, APIs, or customer facts.
- Unsafe code generation.
- Model fallback changing safety behavior.
- Memory poisoning across sessions.
- Insecure output consumed by downstream code.
- Data being sent to providers in violation of policy.

### 6.3 Hallucination and Factuality Tests

Required evaluation set:

- Golden questions with known correct answers.
- Domain-specific edge cases.
- Questions with insufficient information where the correct behavior is to abstain or ask for clarification.
- Citation-required questions.
- Adversarial misleading questions.
- Multi-turn context retention questions.
- Formatting/structured-output tasks.
- Tool-use tasks where the answer must be grounded in tool results.

Metrics:

- Exact correctness where possible.
- Factual consistency.
- Citation support rate.
- Unsupported claim rate.
- Abstention correctness.
- Refusal correctness.
- JSON/schema validity.
- Tool-call correctness.
- Regression against previous model/prompt versions.

Release thresholds must be explicit. Example:

```text
Hallucination gate:
- Critical factual tasks: 98%+ correct or abstain
- Citations: 100% of factual claims in answer must map to retrieved/source content
- Structured output: 99% valid schema
- Unsafe unsupported command suggestions: 0 tolerated
- Known high-risk questions: 0 severe failures
```

### 6.4 Prompt Injection Test Protocol

Required attack classes:

- Direct instruction override: "ignore previous instructions".
- Role/system prompt extraction.
- Policy bypass and jailbreak attempts.
- Tool hijacking: instructions to call tools outside scope.
- Data exfiltration: ask for secrets, tokens, hidden prompts, private documents.
- Indirect injection in retrieved documents.
- Indirect injection in web pages.
- Indirect injection in code comments.
- Indirect injection in email/ticket/chat content.
- Multimodal injection hidden in images or OCR text when applicable.
- Multi-turn gradual manipulation.
- Conflicting instruction hierarchy tests.
- Output injection: model returns content later executed by scripts, shells, SQL, HTML, markdown renderers, or workflow engines.

Mitigation rules:

- Do not rely only on prompt wording as a security boundary.
- Treat model input as untrusted.
- Treat retrieved content as untrusted data, not instructions.
- Enforce permissions in application code.
- Use least-privilege tool tokens.
- Use allowlists for tools, domains, commands, file paths, and data scopes.
- Require human confirmation for consequential actions: purchases, deletes, sends, pushes, deploys, account changes, permission changes, external messages.
- Validate and sanitize model output before downstream use.
- Separate trusted instructions, untrusted content, and tool results in structured messages where the framework supports it.
- Log security-relevant model/tool decisions.
- Block or quarantine suspicious retrieved content.
- Use content provenance and source attribution.

### 6.5 RAG and Vector Store Protocol

Required checks:

- Document ingestion authorization.
- Source provenance.
- Chunk boundaries and metadata.
- Tenant/user isolation.
- Embedding model versioning.
- Poisoned content detection.
- Deletion and retention policy.
- Access control at retrieval time, not only ingestion time.
- Citation traceability.
- Re-ranking behavior.
- Stale document invalidation.
- Private data redaction.

Stop conditions:

- A user can retrieve another tenant's private content.
- Retrieved text can override system/developer instructions.
- Generated answers cite sources that do not support the claim.
- Deleted/private documents remain retrievable without policy approval.

### 6.6 Agent and Tool-Use Protocol

Required checks:

- Tool permission matrix.
- Dry-run mode for destructive tools.
- Human approval for consequential actions.
- Sandboxed file/network access.
- Command allowlists.
- Rate limits and spending limits.
- Secrets never exposed to the model unless absolutely necessary and approved.
- Tool outputs treated as untrusted.
- Model outputs never executed directly as shell/SQL/code without validation and approval.
- Audit trail for every external action.
- Rollback path for tool actions.

Stop conditions:

- Agent can access broad filesystem/network/secrets without task-specific limits.
- Agent can send external messages without review.
- Agent can modify billing, permissions, production data, or deployments without confirmation.
- Agent can execute model-generated commands without policy checks.

### 6.7 Multi-Model AI Evaluation

If more than one model is available, all relevant models must be tested against the same evaluation set before release:

- Primary model.
- Fallback model.
- Cheap/fast model used in production.
- High-reasoning model used for escalation.
- Any local/offline model.
- Any customer-configurable provider.

Compare:

- Correctness.
- Safety/refusal behavior.
- Prompt injection resistance.
- Tool-call behavior.
- Latency.
- Cost.
- Token usage.
- Output format reliability.
- Citation behavior.
- Failure mode.

The release report must state whether model differences are acceptable or whether routing/prompt/tool policies need adjustment.

---

## 7. Security and Penetration Testing Protocol

This protocol applies to all workspace types. It is based on secure development and verification principles used by OWASP ASVS, OWASP WSTG, NIST SSDF, and related guidance.

### 7.1 Security Baseline

Required for all projects:

- No secrets in Git.
- No secrets in package artifacts.
- No private data in logs.
- No debug endpoints in production.
- Least-privilege environment variables and tokens.
- Dependency lockfiles committed.
- Dependency vulnerability scanning.
- Security update policy.
- Authentication and authorization tests.
- Error handling that does not leak sensitive internals.
- Rate limits on abuse-prone paths.
- Audit logs for security-sensitive actions.
- Backup/restore plan when persistent data exists.
- Incident response contact/path.

### 7.2 Secret and Public Exposure Checklist

Never commit, package, expose, or paste into AI context unless explicitly authorized:

- .env files with real values.
- API keys.
- OAuth client secrets.
- JWT/session secrets.
- Database URLs/passwords.
- Cloud access keys.
- Service account JSON files.
- SSH keys.
- TLS private keys.
- Signing certificates.
- Apple/Android keystores and passwords.
- Stripe/PayPal/payment secrets.
- Webhook signing secrets.
- Admin passwords.
- Customer exports.
- Production logs.
- Crash dumps containing user data.
- Proprietary model prompts.
- Internal security reports.

Required before GitHub push:

- Local secret scan.
- `git status` review.
- `.gitignore` review.
- Artifact content review if generated files are committed.
- GitHub secret scanning/push protection enabled where available.

### 7.3 Vulnerability Severity Handling

| Severity | Definition | Required action |
| --- | --- | --- |
| Critical | Remote compromise, auth bypass, tenant breach, secret leak, payment compromise, destructive action | Block release. Fix and retest. |
| High | Likely exploit with serious data/security impact | Block production/customer release. Fix or documented executive waiver only. |
| Medium | Exploitable under constraints or limited impact | Fix before release when feasible; otherwise documented owner acceptance and backlog date. |
| Low | Defense-in-depth, hardening, minor leakage | Track and fix in normal hardening cycle. |

### 7.4 Penetration Test Evidence Template

```text
Penetration Test Summary
Project:
Date:
Tester:
Scope:
Environment:
Roles tested:
Tools used:

Findings:
1. ID:
   Severity:
   Affected surface:
   Reproduction:
   Impact:
   Fix:
   Retest:
   Status:

Release decision:
- Blocked / QA-ready / Release-candidate / Production-ready
- Waivers:
- Residual risks:
```

---

## 8. Scalability for Programming Protocol

Every application must be designed as if it may grow quickly. The AI must avoid coding patterns that only work for one user, one machine, one tenant, one model, one worker, or one happy-path demo.

### 8.1 Scale Intake

Define:

- Current expected users.
- Future target users.
- Concurrent users.
- Requests per second.
- Data size now and after 12 months.
- File storage growth.
- Background jobs per minute.
- Model calls per user action.
- Peak-hour multiplier.
- Regional requirements.
- Latency targets.
- Availability target.
- Cost ceiling.

### 8.2 Required Scale Design Checks

Architecture:

- Stateless application layer or explicit state strategy.
- Horizontal scaling path.
- Load balancer/CDN path.
- Database scaling plan.
- Cache strategy.
- Queue strategy.
- Search/indexing strategy.
- Object/file storage strategy.
- Idempotency for retries.
- Backpressure for overload.
- Circuit breakers for dependencies.
- Graceful degradation.

Code:

- No global mutable state that breaks multi-instance deployment.
- No local filesystem dependency for shared production data unless explicitly designed.
- No unbounded in-memory lists/maps/caches.
- No N+1 query paths.
- No blocking long-running work on request threads.
- No per-request expensive model calls without cache/rate/cost controls.
- No synchronous fan-out to many services without timeout/bulkhead strategy.
- No unpaginated endpoints.

Data:

- Indexes for high-cardinality filters and joins.
- Partitioning/sharding plan where growth demands it.
- Archive/retention plan.
- Migration strategy for large tables.
- Backup/restore testing.
- Read replica or cache plan where needed.

Operations:

- Autoscaling triggers.
- Resource requests/limits.
- Health checks.
- Readiness checks.
- Observability metrics.
- Alert thresholds.
- Runbooks.
- Rollback strategy.

### 8.3 Load Test Types

| Test | Purpose | Required for |
| --- | --- | --- |
| Baseline | Normal expected usage | Every release candidate |
| Load | Target expected peak | Public/customer release |
| Stress | Find breaking point | Major launch or uncertain capacity |
| Spike | Sudden traffic burst | Marketing launches, games, AI apps, public forms |
| Soak | Long-running leaks/queue buildup | Services, games, workers, AI systems |
| Failover | Dependency or instance failure | Production-ready systems |
| Cost | Estimate spend under peak/abuse | AI, serverless, paid APIs, cloud-heavy systems |

### 8.4 Scalability Report Template

```text
Scalability Report
Workspace:
Release target:
Workload model:
Test environment:
Traffic profile:
Commands/tools:

Results:
- p50 latency:
- p95 latency:
- p99 latency:
- Throughput:
- Error rate:
- CPU:
- Memory:
- DB CPU:
- DB slow queries:
- Queue depth:
- Cache hit rate:
- External API/model rate-limit behavior:
- Estimated monthly cost at target:

Bottlenecks:
Mitigations applied:
Remaining risks:
Release decision:
```

---

## 9. Multi-AI and Multi-Model Parallel Testing Protocol

When more than one AI model/agent is available, do not use them only sequentially. Use them as parallel reviewers with distinct responsibilities.

### 9.1 Required Roles

Assign available models to roles:

- Implementer: writes or modifies code.
- Reviewer: checks correctness, maintainability, and tests.
- Security reviewer: checks vulnerabilities, secrets, authorization, prompt injection.
- Scalability reviewer: checks performance, concurrency, data growth, cost.
- Domain reviewer: checks Unity/gameplay, web UX, backend contracts, AI evals, or customer domain.
- Red-team reviewer: attempts to break the feature within authorized scope.

If there are fewer models than roles, one model may perform multiple roles, but the report must say which roles were not independently covered.

### 9.2 Parallel Testing Rules

- Give each model the same release candidate and relevant protocol.
- Give each model a different review lens.
- Do not let the implementer model self-approve security-sensitive work.
- Compare findings and resolve contradictions.
- Re-run tests after fixes.
- Record which model found which issue when useful.

### 9.3 Cross-Model AI Behavior Testing

For AI products, run the same prompts and attack sets against every production-capable model:

- Normal task prompts.
- Ambiguous prompts.
- Insufficient-context prompts.
- High-risk factual prompts.
- Direct prompt injection prompts.
- Indirect prompt injection documents.
- Tool-abuse prompts.
- Secret-extraction prompts.
- Long-context prompts.
- Structured-output prompts.

Release only when the router, prompts, guardrails, and tool policies produce acceptable behavior across models or explicitly restrict production to the passing model.

---

## 10. GitHub, Packaging, and Customer Handoff Protocol

### 10.1 Before Committing

Required:

- Review `git status`.
- Review diffs for unintended changes.
- Apply the relevant domain block from `DOMAIN_SPECIFIC_GITIGNORE_PROTOCOLS.md` before staging generated builds, databases, customer exports, AI artifacts, or package outputs.
- Run relevant tests.
- Run secret scan when any config, env, build artifact, generated file, prompt, or package file is touched.
- Ensure unrelated user changes are not reverted or staged accidentally.
- Ensure generated artifacts are intentionally tracked.

### 10.2 Before Pushing to GitHub

Required:

- Functional gate passed or explicitly documented as branch-only/WIP.
- Security gate passed for touched surfaces.
- Secret scan passed.
- Public exposure review passed.
- CI expected to pass.
- README/docs updated for changed behavior.
- If the repository is public, review every new file as if customers, attackers, competitors, and search engines will read it.

GitHub push protection and secret scanning should be enabled where available.

### 10.3 Before Packaging for Customer

Required:

- Build from clean checkout.
- Include only required runtime files.
- Exclude source files if customer package should be binary-only.
- Exclude tests, fixtures, local configs, logs, and credentials.
- Include setup/run instructions.
- Include version and checksum.
- Include license and third-party notices.
- Include known issues.
- Include minimum system requirements.
- Include support/escalation contact.
- Verify package can be installed/run on a clean machine or container.

### 10.4 Before Production Deployment

Required:

- Release-candidate gate passed.
- Deployment plan.
- Rollback plan.
- Database migration plan and backup.
- Monitoring and alerts.
- Feature flag or staged rollout for risky changes.
- Incident response path.
- Post-deployment smoke tests.
- User/customer communication if behavior changes.

---

## 11. Mobile and Desktop Client Protocol

Use this for Android, iOS, Flutter, React Native, Electron, Tauri, native desktop, and packaged client apps.

Required intake:

- Target OS versions.
- App permissions.
- Signing identity.
- Store/distribution path.
- Local storage.
- Network endpoints.
- Offline behavior.
- Crash reporting.
- Update mechanism.
- Native modules/plugins.

Required checks:

- Secrets not embedded in client package.
- TLS and certificate behavior reviewed.
- Local storage encrypted for sensitive data.
- Logs do not contain personal data or tokens.
- Permissions are minimal and justified.
- Auth tokens refresh and revoke correctly.
- Offline queue is idempotent and safe.
- Deep links validated.
- IPC/native bridge hardened for desktop apps.
- Auto-update path signed and verified.
- Package scanned for private files.
- Install/uninstall/update tested.

Scale/reliability:

- API usage rate-limited.
- Crash-free session target defined.
- Startup time measured.
- Memory and battery impact reviewed.
- Large list/image/file handling tested.

---

## 12. Data, Analytics, and ML Pipeline Protocol

Use this for ETL, BI, analytics dashboards, model training, batch processing, data warehouses, and ML pipelines.

Required intake:

- Data sources.
- Data owners.
- PII/sensitive fields.
- Retention rules.
- Transformations.
- Quality checks.
- Access control.
- Backfill strategy.
- Schedule and failure handling.
- Downstream consumers.

Required checks:

- Schema validation.
- Null/outlier handling.
- Duplicate handling.
- Idempotent pipeline runs.
- Backfill safety.
- Lineage/provenance.
- PII redaction or encryption.
- Least-privilege credentials.
- Query cost review.
- Dashboard permission review.
- Model training/evaluation split correctness.
- Data leakage checks.
- Drift monitoring where ML is production-facing.

Stop conditions:

- PII exported to public or unauthorized storage.
- Training data includes evaluation labels in a way that invalidates metrics.
- Pipeline can double-charge, double-send, or double-write on retry.
- Dashboard exposes cross-tenant/customer data.

---

## 13. Infrastructure, DevOps, and CI/CD Protocol

Use this for Docker, Kubernetes, Terraform, cloud resources, CI/CD pipelines, GitHub Actions, deployments, DNS, certificates, observability, and secrets managers.

Required intake:

- Cloud provider and accounts.
- Environments: dev, staging, production.
- Deployment mechanism.
- IaC tool.
- Secret manager.
- Container registry.
- Runtime platform.
- Network boundaries.
- DNS and certificates.
- CI/CD triggers and permissions.
- Rollback path.

Required checks:

- Least-privilege IAM.
- No long-lived cloud keys in repository or CI logs.
- Environment separation.
- Production deploy requires approval.
- CI workflows safe against untrusted PR input.
- Third-party GitHub Actions pinned to trusted versions where appropriate.
- Container images use minimal base images and non-root users where possible.
- Image vulnerability scan.
- IaC plan review.
- Kubernetes resource requests/limits.
- Readiness/liveness probes.
- HPA or autoscaling policy where needed.
- Network policies/security groups.
- Backup/restore.
- Observability: logs, metrics, traces, alerts.

Stop conditions:

- Publicly exposed database/cache/admin service.
- CI can expose secrets to untrusted pull requests.
- Production credentials available in dev/test contexts.
- No rollback path for risky infra changes.
- Autoscaling configured without meaningful metrics.

---

## 14. Required Final Delivery Report

Every completed task must end with a concise report:

```text
Delivery Report
Workspace type:
Release level:
Changed files:
Functional tests:
Security checks:
Penetration tests:
AI/model tests:
Scalability tests:
Packaging checks:
Public exposure result:
Known risks:
Skipped gates and reason:
Human waivers:
Ready for:
```

Allowed "Ready for" values:

- Local review only.
- Internal QA.
- Staging.
- Release-candidate review.
- Customer acceptance testing.
- Production.
- Not ready.

---

## 15. Reference Standards and Official Guidance

Use these as baseline references when tailoring project-specific gates:

- OWASP Application Security Verification Standard (ASVS): https://owasp.org/www-project-application-security-verification-standard/
- OWASP Web Security Testing Guide (WSTG): https://owasp.org/www-project-web-security-testing-guide/
- OWASP Top 10 for Large Language Model Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- OWASP LLM01:2025 Prompt Injection: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- NIST Secure Software Development Framework (SSDF), SP 800-218: https://csrc.nist.gov/pubs/sp/800/218/final
- NIST AI Risk Management Framework and Generative AI Profile: https://www.nist.gov/itl/ai-risk-management-framework
- GitHub Secret Scanning Push Protection: https://docs.github.com/en/code-security/concepts/secret-security/about-push-protection
- GitHub Actions Secure Use Reference: https://docs.github.com/en/actions/reference/security/secure-use
- Kubernetes Horizontal Pod Autoscaling: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
- OpenTelemetry documentation: https://opentelemetry.io/docs/
- OpenAI prompt injection safety overview: https://openai.com/safety/prompt-injections/
- Unity Script Execution Order settings: https://docs.unity.cn/Documentation/Manual/class-ScriptExecution.html
- Unity Addressables overview: https://docs.unity.cn/Packages/com.unity.addressables%402.2/manual/AddressableAssetsOverview.html

---

## 16. Operational Rule for AI Assistants

When in doubt, the AI must be more conservative at release time than at prototype time.

Prototype behavior:

- Move fast.
- Explain assumptions.
- Keep risks visible.
- Do not claim production readiness.

Release behavior:

- Verify.
- Test.
- Scan.
- Red-team.
- Load test.
- Package cleanly.
- Inform the user before push/package/deploy.
- Record evidence.
- Fix critical findings before delivery.

The final standard is simple: the user should never unknowingly ship a fragile, insecure, non-scalable, hallucination-prone, prompt-injectable, or secret-leaking system just because the feature appeared to work in a short demo.
