# pymqpcf

Python library for IBM MQ PCF automation (bootstrap placeholder).

## Table of Contents

- [Purpose](#purpose)
- [Status](#status)
- [Repository layout](#repository-layout)
- [Branching and releases](#branching-and-releases)
- [Versioning](#versioning)
- [Validation](#validation)

## Purpose

Establish a reusable Python library for PCF command handling. This repository
is bootstrapped with minimal structure and is expected to evolve as the API is
implemented.

## Status

Pre-release. No published artifacts yet.

## Repository layout

```text
docs/
scripts/
src/
tests/
```

## Branching and releases

- `develop` is the integration branch.
- Release branches are named `release/<major>.<minor>.x`.
- Releases are tagged on release branches.

## Versioning

- Uses the library versioning scheme (PEP 440).
- `MAJOR.MINOR.PATCH` is stored in `pyproject.toml`.
- Pre-releases use standard pre-release identifiers.

## Validation

- Full validation: `python3 scripts/dev/validate_local.py`
- Docs-only validation: `python3 scripts/dev/validate_docs.py`
