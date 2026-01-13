---
description: Backend architecture intelligence - search architectures, databases, security, languages
---

# Backend Architect Skill

Search the backend architecture knowledge base for recommendations.

## How to Use

```bash
python3 .cursor/commands/scripts/search.py "<query>" --domain <domain>
```

**Domains**: architecture, database, security, product, language, api, naming, error, platform
**Stacks**: go, python, node, java, dotnet, rust

## Example Searches

```bash
# Product recommendations
python3 .cursor/commands/scripts/search.py "ecommerce" --domain product

# Architecture pattern  
python3 .cursor/commands/scripts/search.py "microservices" --domain architecture

# Stack-specific
python3 .cursor/commands/scripts/search.py "orm" --stack python
```

## Quick Reference

| Team Size | Architecture |
|-----------|--------------|
| < 20 | Modular Monolith |
| > 50 | Microservices |
| Variable | Serverless |

| Use Case | Database |
|----------|----------|
| OLTP | PostgreSQL |
| High-write | Cassandra |
| Cache | Redis |
| AI/Vector | pgvector |
