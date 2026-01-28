# 2026-01-21 UV migration log

## Table of Contents

- [Purpose](#purpose)
- [Context](#context)
- [Commands executed](#commands-executed)
- [Notes](#notes)

## Purpose

Record the operational steps used to migrate pymqpcf from Poetry tooling to uv.

## Context

- Repository: pymqpcf
- Branch: feature/uv-migration
- Issue: [wphillipmoore/pymqpcf#2](https://github.com/wphillipmoore/pymqpcf/issues/2)

## Commands executed

```bash
python3 -m venv .venv
source .venv/bin/activate && python3 -m pip install uv==0.9.26

source .venv/bin/activate && uv lock
source .venv/bin/activate && uv export --frozen --format requirements.txt --output-file requirements.txt --no-hashes --no-emit-project
source .venv/bin/activate && uv export --frozen --format requirements.txt --output-file requirements-dev.txt --no-hashes --group dev --no-emit-project

source .venv/bin/activate && uv sync --frozen --group dev

rm poetry.lock
```

## Notes

- uv 0.9.26 is the pinned toolchain version for this migration.
- Dependency groups now use the `dependency-groups` table in `pyproject.toml`.
- Requirements exports are derived from `uv.lock` and remain the audit inputs.
