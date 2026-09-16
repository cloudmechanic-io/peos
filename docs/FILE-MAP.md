# File map

This is the maintainer-level inventory. Paths below are relative to the distribution repository.

## Distribution root

| File | Responsibility |
| --- | --- |
| `.agents/plugins/marketplace.json` | Codex/ChatGPT workspace marketplace catalog; points to the local plugin folder and proposes install/auth policy. |
| `.claude-plugin/marketplace.json` | Claude marketplace catalog; points to the same plugin folder. |
| `.github/workflows/validate.yml` | Runs dependency-free cross-platform validation on pull requests and `main`. |
| `.gitignore` | Excludes local operating-system, log, temporary, and release scratch files. |
| `README.md` | Product overview, workflow, installation, publishing, customization, and repository map. |
| `CONTRIBUTING.md` | Trunk-based contribution contract and pull-request checklist. |
| `CHANGELOG.md` | Release history consumed by the release preparation script. |
| `evals/scenarios.md` | Representative behavioral acceptance tests for both agent platforms. |

## Maintainer documentation

| File | Responsibility |
| --- | --- |
| `docs/ARCHITECTURE.md` | Dependency direction, artifact model, role model, learning model, and versioning decisions. |
| `docs/CUSTOMIZING-CLIENTS.md` | Upgrade-safe client overlay and provider customization procedure. |
| `docs/ROLLOUT.md` | Maintainer, pilot, organization, and integration rollout phases. |
| `docs/TESTING.md` | Static, behavioral, and upgrade test procedure. |
| `docs/FILE-MAP.md` | This inventory. |

## Maintainer scripts

| File | Responsibility |
| --- | --- |
| `scripts/validate.py` | Validates manifests, versions, skill set, provider registry, references, and unresolved markers using Python stdlib. |
| `scripts/validate.sh` | Runs PEOS validation plus Claude’s native validator when available. |
| `scripts/install-local.sh` | Idempotently configures BMAD and PEOS local marketplaces/plugins for Claude, Codex, or both. |
| `scripts/scaffold-client.sh` | Copies the default `peos/` overlay into a client umbrella repository without overwriting. |
| `scripts/configure-claude-project.py` | Safely merges project-scoped PEOS/BMAD marketplace prompts into a client `.claude/settings.json`. |
| `scripts/set-version.py` | Updates all explicit plugin/marketplace versions and closes the Unreleased changelog section. |
| `scripts/prepare-release.sh` | Creates a short-lived release branch, validates, commits, pushes, and optionally opens a pull request. |
| `scripts/publish.sh` | Validates merged `main`, creates an annotated version tag, and pushes it. |

## Platform manifests

| File | Responsibility |
| --- | --- |
| `plugins/product-engineering-os/.claude-plugin/plugin.json` | Claude identity and metadata; Claude auto-discovers default `skills/` and `agents/`. |
| `plugins/product-engineering-os/.codex-plugin/plugin.json` | Codex identity, UI metadata, and shared skill path. |

## Public capability skills

| File | Responsibility |
| --- | --- |
| `skills/setup/SKILL.md` | Initializes or audits a client workspace and system map. |
| `skills/guide/SKILL.md` | Classifies work, reads lifecycle state, and selects the smallest safe next capability. |
| `skills/shape/SKILL.md` | Runs brainstorming/product discovery and produces normalized requirements. |
| `skills/design/SKILL.md` | Produces repository-grounded current/target technical state, delta spec, and optional ADR. |
| `skills/plan/SKILL.md` | Produces small, dependency-aware delivery slices. |
| `skills/build/SKILL.md` | Implements one approved slice using only affected specialist lenses. |
| `skills/diagnose/SKILL.md` | Investigates incidents, AWS/log signals, or data through bounded read-only evidence. |
| `skills/verify/SKILL.md` | Independently executes quality, QA, architecture, security, and compatibility gates. |
| `skills/sync/SKILL.md` | Previews or publishes approved Git artifacts through client-specific external adapters. |
| `skills/learn/SKILL.md` | Converts repeated human review into a reviewable guideline proposal. |

All skill paths above are under `plugins/product-engineering-os/`.

## Specialist role contracts

| File | Responsibility |
| --- | --- |
| `agents/product-engineering-lead.md` | Integrating front door, router, and lifecycle/governance owner. |
| `agents/product.md` | Product value, scope, evidence, MVP, success, and acceptance-criteria lens. |
| `agents/architect.md` | System boundary, contract, compatibility, operability, and durable-decision lens. |
| `agents/frontend.md` | UI, component/state, accessibility, performance, client-contract, and frontend-test lens. |
| `agents/backend.md` | Domain, API/event, persistence, authorization, reliability, and backend-test lens. |
| `agents/infrastructure.md` | Cloud, IaC, IAM, networking, environments, delivery, resilience, observability, and cost lens. |
| `agents/reviewer.md` | Independent acceptance, quality, architecture, security, compatibility, and residual-risk lens. |

