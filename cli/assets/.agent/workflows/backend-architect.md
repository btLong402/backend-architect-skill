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

### Step 3: Verify Latest Versions (CRITICAL)

**Before implementing**, always verify the latest stable versions of technologies to avoid build failures due to AI knowledge cutoff.

**Required checks**:
```
# Use web search to verify latest versions
search_web "latest stable version <technology> 2026"
```

**Technologies to verify**:
| Category | Examples |
|----------|----------|
| Language Runtime | Go, Python, Node.js, Java, .NET, Rust |
| Base Docker Images | golang:alpine, python:slim, node:alpine |
| Frameworks | Gin, Echo, FastAPI, NestJS, Spring Boot |
| Databases | PostgreSQL, MySQL, MongoDB, Redis |
| Tools | Docker Compose, Kubernetes, Terraform |

**Where to update versions**:
- `Dockerfile` - Base image tags (e.g., `FROM golang:1.24-alpine`)
- `go.mod` - Go version directive
- `package.json` - Node.js engines field
- `pyproject.toml` / `requirements.txt` - Python version
- `docker-compose.yml` - Service image versions
- `.tool-versions` - asdf/mise version management

> **Example**: If AI suggests `golang:1.23-alpine` but web search shows Go 1.24 is latest stable, update to `golang:1.24-alpine`.

---

### Step 4: Stack-Specific Guidelines

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
