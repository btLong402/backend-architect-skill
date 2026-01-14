---
name: backend-architect
description: Backend architecture intelligence - search architectures, databases, security
---

# Backend Architect Skill

## REQUIRED: Verify Latest Versions
**Before starting work**, verify the latest stable versions of technologies via web search (e.g., `latest stable version Go 2026`). Update `Dockerfile`, `go.mod`, `package.json` with the latest stable versions.

Search the backend architecture knowledge base.

## Usage

```bash
python3 .kiro/steering/scripts/search.py "<query>" --domain <domain>
```

**Domains**: architecture, database, security, product, language, api, naming, error, platform
**Stacks**: go, python, node, java, dotnet, rust

## Examples

```bash
python3 .kiro/steering/scripts/search.py "ecommerce" --domain product
python3 .kiro/steering/scripts/search.py "microservices" --domain architecture
python3 .kiro/steering/scripts/search.py "orm" --stack python
```
