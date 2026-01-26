<div align="center">

# 🏗️ Backend Architect Skill

**Expert architectural intelligence for building professional, scalable, and secure backend systems.**

[![npm version](https://img.shields.io/npm/v/backend-architect-cli.svg)](https://www.npmjs.com/package/backend-architect-cli)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Downloads](https://img.shields.io/npm/dm/backend-architect-cli.svg)](https://www.npmjs.com/package/backend-architect-cli)

[Overview](#-overview) | [Features](#-features) | [Installation](#-installation) | [Usage](#-usage) | [Supported Assistants](#-supported-ai-assistants)

</div>

---

## 🌟 Overview

**Backend Architect Skill** is a comprehensive, searchable intelligence layer for modern backend engineering. It provides AI coding assistants with deep knowledge of architectural patterns, database selections, security standards, and platform engineering best practices.

Whether you're designing a high-traffic e-commerce platform, a real-time fintech application, or a scalable SaaS, this skill ensures your AI partner provides expert-level recommendations based on industry-standard patterns (Clean Architecture, Microservices, Event-Driven, etc.).

---

## 🚀 Features

The knowledge base is built on structured data covering over 100+ architectural components:

- **🏗️ Architecture Patterns**: Modular Monolith, Microservices, Serverless, CQRS, Event-Driven, Clean/Hexagonal, Layered, and more.
- **🗄️ Database Intelligence**: Deep insights into 19+ databases including PostgreSQL, MongoDB, Redis, Cassandra, ClickHouse, and Vector DBs.
- **🛡️ Security First**: Integrated guidelines for OWASP Top 10 (2025), API Security, Container Security, and Secrets Management.
- **📱 Product-Specific Blueprints**: Tailored architectures for E-commerce, SaaS, Fintech, Chat, AI Agents, IoT, and more.
- **💻 Language & Framework Excellence**: Best practices for Rust, Go, Java, Python, Node.js, .NET, and Elixir.
- **🔌 API Design Patterns**: Standardized approaches for REST, GraphQL, gRPC, WebSockets, SSE, and MCP.
- **🛠️ Platform & DevOps**: Infrastructure patterns using Kubernetes, Terraform, ArgoCD, Vault, and OpenTelemetry.
- **📏 Standards & Conventions**: Pre-defined naming conventions and error handling patterns (HTTP, gRPC, DB-specific).

---

## 📦 Installation

### The Quick Way (Recommended)

Bootstrap your project with the official CLI. It automatically detects your environment and installs the skill for your preferred AI assistants.

```bash
npx backend-architect-cli
```

### Global Installation

For frequent use across multiple projects:

```bash
# Install globally
npm install -g backend-architect-cli

# Initialize in any project
backend-architect init

# Check available versions
backend-architect versions

# Update to latest version
backend-architect update
```

---

## 🤖 Supported AI Assistants

Deploy **Backend Architect** to your entire development workflow (14 platforms):

| Assistant | Integration Method | Purpose |
|-----------|---------------------|---------|
| **Claude Code** | `.claude/skills/` | Direct skill execution & environment injection |
| **Cursor** | `.cursor/commands/` + `.shared/` | Custom terminal commands & context indexing |
| **Windsurf** | `.windsurf/workflows/` + `.shared/` | Agentic workflow automation |
| **Antigravity** | `.agent/skills/` + `.shared/` | Advanced multi-step architecture design |
| **Gemini CLI** | `.gemini/skills/` + `.shared/` | Google Gemini native skill extensions |
| **GitHub Copilot** | `.github/prompts/` + `.shared/` | Custom prompt templates & system instructions |
| **RooCode** | `.roo/commands/` + `.shared/` | Specialized custom command integration |
| **Kiro** | `.kiro/steering/` + `.shared/` | Rule-based steering and architectural constraints |
| **Qoder** | `.qoder/rules/` + `.shared/` | Custom rules for Qoder AI |
| **Codex** | `.codex/skills/` + `.shared/` | OpenAI Codex skill definitions |
| **CodeBuddy** | `.codebuddy/commands/` + `.shared/` | CodeBuddy terminal skills |
| **Trae** | `.trae/rules/` + `.shared/` | Trae AI custom rules |
| **OpenCode** | `.opencode/prompts/` + `.shared/` | OpenCode prompt templates |
| **Continue** | `.continue/prompts/` + `.shared/` | Continue AI prompt integration |

---

## 🛠️ Usage

### Workflow-Based (Cursor, Windsurf, Antigravity)
Use the slash command or workflow runner:
```
/backend-architect Create a microservices design for a payment processing system
```

### Skill-Based (Claude Code, Gemini CLI)
The skill activates automatically when you request architectural work. You can also trigger it manually:
```
Design a scalable backend for a real-time IoT telemetry system using Go and Kafka.
```

### Example Prompts
- *"Recommend a database strategy for a multi-tenant SaaS with global users."*
- *"Review my current architecture for OWASP 2025 security compliance."*
- *"Generate a naming convention guide for a new Rust-based backend project."*

---

## 📖 How It Works

1.  **Requirement Analysis**: The AI analyzes your product type, expected scale, and technology preferences.
2.  **Domain Searching**: It searches the specific knowledge domains (Architecture, Security, Database, etc.) within the `.shared/` database.
3.  **Cross-Reference**: Matches your needs against established patterns and trade-offs.
4.  **Actionable Output**: Delivers specific, version-aware implementation guidance with reasoning.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built for architects, by architects. Happy coding!**

</div>
