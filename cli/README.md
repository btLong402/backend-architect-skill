<div align="center">

# 🏗️ Backend Architect CLI

**The official installer for the Backend Architect Skill - Bring architecture intelligence to your favorite AI coding assistant.**

[![npm version](https://img.shields.io/npm/v/backend-architect-cli.svg)](https://www.npmjs.com/package/backend-architect-cli)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/btLong402/backend-architect-skill/blob/main/LICENSE)
[![Downloads](https://img.shields.io/npm/dm/backend-architect-cli.svg)](https://www.npmjs.com/package/backend-architect-cli)

</div>

---

## 🌟 Overview

`backend-architect-cli` is a powerful initialization tool that sets up the **Backend Architect Skill** for various AI coding assistants. It ensures your AI has access to a deep knowledge base of architectural patterns, database selections, security guidelines, and professional best practices.

## 🚀 Quick Start

Initialize for your active project in one command:

```bash
npx backend-architect-cli
```

*The CLI will automatically detect your project structure and offer to install for the appropriate AI assistants.*

---

## 🛠️ Features

- **Auto-Detection**: Smartly identifies existing configurations for Claude, Cursor, Windsurf, etc.
- **Interactive Setup**: Simple, user-friendly prompts to guide the installation.
- **Multi-AI Support**: 14 AI assistants supported. Install for all at once with `--ai all`.
- **Template-Based Generation**: Fast local generation without network dependency.
- **Version Management**: Check available versions and update with `versions` and `update` commands.
- **Shared Resources**: `.shared/` folder for efficient data/scripts reuse across platforms.
- **Global Installation**: Optional global install for convenience.

---

## 📦 Installation

### Global Install

```bash
# Install the package globally
npm install -g backend-architect-cli

# Run the interactive setup anywhere
backend-architect

# Or run with specific commands
backend-architect init --ai all
```

Once installed globally, the `backend-architect` command is available system-wide. You can use it in any project directory:

```bash
# Interactive setup
backend-architect

# Specific AI setup
backend-architect init --ai claude
backend-architect init --ai cursor
backend-architect init --ai gemini
backend-architect init --ai windsurf
backend-architect init --ai roocode
backend-architect init --ai copilot
backend-architect init --ai kiro
backend-architect init --ai all
```

### Specific AI Installation

You can skip the interactive mode by specifying target assistants:

```bash
# Claude Code (.claude/skills/)
npx backend-architect-cli init --ai claude

# Cursor (.cursor/commands/)
npx backend-architect-cli init --ai cursor

# Gemini CLI (.gemini/skills/)
npx backend-architect-cli init --ai gemini

# Windsurf (.windsurf/workflows/)
npx backend-architect-cli init --ai windsurf

# RooCode / RooCline (.roo/commands/)
npx backend-architect-cli init --ai roocode

# GitHub Copilot (.github/skills/)
npx backend-architect-cli init --ai copilot

# VS Code (.github/skills/)
npx backend-architect-cli init --ai vscode

# Kiro AI (.kiro/steering/)
npx backend-architect-cli init --ai kiro

# CodeBuddy (.codebuddy/commands/)
npx backend-architect-cli init --ai codebuddy

# Qoder (.qoder/rules/)
npx backend-architect-cli init --ai qoder

# Trae AI (.trae/rules/)
npx backend-architect-cli init --ai trae

# OpenCode (.opencode/prompts/)
npx backend-architect-cli init --ai opencode

# Continue AI (.continue/prompts/)
npx backend-architect-cli init --ai continue

# All 14 assistants at once
npx backend-architect-cli init --ai all
```

### Additional Commands

```bash
# Check available versions
npx backend-architect-cli versions

# Update to latest version
npx backend-architect-cli update

# Use legacy ZIP-based installation
npx backend-architect-cli init --ai claude --legacy
```

---

## 🤖 Supported AI Assistants

| Assistant | Location | Description |
|-----------|----------|-------------|
| **Claude Code** | `.claude/skills/` | Integrated AI skill definitions |
| **Cursor** | `.cursor/commands/` + `.shared/` | Custom terminal commands |
| **Windsurf** | `.windsurf/workflows/` + `.shared/` | AI-driven workflows |
| **Antigravity** | `.agent/skills/` + `.shared/` | Advanced agentic skills |
| **Copilot** | `.github/skills/` | Custom GitHub Copilot skills |
| **VS Code** | `.github/skills/` | VS Code AI skills |
| **Gemini CLI** | `.gemini/skills/` + `.shared/` | Google Gemini skill extensions |
| **RooCode** | `.roo/commands/` + `.shared/` | RooCode custom commands |
| **Kiro** | `.kiro/steering/` + `.shared/` | Kiro AI steering files |
| **Qoder** | `.qoder/rules/` + `.shared/` | Qoder custom rules |
| **CodeBuddy** | `.codebuddy/commands/` + `.shared/` | CodeBuddy terminal skills |
| **Codex** | `.codex/skills/` + `.shared/` | Codex skill definitions |
| **Trae** | `.trae/rules/` + `.shared/` | Trae AI custom rules |
| **OpenCode** | `.opencode/prompts/` + `.shared/` | OpenCode prompt templates |
| **Continue** | `.continue/prompts/` + `.shared/` | Continue AI prompt integration |

---

## 💻 Development

Interested in contributing or running locally?

```bash
# Clone the repository
git clone https://github.com/btLong402/backend-architect-skill.git
cd cli

# Install dependencies
bun install

# Run in development mode
bun run dev

# Build and sync assets
bun run build
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/btLong402/backend-architect-skill/blob/main/LICENSE) file for details.

---

## 📝 Changelog

### v2.2.0 (2026-02-06)
- **VS Code 1.109 Support**: GitHub Copilot and VS Code now use `.github/skills/` format
- **Breaking Change**: Prompts renamed to Skills for Copilot/VS Code platforms
- **Added**: VS Code as standalone platform option

### v2.1.0 (2026-01-27)
- **Type Safety**: Full Python type hints for Pylance strict mode
- **Python 3.10+**: Minimum Python version updated
- **Code Quality**: Removed unused imports, fixed linter warnings

### v2.0.0
- Initial release with 14 AI assistant support

---

<div align="center">

**[GitHub](https://github.com/btLong402/backend-architect-skill) | [npm](https://www.npmjs.com/package/backend-architect-cli)**

</div>
