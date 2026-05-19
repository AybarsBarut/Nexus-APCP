# Domain-Specific Gitignore Protocols and AI Prompts
## Field-specific ignore rules for safe GitHub publishing, customer packaging, and AI-assisted delivery

Version: 1.0
Status: Mandatory companion guide for APCP, MACP, and WSDP projects
Scope: Git ignore strategy, domain-specific artifact exclusion, sensitive-data prevention, and AI prompt templates for generating project-specific `.gitignore` files.

---

## 0. Prime Directive

A `.gitignore` file is a safety rail, not a security boundary. It helps prevent accidental commits of generated files, local data, build outputs, secrets, and domain-sensitive artifacts. It does not protect files that are already tracked by Git, already pushed to GitHub, copied into a package, leaked in logs, or pasted into an AI prompt.

Before GitHub push, customer packaging, public release, or production deployment, every AI assistant must verify that the project has an appropriate `.gitignore` for its workspace and domain.

If sensitive material was already committed:

- Do not rely on `.gitignore` as the fix.
- Remove the file from Git tracking.
- Rotate the exposed secret or credential.
- Purge history only when needed and with owner approval.
- Re-scan the repository and release artifact.
- Document the incident in the delivery report.

---

## 1. Gitignore Operating Model

### 1.1 What Belongs in `.gitignore`

Project `.gitignore` files should include patterns that all contributors should share:

- Build outputs.
- Dependency directories.
- Runtime caches.
- Logs.
- Temporary files.
- Local environment files.
- Local databases.
- Generated test reports.
- Generated AI context bundles.
- Private project structure and backend architecture maps.
- Game engine cache/build folders.
- ML datasets and model checkpoints.
- Infrastructure state files.
- Customer data exports.
- Banking, healthcare, legal, and enterprise-sensitive local data.

### 1.2 What Belongs in Local Git Exclude Instead

Use `.git/info/exclude` for personal-only files that should not be shared with the team:

- Personal scratch files.
- One developer's local editor output.
- Experimental local scripts.
- Machine-specific paths.
- Temporary notes not relevant to the project.

### 1.3 What Must Stay Tracked

Do not ignore these unless the project has a documented reason:

- Source code.
- Tests.
- Documentation.
- Migration files.
- `.env.example`, `.env.sample`, `.env.template`.
- Lockfiles for applications.
- Package manifests.
- CI workflows.
- Dockerfiles.
- Terraform `.tf` files.
- Kubernetes manifests without secrets.
- OpenAPI/GraphQL/protobuf contracts.
- Unity `Assets/`, `Packages/`, `ProjectSettings/`, and `.meta` files.
- Unreal `.uproject`, `Config/`, `Content/`, `Source/`, and source plugin files.
- Godot `project.godot`, scenes, scripts, and source assets.
- License and third-party attribution files.

### 1.4 Gitignore Cannot Fix Already Tracked Files

If a file is already tracked, adding it to `.gitignore` will not stop Git from tracking changes. Use:

```bash
git rm --cached path/to/file
```

For directories:

```bash
git rm -r --cached path/to/directory
```

Only run removal commands after confirming the file should remain locally but disappear from Git. For secrets, also rotate the secret.

---

## 2. Universal Baseline Gitignore Block

Use this block in almost every software project. Add domain-specific blocks after it.

```gitignore
# Secrets and environment files
.env
.env.*
!.env.example
!.env.sample
!.env.template
*.env.local
*.secret
*.secrets
secrets/
.secrets/
credentials/
.credentials/
private/
.private/
*.pem
*.key
*.p8
*.p12
*.pfx
*.jks
*.keystore
id_rsa
id_rsa.*
id_ed25519
id_ed25519.*
service-account*.json
firebase-adminsdk*.json
google-credentials*.json
aws-credentials*
gcp-credentials*
azure-credentials*

# OS and editor
.DS_Store
Thumbs.db
Desktop.ini
*.swp
*.swo
*~
.idea/
.vscode/*
!.vscode/extensions.json
!.vscode/settings.example.json
.history/

# Logs, temporary files, test reports
*.log
logs/
tmp/
temp/
*.tmp
*.temp
coverage/
.coverage
.coverage.*
htmlcov/
test-results/
playwright-report/
cypress/videos/
cypress/screenshots/
junit.xml
*.lcov
*.dmp
crash-dumps/
memory-dumps/

# Private project context and internal architecture
AI_PROJECT_CONTEXT.md
PROJECT_CONTEXT.md
PROJECT_STRUCTURE.md
PROJECT_MAP.md
REPO_MAP.md
CODEBASE_MAP.md
BACKEND_MAP.md
DATABASE_SCHEMA_INTERNAL.md
INFRASTRUCTURE_MAP.md
DEPLOYMENT_MAP.md
THREAT_MODEL_INTERNAL.md
SECURITY_ARCHITECTURE.md
ARCHITECTURE_INTERNAL.md
ARCHITECTURE_PRIVATE.md
*_INTERNAL.md
*_PRIVATE.md
*_LOCAL.md
docs/internal/
docs/private/
docs/local/
docs/architecture-internal/
docs/backend-map/
docs/security-internal/
internal-docs/
private-docs/
local-context/
```

