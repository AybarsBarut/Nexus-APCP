# Nexus-APCP: AI Project Context Protocol
## Project Context Protocol for AI coding assistants, AI agents, and LLM workflows v1.0

---

## QUICK START

This file is the **single source of truth** for AI coding assistants and agents (Claude Code, Cursor, ChatGPT, Gemini, GitHub Copilot, local LLMs, etc.) to understand your entire project and work consistently. When this file is updated:
- The model **does not** have to learn the project from scratch
- The token budget is used effectively
- Changes are synchronized automatically
- The AI takes on the role of project manager

### Active Context Profile

Nexus-APCP supports profile-based context loading through `apcp-profile.json`.
Use `core` unless the project clearly needs `web`, `backend-api`, `cli`, `game`, `ai-rag`, or `full`.
Specialized protocols outside the active profile are references, not standing instructions, unless the current user request or task explicitly invokes them.

Rule priority:
1. Current user request and explicit approvals.
2. Security, privacy, secret-handling, and public/private boundary rules.
3. Filled project context and current task state.
4. Selected APCP profile files and task-invoked specialized protocols.
5. General examples, templates, and optional reference protocols.

---

## SECTION 1: GENERAL PROJECT INFORMATION

### 1.1 Project Identity
```yaml
Project Name: [PROJECT_NAME]
Description: [PROJECT_DESCRIPTION]
Owner: [OWNER_NAME/ORGANIZATION]
GitHub Repo: [https://github.com/username/repo]
Main Language: [Python/JavaScript/TypeScript/Go/etc]
Start Date: [YYYY-MM-DD]
Last Updated: [YYYY-MM-DD]
```

### 1.2 Project Goals and Scope
```
1. [Goal 1]
2. [Goal 2]
3. [Goal 3]

OUT OF SCOPE:
- [Excluded Topic 1]
- [Excluded Topic 2]
```

### 1.3 Stakeholders and Roles
| Role | Name | Responsibility | Contact |
|-----|-----|-----------|----------|
| **Project Manager** | [Name] | Project oversight, deadlines | [email/slack] |
| **Tech Lead** | [Name] | Technical decisions, reviews | [email/slack] |
| **DevOps/Infrastructure** | [Name] | Deployment, CI/CD | [email/slack] |
| **AI Assistant** | Claude | Coding, documentation, analysis | Automatic |

---

## SECTION 2: PROJECT FILE HIERARCHY

```
[PROJECT_NAME]/
│
├──  src/                           # Source code
│   ├──  core/                      # Core functionality
│   │   ├── auth.py                   # Authentication
│   │   ├── database.py               # Database connections
│   │   ├── config.py                 # Configuration management
│   │   └── utils.py                  # Common helper functions
│   │
│   ├──  api/                       # API endpoints
│   │   ├── routes.py                 # Flask/FastAPI routes
│   │   ├── middleware.py             # Middlewares
│   │   ├── validators.py             # Input validation
│   │   └── responses.py              # Standardized response formats
│   │
│   ├──  models/                    # Data models (ORM, schemas)
│   │   ├── user.py                   # User model
│   │   ├── product.py                # Product model
│   │   └── schemas.py                # Pydantic/Marshmallow schemas
│   │
│   ├──  services/                  # Business logic
│   │   ├── user_service.py           # User operations
│   │   ├── payment_service.py        # Payment operations
│   │   └── notification_service.py   # Notification operations
│   │
│   ├──  tasks/                     # Background tasks (Celery, etc)
│   │   ├── email_tasks.py
│   │   ├── export_tasks.py
│   │   └── cleanup_tasks.py
│   │
│   ├──  tests/                     # Test files
│   │   ├── unit/
│   │   ├── integration/
│   │   └── fixtures.py
│   │
│   └── main.py / app.py              # Application entry point
│
├──  infrastructure/                # DevOps and configuration
│   ├── docker/
│   │   ├── Dockerfile
│   │   ├── docker-compose.yml
│   │   └── .dockerignore
│   ├── kubernetes/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── configmap.yaml
│   ├── terraform/                    # IaC
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── scripts/
│       ├── deploy.sh
│       ├── backup.sh
│       └── migrate.sh
│
├──  docs/                          # Documentation
│   ├── ARCHITECTURE.md               # Architecture document
│   ├── API.md                        # API documentation
│   ├── SETUP.md                      # Setup guide
│   ├── DEPLOYMENT.md                 # Deployment procedure
│   ├── TROUBLESHOOTING.md            # Troubleshooting
│   └── CHANGELOG.md                  # Change log
│
├──  config/                        # Configuration files
│   ├── development.env
│   ├── staging.env
│   ├── production.env
│   └── logging.yaml
│
├──  .github/                       # GitHub configuration
│   ├── workflows/
│   │   ├── ci.yml
│   │   ├── cd.yml
│   │   └── tests.yml
│   └── ISSUE_TEMPLATE/
│
├── requirements.txt / package.json   # Dependencies
├── .gitignore
├── .env.example
├── README.md
├── LICENSE
└── AI_PROJECT_CONTEXT.md             #  Local/private filled project context by default
```

### 2.1 Important Directory Descriptions

| Directory | Purpose | Access Rule |
|-------|------|---------------|
| `src/core/` | Core functions used by all modules | `from core import auth, config` |
| `src/services/` | Business logic, data processing | Used between internal modules |
| `src/tests/` | Unit and integration tests | Run with `pytest` |
| `infrastructure/` | DevOps and deployment | DevOps/Infrastructure team only |
| `docs/` | Technical documents | **ALWAYS READ BEFORE STARTING** |

