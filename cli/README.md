# Backend Architect CLI

CLI to install Backend Architect skill for AI coding assistants.

## Installation

```bash
npx backend-architect-cli
```

Or install globally:

```bash
npm install -g backend-architect-cli
backend-architect init
```

## Usage

### Quick Start (Interactive)

```bash
npx backend-architect-cli
```

This will:
1. Auto-detect which AI assistants you have configured
2. Prompt you to select which AI to install for
3. Copy the appropriate skill files

### Specific AI Assistant

```bash
npx backend-architect-cli init --ai claude
npx backend-architect-cli init --ai cursor
npx backend-architect-cli init --ai gemini
npx backend-architect-cli init --ai all
```

### Available AI Types

- `claude` - Claude Code (.claude/skills/)
- `cursor` - Cursor (.cursor/commands/)
- `windsurf` - Windsurf (.windsurf/workflows/)
- `antigravity` - Antigravity (.agent/workflows/)
- `copilot` - GitHub Copilot (.github/prompts/)
- `kiro` - Kiro (.kiro/steering/)
- `codex` - Codex (.codex/skills/)
- `roocode` - RooCode (.roo/commands/)
- `qoder` - Qoder (.qoder/rules/)
- `gemini` - Gemini CLI (.gemini/skills/)
- `codebuddy` - CodeBuddy (.codebuddy/commands/)
- `all` - Install for all AI assistants

## Development

```bash
cd cli
bun install
bun run dev
```

Build for distribution:

```bash
bun run build
```
