#!/usr/bin/env python3
"""
Docs-only validation helper.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

MIN_MARKDOWNLINT_VERSION = "0.41.0"


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run docs-only validation.")
    parser.add_argument(
        "--paths",
        nargs="*",
        default=None,
        help="Optional list of markdown files to validate.",
    )
    return parser.parse_args()


def ensure_project_root() -> None:
    """Fail fast if invoked outside the repository root."""
    if not Path("pyproject.toml").is_file():
        raise SystemExit("Run from the repository root (pyproject.toml missing).")


def gather_default_paths() -> list[str]:
    """Collect default markdown files for docs-only validation."""
    candidates: list[Path] = []
    docs_root = Path("docs")
    if docs_root.exists():
        candidates.extend(docs_root.rglob("*.md"))

    for filename in ("README.md", "CHANGELOG.md"):
        path = Path(filename)
        if path.is_file():
            candidates.append(path)

    unique_paths = sorted(set(candidates))
    return [str(path) for path in unique_paths]


def parse_version(version_output: str) -> tuple[int, int, int] | None:
    """Parse a semantic version from markdownlint output."""
    parts = version_output.strip().split(".")
    if len(parts) != 3 or not all(part.isdigit() for part in parts):
        return None
    return int(parts[0]), int(parts[1]), int(parts[2])


def resolve_markdownlint() -> tuple[str, str]:
    """Resolve markdownlint binary and version."""
    markdownlint = shutil.which("markdownlint")
    if not markdownlint:
        raise SystemExit(
            "markdownlint is required for docs-only validation. "
            f"Install markdownlint >= {MIN_MARKDOWNLINT_VERSION} and ensure it is on PATH."
        )

    version_output = subprocess.run(
        (markdownlint, "--version"), check=True, text=True, capture_output=True
    ).stdout.strip()
    parsed_version = parse_version(version_output)
    if not parsed_version:
        raise SystemExit(
            "Unable to parse markdownlint version output: "
            f"{version_output!r}."
        )

    minimum = parse_version(MIN_MARKDOWNLINT_VERSION)
    if parsed_version < minimum:
        raise SystemExit(
            "markdownlint version too old. "
            f"Expected >= {MIN_MARKDOWNLINT_VERSION}, found {version_output}."
        )
    return markdownlint, version_output


def run_markdownlint(paths: list[str]) -> int:
    """Run markdownlint using the resolved toolchain."""
    markdownlint_cmd, _version = resolve_markdownlint()

    if not paths:
        print("No markdown files found to validate.")
        return 0

    command = (markdownlint_cmd, *paths)
    print(f"Running: {' '.join(command)}")
    return subprocess.run(command).returncode


def main() -> int:
    arguments = parse_arguments()
    ensure_project_root()

    paths = arguments.paths or gather_default_paths()
    return run_markdownlint(paths)


if __name__ == "__main__":
    raise SystemExit(main())