---

## SECTION 3: COMMON FUNCTIONS AND IMPORT STRUCTURE

### 3.1 Core Module (src/core/)

**auth.py** - Authentication functions
```python
from src.core.auth import (
    authenticate_user,      # User login
    verify_token,           # JWT/Token validation
    create_token,           # Generate token
    require_auth            # Decorator: route protection
)
```
 **Usage Areas**: API routes, middleware, services

**database.py** - Database operations
```python
from src.core.database import (
    get_db,                 # Database session (context manager)
    init_db,                # Initialize database
    execute_query,          # Raw SQL query
    close_db                # Close connection
)
```
 **Usage Areas**: Services, models

**config.py** - Configuration management
```python
from src.core.config import (
    get_config,             # Load config based on environment
    get_env,                # Read environment variable
    SETTINGS                # Global settings object
)
```
 **Usage Areas**: Entry file, services

**utils.py** - Helper functions
```python
from src.core.utils import (
    generate_id,            # Generate UUID/custom ID
    hash_password,          # Hash password (bcrypt)
    verify_password,        # Verify password
    format_date,            # Date formatting
    send_notification,      # Send notification
    log_event               # Event logging
)
```
 **Usage Areas**: Everywhere

### 3.2 Services Layer (src/services/)

Each service contains all the logic for a specific business domain:

```python
from src.services.user_service import UserService
from src.services.payment_service import PaymentService
from src.services.notification_service import NotificationService

# Usage
user_service = UserService()
user = user_service.create_user(email="user@example.com", password="...")
```

### 3.3 Import Rules (CRITICAL!)

 **DOS**:
```python
# Use absolute imports
from src.core.auth import authenticate_user
from src.services.user_service import UserService

# Relative imports (within the same directory)
from .utils import helper_function
```

 **DON'TS**:
```python
# Creating circular imports
from src import something  # Don't!

# Too long chains
from src.api.routes.users.handlers.v1 import func  # Simplify!
```

---

## SECTION 4: SECURITY AND SENSITIVE DATA RULES

### 4.1 WHAT MUST BE PROTECTED

The following will **NEVER** be written in this file or in code reviews:

```yaml
Type: API Keys / Tokens
Examples:
  - JWT Secret: "<REDACTED_JWT_SECRET>"
  - Database Password: "<REDACTED_DATABASE_PASSWORD>"
  - AWS Access Key: "<REDACTED_AWS_ACCESS_KEY_ID>"
  - OpenAI API Key: "<REDACTED_OPENAI_API_KEY>"
  - Stripe Secret Key: "<REDACTED_STRIPE_SECRET_KEY>"
Storage: .env file or Secrets Manager
Rule: Will never be committed to the repo
```

### 4.2 .env File Template (.env.example)

```bash
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
DATABASE_POOL_SIZE=10
DATABASE_TIMEOUT=30

# Authentication
JWT_SECRET=<SHOULD_BE_IN_SECRETS_MANAGER>
JWT_ALGORITHM=HS256
JWT_EXPIRATION=3600

# API Keys (External Services)
OPENAI_API_KEY=<SHOULD_BE_IN_SECRETS_MANAGER>
STRIPE_API_KEY=<SHOULD_BE_IN_SECRETS_MANAGER>
SENDGRID_API_KEY=<SHOULD_BE_IN_SECRETS_MANAGER>

# Environment
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=INFO

# CORS
CORS_ORIGINS=http://localhost:3000,http://localhost:8000
```

### 4.3 Administrative Use of Sensitive Data

If you need to show sensitive data to the AI model:

```
[REDACTED_API_KEY_BEGINS_WITH: sk_live_]
[REDACTED_DATABASE_PASSWORD]
[REDACTED_JWT_SECRET]
```

### 4.4 Private Project Context and Architecture Exposure

Filled project-context files are treated like sensitive material when they reveal how the system is built. The following must stay local/private unless a sanitized public version is explicitly approved:

```yaml
Type: Internal project structure and architecture context
Examples:
  - AI_PROJECT_CONTEXT.md filled for a real private project
  - Installed Nexus-APCP operating files copied into a downstream product repository
  - AI_MAIN.md, TASK_PROGRESS.yaml, DECISION_LOG_PROTOCOL.md, and local protocol files when they expose the AI workflow or private delivery state
  - Backend route maps and service topology
  - Database schema internals and production migration notes
  - Infrastructure/deployment maps and internal hostnames
  - Admin workflows, runbooks, threat models, pentest reports
  - Private AI system prompts, tool policies, vector-store layout
Storage: local workspace, private docs, or approved internal knowledge base
Rule: Do not commit to public GitHub or customer packages by default. AI agents may read these files locally, from private/cloud knowledge bases, or from generated context bundles. Create a sanitized public summary or template only when explicitly approved.
```

### 4.5 Website Backend Public/Private Boundary

For website projects, apply `WEBSITE_BACKEND_SECURITY_OPTIMIZATION_PROTOCOL.md` before adding backend, API, auth, storage, or serverless logic.

Default rules:

- Static-first for portfolios, landing pages, brochure sites, and public content.
- No SQL database for portfolio sites unless the user requests real dynamic records, private submissions, CMS-style editing, or stored analytics.
- Browser-exposed values are public by design; private API keys, service role keys, database URLs, payment secrets, mail keys, webhook signing secrets, and AI provider keys stay server-side.
- Use serverless/edge/backend proxies only when they enforce validation, authorization, secret protection, rate limits, caching, quotas, or webhook verification.
- End website backend work with functional tests, build review, secret scan, dependency scan, public bundle review, authorized penetration testing, fixes, and retest before release-ready delivery.

