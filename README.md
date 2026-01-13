<div align="center">

# 🏗️ Backend Architect Skill

**An AI SKILL that provides architecture intelligence for building professional backend systems**

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

## Overview

Backend Architect Skill is a searchable database of backend architectures, databases, security guidelines, language best practices, API patterns, and platform engineering recommendations. It works as a skill/workflow for AI coding assistants (Claude Code, Codex, Cursor, Windsurf, Gemini, Copilot, etc.).

## Features

- **13 Architecture Patterns** - Modular Monolith, Microservices, Serverless, CQRS, Event-Driven, Clean/Hexagonal, and more
- **19 Databases** - PostgreSQL, MongoDB, Redis, Cassandra, ClickHouse, vector DBs, and more
- **14 Security Guidelines** - OWASP Top 10 2025, API Security, Container Security, Secrets Management
- **15 Product Types** - E-commerce, SaaS, Fintech, Chat, AI Agent, IoT, and more
- **13 Languages/Frameworks** - Rust, Go, Java, Python, Node.js, .NET, Elixir, and more
- **7 API Patterns** - REST, GraphQL, gRPC, WebSocket, SSE, tRPC, MCP
- **28 Naming Conventions** - Python, Go, Java, TypeScript, SQL, MongoDB, Redis
- **32 Error Codes** - HTTP, gRPC, PostgreSQL, MongoDB, OAuth2
- **18 Platform Tools** - Kubernetes, Terraform, ArgoCD, Vault, OpenTelemetry
- **6 Stack Guidelines** - Go, Python, Node, Java, .NET, Rust

---

## Installation

### Using CLI (Recommended)

```bash
npx backend-architect-cli
```

Or install globally:

```bash
npm install -g backend-architect-cli
backend-architect init
```

### Install for Specific AI

```bash
npx backend-architect-cli init --ai claude
npx backend-architect-cli init --ai cursor
npx backend-architect-cli init --ai gemini
npx backend-architect-cli init --ai all
```

### Manual Installation

Clone this repository into your project:

```bash
git clone https://github.com/your-username/backend-architect-skill.git
```

---

## Prerequisites

- Python 3.8+ (uses only standard library, no external dependencies)

---

## Usage

### Claude Code

The skill activates automatically when you request backend architecture work. Just chat naturally:

```
Design a backend for an e-commerce platform
```

### Cursor / Windsurf / Antigravity

Use the slash command to invoke the skill:

```
/backend-architect Design a backend for an e-commerce platform
```

### GitHub Copilot

Type `/` in chat to see available prompts, then select `backend-architect`:

```
/backend-architect Design a backend for an e-commerce platform
```

### Gemini CLI

The skill activates automatically for backend architecture requests.

```
Design a backend for an e-commerce platform
```

---

## Example Prompts

```
Design a backend for an e-commerce platform with high traffic
Build a real-time chat application backend
Create a microservices architecture for a fintech app
Recommend a database for an IoT telemetry system
What security guidelines should I follow for a SaaS?
```

---

## How It Works

1. **You ask** - Request any backend architecture task (design, recommend, choose, review)
2. **Skill activates** - The AI automatically searches the architecture database
3. **Smart recommendations** - Based on your product type and requirements, it finds the best matching patterns
4. **Implementation guidance** - Provides specific recommendations with trade-offs and best practices

---

## Available Domains

| Domain | Description |
|--------|-------------|
| `architecture` | System architecture patterns (Microservices, Monolith, Serverless) |
| `database` | Database selection and recommendations |
| `security` | OWASP, API Security, Container Security |
| `product` | Product-specific architecture recommendations |
| `language` | Language and framework selection |
| `api` | API design patterns (REST, GraphQL, gRPC) |
| `naming` | Naming conventions for different languages |
| `error` | Error handling patterns and status codes |
| `platform` | DevOps and Platform engineering tools |

---

## License

MIT License - see [LICENSE](LICENSE) for details.

---

<div align="center">

**Made with ❤️ for backend developers**

</div>
