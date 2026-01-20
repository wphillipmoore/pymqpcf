# 2026-01-20 Bootstrap Log

## Table of Contents
- [Purpose](#purpose)
- [Assumptions](#assumptions)
- [Commands executed](#commands-executed)
- [Manual edits](#manual-edits)

## Purpose
Record the exact bootstrap steps used to create the `pymqpcf` repository.

## Assumptions
- Repository created under the `wphillipmoore` GitHub account.
- Default branch is `develop`.
- Python virtual environment created at `.venv`.

## Commands executed
```
mkdir -p /Users/pmoore/dev/github/pymqpcf
git init -b develop

mkdir -p /Users/pmoore/dev/github/pymqpcf/.github/ISSUE_TEMPLATE \
  /Users/pmoore/dev/github/pymqpcf/.github/workflows \
  /Users/pmoore/dev/github/pymqpcf/docs/decisions \
  /Users/pmoore/dev/github/pymqpcf/docs/development \
  /Users/pmoore/dev/github/pymqpcf/docs/operations \
  /Users/pmoore/dev/github/pymqpcf/scripts/dev \
  /Users/pmoore/dev/github/pymqpcf/src/pymqpcf \
  /Users/pmoore/dev/github/pymqpcf/tests

cp /Users/pmoore/dev/github/pymqrest/.gitignore /Users/pmoore/dev/github/pymqpcf/.gitignore
cp /Users/pmoore/dev/github/standard-actions/.markdownlint.json /Users/pmoore/dev/github/pymqpcf/.markdownlint.json
cp /Users/pmoore/dev/github/standard-actions/LICENSE /Users/pmoore/dev/github/pymqpcf/LICENSE

cat <<'EOF' > /Users/pmoore/dev/github/pymqpcf/README.md
...
EOF

cat <<'EOF' > /Users/pmoore/dev/github/pymqpcf/AGENTS.md
...
EOF

cat <<'EOF' > /Users/pmoore/dev/github/pymqpcf/docs/standards-and-conventions.md
...
EOF

cat <<'EOF' > /Users/pmoore/dev/github/pymqpcf/docs/development/overview.md
...
EOF

cat <<'EOF' > /Users/pmoore/dev/github/pymqpcf/docs/development/environment-and-tooling.md
...
EOF

cat <<'EOF' > /Users/pmoore/dev/github/pymqpcf/docs/development/tooling-dependencies.md
...
EOF

cat <<'EOF' > /Users/pmoore/dev/github/pymqpcf/docs/development/validation.md
...
EOF

cat <<'EOF' > /Users/pmoore/dev/github/pymqpcf/docs/decisions/0001-repo-structure.md
...
EOF

cp /Users/pmoore/dev/github/pymqrest/.github/ISSUE_TEMPLATE/config.yml \
  /Users/pmoore/dev/github/pymqpcf/.github/ISSUE_TEMPLATE/config.yml
cp /Users/pmoore/dev/github/pymqrest/.github/ISSUE_TEMPLATE/issue.yml \
  /Users/pmoore/dev/github/pymqpcf/.github/ISSUE_TEMPLATE/issue.yml
cp /Users/pmoore/dev/github/pymqrest/.github/pull_request_template.md \
  /Users/pmoore/dev/github/pymqpcf/.github/pull_request_template.md
cp /Users/pmoore/dev/github/pymqrest/.github/workflows/ci.yml \
  /Users/pmoore/dev/github/pymqpcf/.github/workflows/ci.yml

cp /Users/pmoore/dev/github/pymqrest/scripts/dev/validate_dependency_specs.py \
  /Users/pmoore/dev/github/pymqpcf/scripts/dev/validate_dependency_specs.py
cp /Users/pmoore/dev/github/pymqrest/scripts/dev/validate_docs.py \
  /Users/pmoore/dev/github/pymqpcf/scripts/dev/validate_docs.py
cp /Users/pmoore/dev/github/pymqrest/scripts/dev/validate_local.py \
  /Users/pmoore/dev/github/pymqpcf/scripts/dev/validate_local.py
cp /Users/pmoore/dev/github/pymqrest/scripts/dev/validate_version.py \
  /Users/pmoore/dev/github/pymqpcf/scripts/dev/validate_version.py

cat <<'EOF' > /Users/pmoore/dev/github/pymqpcf/src/pymqpcf/__init__.py
...
EOF

cat <<'EOF' > /Users/pmoore/dev/github/pymqpcf/tests/test_smoke.py
...
EOF

cat <<'EOF' > /Users/pmoore/dev/github/pymqpcf/pyproject.toml
...
EOF

python3 -m venv .venv
source .venv/bin/activate && poetry lock
source .venv/bin/activate && poetry export -f requirements.txt --output requirements.txt --without-hashes
source .venv/bin/activate && poetry export -f requirements.txt --output requirements-dev.txt --without-hashes --with dev
```

## Manual edits
- Updated coverage target in `.github/workflows/ci.yml` to `pymqpcf`.
- Updated coverage target in `scripts/dev/validate_local.py` to `pymqpcf`.
- Updated the description in `scripts/dev/validate_version.py` to `pymqpcf`.
