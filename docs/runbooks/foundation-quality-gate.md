# Foundation Quality Gate

This runbook defines the baseline scaffold validation gate for DevPulse AI.

## Purpose

Ensure the repository always keeps its required monorepo structure and critical architecture documents.

## Local Validation

Run from repository root:

```bash
python scripts/quality/scaffold_check.py
```

Expected output:

- `Scaffold check passed.` when structure/docs are valid.
- A deterministic list of missing or empty required paths otherwise.

## CI Validation

The `CI` workflow runs this command on `push`, `pull_request`, and manual dispatch:

```bash
python scripts/quality/scaffold_check.py
```

If the command exits with non-zero status, the quality gate fails and blocks merge until fixed.
