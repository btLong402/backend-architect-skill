---
description: Backend architecture intelligence - search architectures, databases, security, languages, and platform tools
---

# Backend Architect Skill

Search the backend architecture knowledge base for recommendations.

## Prerequisites
- Python 3.8+ (standard library only)

## How to Use This Workflow

### Step 1: Analyze User Requirements
Identify from user request:
- **Product type**: SaaS, E-commerce, Fintech, Chat, AI Agent, etc.
- **Scale**: Startup / Enterprise / Global
- **Stack preference**: Go, Python, Node, Java, .NET, Rust

### Step 2: Search Relevant Domains

```bash
python3 .agent/workflows/scripts/search.py "<query>" --domain <domain>
```

**Domains**: architecture, database, security, product, language, api, naming, error, platform

**Example searches**:
```bash
# Product recommendations
python3 .agent/workflows/scripts/search.py "ecommerce" --domain product

# Architecture pattern
python3 .agent/workflows/scripts/search.py "microservices" --domain architecture

# Database selection
python3 .agent/workflows/scripts/search.py "postgresql" --domain database

# Security guidelines
python3 .agent/workflows/scripts/search.py "injection" --domain security
```

### Step 3: Stack-Specific Guidelines

```bash
python3 .agent/workflows/scripts/search.py "<query>" --stack <stack>
```

**Stacks**: go, python, node, java, dotnet, rust

---

## Quick Reference

### Architecture Decision
| Team Size | Recommended |
|-----------|-------------|
| < 20 devs | Modular Monolith |
| > 50 devs | Microservices |
| Variable traffic | Serverless |
| Real-time | Event-Driven |

### Database Selection
| Use Case | Recommended |
|----------|-------------|
| OLTP | PostgreSQL |
| High-write | Cassandra, ClickHouse |
| Caching | Redis |
| Vector/AI | pgvector, Qdrant |

### API Pattern
| Use Case | Recommended |
|----------|-------------|
| Public API | REST |
| Complex queries | GraphQL |
| Internal services | gRPC |
| Real-time | WebSocket |
