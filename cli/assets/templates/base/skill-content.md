# {{TITLE}}

{{DESCRIPTION}}
{{QUICK_REFERENCE}}
## Prerequisites

Check if Python is installed:

```bash
python3 --version || python --version
```

If Python is not installed, install it based on your OS:

**macOS:**
```bash
brew install python3
```

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install python3
```

**Windows:**
```powershell
winget install Python.Python.3.12
```

---

## How to Use This {{SKILL_OR_WORKFLOW}}

When user requests backend architecture work (design, build, create, implement, review, fix, improve), follow this workflow:

### Step 1: Analyze User Requirements

Extract key information from user request:
- **System type**: Microservices, Monolith, Event-driven, Serverless, etc.
- **Scale requirements**: Startup, Mid-size, Enterprise
- **Domain**: E-commerce, Fintech, Healthcare, SaaS, Social, Gaming, etc.
- **Stack**: Node.js, Python, Go, Java, Rust, .NET

### Step 2: Search Architecture Recommendations

Use the search script to find relevant patterns and best practices:

```bash
python3 {{SCRIPT_PATH}} "<keywords>" --domain <domain>
```

**Available domains:**
- `architecture` - System architecture patterns (microservices, event-driven, CQRS)
- `database` - Database selection and design patterns
- `security` - Security best practices and authentication
- `scaling` - Scaling strategies and performance optimization
- `api` - API design patterns and best practices
- `messaging` - Message queues and event streaming
- `caching` - Caching strategies and implementation
- `monitoring` - Observability, logging, and alerting

**Examples:**
```bash
# Find microservices patterns for e-commerce
python3 {{SCRIPT_PATH}} "microservices ecommerce" --domain architecture

# Database recommendations for high-traffic system
python3 {{SCRIPT_PATH}} "high traffic read-heavy" --domain database

# Security patterns for fintech
python3 {{SCRIPT_PATH}} "fintech authentication" --domain security
```

### Step 3: Stack-Specific Guidelines

Get implementation-specific best practices:

```bash
python3 {{SCRIPT_PATH}} "<keyword>" --stack <stack>
```

**Available stacks:** `node`, `python`, `go`, `java`, `rust`, `dotnet`

**Examples:**
```bash
# Node.js microservices patterns
python3 {{SCRIPT_PATH}} "microservices api" --stack node

# Go concurrency patterns
python3 {{SCRIPT_PATH}} "concurrency patterns" --stack go

# Python async patterns
python3 {{SCRIPT_PATH}} "async api" --stack python
```

---

## Search Reference

### Available Domains

| Domain | Use For | Example Keywords |
|--------|---------|------------------|
| `architecture` | System design patterns | microservices, event-driven, CQRS, saga, DDD |
| `database` | Database selection and design | PostgreSQL, MongoDB, sharding, replication |
| `security` | Security best practices | OAuth, JWT, encryption, RBAC, rate-limiting |
| `scaling` | Performance and scaling | horizontal, vertical, caching, CDN, load-balancing |
| `api` | API design patterns | REST, GraphQL, gRPC, versioning, pagination |
| `messaging` | Event streaming and queues | Kafka, RabbitMQ, pub-sub, event-sourcing |
| `caching` | Caching strategies | Redis, Memcached, CDN, cache-invalidation |
| `monitoring` | Observability | logging, tracing, metrics, alerting, APM |

### Available Stacks

| Stack | Focus |
|-------|-------|
| `node` | Express, Fastify, NestJS, async patterns |
| `python` | FastAPI, Django, async, type hints |
| `go` | Gin, Echo, concurrency, channels |
| `java` | Spring Boot, microservices, JPA |
| `rust` | Actix, Tokio, memory safety |
| `dotnet` | ASP.NET Core, Entity Framework |

---

## Example Workflow

**User request:** "Design a backend for an e-commerce platform with high traffic"

### Step 1: Analyze Requirements
- System type: Microservices (for scalability)
- Scale: Enterprise-level, high traffic
- Domain: E-commerce
- Stack: Node.js (default)

### Step 2: Search Architecture Patterns

```bash
# Get microservices patterns for e-commerce
python3 {{SCRIPT_PATH}} "ecommerce microservices" --domain architecture

# Get database recommendations
python3 {{SCRIPT_PATH}} "ecommerce high-traffic" --domain database

# Get caching strategies
python3 {{SCRIPT_PATH}} "high-traffic caching" --domain caching
```

### Step 3: Stack Guidelines

```bash
python3 {{SCRIPT_PATH}} "api microservices" --stack node
```

**Then:** Synthesize patterns and implement the architecture.

---

## Common Rules for Professional Backend

### Database Design

| Rule | Do | Don't |
|------|----|----- |
| **Normalization** | Normalize to 3NF, denormalize with purpose | Over-normalize or ignore normalization |
| **Indexing** | Index frequently queried columns | Index everything blindly |
| **Connection pooling** | Use connection pools | Create new connections per request |
| **Migrations** | Use versioned migrations | Manual schema changes in production |

### API Design

| Rule | Do | Don't |
|------|----|----- |
| **Versioning** | Use URL or header versioning | Break existing clients |
| **Pagination** | Implement cursor or offset pagination | Return unbounded results |
| **Error handling** | Return consistent error format | Return unstructured errors |
| **Rate limiting** | Implement rate limits | Allow unlimited requests |

### Security

| Rule | Do | Don't |
|------|----|----- |
| **Authentication** | Use industry standards (OAuth2, JWT) | Roll your own auth |
| **Secrets** | Use secret managers | Hardcode credentials |
| **Input validation** | Validate and sanitize all input | Trust user input |
| **HTTPS** | Always use HTTPS | Allow HTTP in production |

### Scaling

| Rule | Do | Don't |
|------|----|----- |
| **Stateless** | Design stateless services | Store session in memory |
| **Caching** | Cache at multiple layers | Cache everything forever |
| **Async processing** | Use queues for heavy tasks | Block on long operations |
| **Database** | Use read replicas for read-heavy | Single database for everything |

---

## Pre-Architecture Checklist

Before designing, verify these requirements:

### Functional
- [ ] Core business requirements documented
- [ ] Data models identified
- [ ] API contracts defined
- [ ] Third-party integrations listed

### Non-Functional
- [ ] Expected traffic/load defined
- [ ] Latency requirements specified
- [ ] Availability SLA determined (99.9%, 99.99%)
- [ ] Data retention policies defined

### Operational
- [ ] Deployment strategy chosen
- [ ] Monitoring requirements defined
- [ ] Backup and recovery plan
- [ ] Security and compliance requirements

---

## Tips for Better Results

1. **Be specific with keywords** - "ecommerce microservices payment" > "backend"
2. **Search multiple domains** - Architecture + Database + Security = Complete design
3. **Use stack flag** - Get implementation-specific patterns
4. **Combine patterns** - Mix and match based on requirements
5. **Consider trade-offs** - Every pattern has pros and cons
6. **Start simple** - Don't over-engineer; scale when needed