Universal rule:

- Keep examples tracked.
- Ignore real secrets.
- Keep docs tracked.
- Ignore generated reports unless intentionally published.
- Keep lockfiles tracked for deployable apps.
- Ignore dependency directories.
- Keep only sanitized public architecture docs tracked; real backend maps, internal architecture, threat models, deployment maps, and project-specific AI context files stay local/private.

### 2.1 Private Architecture and Project Context Rule

Treat filled project context files like secrets when they reveal how the system is built. Backend topology, route maps, service names, database internals, private infrastructure, internal admin flows, security controls, deployment topology, private prompts, tool policies, vector-store layout, threat models, penetration-test reports, and runbooks should not be pushed to a public repository or included in a customer package by default.

For downstream product repositories that should not reveal local AI workflow files on GitHub, use local Git excludes instead of committed ignore rules. `.git/info/exclude` and private global excludes files let AI agents read APCP files locally while keeping the public repository free of the protocol filenames and generated context artifacts.

If public documentation is needed, create a sanitized public version that removes internal hostnames, admin routes, service topology, database details, security controls, credentials, private prompts, and exploit-relevant implementation details.

AI prompt:

```text
You are auditing a repository for private architecture and project-context exposure.
Find files that explain internal project structure, backend topology, route maps, database schema internals, infrastructure layout, deployment topology, threat models, penetration-test reports, private runbooks, AI system prompts, tool policies, vector-store layout, or filled APCP project context.
Update `.gitignore` so internal project context and architecture maps stay local/private.
Keep only sanitized protocol templates and public documentation tracked.
Report already tracked internal files and propose `git rm --cached` remediation.
State whether the repository is safe for public GitHub.
```

---

## 3. AI-Assisted Project and APCP Gitignore Block

Use for APCP/MACP projects, AI coding sessions, prompt packs, context gatherers, and multi-agent workflows. Apply this block to `.git/info/exclude` when public GitHub should not show the local AI workflow filenames. Apply it to committed `.gitignore` only when the repository intentionally makes those ignore rules public.

```gitignore
# APCP / MACP / AI-generated context
PROMPT_READY.txt
PROMPT_READY.tmp
.checkpoint
.apcp-cache/
.ai-cache/
.ai-output/
.ai-runs/
.ai_scratch/
.ai_team/heartbeats/
.ai_team/session-logs/
*.prompt.local
*.context.local
*.scratch.md

# Installed Nexus-APCP operating files in downstream product repos
AI_PROJECT_CONTEXT_PROTOCOL.md
AI_MAIN.md
TASK_PROGRESS.yaml
DECISION_LOG_PROTOCOL.md
CONTEXT_OPTIMIZATION.md
CAVEMAN_RULES.md
EMOJI_POLICY.md
VISUAL_CONTEXT_MERMAID.md
AI_AGENT_SKILLS_PROTOCOL.md
AI_TOOL_ADAPTER_COMPATIBILITY_PROTOCOL.md
FILE_STRUCTURE_REFACTOR_PROTOCOL.md
WORKSPACE_SPECIFIC_DELIVERY_PROTOCOLS.md
WEBSITE_BACKEND_SECURITY_OPTIMIZATION_PROTOCOL.md
DOMAIN_SPECIFIC_GITIGNORE_PROTOCOLS.md
UPDATE_SYSTEM_RECOMMENDATION_PROTOCOL.md
DEBLOAT_APPLICATION_GUIDE.md
DISCOVER_ALGORITHM_DESIGN_GUIDE.md
FRONTEND_APPLICATION_DESIGN_PROTOCOL.md
MACP_IMPLEMENTATION_GUIDE.md
UNIVERSAL_APPLICATION_SECURITY_PROTOCOL.md
WATERFALL_DEVELOPMENT_PROTOCOL.md
README_APCP_KIT.md
MASTER_PROMPT.md
AI_ASSISTANT_PROMPT_TEMPLATES.md
docs/AI_ASSISTANT_PROMPT_TEMPLATES.md
scripts/apcp-gather.py

# Filled APCP project context is private by default
AI_PROJECT_CONTEXT.md
PROJECT_CONTEXT.md
local-context/

# Keep shared templates and state if intentionally part of protocol
!.ai_team/templates/
!.ai_team/handshakes/
!.ai_team/handoffs/
!.ai_team/conflicts/
!.ai_team/AI_TEAM_STATE.json
```

Rules:

- Do not commit raw AI logs containing secrets, private prompts, customer data, local file paths, or credentials.
- Do not commit temporary prompt bundles generated from private repositories.
- Do not commit installed Nexus-APCP operating files to downstream public product repositories by default; keep them local or in an approved private/cloud knowledge base for AI agents.
- Do not commit filled `AI_PROJECT_CONTEXT.md` files for real projects when they expose backend structure, database layout, infrastructure, internal services, route maps, private prompts, or security assumptions.
- Do commit sanitized protocol templates only when the repository intentionally publishes its AI workflow templates.
- Do commit decision logs if they contain no secrets or customer data.
- Do not paste local secret files into AI context.

AI prompt:

```text
You are preparing an APCP/MACP repository for safe GitHub use.
Review the project for AI-generated context artifacts, local prompt bundles, heartbeats, temporary scratch files, and private session logs.
If public GitHub should not reveal local AI workflow files, add installed APCP operating files and generated AI artifacts to `.git/info/exclude` or a private global excludes file instead of committed `.gitignore`.
Use committed `.gitignore` only when the public ignore rule itself is acceptable.
Keep protocol templates, sanitized handoffs, sanitized state files, and documentation trackable only when the repository intentionally publishes them.
Also list any file currently tracked that should be removed from Git with `git rm --cached`.
```

---

## 4. Web Frontend and Full-Stack JavaScript Gitignore Block

Use for React, Next.js, Vue, Nuxt, SvelteKit, Astro, Angular, Remix, Express, Node, Bun, Deno, and TypeScript apps.

```gitignore
# Dependencies
node_modules/
bower_components/
jspm_packages/
.pnp/
.pnp.*
.yarn/cache/
.yarn/unplugged/
.yarn/build-state.yml
.yarn/install-state.gz
.pnpm-store/
.npm/

# Build outputs and framework caches
dist/
build/
out/
.next/
.nuxt/
.output/
.vercel/
.netlify/
.svelte-kit/
.astro/
.vite/
.vitepress/cache/
storybook-static/
*.tsbuildinfo

# Test and browser automation artifacts
coverage/
.nyc_output/
playwright-report/
test-results/
cypress/videos/
cypress/screenshots/

# Local env
.env
.env.*
!.env.example
!.env.sample
!.env.template
```

Rules:

- Never expose private variables through `NEXT_PUBLIC_*`, `VITE_*`, `PUBLIC_*`, or similar client-exposed prefixes unless the value is intentionally public.
- Do not commit production source maps unless access is controlled and approved.
- Do not commit static JSON exports containing user/customer data.
- Do not commit generated HTML snapshots containing private routes or data.
- Keep lockfiles tracked: `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`, `bun.lockb` when used.

AI prompt:

```text
You are reviewing a web/full-stack JavaScript project before GitHub push.
Identify the framework, package manager, build output folders, deployment platform, env variable exposure model, test report folders, and client bundle risks.
Update `.gitignore` so dependency directories, build outputs, local env files, source maps if private, and test artifacts are ignored.
Do not ignore package manifests, lockfiles, CI workflows, public assets, or docs.
Then inspect the built output for accidentally exposed secrets, internal URLs, admin endpoints, private prompts, and customer data.
```

---

## 5. Python Backend, API, and Automation Gitignore Block

Use for FastAPI, Django, Flask, Celery, CLI tools, automation scripts, and Python services.

```gitignore
__pycache__/
*.py[cod]
*$py.class
.Python
.venv/
venv/
env/
ENV/
pip-wheel-metadata/
*.egg-info/
.eggs/
build/
dist/
site/
.mypy_cache/
.pytest_cache/
.ruff_cache/
.tox/
.nox/
htmlcov/
.coverage
.coverage.*

# Local env and secrets
.env
.env.*
!.env.example
!.env.sample
!.env.template
```

Rules:

- Keep `requirements.txt`, `pyproject.toml`, `poetry.lock`, `uv.lock`, and `Pipfile.lock` tracked for applications.
- Do not ignore migrations.
- Do not commit SQLite production databases.
- Do not commit Celery beat schedule files when they contain runtime state.
- Do not commit local notebooks with secrets or private datasets unless sanitized.

AI prompt:

```text
You are reviewing a Python backend before GitHub push.
Update `.gitignore` for virtual environments, bytecode, caches, test reports, build artifacts, local env files, local SQLite databases, and runtime scheduler files.
Keep dependency manifests, lockfiles, migrations, tests, docs, Dockerfiles, and CI workflows tracked.
Report any tracked `.env`, `.sqlite`, `.db`, dump, notebook, or private dataset that must be removed from Git.
```

---

## 6. Unity Game Project Gitignore Block

Use for Unity games, simulations, AR/VR apps, mobile Unity apps, and Unity packages.

```gitignore
# Unity generated folders
[Ll]ibrary/
[Tt]emp/
[Oo]bj/
[Bb]uild/
[Bb]uilds/
[Ll]ogs/
[Uu]ser[Ss]ettings/
[Mm]emoryCaptures/
[Rr]ecordings/

# IDE/project files generated by Unity
*.csproj
*.unityproj
*.sln
*.suo
*.tmp
*.user
*.pidb
*.booproj
*.svd
*.pdb
*.mdb
*.opendb
*.VC.db
sysinfo.txt

# Mobile/build artifacts
*.apk
*.aab
*.ipa
*.unitypackage

# Secrets/signing
*.keystore
*.jks
*.p12
*.pfx
```

Must stay tracked:

- `Assets/`
- `Packages/`
- `ProjectSettings/`
- `.meta` files
- Assembly definition files
- Editor scripts intended for the team
- Addressables settings when part of the project

Rules:

- Never ignore `.meta` files in Unity; they preserve GUID references.
- Do not commit `Build/` or `Builds/` outputs.
- Do not commit `Library/`, `Temp/`, `Obj/`, or logs.
- Do not commit signing keys, keystores, provisioning profiles, or service account files.
- Do not commit generated Addressables build output unless the release process explicitly requires it.
- Do not commit crash dumps, memory captures, recordings, or profiler snapshots unless sanitized and intentionally shared.
- For online games, never commit server secrets, economy configs with production credentials, anti-cheat secrets, admin endpoints, or private matchmaking credentials.

AI prompt:

```text
You are preparing a Unity project for safe GitHub push and customer build delivery.
Inspect the project for Unity version, render pipeline, target platforms, Addressables usage, signing files, generated builds, Library/Temp/Obj folders, logs, profiler captures, memory captures, and local service credentials.
Update `.gitignore` so generated Unity folders and builds are ignored.
Ensure Assets, Packages, ProjectSettings, assembly definitions, and all `.meta` files remain trackable.
Warn if any build artifact, keystore, API key, service account file, server credential, or production config is already tracked.
```

---

## 7. Unreal Engine Gitignore Block

Use for Unreal Engine games, simulations, virtual production, and Unreal plugins.

```gitignore
# Unreal generated folders
Binaries/
DerivedDataCache/
Intermediate/
Saved/
.vs/

# Generated project files
*.opensdf
*.sdf
*.sln
*.suo
*.xcodeproj/
*.xcworkspace/
*.xcuserstate
*.pdb
*.target
*.modules

# Builds and packages
Builds/
Packaged/
Releases/
*.pak
*.utoc
*.ucas

# Secrets/signing
*.p12
*.pfx
*.key
*.keystore
*.jks
```

Must stay tracked:

- `.uproject`
- `Config/`
- `Content/`
- `Source/`
- Project plugin source
- Build scripts
- Default config files that do not contain secrets

Rules:

- Do not commit `Binaries/`, `Intermediate/`, `Saved/`, or `DerivedDataCache/`.
- Do not commit packaged builds unless the repository is explicitly a release-artifact repository.
- Do not ignore source assets under `Content/`.
- Review config files for secrets before push.
- Treat game clients as hostile; do not ship production server secrets.

AI prompt:

```text
You are reviewing an Unreal Engine repository before GitHub push.
Update `.gitignore` for Unreal-generated folders, packaged builds, IDE-generated project files, crash dumps, logs, and signing credentials.
Keep `.uproject`, Config, Content, Source, plugin source, and build scripts tracked.
Check whether any generated binary, packaged build, production config, private asset pack, or credential is already tracked and report remediation steps.
```

---

## 8. Godot Game Project Gitignore Block

Use for Godot 3.x and 4.x projects.

```gitignore
# Godot generated/import cache
.godot/
.import/
*.translation
*.import

# Export presets can contain signing credentials or private paths
export_presets.cfg

# Builds
build/
builds/
exports/
*.pck
*.exe
*.apk
*.aab
*.ipa
*.app
```

Must stay tracked:

- `project.godot`
- Scenes
- Scripts
- Source assets
- Addons intended for the team
- Sanitized export preset templates if needed

Rules:

- Review `export_presets.cfg`; it can contain private export paths or signing data.
- Do not commit platform builds by default.
- Do not commit imported cache folders.
- Keep project settings and source scenes tracked.

AI prompt:

```text
You are preparing a Godot project for safe GitHub use.
Detect Godot version, export targets, generated import cache, export presets, platform build artifacts, and signing files.
Update `.gitignore` so `.godot`, `.import`, builds, and private export presets are ignored.
Keep project.godot, scenes, scripts, source assets, addons, and sanitized template configs tracked.
```

---

## 9. Mobile App Gitignore Block

Use for Android, iOS, Flutter, React Native, Expo, Capacitor, Ionic, and native mobile apps.

```gitignore
# Android
.gradle/
build/
app/build/
local.properties
captures/
.externalNativeBuild/
.cxx/
*.apk
*.aab
*.ap_
*.idsig

# Android signing
*.jks
*.keystore
*.p12
*.pfx

# iOS/macOS
DerivedData/
xcuserdata/
*.xcuserstate
*.xcworkspace/xcuserdata/
*.xcodeproj/xcuserdata/
*.ipa
*.dSYM/
*.dSYM.zip

# Flutter / Dart
.dart_tool/
.flutter-plugins
.flutter-plugins-dependencies
.packages
build/

# React Native / Expo
node_modules/
.expo/
.expo-shared/
android/app/build/
ios/build/
```

Rules:

- Do not commit signing keys, keystores, provisioning profiles, private certificates, or store credentials.
- Keep Gradle files, Podfile, package manifests, and lockfiles tracked.
- `ios/Pods/` policy must be explicit; some teams commit Pods, many do not.
- Do not commit generated app packages unless this is a release-artifact repository.
- Do not commit crash reports with user data.
- Do not embed server secrets in mobile clients.

AI prompt:

```text
You are reviewing a mobile app before GitHub push or store/customer packaging.
Identify Android, iOS, Flutter, React Native, Expo, Capacitor, or native stack.
Update `.gitignore` for build outputs, local properties, generated packages, DerivedData, IDE user files, signing keys, provisioning files, and crash reports.
Keep source code, manifests, dependency lockfiles, sanitized config templates, and CI workflows tracked.
Flag any client-embedded API secret, keystore, provisioning profile, Firebase admin file, or production credential already tracked.
```