---

## SECTION 5: CODE STRUCTURE AND DESIGN PATTERNS

### 5.1 Classic Layered Architecture

```
Request → API Routes → Validators → Services → Models → Database
                             ↓
                        Core Utilities
                        (auth, config, utils)
```

### 5.2 Service Layer Example

```python
# src/services/user_service.py
from src.core.auth import hash_password, verify_password
from src.core.database import get_db
from src.models.user import User

class UserService:
    def create_user(self, email: str, password: str):
        """Create a new user"""
        db = get_db()
        hashed = hash_password(password)
        user = User(email=email, password_hash=hashed)
        db.add(user)
        db.commit()
        return user
    
    def authenticate(self, email: str, password: str):
        """Verify user"""
        db = get_db()
        user = db.query(User).filter(User.email == email).first()
        if user and verify_password(password, user.password_hash):
            return user
        return None
```

### 5.3 API Route Example

```python
# src/api/routes/users.py
from flask import Blueprint, request
from src.core.auth import require_auth
from src.api.validators import validate_email
from src.api.responses import success_response, error_response
from src.services.user_service import UserService

bp = Blueprint('users', __name__, url_prefix='/api/v1/users')
user_service = UserService()

@bp.route('/register', methods=['POST'])
def register():
    """Register a new user"""
    data = request.json
    
    # Validate
    if not validate_email(data.get('email')):
        return error_response("Invalid email", 400)
    
    # Create
    user = user_service.create_user(
        email=data['email'],
        password=data['password']
    )
    
    return success_response({"user_id": user.id}, 201)

@bp.route('/profile', methods=['GET'])
@require_auth
def get_profile():
    """User profile (protected)"""
    user_id = request.user_id  # Set by require_auth middleware
    user = user_service.get_user_by_id(user_id)
    return success_response(user.to_dict())
```

### 5.4 Naming Conventions

| Type | Convention | Example |
|-----|-----------|--------|
| **File Name** | snake_case | `user_service.py`, `payment_handler.py` |
| **Class Name** | PascalCase | `UserService`, `PaymentHandler` |
| **Function Name** | snake_case | `create_user()`, `validate_email()` |
| **Constant** | UPPER_SNAKE_CASE | `MAX_RETRIES`, `DEFAULT_TIMEOUT` |
| **Private Variable** | _leading_underscore | `_internal_state`, `_cache` |
| **Magic Method** | __dunder__ | `__init__`, `__str__` |
| **Database Table** | plural_snake | `users`, `products`, `orders` |
| **Route Endpoint** | /api/v1/resource | `/api/v1/users`, `/api/v1/products/{id}` |

---

## SECTION 6: GIT FLOW AND CHECKPOINT SYSTEM

### 6.1 Branch Strategy (Git Flow)

```
main (production)
 ↑
release/v1.0.0
 ↑
develop (staging)
 ↑
feature/user-authentication
feature/payment-integration
bugfix/login-issue
```

### 6.2 Commit Message Format (Conventional Commits)

```
<type>(<scope>): <subject>

<body>

<footer>

EXAMPLE:
feat(auth): add JWT token refresh endpoint

Add ability to refresh expired JWT tokens without re-authentication.
Implements refresh token rotation for security.

Closes #123
Breaking-Change: POST /auth/login now returns refresh_token field
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `refactor`: Code structure change (functionality remains same)
- `test`: Adding/updating tests
- `chore`: Build, dependency update
- `perf`: Performance improvement
- `ci`: CI/CD configuration

### 6.3 Pre-Commit Checkpoint System

Perform these checks **BEFORE** making changes:

```bash
# 1. Verify tests run
pytest src/tests/ -v
# All tests must pass

# 2. Check code format
black src/
flake8 src/
# No errors/warnings allowed

# 3. Type checking
mypy src/
# Type hints must be correct

# 4. Security scan
bandit -r src/
# No security issues allowed

# 5. Dependency security
safety check
# No known vulnerabilities allowed

# 6. Check git status
git status
# Only intended files should change
```

### 6.4 Safe Checkpoint Command

```bash
#!/bin/bash
# scripts/checkpoint.sh

set -e  # Stop on error

echo " Running tests..."
pytest src/tests/ -v --tb=short

echo " Formatting code..."
black src/ --check
flake8 src/ --max-line-length=100

echo " Running security checks..."
bandit -r src/ -ll
safety check

echo " All checks passed! Safe to commit."
echo "Next: git add . && git commit -m 'type(scope): message'"
```

**Usage**:
```bash
bash scripts/checkpoint.sh
```

---

## SECTION 7: TASK PROGRESS TRACKER

### 7.1 Tasks.yaml File Structure

Create a `TASK_PROGRESS.yaml` file in the project root:

```yaml
# TASK_PROGRESS.yaml
# Last Updated: [YYYY-MM-DD HH:MM:SS UTC]
# Completion Rate: [X]%

Project: [PROJECT_NAME]
Sprint: Sprint 1 / Week 1-2
Period: [YYYY-MM-DD] - [YYYY-MM-DD]

