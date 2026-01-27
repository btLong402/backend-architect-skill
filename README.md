<div align="center">

# 🏗️ Backend Architect Skill

**Expert architectural intelligence for building professional, scalable, and secure backend systems.**

[![npm version](https://img.shields.io/npm/v/backend-architect-cli.svg)](https://www.npmjs.com/package/backend-architect-cli)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
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

| Assistant | Install Type | Structure |
|-----------|--------------|-----------|
| **Claude Code** | Full | `.claude/skills/backend-architect/` |
| **Codex** | Full | `.codex/skills/backend-architect/` |
| **Continue** | Full | `.continue/skills/backend-architect/` |
| **Antigravity** | Full | `.agent/skills/backend-architect/` |
| **Gemini CLI** | Full | `.gemini/skills/backend-architect/` |
| **OpenCode** | Full | `.opencode/skills/backend-architect/` |
| **CodeBuddy** | Full | `.codebuddy/skills/backend-architect/` |
| **Trae** | Full | `.trae/skills/backend-architect/` |
| **Cursor** | Reference | `.cursor/commands/` + `.shared/` |
| **Windsurf** | Reference | `.windsurf/skills/` + `.shared/` |
| **GitHub Copilot** | Reference | `.github/prompts/` + `.shared/` |
| **Kiro** | Reference | `.kiro/steering/` + `.shared/` |
| **Qoder** | Reference | `.qoder/skills/` + `.shared/` |
| **Roo Code** | Reference | `.roo/commands/` + `.shared/` |

**Install Types:**
- **Full**: Data và scripts nằm trong skill folder (standalone)
- **Reference**: Skill file trỏ đến `.shared/` folder chung (tiết kiệm dung lượng)

---

## 🛠️ Usage

### Skill Mode (Auto-activate)

**Supported:** Claude Code, Codex, Continue, Antigravity, Gemini CLI, OpenCode, CodeBuddy, Trae

The skill activates automatically when you request architectural work. Just chat naturally:

```
Design a scalable backend for a real-time IoT telemetry system using Go and Kafka.
```

> **Trae**: Switch to **SOLO** mode first. The skill will activate for architecture requests.

### Workflow Mode (Slash Command)

**Supported:** Cursor, Windsurf, GitHub Copilot, Kiro, Qoder, Roo Code

Use the slash command to invoke the skill:

```
/backend-architect Create a microservices design for a payment processing system
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

## � Acknowledgements

Inspired by [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) by [@viettranx](https://github.com/viettranx). The architecture, CLI design, and multi-platform skill system are adapted from this excellent project.

---

## �📝 Changelog

### v2.1.0 (2026-01-27)
- **Type Safety**: Full Python type hints for Pylance strict mode compatibility
- **Python 3.10+**: Updated minimum Python version (uses modern union syntax `str | None`)
- **Code Quality**: Removed unused imports, fixed all linter warnings

### v2.0.0
- Initial public release with 14 AI assistant support
- BM25-based semantic search engine
- Architecture System Generator

---

<div align="center">

**Built for architects, by architects. Happy coding!**

</div>
