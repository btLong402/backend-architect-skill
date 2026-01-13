# Backend Architect Skill - Architecture Intelligence

Searchable database of backend architectures, databases, security guidelines, language best practices, API patterns, and platform engineering recommendations.

## Prerequisites

- Python 3.8+
- No external dependencies (uses only standard library)

## How to Use This Skill

### Step 1: Analyze User Requirements
Extract key information from user request:
- **Product type**: SaaS, E-commerce, Fintech, Social, Chat, IoT, AI Agent, etc.
- **Scale requirements**: Startup (<20 devs), Enterprise (>50 devs), Global scale
- **Critical features**: Real-time, High-write, ACID transactions, AI/ML integration
- **Preferred stack**: Go, Python, Node, Java, .NET, Rust

### Step 2: Search Relevant Domains
Use `search.py` multiple times to gather comprehensive information:

```bash
python3 .claude/skills/backend-architect/scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]
```

**Recommended search order:**

1. **Product** - Get architecture recommendations for product type
2. **Architecture** - Get detailed architecture pattern (components, trade-offs)
3. **Database** - Get database recommendations for data model
4. **Security** - Get security guidelines (OWASP, API Security)
5. **Language** - Get language/framework recommendations
6. **API** - Get API pattern recommendations (REST, GraphQL, gRPC)
7. **Naming** - Get naming conventions for the stack
8. **Error** - Get error handling patterns
9. **Platform** - Get DevOps/Platform engineering tools
10. **Stack** - Get stack-specific guidelines

### Step 3: Stack Guidelines
Get stack-specific recommendations:

```bash
python3 .claude/skills/backend-architect/scripts/search.py "<keyword>" --stack <stack>
```

Available stacks: `go`, `python`, `node`, `java`, `dotnet`, `rust`

---

## Search Reference

### Available Domains

| Domain | Use For | Example Keywords |
|--------|---------|------------------|
| `architecture` | System architecture patterns | microservices, modular monolith, serverless, CQRS |
| `database` | Database selection | postgresql, mongodb, redis, vector, timescale |
| `security` | Security best practices | OWASP, injection, auth, encryption, secrets |
| `product` | Product-specific recommendations | ecommerce, saas, fintech, chat, iot, ai agent |
| `language` | Language/framework selection | rust, go, python, node, java, dotnet |
| `api` | API design patterns | rest, graphql, grpc, websocket, mcp |
| `naming` | Naming conventions | python, go, sql, graphql, redis |
| `error` | Error handling patterns | http, grpc, postgres, mongodb, oauth |
| `platform` | DevOps/Platform tools | kubernetes, terraform, argocd, vault |

### Available Stacks

| Stack | Focus |
|-------|-------|
| `go` | Gin/Echo, GORM, Testcontainers, Cloud-native |
| `python` | FastAPI/Django, SQLAlchemy, Pytest, AI/ML |
| `node` | NestJS/Fastify, Prisma, TypeScript, Full-stack |
| `java` | Spring Boot/Quarkus, Virtual Threads, Enterprise |
| `dotnet` | ASP.NET Core, EF Core, Minimal APIs, Cloud-native |
| `rust` | Axum/Actix, SQLx, High-performance, Systems |

---

## Example Workflow

**User request**: "Build a real-time chat application"

```bash
# 1. Get product recommendations
python3 .claude/skills/backend-architect/scripts/search.py "chat messaging" --domain product

# 2. Get architecture pattern
python3 .claude/skills/backend-architect/scripts/search.py "real-time event driven" --domain architecture

# 3. Get database recommendations
python3 .claude/skills/backend-architect/scripts/search.py "high write throughput cassandra" --domain database

# 4. Get language recommendations
python3 .claude/skills/backend-architect/scripts/search.py "elixir actor model" --domain language

# 5. Get API pattern
python3 .claude/skills/backend-architect/scripts/search.py "websocket real-time" --domain api

# 6. Get security guidelines
python3 .claude/skills/backend-architect/scripts/search.py "api security rate limit" --domain security
```

---

## Tips for Better Results

- Search multiple domains for comprehensive recommendations
- Cross-reference product recommendations with architecture patterns
- Always check security guidelines before finalizing design
- Use stack-specific search for implementation details

---

## Common Rules for Professional Backend

### Database Selection
- **OLTP (transactions)**: PostgreSQL, MySQL, CockroachDB
- **High-write (logs/events)**: Cassandra, ScyllaDB, ClickHouse
- **Caching**: Redis, Memcached, Dragonfly
- **Vector (AI/RAG)**: pgvector, Qdrant, Pinecone
- **Time-series**: TimescaleDB, InfluxDB

### Architecture Decision Matrix
- **Team < 20**: Modular Monolith
- **Team > 50**: Microservices
- **Unpredictable traffic**: Serverless
- **Real-time**: Event-Driven
- **AI/LLM**: Agentic Architecture

### API Pattern Selection
- **Public API**: REST (universal compatibility)
- **Complex frontend**: GraphQL (flexible queries)
- **Internal services**: gRPC (performance)
- **Real-time bidirectional**: WebSocket
- **AI integration**: MCP (Model Context Protocol)

---

## Pre-Implementation Checklist

### Architecture Quality
- [ ] Is the architecture appropriate for team size?
- [ ] Are trade-offs clearly understood?
- [ ] Is data consistency model defined?

### Security
- [ ] OWASP Top 10 addressed?
- [ ] API security (rate limiting, auth)?
- [ ] Secrets management configured?

### Scalability
- [ ] Database bottlenecks identified?
- [ ] Horizontal scaling strategy defined?
- [ ] Caching layer planned?

### Observability
- [ ] Structured logging configured?
- [ ] Distributed tracing enabled?
- [ ] Metrics and alerting set up?