Tasks:
  - id: TASK-001
    title: "Create project structure"
    description: "Core directory structure, git config, Docker setup"
    status: COMPLETED
    priority: CRITICAL
    assigned_to: AI Assistant
    start_date: 2024-01-01
    due_date: 2024-01-03
    completion_date: 2024-01-03
    effort_estimate: 4h
    actual_effort: 3.5h
    subtasks:
      - " Create src/ and infrastructure/ directories"
      - " Configure .gitignore and .env.example"
      - " Add requirements.txt / package.json"
      - " Complete Docker setup"
    notes: |
      - All core modules ready
      - Testing framework set up (pytest)
    blockers: "None"
    dependencies: []

  - id: TASK-002
    title: "Develop API authentication system"
    description: "JWT-based auth, role-based access control"
    status: IN_PROGRESS (60%)
    priority: CRITICAL
    assigned_to: AI Assistant
    start_date: 2024-01-04
    due_date: 2024-01-08
    completion_date: null
    effort_estimate: 12h
    actual_effort: 7.2h (to date)
    subtasks:
      - " Develop Auth service"
      - " Implement JWT token logic"
      - " Integrate middleware (in progress)"
      - " Write unit tests"
      - " Write integration tests"
    notes: |
      - Service layer completed
      - Issues with middleware testing
    blockers: "JWT secret missing in test environment in config.py"
    dependencies: ["TASK-001"]

  - id: TASK-003
    title: "User model and database migrations"
    description: "User table, relationships, indexes"
    status: NOT_STARTED
    priority: HIGH
    assigned_to: AI Assistant
    start_date: 2024-01-09
    due_date: 2024-01-12
    completion_date: null
    effort_estimate: 8h
    actual_effort: 0h
    subtasks:
      - " Write user model (with Alembic)"
      - " Apply database migrations"
      - " Add constraints and indexes"
    notes: "Should start after TASK-002 is completed"
    blockers: "Auth service not yet completed"
    dependencies: ["TASK-002"]

Sprint_Summary:
  total_tasks: 3
  completed: 1
  in_progress: 1
  not_started: 1
  completion_percentage: 33%
  velocity: "Average: 3.5h/task, Estimated remaining: 20h"
  risks: |
    - JWT secret missing in test environment
    - Complex relations in middleware integration
  upcoming_blockers: "Database migration strategy must be determined"
```

### 7.2 Task Status Legend

```
 COMPLETED   - Fully finished, tested, merged
 IN_PROGRESS - Active work ongoing (% progress)
 NOT_STARTED - Not yet started (blockers/dependencies noted if any)
 BLOCKED     - Waiting for another task to complete
 REVIEW      - PR opened, waiting for code review
```

### 7.3 Priority Levels

```
 CRITICAL   - System might not work, blocker, required immediately
 HIGH       - Important, should be in the sprint
 MEDIUM     - Standard, will be done as time permits
 LOW        - Nice-to-have, can wait in the backlog
```

### 7.4 AI Assistant's Task Management

Before starting each task:

```
Before starting TASK-002:
1. Read TASK_PROGRESS.yaml
2. Identify blockers if any
3. Check dependencies
4. Read and understand subtasks
5. Note start_date
6. Set status to IN_PROGRESS

As each subtask is completed:
- Mark completed subtasks with `DONE`
- Update percentage (TASK-002: 60% → 75%)
- Update actual_effort
- Add what was done to notes

When task is completed:
- Set status to COMPLETED
- Add completion_date
- Finalize actual_effort
- Write a short summary
```

---

## SECTION 8: DOCUMENTATION AND RESOURCES

### 8.1 Mandatory Documentation Files

Must always be present in the project:

```
docs/
├── README.md
├── SETUP.md                 # Developer environment setup
├── ARCHITECTURE.md          # System architecture
├── API.md                   # API endpoints
├── DATABASE.md              # Schema, migrations
├── DEPLOYMENT.md            # Production deployment
├── TROUBLESHOOTING.md       # Common issues and solutions
├── SECURITY.md              # Security policies
├── WORKSPACE_SPECIFIC_DELIVERY_PROTOCOLS.md # Workspace-specific security, AI, packaging, and scalability gates
├── WEBSITE_BACKEND_SECURITY_OPTIMIZATION_PROTOCOL.md # Website backend security, API secrecy, static-first, and pentest gates
├── DOMAIN_SPECIFIC_GITIGNORE_PROTOCOLS.md # Domain-specific ignore rules and safe-push prompts
├── UPDATE_SYSTEM_RECOMMENDATION_PROTOCOL.md # User-requested updater fit checks and safe implementation prompt
├── VISUAL_CONTEXT_MERMAID.md # Mermaid README flowchart and visual context protocol
├── AI_AGENT_SKILLS_PROTOCOL.md # Reusable AI agent skill workflows for diagnosis, TDD, triage, PRDs, handoff, architecture review, and prototypes
├── AI_TOOL_ADAPTER_COMPATIBILITY_PROTOCOL.md # Safe AI tool adapter compatibility and prompt-source hygiene
├── FILE_STRUCTURE_REFACTOR_PROTOCOL.md # Safe iterative file and folder restructuring protocol
├── CONTRIBUTING.md          # Contributor guidelines
├── CHANGELOG.md             # Version history
└── API_REFERENCE.yaml       # OpenAPI/Swagger spec
```

### 8.2 README.md Structure (Minimum)

````markdown
# [Project Name]

[1-2 sentence description]

## Project Flow

This flowchart shows the public, high-level path through the project. Keep it simple enough for a first-time reader and safe enough for a public repository.

```mermaid
flowchart TD
    User[User or Client] --> Entry[UI, CLI, or API Entry Point]
    Entry --> App[Application Layer]
    App --> Domain[Core Domain Logic]
    Domain --> Data[(Data Store)]
    Domain --> Integrations[External Services]
    App --> Delivery[Build and Deployment]
