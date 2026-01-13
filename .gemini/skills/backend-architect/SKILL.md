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
python3 .gemini/skills/backend-architect/scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]
```

**Recommended search order:**

1. **Product** - Get architecture recommendations for product type
2. **Architecture** - Get detailed architecture pattern (components, trade-offs)
3. **Database** - Get database recommendations for data model
4. **Security** - Get security guidelines (OWASP, API Security)
5. **Language** - Get language/framework recommendations
6. **API** - Get API pattern recommendations (REST, GraphQL, gRPC)
7. **Stack** - Get stack-specific guidelines

### Step 3: Stack Guidelines

```bash
python3 .gemini/skills/backend-architect/scripts/search.py "<keyword>" --stack <stack>
```

Available stacks: `go`, `python`, `node`, `java`, `dotnet`, `rust`

---

## Search Reference

### Available Domains
| Domain | Use For | Example Keywords |
|--------|---------|------------------|
| `architecture` | System architecture patterns | microservices, modular monolith, serverless |
| `database` | Database selection | postgresql, mongodb, redis, vector |
| `security` | Security best practices | OWASP, injection, auth, encryption |
| `product` | Product-specific recommendations | ecommerce, saas, fintech, chat |
| `language` | Language/framework selection | rust, go, python, node |
| `api` | API design patterns | rest, graphql, grpc, websocket |
| `naming` | Naming conventions | python, go, sql, graphql |
| `error` | Error handling patterns | http, grpc, postgres |
| `platform` | DevOps/Platform tools | kubernetes, terraform, argocd |

### Available Stacks
| Stack | Focus |
|-------|-------|
| `go` | Gin/Echo, Cloud-native |
| `python` | FastAPI/Django, AI/ML |
| `node` | NestJS/Fastify, Full-stack |
| `java` | Spring Boot, Enterprise |
| `dotnet` | ASP.NET Core, Cloud-native |
| `rust` | Axum/Actix, High-performance |

---

## Example Workflow

**User request**: "Build a real-time chat application"

```bash
python3 .gemini/skills/backend-architect/scripts/search.py "chat messaging" --domain product
python3 .gemini/skills/backend-architect/scripts/search.py "real-time event driven" --domain architecture
python3 .gemini/skills/backend-architect/scripts/search.py "high write cassandra" --domain database
python3 .gemini/skills/backend-architect/scripts/search.py "websocket" --domain api
```

---

## Common Rules for Professional Backend

### Database Selection
- **OLTP**: PostgreSQL, MySQL
- **High-write**: Cassandra, ClickHouse
- **Caching**: Redis
- **Vector (AI)**: pgvector, Qdrant

### Architecture Decision
- **Team < 20**: Modular Monolith
- **Team > 50**: Microservices
- **Real-time**: Event-Driven
- **AI/LLM**: Agentic Architecture
