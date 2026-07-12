# DevPulse AI Monorepo Foundation

This repository uses a production-grade monorepo foundation aligned to Clean Architecture, Hexagonal Architecture, Domain-Driven Design, Event-Driven Architecture, Plugin-first architecture, and AI-first system design.

## Top-Level Modules

- `apps/` — Deployable applications and service entrypoints.
- `packages/` — Reusable domain, platform, SDK, and contract modules.
- `plugins/` — Plugin ecosystem structure and trust boundaries.
- `infrastructure/` — Infrastructure-as-code and runtime topology.
- `tests/` — Layered testing strategy aligned to architectural boundaries.
- `docs/` — Architecture, API, governance, and onboarding documentation.
- `.github/` — CI/CD, governance templates, and reusable workflows.
- `scripts/` — Operational scripts and automation wrappers.
- `config/` — Typed, environment-aware, policy-driven configuration layout.
- `governance/` — ADRs, RFCs, standards, and ownership controls.

## Module Boundaries

1. Apps orchestrate use-cases; they do not contain domain business logic.
2. Domain packages own business logic and stay framework/infrastructure agnostic.
3. Platform packages provide cross-cutting interfaces and shared capabilities.
4. Contracts are the single source of truth for shared API/event/config schemas.
5. Plugins integrate only via `packages/sdk/plugin-sdk` and manifest policy.
6. Infrastructure contains runtime/deployment concerns only.
7. Tests mirror boundaries: isolated domain tests plus cross-boundary integration/e2e/contract tests.

## Dependency Rules

- Allowed direction: `apps -> application/use-cases -> domain ports -> adapters`.
- `packages/domains/*` must not depend on infrastructure frameworks directly.
- Infrastructure adapters may depend on domain ports/contracts; inverse is forbidden.
- Cross-domain communication should use published events or explicit contracts.
- Plugins cannot import internal domain modules directly.
- Shared utilities belong in `packages/platform` or `packages/tooling`.

## Naming Conventions

- Folder/package names: `kebab-case`
- Domain events: `domain.entity.action.vN`
- Workflow IDs: `{domain}.{usecase}.{version}`
- Plugin IDs: `vendor.plugin-name`
- Config files: `{service}.{env}.config`

## Future Extensibility

- Add capabilities by introducing new bounded contexts in `packages/domains/`.
- Add providers by creating adapters without changing domain core.
- Scale plugin ecosystem through manifest policy and compatibility matrices.
- Evolve interfaces using versioned contracts in `packages/contracts/`.
- Support enterprise variants through `infrastructure/environments/` overlays.
