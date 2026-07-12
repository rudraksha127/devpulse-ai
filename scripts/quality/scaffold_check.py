#!/usr/bin/env python3
"""Validate DevPulse monorepo scaffold foundations."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REQUIRED_DIRECTORIES: tuple[str, ...] = (
    "apps",
    "packages",
    "plugins",
    "infrastructure",
    "tests",
    "docs",
    "config",
    "governance",
    ".github",
    "scripts",
    "data",
)

REQUIRED_FILES: tuple[str, ...] = (
    "ARCHITECTURE.md",
    "docs/architecture/monorepo-foundation.md",
    ".github/copilot-instructions.md",
)

NON_EMPTY_FILES: tuple[str, ...] = REQUIRED_FILES


@dataclass(frozen=True)
class ValidationIssue:
    path: str
    message: str


def _check_required_paths(root: Path, relative_paths: Iterable[str], expected: str) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    for relative_path in relative_paths:
        target = root / relative_path
        if expected == "directory" and not target.is_dir():
            issues.append(ValidationIssue(relative_path, "missing required directory"))
        if expected == "file" and not target.is_file():
            issues.append(ValidationIssue(relative_path, "missing required file"))
    return issues


def _check_non_empty_files(root: Path, relative_paths: Iterable[str]) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    for relative_path in relative_paths:
        target = root / relative_path
        if not target.exists():
            continue
        if target.is_file() and target.stat().st_size == 0:
            issues.append(ValidationIssue(relative_path, "critical document is empty"))
    return issues


def run_scaffold_check(root: Path) -> list[ValidationIssue]:
    issues = _check_required_paths(root, REQUIRED_DIRECTORIES, expected="directory")
    issues.extend(_check_required_paths(root, REQUIRED_FILES, expected="file"))
    issues.extend(_check_non_empty_files(root, NON_EMPTY_FILES))
    return issues


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    issues = run_scaffold_check(repo_root)
    if issues:
        print("Scaffold check failed:")
        for issue in issues:
            print(f"- {issue.path}: {issue.message}")
        return 1

    print("Scaffold check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