```

## Quick Start

```bash
git clone [repo-url]
cd [project-name]
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
python -m flask run
```

## Features

- Feature 1
- Feature 2
- Feature 3

## Architecture

[Brief high-level overview + reference to docs/ARCHITECTURE.md and VISUAL_CONTEXT_MERMAID.md]

## API Documentation

[Key endpoints + reference to docs/API.md]

## Database

[Schema description + reference to docs/DATABASE.md]

## Development

### Running Tests
```bash
pytest src/tests/ -v
```

### Code Style
```bash
black src/
flake8 src/
```

## Deployment

[Deployment steps + reference to docs/DEPLOYMENT.md]

## Contributing

Please read docs/CONTRIBUTING.md.

## License

[LICENSE type]

## Support

- Email: [support email]
- Issues: [GitHub Issues URL]
- Docs: [docs URL]
````

### 8.3 ARCHITECTURE.md Template

````markdown
# Architecture

## High-Level Overview

```mermaid
flowchart TD
    Entry[Entry Point] --> App[Application Layer]
    App --> Services[Service Layer]
    Services --> Data[(Data Layer)]
    Services --> External[External Integrations]
```

## Components

### 1. API Layer (src/api/)
- Purpose: HTTP request handling
- Framework: [Flask/FastAPI]
- Key files: routes.py, middleware.py, validators.py

### 2. Service Layer (src/services/)
- Purpose: Business logic
- Key classes: UserService, PaymentService, etc.
- Responsibilities: Data processing, calculations, external API calls

### 3. Data Layer (src/models/)
- Purpose: Data modeling and persistence
- ORM: [SQLAlchemy/Mongoose]
- Key models: User, Product, Order

### 4. Core Layer (src/core/)
- Purpose: Shared utilities
- Modules: auth, config, database, utils

## Data Flow

[Description of request-response cycle]

## Database Schema

[ERD diagram or table descriptions]

## Authentication & Authorization

[Description of JWT flow, roles, permissions]

## External Integrations

- Service 1: [URL, docs]
- Service 2: [URL, docs]

## Error Handling

[Global error handling strategy]

## Caching Strategy

[Cache mechanisms, TTL values]

## Scalability Considerations

[Performance optimizations, bottlenecks]
````

### 8.4 API.md Template

```markdown
# API Documentation

## Base URL

```
Development: http://localhost:8000/api/v1
Production: https://api.example.com/api/v1
```

## Authentication

All endpoints require JWT token in header:
```
Authorization: Bearer <token>
```

## Endpoints

### Users

#### Register User
```
POST /users/register
Content-Type: application/json

Request:
{
  "email": "user@example.com",
  "password": "secure_password",
  "name": "User Name"
}

Response (201):
{
  "user_id": "uuid",
  "email": "user@example.com",
  "created_at": "2024-01-15T10:30:00Z"
}

Errors:
- 400: Invalid input
- 409: Email already exists
```

#### Login
```
POST /auth/login
...
```

#### Get User Profile
```
GET /users/{user_id}
Authorization: Bearer <token>

Response (200):
{
  "user_id": "uuid",
  "email": "...",
  ...
}

Errors:
- 401: Unauthorized
- 404: User not found
```

