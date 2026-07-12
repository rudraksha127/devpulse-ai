# DevPulse AI / daily-log repository instructions

This repository is the foundation of DevPulse AI, an AI operating system for developers.

## Project purpose
Build a modular AI platform for:
- developer learning
- research aggregation
- GitHub intelligence
- memory and RAG
- workflow automation
- human-in-the-loop approvals

This repository is in the foundation stage. Keep implementation minimal, well-structured, and future-proof.

## Core rules
- Prefer small, reviewable changes.
- Follow existing architecture and folder conventions.
- Do not introduce unnecessary complexity.
- Keep modules independent and replaceable.
- Use production-grade error handling.
- Do not hardcode secrets or credentials.
- Do not create fake commits or empty automation just to inflate activity.
- Human approval is required before any public/profile-impacting changes.

## Engineering standards
- Use clear, descriptive names.
- Keep functions small and focused.
- Prefer typed, explicit code.
- Write tests for non-trivial logic.
- Document public APIs and important workflows.
- Keep outputs deterministic where possible.

## Build / test / validate
Before completing any change:
- run the relevant tests
- verify formatting / linting if configured
- ensure the repository still works on the default branch
- update documentation when behavior changes

## GitHub automation guidance
If working on automation:
- keep GitHub Actions reliable and idempotent
- avoid duplicate commits
- commit only when file content changes
- use meaningful commit messages
- prefer stable, maintained services over fragile third-party widgets

## Current priorities
1. Foundation and repo hygiene
2. Reliable daily learning log automation
3. Modular architecture for future DevPulse AI expansion
4. Clear documentation and maintainability

## Output expectations
When making changes, prefer:
- clean markdown
- compact YAML
- readable scripts
- explicit comments only where needed
- no speculative architecture unless requested