---

## 10. Banking, FinTech, Payments, and Insurance Gitignore Block

Use for banking apps, wallets, payment systems, card processing, lending, insurance, accounting, reconciliation, compliance, and financial analytics projects.

```gitignore
# Local databases and runtime storage
*.db
*.db-*
*.sqlite
*.sqlite3
*.sqlite-journal
*.sqlite-shm
*.sqlite-wal
*.mdb
*.accdb

# Dumps, backups, and exports
*.dump
*.dump.gz
*.sql.gz
*dump*.sql
*backup*.sql
*database-export*.sql
*.bak
*.backup
*.bkp
/dumps/
/backups/
/exports/
/customer-exports/

# Banking/finance sensitive data
/customer_data/
/customer-data/
/kyc/
/aml/
/statements/
/reconciliations/
/settlements/
/ledger-exports/
/payment-exports/
/chargeback-exports/
/card-data/
/pci/

# Certificates, keys, HSM/client credentials
*.pem
*.key
*.p8
*.p12
*.pfx
*.jks
*.keystore
```

Must stay tracked:

- Sanitized migrations.
- Sanitized schema files.
- Sanitized test fixtures.
- Compliance documentation without customer data.
- API contracts.
- Infrastructure code without secrets.

Rules:

- Never commit production databases.
- Never commit backend topology maps, internal ledger architecture, private reconciliation workflows, fraud-rule internals, or payment-provider integration maps to a public repository.
- Never commit customer exports.
- Never commit cardholder data.
- Never commit KYC/AML documents.
- Never commit statements, reconciliation exports, settlement files, or chargeback exports.
- Never commit HSM credentials, payment provider secrets, webhook signing secrets, bank API certificates, or private keys.
- Use synthetic data for tests.
- Use tokenized/masked examples in docs.
- Keep migrations tracked unless they contain real data.
- Keep seed files only when they are synthetic and reviewed.

AI prompt:

```text
You are reviewing a banking/fintech/payment repository before GitHub push, customer delivery, or production release.
Create or update `.gitignore` to prevent local databases, dumps, backups, customer exports, KYC/AML files, statements, reconciliation files, settlement exports, cardholder data, webhook secrets, HSM credentials, bank API certificates, and payment provider secrets from being committed.
Keep migrations, schema definitions, API contracts, synthetic fixtures, docs, and CI workflows tracked.
Inspect the current Git index for already tracked `.db`, `.sqlite`, `.sql.gz`, dump, backup, export, KYC, AML, statement, settlement, reconciliation, card-data, certificate, or key files.
If anything sensitive is tracked, report `git rm --cached` steps and remind the owner to rotate/revoke affected credentials.
```

---

## 11. Healthcare, Legal, Education, and Regulated Data Gitignore Block

Use for systems that may handle PHI, PII, medical records, legal discovery, student records, HR files, government records, or regulated enterprise data.

```gitignore
# Sensitive local data
/phi/
/pii/
/patient-data/
/medical-records/
/legal-discovery/
/case-files/
/student-records/
/hr-records/
/customer-exports/
/private-reports/

# Medical and document exports
*.dcm
*.nii
*.hl7
*.fhir.json
*.xlsx
*.xls
*.csv

# Local databases and dumps
*.db
*.sqlite
*.sqlite3
*.dump
*.dump.gz
*.sql.gz
*backup*.sql
*dump*.sql
```

Rules:

- Be careful with broad `*.csv`, `*.xlsx`, and `*.json` ignores; they may hide legitimate config or test fixtures. Prefer directory-specific rules when possible.
- Never commit PHI/PII or legal evidence.
- Never commit production exports.
- Use synthetic fixtures.
- Keep schemas, mappings, and validators tracked.
- Keep de-identified test data only after review.

AI prompt:

```text
You are reviewing a regulated-data project before GitHub push.
Classify whether the repository may contain PHI, PII, student records, HR records, legal discovery, government data, or enterprise confidential data.
Update `.gitignore` to exclude local sensitive-data folders, exports, medical files, discovery files, databases, dumps, and generated private reports.
Keep schema definitions, validators, synthetic fixtures, documentation, and compliance-safe templates tracked.
Report any tracked sensitive file and explain that `.gitignore` does not remediate already pushed data.
```

---

## 12. AI, LLM, RAG, Agent, and Model Development Gitignore Block

Use for chatbots, copilots, RAG systems, embeddings, vector databases, agents, eval harnesses, model fine-tuning, and local inference projects.

```gitignore
# Local corpora and private data
/data/
/datasets/
/corpora/
/private-corpus/
/raw-data/
/processed-data/

# Model artifacts
/model-artifacts/
/checkpoints/
/weights/
*.pt
*.pth
*.ckpt
*.onnx
*.pb
*.tflite
*.safetensors
*.gguf
*.bin

# Vector stores and embedding indexes
/vectorstore/
/vectorstores/
/chroma/
/.chroma/
/qdrant_storage/
/weaviate-data/
/milvus-data/
/lancedb/
/.lancedb/
*.faiss
*.hnsw
*.ann
*.index

# Experiment tracking
/mlruns/
/wandb/
/lightning_logs/
/runs/
/outputs/

# Private prompts and local eval results
*.prompt.local
*.context.local
eval-results/
redteam-results/
attack-corpus/
```