## Normalized contracts

| File | Responsibility |
| --- | --- |
| `contracts/lifecycle.md` | Common frontmatter, classifications, statuses, approvals, provenance, and paths. |
| `contracts/workspace.md` | Required client setup/configuration result. |
| `contracts/guide.md` | Required routing decision result. |
| `contracts/product-requirement.md` | Quick acceptance brief and feature/strategic PRD shape. |
| `contracts/change-spec.md` | Technical current/target state and ADDED/MODIFIED/REMOVED/RENAMED delta shape. |
| `contracts/adr.md` | Durable architecture decision criteria and document shape. |
| `contracts/delivery-plan.md` | Delivery slice and sequencing shape. |
| `contracts/implementation-record.md` | Implementation scope, evidence, deviations, and remaining-work shape. |
| `contracts/diagnostic-report.md` | Sanitized read-only investigation evidence and hypothesis shape. |
| `contracts/review-report.md` | Acceptance traceability and independent gate result shape. |
| `contracts/sync-record.md` | External publication provenance and read-back shape. |
| `contracts/learning-proposal.md` | Human feedback evidence and proposed guideline diff shape. |

## Providers and shared runtime rules

| File | Responsibility |
| --- | --- |
| `providers/registry.json` | Versioned map from every public capability to contract, default provider, and adapter. |
| `providers/bmad/shape.md` | Maps PEOS discovery classes to BMAD brainstorming, brief/PRFAQ, PRD, and spec skills. |
| `providers/bmad/design.md` | Maps technical analysis to BMAD spec/architecture while enforcing the PEOS delta. |
| `providers/bmad/plan.md` | Maps planning to BMAD stories/sprint flows without forcing ticket creation. |
| `providers/bmad/build.md` | Maps implementation to BMAD build/development while retaining PEOS specialist scope. |
| `providers/bmad/verify.md` | Maps review/QA to BMAD and repository-native gates. |
| `providers/native/setup.md` | PEOS-owned safe workspace bootstrap procedure. |
| `providers/native/guide.md` | PEOS-owned lifecycle router. |
| `providers/native/diagnose.md` | PEOS-owned read-only operations/data investigation adapter. |
| `providers/native/sync.md` | PEOS-owned external publication adapter contract. |
| `providers/native/learn.md` | PEOS-owned explicit guideline-learning procedure. |
| `references/runtime-conventions.md` | Context loading, provider resolution, execution, specialist, and completion rules. |
| `references/routing.md` | Quick/feature/strategic classification and specialist routing matrix. |
| `references/governance.md` | Decision rights, lifecycle transitions, ADR threshold, external action, and learning policy. |
| `references/security-and-integrations.md` | Credential, read-only diagnostic, database, publication, and cloud boundaries. |

## Client overlay defaults

All paths below are under `plugins/product-engineering-os/defaults/project/peos/` and are copied into the client repository.

| File | Responsibility |
| --- | --- |
| `README.md` | Explains the client-owned overlay. |
| `config.yaml` | Sensible providers, routing, governance, validation, integration switches, and repository list. |
| `context/system-map.md` | Evidence-backed template for product, repository, runtime, contract, and risk context. |
| `changes/README.md` | Change-folder naming and artifact guidance. |
| `diagnostics/README.md` | Sanitized diagnostic-report storage guidance. |
| `decisions/README.md` | ADR naming and decision guidance. |
| `guidelines/product.md` | Default product discovery and requirements rules. |
| `guidelines/engineering.md` | Default cross-cutting brownfield engineering rules. |
| `guidelines/frontend.md` | Default frontend-only design and implementation rules. |
| `guidelines/backend.md` | Default backend-only contract, data, and reliability rules. |
| `guidelines/infrastructure.md` | Default cloud/IaC/operations rules. |
| `guidelines/security.md` | Default security, privacy, secret, and least-privilege rules. |
| `guidelines/quality.md` | Default acceptance traceability and verification rules. |
| `providers/provider.example.md` | Upgrade-safe contract for a client-supplied provider adapter. |
| `templates/product-requirement.md` | Editable client template for requirements. |
| `templates/change-spec.md` | Editable client template for technical deltas. |
| `templates/delivery-plan.md` | Editable client template for delivery slices. |
| `templates/adr.md` | Editable client template for durable decisions. |
| `templates/review-report.md` | Editable client template for independent verification. |
