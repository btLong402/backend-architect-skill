
## Quick Reference

### Common Search Commands

```bash
# Architecture patterns
python3 {{SCRIPT_PATH}} "microservices" --domain architecture
python3 {{SCRIPT_PATH}} "event-driven" --domain architecture
python3 {{SCRIPT_PATH}} "CQRS saga" --domain architecture

# Database patterns
python3 {{SCRIPT_PATH}} "postgresql sharding" --domain database
python3 {{SCRIPT_PATH}} "mongodb schema" --domain database

# Security patterns
python3 {{SCRIPT_PATH}} "oauth jwt" --domain security
python3 {{SCRIPT_PATH}} "rate-limiting" --domain security

# Stack-specific
python3 {{SCRIPT_PATH}} "api patterns" --stack node
python3 {{SCRIPT_PATH}} "concurrency" --stack go
```

### Domain Quick Guide

| Need | Search |
|------|--------|
| System design | `--domain architecture` |
| Database choice | `--domain database` |
| Security patterns | `--domain security` |
| Performance | `--domain scaling` |
| API design | `--domain api` |
| Message queues | `--domain messaging` |
| Caching strategy | `--domain caching` |
| Observability | `--domain monitoring` |