Must stay tracked:

- Sanitized prompt templates intended to ship.
- Evaluation harness code.
- Red-team test definitions without secrets/customer data.
- Model cards.
- Dataset cards.
- Safety policies.
- RAG ingestion code.
- Schema/contracts.

Rules:

- Do not commit private corpora.
- Do not commit production vector stores.
- Do not commit customer documents used for RAG.
- Do not commit model provider API keys.
- Do not commit system prompts if they contain secrets or proprietary policy not meant for public release.
- Do not commit local eval output containing real user prompts.
- Do not commit model weights unless license, size, LFS policy, and release intent are explicit.
- Treat retrieved data as potentially sensitive.

AI prompt:

```text
You are reviewing an AI/LLM/RAG/agent project before GitHub push or customer packaging.
Inventory models, prompts, evals, vector stores, private corpora, tool logs, agent traces, memory stores, and provider credentials.
Update `.gitignore` so local corpora, private datasets, vector databases, embedding indexes, model checkpoints, local eval outputs, red-team outputs, agent traces, and private prompts are ignored.
Keep sanitized prompt templates, eval harness code, model cards, dataset cards, safety docs, and schema definitions tracked.
Report any tracked vector store, private document corpus, API key, system prompt with secrets, or model checkpoint that should not be public.
```

---

## 13. Data Science, Analytics, and ML Pipeline Gitignore Block

Use for ETL, notebooks, BI, analytics dashboards, data pipelines, model training, forecasting, and reporting systems.

```gitignore
# Data folders
/data/
/datasets/
/raw-data/
/processed-data/
/exports/
/reports/private/

# Large data formats
*.parquet
*.feather
*.npy
*.npz
*.h5
*.hdf5
*.pkl
*.pickle

# Notebooks and execution artifacts
.ipynb_checkpoints/
notebooks/.ipynb_checkpoints/

# ML artifacts
/artifacts/
/model-artifacts/
/checkpoints/
/mlruns/
/wandb/
/runs/
/outputs/
```

Rules:

- Do not ignore notebooks by default; review them for outputs and secrets.
- Clear notebook outputs before commit when outputs contain sensitive data.
- Keep pipeline code, schemas, data contracts, and synthetic fixtures tracked.
- Do not commit raw production datasets.
- Do not commit generated dashboards containing customer data.
- Do not commit pickled objects from untrusted sources.

AI prompt:

```text
You are reviewing a data/ML repository before GitHub push.
Identify raw datasets, processed datasets, exports, generated private reports, notebooks, model artifacts, experiment tracking output, and local caches.
Update `.gitignore` to exclude data folders and large/generated artifacts while preserving source code, schemas, data contracts, synthetic fixtures, docs, and sanitized notebooks.
Inspect notebooks for embedded outputs, credentials, customer data, and absolute private paths.
```

---

## 14. DevOps, Infrastructure, Cloud, and CI/CD Gitignore Block

Use for Terraform, OpenTofu, Pulumi, Kubernetes, Helm, Docker, cloud SDKs, CI/CD, and deployment automation.

```gitignore
# Terraform / OpenTofu
.terraform/
*.tfstate
*.tfstate.*
*.tfvars
*.tfvars.json
crash.log
override.tf
override.tf.json
*_override.tf
*_override.tf.json
*.tfplan
plan.out

# Kubernetes / Helm secrets
.kube/
*.kubeconfig
kubeconfig
.helm/secrets/
helm-secrets/

# Docker/local overrides
.docker/
docker-compose.override.yml
docker-compose.*.local.yml

# Cloud credentials
aws-credentials*
gcp-credentials*
azure-credentials*
service-account*.json
google-credentials*.json
*.pem
*.key
*.p12
*.pfx
```

Must stay tracked:

- Terraform/OpenTofu `.tf` files without secrets.
- Sanitized `.tfvars.example`.
- Kubernetes manifests without secrets.
- Helm charts without secrets.
- Dockerfiles.
- CI workflow definitions.
- Deployment scripts without credentials.

Rules:

- Never commit state files.
- Never commit internal infrastructure maps, private network diagrams, admin runbooks, deployment topology maps, or disaster-recovery details to public repositories.
- Never commit `.tfvars` with real values.
- Never commit kubeconfig.
- Never commit cloud credentials.
- Do not commit decrypted Helm secrets.
- Do not commit local Docker override files with credentials.
- Be careful with CI logs; they can expose secrets.

AI prompt:

```text
You are reviewing an infrastructure/DevOps repository before GitHub push.
Update `.gitignore` for Terraform/OpenTofu state, plans, real tfvars, kubeconfigs, Helm secrets, local Docker overrides, cloud credentials, service account files, and private keys.
Keep IaC source files, Dockerfiles, CI workflows, sanitized examples, charts, manifests, and docs tracked.
Inspect the Git index for tracked state files, kubeconfigs, private keys, service account JSON, real tfvars, or decrypted secrets.
```

