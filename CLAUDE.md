# Backend Architect Skill

This repository contains an AI skill for backend architecture recommendations.

## Quick Start

Search the knowledge base:

```bash
python3 .shared/backend-architect-skill/scripts/search.py "<query>" --domain <domain>
```

**Domains**: architecture, database, security, product, language, api, naming, error, platform  
**Stacks**: go, python, node, java, dotnet, rust

## Examples

```bash
# Product recommendations
python3 .shared/backend-architect-skill/scripts/search.py "ecommerce" --domain product

# Architecture pattern
python3 .shared/backend-architect-skill/scripts/search.py "microservices" --domain architecture

# Database selection
python3 .shared/backend-architect-skill/scripts/search.py "postgresql" --domain database

# Stack-specific
python3 .shared/backend-architect-skill/scripts/search.py "orm" --stack python
```

## Data Files

- `architectures.csv` - 13 architecture patterns
- `databases.csv` - 19 database technologies
- `security.csv` - 14 security guidelines (OWASP 2025)
- `product.csv` - 15 product type recommendations
- `languages.csv` - 13 languages/frameworks
- `api-patterns.csv` - 7 API patterns
- `naming-conventions.csv` - 28 naming rules
- `error-codes.csv` - 32 error codes
- `platform.csv` - 18 DevOps tools
- `stacks/` - Stack-specific guidelines (Go, Python, Node, Java, .NET, Rust)
