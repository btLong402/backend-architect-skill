---
mode: 'agent'
description: 'Backend architecture intelligence - search architectures, databases, security, languages'
---

# Backend Architect Skill

Search the backend architecture knowledge base for recommendations.

## REQUIRED: Verify Latest Versions
**Before starting work**, verify the latest stable versions of technologies via web search (e.g., `latest stable version Go 2026`). Update `Dockerfile`, `go.mod`, `package.json` accordingly.

## REQUIRED: Verify Latest Versions
**Before starting work**, verify the latest stable versions of technologies via web search (e.g., `latest stable version Go 2026`). Update `Dockerfile`, `go.mod`, `package.json` accordingly.

## How to Use

```bash
python3 .github/prompts/scripts/search.py "<query>" --domain <domain>
```

**Domains**: architecture, database, security, product, language, api, naming, error, platform
**Stacks**: go, python, node, java, dotnet, rust

## Example Searches

```bash
# Product recommendations
python3 .github/prompts/scripts/search.py "ecommerce" --domain product

# Architecture pattern  
python3 .github/prompts/scripts/search.py "microservices" --domain architecture

# Stack-specific
python3 .github/prompts/scripts/search.py "orm" --stack python
```