[All endpoints should be documented]
```

---

## SECTION 9: EXTERNAL RESOURCES AND REFERENCES

### 9.1 Documentation Links

| Technology | Official Documentation | Internal Doc |
|-----------|-------------------|--------------|
| **Flask** | https://flask.palletsprojects.com/en/ | docs/API.md |
| **FastAPI** | https://fastapi.tiangolo.com/ | docs/API.md |
| **SQLAlchemy** | https://docs.sqlalchemy.org/ | docs/DATABASE.md |
| **PostgreSQL** | https://www.postgresql.org/docs/ | docs/DATABASE.md |
| **Docker** | https://docs.docker.com/ | infrastructure/docker/ |
| **Kubernetes** | https://kubernetes.io/docs/ | infrastructure/kubernetes/ |
| **JWT.io** | https://jwt.io/introduction | docs/SECURITY.md |
| **Pytest** | https://docs.pytest.org/ | src/tests/ |
| **Git** | https://git-scm.com/doc | docs/CONTRIBUTING.md |

### 9.2 GitHub Resources

```
Repository: [https://github.com/username/project]
Issues: [https://github.com/username/project/issues]
Discussions: [https://github.com/username/project/discussions]
Projects: [https://github.com/username/project/projects]
Wiki: [https://github.com/username/project/wiki]

Pull Request Template: .github/pull_request_template.md
Issue Templates: .github/ISSUE_TEMPLATE/
Actions: .github/workflows/
```

### 9.3 External Services & APIs

| Service | Purpose | Documentation | API Key Location |
|--------|------|-------------|-----------------|
| **OpenAI** | AI completions | https://platform.openai.com/docs | .env: OPENAI_API_KEY |
| **Stripe** | Payments | https://stripe.com/docs/api | .env: STRIPE_API_KEY |
| **SendGrid** | Email | https://docs.sendgrid.com/ | .env: SENDGRID_API_KEY |
| **AWS S3** | File storage | https://docs.aws.amazon.com/s3/ | .env: AWS_ACCESS_KEY |

### 9.4 Third-Party Libraries

```
All dependencies in requirements.txt / package.json:

Python example:
- flask==2.3.0              # Web framework
- sqlalchemy==2.0.0         # ORM
- pydantic==2.0.0           # Data validation
- pytest==7.0.0             # Testing
- python-dotenv==1.0.0      # Environment management
- pyjwt==2.8.0              # JWT handling

Relevant docs link should be next to each library
```

---

## SECTION 10: SPECIAL RULES AND CONVENTIONS

### 10.1 Error Handling

Return all errors in this standard:

```python
# src/api/responses.py
def error_response(message: str, code: int, error_type: str = None):
    """Standardized error response"""
    return {
        "success": False,
        "error": {
            "type": error_type or "GenericError",
            "message": message,
            "code": code,
            "timestamp": datetime.utcnow().isoformat()
        }
    }, code
```

Usage:
```python
return error_response("User not found", 404, "UserNotFoundError")
```

### 10.2 Logging

```python
import logging

logger = logging.getLogger(__name__)

logger.info("User created", extra={"user_id": user.id})
logger.warning("High memory usage", extra={"memory_mb": 850})
logger.error("Database connection failed", exc_info=True)
```

### 10.3 Validation

```python
from pydantic import BaseModel, EmailStr, Field

class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    name: str = Field(..., max_length=100)
    
    class Config:
        schema_extra = {
            "example": {
                "email": "user@example.com",
                "password": "secure_password",
                "name": "John Doe"
            }
        }
```

### 10.4 Database Conventions

```python
# Table names: plural, snake_case
class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID, primary_key=True, default=uuid4)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    orders = relationship("Order", back_populates="user")
```

---

## SECTION 11: NEW MODEL TRANSITION PROTOCOL

**Scenario**: You are switching to a new AI model or fresh session and reached the token limit.

### 11.1 Checklist

```
BEFORE SWITCHING MODELS:

 1. Create/update this file (AI_PROJECT_CONTEXT_PROTOCOL.md)
 2. Update TASK_PROGRESS.yaml (save last state)
 3. Commit to Git: "docs: update project context and task progress"
 4. If there are open PRs, merge branch from latest main
 5. Clean local branches: git branch -D feature/...

AT THE BEGINNING OF PROMPT (with New Model):

 1. Put this file (AI_PROJECT_CONTEXT_PROTOCOL.md) in internal context
 2. Read TASK_PROGRESS.yaml
 3. Read last task: "Where were we?"
 4. Continue from where we left off
```

### 11.2 New Model Prompt Starters

**Option 1: Continue without summary**
```
I'm switching to a new AI model on project [PROJECT_NAME].

[Paste entire AI_PROJECT_CONTEXT_PROTOCOL.md]

[Paste entire TASK_PROGRESS.yaml]

Where were we? Let me know the last completed task and what's next.
```

**Option 2: With summary (token efficiency)**
```
Continuing work on [PROJECT_NAME].

Last completed task: TASK-002 (API authentication system, 60% complete)
Current blockers: JWT secret not configured in test environment
Next task: TASK-003 (User model and database migrations)

[Paste AI_PROJECT_CONTEXT_PROTOCOL.md - SECTION 2-5 only]
[Paste TASK_PROGRESS.yaml - current sprint only]

Help me implement TASK-003. What should I do first?
```

---

## SECTION 12: METRICS AND MONITORING

### 12.1 Development Metrics

Metrics to track (in TASK_PROGRESS.yaml):

```yaml
Metrics:
  - Velocity: [X] tasks/sprint (Moving average: 3-sprint)
  - Sprint Completion: [X]% (Target: 90%)
  - Code Coverage: [X]% (Target: 80%+)
  - Test Pass Rate: [X]% (Target: 100%)
  - Average Review Time: [X] hours
  - Bug Fix Time: [X] hours (Mean)
  - Documentation Coverage: [X]%
```

### 12.2 Production Health (Post-Deployment)

```yaml
Production_Metrics:
  - Uptime: [X]% (Target: 99.9%)
  - Response Time (p95): [X]ms (Target: <200ms)
  - Error Rate: [X]% (Target: <0.1%)
  - Database Query Time (p95): [X]ms
  - Memory Usage: [X]MB (vs baseline)
  - API Rate: [X] req/sec
```

---

## SECTION 13: FILE UPDATE PROCEDURE

How and when will this file (APCP) be updated?

### 13.1 Auto-Update Triggers

The model should update automatically in the following situations:

```
 New file added → Update docs/ section
 New external service integrated → Update Section 9.3
 Folder structure changed → Update Section 2
 New import convention → Update Section 3
 Security policy changed → Update Section 4
 Task completed → Update Section 7
```

### 13.2 Manual Update (by User)

Weekly (on Friday):
1. Open this file
2. Update the "Last Updated" date
3. Update new/changed sections
4. Commit to Git

### 13.3 User-Requested Update System Recommendation

When the user asks for an updater, version checker, GitHub sync, or launcher that updates before app start, read `UPDATE_SYSTEM_RECOMMENDATION_PROTOCOL.md` before proposing implementation.

Default rule:
- Do not add an update system automatically for every project.
- Recommend the lightweight GitHub SemVer + zip-sync pattern only when the user asks for update behavior and the project profile fits.
- If the project is SaaS, API-only backend, mobile app store, browser extension store, package-manager distributed software, or requires signed installers or staged rollout, recommend the appropriate release strategy instead.
- Always protect `.env`, local user data, settings files, backups, logs, generated prompt bundles, and filled private context files.

### 13.4 Existing Project File Structure Refactor

When Nexus-APCP is added to an existing project and the user asks to reorganize files, folders, modules, imports, scripts, tests, or documentation structure, read `FILE_STRUCTURE_REFACTOR_PROTOCOL.md` before moving files.

Default rule:
- Do not treat file movement as complete until imports, entry points, tests, builds, scripts, assets, and documentation references are updated.
- Migrate in small iterations with verification after each iteration.
- Preserve existing behavior unless the user explicitly approves a breaking migration.
- Use temporary compatibility wrappers, re-exports, or aliases when old paths are still used.
- Stop moving new files if verification fails, then repair the current iteration before continuing.
- Update this protocol, README flowcharts, architecture docs, and `TASK_PROGRESS.yaml` when the visible structure changes.

### 13.5 AI Agent Skill Workflows

When the user asks for a named skill, slash-command-like workflow, repeated agent behavior, diagnosis, TDD, issue triage, PRD generation, architecture deepening, prototyping, handoff, or skill creation, read `AI_AGENT_SKILLS_PROTOCOL.md` before choosing the workflow.

Default rule:
- Treat skills as operating protocols, not private project context.
- Configure issue tracker, triage labels, and domain docs before publishing issues or PRDs.
- Prefer behavior contracts over file-path instructions in issues and agent briefs.
- Record durable terms and decisions in the project glossary, decision log, or ADRs.
- Keep copied third-party skill text or scripts license-compliant and attributed.

### 13.6 AI Tool Adapter Compatibility

When the user asks to support, compare, or update behavior for Claude Code, Cursor, ChatGPT, Gemini, Copilot, local LLMs, IDE agents, CLI agents, or other AI coding tools, read `AI_TOOL_ADAPTER_COMPATIBILITY_PROTOCOL.md` before changing adapter files or prompt guidance.

Default rule:
- Keep adapter files short and point back to canonical Nexus-APCP files.
- Document observable tool modes, available tools, context loading, verification paths, and drift risks.
- Prefer official docs for current tool behavior.
- Do not copy vendor system prompts, prompt dumps, proprietary tool schemas, prompt-extraction instructions, private model routing notes, or generated prompt bundles.
- Update `TASK_PROGRESS.yaml` when a visible adapter compatibility task is completed.

---

## SECTION 14: BEST PRACTICES AND TIPS

### 14.1 Tips for AI Assistant

```
 DOS:
- Read TASK_PROGRESS before starting each task
- Read internal docs first if there are unknown parts
- Follow patterns in Section 5 when writing code
- Use `AI_AGENT_SKILLS_PROTOCOL.md` before invoking reusable skill workflows
- Use `AI_TOOL_ADAPTER_COMPATIBILITY_PROTOCOL.md` before changing AI tool adapter files or prompt-source guidance
- Use `UPDATE_SYSTEM_RECOMMENDATION_PROTOCOL.md` before suggesting an updater
- Use `FILE_STRUCTURE_REFACTOR_PROTOCOL.md` before reorganizing existing project files
- Use commit format in Section 6.2 when making breaking changes
- Ask user when there is uncertainty (don't guess!)

 DON'TS:
- Don't commit sensitive data to the repo (Section 4)
- Don't ignore design patterns
- Don't establish arbitrary imports (Section 3.3)
- Don't forget to update documentation
- Don't continue old code patterns (refactor them!)
```

### 14.2 Token Budget Management

**Lightweight/fast model**:
```
- Load this file FULL initially (Token cost: ~3000-4000)
- Read TASK_PROGRESS.yaml (Token cost: ~1000)
- Make incremental updates in every request
- Minify outputs of unit tests (debug)
```

**Balanced coding model**:
```
- Load this file FULL
- Read TASK_PROGRESS.yaml + git history
- More detailed error logging
- Full code reviews
```

**Advanced reasoning model**:
```
- Everything + benchmarking
- Full test coverage analysis
- Detailed architectural reviews
```

### 14.3 Code Review Checklist

The model should check this for every PR:

```yaml
Code Review Checklist:
  - Does the code follow patterns in Section 5?
  - Are naming conventions correct?
  - Are imports optimal (no circular dependency)?
  - Were tests written? (80%+ coverage)
  - Is there error handling?
  - Is logging appropriate?
  - Is documentation updated?
  - Are breaking changes documented?
  - Security checks passed? (bandit, safety)
  - Is there a performance regression?
```

---

## SECTION 15: EMERGENCY CONTACTS & ESCALATION

When needed:

```yaml
Escalation:
  - Code Issue / Bug: Create GitHub Issue with [bug] label
  - Architecture Decision: Discuss with Tech Lead via email/Slack
  - Security Concern: Email to [security@example.com] immediately
  - Performance Issue: Create GitHub Issue with [performance] label
  - Deployment Error: Contact DevOps team on Slack #devops-emergency

Support Channels:
  - Email: [support@example.com]
  - Slack: [#project-support]
  - GitHub Issues: [https://github.com/username/project/issues]
  - Office Hours: [day, time, timezone]
```

---

## APPENDIX A: EXAMPLE SCENARIO

### Scenario: New Feature Development (User Profile Update)

```
1 AI ASSISTANT START
   - Read this file (APCP)
   - Read TASK_PROGRESS.yaml
   - Request requirements from user

2 CREATE TASK
   - Create TASK-004: "Implement user profile update API"
   - Add to TASK_PROGRESS.yaml (status: NOT_STARTED)
   - Determine subtasks
   - Set due date

3 CREATE GIT BRANCH
   bash
   git checkout -b feature/user-profile-update
   

4 WRITING CODE (Follow Section 5 patterns)
   a. Write Service:
      - Add update_profile() method to src/services/user_service.py
      - Write input validation
      - Add error handling
      - Write tests
   
   b. Write API Endpoint:
      - Add PUT /users/{id} endpoint to src/api/routes/users.py
      - Add middleware (require_auth)
      - Make response standardized (src/api/responses.py)
   
   c. Tests:
      - Write test in src/tests/unit/test_user_service.py
      - Write test in src/tests/integration/test_user_api.py

5 TAKING CHECKPOINT (Section 6.4)
   bash
   bash scripts/checkpoint.sh
   
6 MAKING COMMIT (Section 6.2 format)
   bash
   git add src/
   git commit -m "feat(user): add profile update endpoint
   
   - Implement PUT /users/{id} endpoint
   - Add input validation with Pydantic
   - Add comprehensive unit and integration tests
   - Update API documentation
   
   Closes #42"
   

7 UPDATE TASK_PROGRESS
   - TASK-004 status: COMPLETED
   - set completion_date
   - update actual_effort
   - add PR link

8 UPDATE DOCUMENTATION
   - Add new endpoint to docs/API.md
   - Update docs/CHANGELOG.md
   - Update README (add to feature list)

9 OPEN PR
   - Title: "feat: User profile update API"
   - Description: Copy commit message
   - Write Close #42
   - Reference related PRs

 AFTER REVIEW
   - Apply feedback
   - Local: git rebase main && git push -f
   - Approved? 
   - Merge to main
   - Final update to TASK_PROGRESS
```

---

## APPENDIX B: VELOCITY TRACKING TEMPLATE

```yaml
# VELOCITY_HISTORY.yaml
# Sprint wise performance tracking

Sprint_1:
  planned_velocity: 8 tasks
  actual_completed: 6 tasks
  completion_rate: 75%
  estimated_effort: 40h
  actual_effort: 38.5h
  accuracy: 96%
  notes: "Good progress, scope creep on TASK-002"

Sprint_2:
  planned_velocity: 8 tasks
  actual_completed: 7 tasks
  completion_rate: 87%
  estimated_effort: 35h
  actual_effort: 36.2h
  accuracy: 97%
  notes: "Better estimation, 1 task carried over"

Trend_Analysis:
  average_velocity: 6.5 tasks/sprint
  velocity_trend: "↗ Improving"
  accuracy: "96% (Good)"
  bottleneck: "Integration testing takes longer than estimated"
  recommendation: "Plan extra 30% buffer for integration testing"
```

---

## APPENDIX C: QUICK REFERENCE CARD (Token-Light)

For quick reference while keeping content minimal:

```
┌─────────────────────────────────────────────────────┐
│ AI PROJECT CONTEXT - QUICK REFERENCE (v1.0)         │
├─────────────────────────────────────────────────────┤
│  FOLDER STRUCTURE                                  │
│ src/core/        → auth, config, database, utils    │
│ src/services/    → business logic                    │
│ src/models/      → data models                       │
│ src/api/         → routes, middleware                │
│ docs/            → documentation                     │
│                                                      │
│  NEVER COMMIT                                      │
│ - API Keys (.env → .env.example)                     │
│ - Passwords, secrets                                 │
│ - Private tokens                                     │
│                                                      │
│  BEFORE COMMITTING                                 │
│ $ bash scripts/checkpoint.sh                         │
│    Tests pass                                       │
│    Code formatted (black, flake8)                   │
│    Security scan (bandit, safety)                   │
│    Type check (mypy)                                │
│                                                      │
│  TASK MANAGEMENT                                   │
│ 1. Read TASK_PROGRESS.yaml                           │
│ 2. Check blockers/dependencies                       │
│ 3. Mark status: →→                              │
│ 4. Update actual_effort                              │
│                                                      │
│  KEY IMPORTS                                       │
│ from src.core.auth import authenticate_user         │
│ from src.core.config import get_config              │
│ from src.core.database import get_db                │
│ from src.services.* import *Service                 │
│                                                      │
│  KEY DOCS                                          │
│ - docs/ARCHITECTURE.md (System design)               │
│ - docs/API.md (Endpoints)                            │
│ - docs/DATABASE.md (Schema)                          │
│ - docs/SETUP.md (Development env)                    │
│                                                      │
│  GIT WORKFLOW                                      │
│ git checkout -b feature/name                         │
│ ... make changes ...                                 │
│ bash scripts/checkpoint.sh                           │
│ git add . && git commit -m "type(scope): message"    │
│ git push origin feature/name                         │
│ Create PR → Review → Merge                           │
│                                                      │
│  MODEL SWITCHING                                   │
│ New Model: Paste full APCP + TASK_PROGRESS.yaml      │
│ Then: "Where were we? Continue from TASK-X"          │
│                                                      │
│  UNCERTAIN? ASK USER FIRST                         │
└─────────────────────────────────────────────────────┘
```

---

## VERSION HISTORY

| Version | Date | Changes | Updated By |
|---------|------|---------|-----------|
| v1.0 | 2024-01-15 | Initial APCP creation | AI Assistant |

---

## FINAL NOTES

**This file is:**
- A reference book (that you will read from beginning to end)
- A system design document (overview of architecture)
- A checklist (before starting tasks)
- An onboarding guide (when switching to a new model)
- A context manager (token efficiency)

**When to use it:**
- Before starting each task
- When switching to a new model
- When making architecture decisions
- When performing code reviews
- When there is uncertainty

**Must be updated regularly:**
- At the end of each sprint
- Upon significant changes
- When adding external services
- When establishing new conventions

---

**Created for AI-Assisted Development**

---

**Questions or Improvements?** 
Please create an issue on GitHub or contact the project manager.

**Last Updated**: [YYYY-MM-DD]
**Maintained By**: AI Assistant & Project Team
**License**: Same as project license
