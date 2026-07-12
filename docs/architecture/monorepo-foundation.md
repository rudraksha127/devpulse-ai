# Monorepo Foundation Map

## Apps
- `apps/control-plane-api/` — Administrative and orchestration API boundary.
- `apps/developer-studio-web/` — Developer dashboard and control surface.
- `apps/devpulse-cli/` — Local command-line interface and automation entrypoint.
- `apps/agent-gateway/` — Ingress for external API traffic, policy, and tenancy routing.
- `apps/workflow-runner/` — Durable execution host for workflow state machines.
- `apps/event-bus-relay/` — Event normalization, translation, and fan-out.
- `apps/plugin-host/` — Isolated runtime boundary for plugin execution.

## Packages
- `packages/domains/` — Bounded contexts owning core business language and rules.
- `packages/platform/` — Cross-cutting capabilities exposed as interfaces.
- `packages/sdk/` — Public SDK surfaces for clients, servers, and plugins.
- `packages/contracts/` — Shared API/event/config schema source of truth.
- `packages/tooling/` — Shared build/test/codegen wrappers.

### Domain Bounded Contexts
- `multi-agent/` — Agent lifecycle, task decomposition, and coordination contracts.
- `hybrid-rag/` — Retrieval orchestration across vector, graph, and keyword systems.
- `memory/` — Long-term memory policy, indexing, and recall boundaries.
- `knowledge-graph/` — Entity-relation graph interfaces and reasoning boundaries.
- `workflow-engine/` — Workflow definitions, transitions, retries, and compensations.
- `ai-router/` — Provider/model routing policies and decision contracts.
- `human-in-loop/` — Review, approval, override, and escalation boundaries.
- `github-intelligence/` — Repository and contribution intelligence abstractions.
- `learning-engine/` — Feedback loops, scoring, adaptation interfaces.
- `research-engine/` — Evidence retrieval, ranking, and synthesis contracts.
- `career-intelligence/` — Skills graph and growth intelligence boundaries.
- `dashboard-analytics/` — Aggregation contracts for operational intelligence views.
- `marketplace/` — Plugin catalog, trust, compatibility, and lifecycle contracts.

### Platform Modules
- `eventing/` — Event contract helpers and broker-facing adapter abstractions.
- `observability/` — Logging, metrics, tracing, and audit interfaces.
- `security/` — Authentication, authorization, secrets, and policy primitives.
- `tenancy/` — Tenant isolation, quota, and governance boundaries.
- `identity/` — User/service identity contracts.
- `billing/` — Usage metering and charging abstractions.
- `feature-flags/` — Progressive delivery and experimentation controls.

### SDK and Contracts
- `sdk/server-sdk/` — Integration facade for backend systems.
- `sdk/client-sdk/` — Integration facade for web/CLI clients.
- `sdk/plugin-sdk/` — Plugin lifecycle, capability, and sandbox API.
- `contracts/api/` — External API contracts and versioned interfaces.
- `contracts/events/` — Event schemas and version conventions.
- `contracts/config/` — Typed configuration schema contracts.

## Plugins
- `plugins/official/` — First-party plugins maintained by core team.
- `plugins/community/` — Community-maintained plugins under governance.
- `plugins/experimental/` — Incubation stage plugins.
- `plugins/manifests/` — Signed metadata and permission declarations.
- `plugins/compatibility-matrix/` — Version support mapping for platform/plugin pairs.
- `plugins/sandbox-profiles/` — Runtime isolation and permission templates.

## Infrastructure
- `terraform/` — Cloud resources and shared infrastructure provisioning.
- `kubernetes/` — Workload manifests and cluster policy controls.
- `helm/` — Release packaging and environment composition.
- `environments/` — Dev/stage/prod/enterprise overlays.
- `data/` — Topology for DB, graph, vector, and messaging systems.
- `policy/` — Policy-as-code and compliance controls.
- `observability/` — Monitoring, alerting, and telemetry stack definitions.

## Tests
- `unit/` — Isolated domain and utility tests.
- `contract/` — API/event/config compatibility verification.
- `integration/` — Adapter and infrastructure interaction tests.
- `e2e/` — End-to-end user and orchestration flows.
- `performance/` — Throughput/latency/regression benchmarking.
- `security/` — Security abuse-case and hardening validation.
- `chaos/` — Failure injection and resilience verification.
- `test-fixtures/` — Shared fixtures, datasets, and mock assets.

## Docs
- `architecture/` — System design, context maps, and architectural decisions.
- `domains/` — Ubiquitous language and bounded-context documentation.
- `runbooks/` — Operations and incident procedures.
- `api/` — API reference and lifecycle policies.
- `plugins/` — Plugin development, publication, and governance docs.
- `security/` — Threat model and hardening guidance.
- `governance/` — RFC and decision governance documentation.
- `onboarding/` — Contributor and maintainer onboarding guides.
- `roadmap/` — Public capability and release evolution plans.

## GitHub
- `.github/workflows/` — CI/CD/security/release/quality pipeline definitions.
- `.github/ISSUE_TEMPLATE/` — Structured issue intake templates.
- `.github/workflows-reusable/` — Reusable workflow building blocks.
- `.github/CODEOWNERS` — Ownership boundaries for reviews.
- `.github/PULL_REQUEST_TEMPLATE.md` — PR quality checklist.

## Scripts
- `bootstrap/` — Environment bootstrap and setup wrappers.
- `quality/` — Lint/test/coverage orchestration.
- `release/` — Release preparation and publishing support.
- `migrations/` — Data and schema migration orchestration.
- `dataset/` — Synthetic and sample dataset lifecycle.
- `ops/` — Operational maintenance jobs.

## Config
- `defaults/` — Global baseline settings.
- `environments/` — Environment-specific overrides.
- `feature-flags/` — Feature gate definitions.
- `policy/` — Runtime and compliance policy configs.
- `model-routing/` — AI model/provider routing policies.

## Governance
- `adr/` — Architecture Decision Records.
- `rfc/` — Change proposal and review process.
- `standards/` — Coding/API/event/observability standards.
- `ownership/` — Team ownership and escalation map.
