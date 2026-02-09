# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Documentation Strategy

This repository uses two complementary approaches for AI agent guidance:

- **AGENTS.md**: Generic AI agent instructions using include directives to force documentation indexing. Contains canonical standards references, shared skills loading, and user override support.
- **CLAUDE.md** (this file): Claude Code-specific guidance with prescriptive commands, architecture details, and development workflows optimized for `/init`.

### Integration Approach

**For Claude Code** (`/init` command):
1. Read CLAUDE.md (this file) first for optimized quick-start guidance
2. Process include directives to load repository standards
3. Reference AGENTS.md for shared skills and canonical standards location
4. Apply layered standards: canonical → project-specific → user overrides

**For other AI agents** (Codex, generic LLMs):
1. Read AGENTS.md first as the primary entry point
2. Process include directives to load all referenced documentation
3. Resolve canonical standards repo path (local or GitHub)
4. Load shared skills from standards repo
5. Apply user overrides from `~/AGENTS.md` if present

**Key differences**:
- **CLAUDE.md**: Prescriptive, command-focused, optimized for `/init`
- **AGENTS.md**: Declarative, include-directive-driven, forces full documentation indexing

Both files share the same underlying standards via include directives, ensuring consistency across all AI agents working in this repository.

### Best Practices for Dual-File Approach

**What goes in AGENTS.md**:
- Include directives for documentation indexing
- Canonical standards repository references
- Shared skills loading instructions
- User override mechanisms
- Minimal, declarative content

**What goes in CLAUDE.md**:
- Claude Code-specific quick-start commands
- Detailed architecture and design patterns
- Implementation notes and common workflows
- Integration guidance between the two files
- More verbose, prescriptive content

**What goes in neither (use includes instead)**:
- Repository standards (keep in `docs/repository-standards.md`)
- Canonical standards (reference external repo)
- Project-specific conventions (keep in referenced docs)

**Maintenance strategy**:
- Update standards in source files, not in AGENTS.md or CLAUDE.md
- Use include directives to pull in shared content
- Keep AGENTS.md minimal and CLAUDE.md focused on Claude Code workflows
- Test both entry points when updating documentation structure

<!-- include: docs/standards-and-conventions.md -->
<!-- include: docs/repository-standards.md -->

## Project Overview

`pymqpcf` is a Python library for IBM MQ PCF (Programmable Command Format) automation. The project provides Python bindings for constructing, sending, and parsing PCF commands against IBM MQ queue managers.

**Status**: Pre-release (bootstrap)

**Canonical Standards**: This repository follows standards at https://github.com/wphillipmoore/standards-and-conventions (local path: `../standards-and-conventions` if available)

## Development Commands

### Environment Setup

```bash
# Install dependencies and sync environment
uv sync --group dev
```

### Validation

```bash
# Run full validation suite (matches CI hard gates)
uv run python3 scripts/dev/validate_local.py

# Docs-only validation (requires markdownlint on PATH)
uv run python3 scripts/dev/validate_docs.py
```

The full validation suite includes:
- Virtual environment validation
- Dependency specification validation
- Version validation
- Lock file verification
- Security audit (pip-audit)
- Ruff linting and formatting
- mypy type checking
- ty type checking
- pytest with 100% coverage requirement

### Testing

```bash
# Run tests with coverage
uv run pytest --cov=pymqpcf --cov-report=term-missing --cov-branch --cov-fail-under=100

# Run specific test file
uv run pytest tests/test_smoke.py
```

### Linting and Formatting

```bash
# Run Ruff linter
uv run ruff check

# Run Ruff formatter (check only)
uv run ruff format --check .

# Run Ruff formatter (fix)
uv run ruff format .

# Run mypy type checker
uv run mypy src/

# Run ty type checker
uv run ty check src
```

### Local MQ Container

For PCF command validation against a real queue manager:

```bash
# Start the containerized MQ queue manager
./scripts/dev/mq_start.sh

# Seed deterministic test objects
./scripts/dev/mq_seed.sh

# Verify REST-based MQSC responses
./scripts/dev/mq_verify.sh

# Stop the queue manager
./scripts/dev/mq_stop.sh

# Reset to clean state (removes data volume)
./scripts/dev/mq_reset.sh
```

Container details:
- Queue manager: `QM1`
- Ports: `1414` (MQ listener), `9443` (mqweb console + REST API)
- Admin credentials: `mqadmin` / `mqadmin`
- Read-only credentials: `mqreader` / `mqreader`
- REST base URL: `https://localhost:9443/ibmmq/rest/v2`

## Architecture

### Core Components

**Package** (`src/pymqpcf/`):
- Bootstrap package with minimal structure
- Will provide PCF command construction, transport, and response parsing

### Key Design Patterns

1. **Sister Library**: Companion to `pymqrest` (MQ REST API wrapper)
2. **PCF Focus**: Native PCF command format (vs REST/MQSC in pymqrest)
3. **Shared Standards**: Same repository conventions, tooling, and CI as pymqrest

## Repository Standards Quick Reference

The include directives at the top of this file load the full repository standards. Key highlights for quick reference:

**Pre-flight Checklist**:
- Check current branch: `git status -sb`
- If on `develop`, create `feature/*` branch or get explicit approval
- Enable git hooks: `git config core.hooksPath scripts/git-hooks`

**Python Invocation**: Always use `uv run python3 <script>`

**Tooling**: `uv` version `0.9.26`

**Code Quality**: Ruff (all rules), mypy (strict), 100% test coverage, Python 3.14+

**Repository Profile**: library, library-release branching, artifact-publishing

See `docs/repository-standards.md` for complete details.

## Documentation Indexing Strategy

This repository uses `<!-- include: path/to/file.md -->` directives to force documentation indexing. When you encounter these directives:

1. **Read the referenced files** to understand the full context
2. **Apply layered standards** in order:
   - Canonical standards (from `standards-and-conventions` repo)
   - Project-specific standards (`docs/repository-standards.md`)
   - User overrides (`~/AGENTS.md` if present)
3. **Load shared skills** from `<standards-repo-path>/skills/**/SKILL.md`

The include directives appear in:
- `AGENTS.md` - Includes repository standards and conventions
- `CLAUDE.md` - Includes same standards for Claude Code
- `docs/standards-and-conventions.md` - Includes canonical standards reference

This approach ensures all AI agents (Codex, Claude, etc.) have access to the same foundational documentation.

## Documentation Structure

- `README.md` - Project overview and quick start
- `AGENTS.md` - Generic AI agent instructions with include directives
- `CLAUDE.md` - This file, Claude Code-specific guidance
- `docs/mq-container-local-dev.md` - Local development with MQ container
- `docs/repository-standards.md` - Project-specific standards (included from AGENTS.md)
- `docs/standards-and-conventions.md` - Canonical standards reference (includes external repo)

## Key References

**Canonical Standards**: https://github.com/wphillipmoore/standards-and-conventions
- Local path (preferred): `../standards-and-conventions`
- Load all skills from: `<standards-repo-path>/skills/**/SKILL.md`

**External Documentation**:
- IBM MQ 9.4 PCF command reference
- IBM MQ 9.4 administrative REST API (sister library: pymqrest)

**User Overrides**: `~/AGENTS.md` (optional, applied if present and readable)

## Temporary Workarounds

**Codex Branch Deletion**: The Codex execution harness may reject `git branch -d` even with `sandbox_mode = "danger-full-access"`. Workaround: use `git update-ref -d refs/heads/<branch>` when cleanup is required.