---

## 15. E-Commerce, Marketplace, CRM, and SaaS Business Apps

Use for SaaS apps handling accounts, customers, subscriptions, invoices, orders, tickets, and payment records.

```gitignore
# Customer/business exports
/customer-exports/
/tenant-exports/
/order-exports/
/invoice-exports/
/billing-exports/
/support-exports/
/crm-exports/
/reports/private/

# Local databases and backups
*.db
*.sqlite
*.sqlite3
*.dump
*.dump.gz
*.sql.gz
*backup*.sql
*dump*.sql
/backups/
/dumps/

# Payment/provider secrets
*.pem
*.key
*.p12
*.pfx
.env
.env.*
!.env.example
```

Rules:

- Never commit customer exports.
- Never commit tenant data.
- Never commit invoice/order exports containing personal data.
- Never commit support ticket exports.
- Never commit payment provider secrets.
- Keep migrations and seed data only if synthetic.
- Keep public sample CSV files only if sanitized and small.

AI prompt:

```text
You are reviewing a SaaS/e-commerce/CRM repository before GitHub push.
Update `.gitignore` for customer exports, tenant exports, order/invoice/billing exports, support exports, local databases, dumps, backups, payment provider secrets, and local env files.
Keep migrations, API contracts, synthetic fixtures, documentation, and sanitized examples tracked.
Report any tracked real customer data, invoice export, support export, payment secret, or local database.
```

---

## 16. Desktop Apps, Electron, Tauri, and Packaged Tools

Use for Electron, Tauri, Qt, WPF, WinUI, desktop agents, installers, and packaged tools.

```gitignore
# Node/Electron
node_modules/
dist/
build/
out/
release/
releases/
*.asar

# Tauri/Rust
src-tauri/target/
target/

# Installers and packages
*.exe
*.msi
*.dmg
*.pkg
*.app
*.deb
*.rpm
*.AppImage

# Signing and credentials
*.p12
*.pfx
*.pem
*.key
*.jks
*.keystore
```

Rules:

- Do not commit signed installers unless this is a release-artifact repository.
- Do not commit signing certificates.
- Do not commit auto-update private keys.
- Do not commit crash dumps or logs with user data.
- Keep source, manifests, lockfiles, and updater configuration templates tracked.

AI prompt:

```text
You are reviewing a desktop app repository before GitHub push or customer packaging.
Identify Electron/Tauri/native build outputs, installers, release folders, crash dumps, signing certificates, updater keys, and local logs.
Update `.gitignore` so generated packages and private signing material are ignored.
Keep source code, manifests, lockfiles, sanitized config templates, and docs tracked.
```

---

## 17. Release Artifact Repositories

Sometimes a repository intentionally stores release artifacts. This must be explicit.

If artifacts are intentionally tracked, create a release policy:

- Which artifact types are allowed.
- Who approves adding them.
- Size limits.
- License checks.
- Malware scan requirements.
- Checksum requirements.
- Signing requirements.
- Retention policy.
- Whether Git LFS is required.

Default rule:

- Application source repositories should not track generated builds, installers, dumps, or binary packages.
- Release artifacts should usually go to GitHub Releases, package registries, object storage, app stores, or artifact repositories.

AI prompt:

```text
This repository may intentionally store release artifacts.
Before editing `.gitignore`, determine whether it is a source repository, artifact repository, or hybrid.
If artifacts are intentionally tracked, propose an artifact policy with allowed file types, approval rules, checksums, signing, malware scan, retention, and Git LFS requirements.
Do not blanket-ignore release artifacts if the owner explicitly wants them versioned.
```

---

## 18. Pre-Push Gitignore Audit Protocol

Run before every GitHub push when the project has sensitive surfaces.

Checklist:

- `git status --short`
- `git diff --cached --stat`
- `git diff --cached --name-only`
- `git check-ignore -v path/to/suspicious/file` for any file that should be ignored.
- Confirm no `.env`, local database, dump, build, package, credential, customer export, private dataset, vector store, or model checkpoint is staged.
- Confirm no filled project context, backend map, internal architecture, private threat model, deployment topology, database internals, penetration-test report, or security runbook is staged for a public repository.
- Confirm no downstream installed APCP operating file or generated context bundle is staged unless sanitized publication was explicitly approved.
- If public GitHub should not reveal AI workflow filenames, confirm APCP rules live in `.git/info/exclude` or a private global excludes file instead of committed `.gitignore`.
- Confirm `.env.example` is staged/tracked when config changed.
- Confirm migrations are tracked when schema changed.
- Confirm lockfiles are tracked when dependencies changed.
- Confirm generated artifacts are intentionally tracked or ignored.
- Run a secret scanner before push.
- If a sensitive file is already tracked, use `git rm --cached` and rotate credentials if necessary.

AI prompt:

```text
Perform a pre-push gitignore audit.
1. Read `.gitignore` and, when relevant, `.git/info/exclude`.
2. Read `git status --short`.
3. Inspect staged and unstaged file names.
4. Identify any secrets, environment files, local DBs, dumps, generated builds, customer exports, AI vector stores, model checkpoints, logs, crash dumps, downstream installed APCP operating files, generated context bundles, private project context, backend maps, internal architecture docs, private threat models, deployment topology maps, or domain-sensitive data that should not be committed.
5. Identify any important source/config files that are accidentally ignored.
6. If public GitHub should not reveal AI workflow filenames, prefer local exclude remediation over committed `.gitignore` changes.
7. Provide exact remediation commands, but do not run destructive commands without approval.
8. State whether the repository is safe to push.
```

---

## 19. Domain Selection Prompt

Use this when starting a new project or when the workspace type is unclear.

```text
You are configuring `.gitignore` for a new repository.
First classify the workspace:
- Web frontend
- Backend/API
- Full-stack SaaS
- Unity game
- Unreal game
- Godot game
- Mobile app
- Desktop app
- AI/LLM/RAG/agent
- Data/ML
- Infrastructure/DevOps
- Banking/fintech/payments
- Healthcare/legal/regulated data
- E-commerce/CRM/SaaS business app
- Release artifact repository
- Mixed project

Then generate a `.gitignore` with:
- Universal baseline rules
- Language/framework rules
- Domain-sensitive rules
- Build/package artifact rules
- Secret/env rules
- AI-generated artifact rules if relevant
- Internal architecture/project-context rules
- Explicit keep-tracked notes for files that must not be ignored

Finally, list:
- Files that must stay tracked
- Files that must never be committed
- Internal architecture/context files that must stay local
- Commands to untrack already committed sensitive files
- Secret rotation warnings
- Pre-push verification steps
```

---

## 20. Gitignore Review Prompt for Existing Repositories

```text
You are auditing an existing repository's `.gitignore`.
Do not assume the current ignore rules are safe.

Tasks:
1. Identify the stack, framework, language, runtime, and domain.
2. Identify generated folders and build artifacts.
3. Identify local secrets, env files, credentials, certificates, and cloud config.
4. Identify domain-sensitive data that must never be pushed.
5. Identify internal project context, backend maps, architecture maps, database internals, deployment maps, private threat models, and security runbooks that must stay local/private.
6. Identify project-critical files that must remain tracked.
7. Compare current `.gitignore` against the needed rules.
8. Propose a patch that adds missing protections without hiding important source files.
9. Check whether sensitive or internal files are already tracked.
10. Provide remediation steps for already tracked files.
11. Provide a final "safe to push" or "not safe to push" verdict.
```

---

## 21. Customer Package Gitignore Prompt

```text
You are preparing a customer package.
Review `.gitignore`, package scripts, build output, and included files.

Ensure the package excludes:
- `.git`
- `.env` and local config
- private keys and certificates
- service account files
- local databases
- dumps and backups
- customer exports
- logs and crash dumps
- test reports
- AI prompt logs and private context bundles
- vector stores and private corpora
- game engine cache folders
- raw datasets
- internal docs not meant for customer delivery
- filled project context files and backend architecture maps
- debug builds unless explicitly intended

Ensure the package includes:
- runtime files
- license notices
- third-party attributions
- setup/run instructions
- version and checksum
- sanitized config example
- known issues
```

---

## 22. Final Delivery Report Addition

Every delivery report should include a `.gitignore` section:

```text
Gitignore and public exposure:
- Workspace/domain:
- .gitignore updated: yes/no
- Local exclude used for APCP/AI workflow files: yes/no
- Domain-specific blocks applied:
- Files intentionally ignored:
- Files intentionally kept tracked:
- Already-tracked sensitive files found:
- Internal architecture/context exposure found:
- Remediation performed:
- Secret rotation required:
- Secret scan status:
- Safe to push/package:
```

---

## 23. Official References

Use these references when customizing rules:

- GitHub Docs - Ignoring files: https://docs.github.com/en/get-started/git-basics/ignoring-files
- Git documentation - gitignore: https://git-scm.com/docs/gitignore
- GitHub `.gitignore` template collection: https://github.com/github/gitignore
- GitHub Docs - Detecting secret leaks: https://docs.github.com/en/code-security/how-tos/secure-your-secrets/detect-secret-leaks
- Unity Support - generated folders such as Library and Temp should not be added to Unity version control: https://support.unity.com/hc/en-us/articles/360047016552--Application-gitignore-for-Unity-Version-Control-formerly-known-as-Plastic-SCM

---

## 24. Operational Rule for AI Assistants

Before suggesting "push to GitHub", "package this", "send to the customer", or "release this", the AI must ask:

- Does the `.gitignore` match the workspace?
- Does it match the domain?
- Does it block generated builds?
- Does it block local databases?
- Does it block customer data?
- Does it block internal project context, backend maps, architecture maps, deployment maps, and private threat models?
- Does it block secrets and private keys?
- Does it block AI private context and vector stores?
- If public GitHub should not reveal AI workflow files, are installed APCP files handled through local/private excludes instead of committed public ignore rules?
- Does it avoid hiding files that must be tracked?
- Were already tracked sensitive files checked?
- Was a secret scan run?

If the answer is uncertain, the correct status is not "ready". The correct status is "needs gitignore/public exposure audit".
