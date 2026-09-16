---
name: design
description: Analyze the current system and design the target technical state, explicit behavioral delta, compatibility and rollout plan, plus ADRs only for durable decisions.
---

# Design the technical change

Use after product intent is sufficiently clear, or when a user explicitly requests repository-grounded technical analysis, architecture, a change specification, or an ADR.

## Required context

Read:

- `../../references/runtime-conventions.md`
- `../../references/routing.md`
- `../../references/governance.md`
- `../../contracts/lifecycle.md`
- `../../contracts/change-spec.md`
- `../../contracts/adr.md`
- `../../agents/architect.md`

Resolve the provider through `../../providers/registry.json`; the default adapter is `../../providers/bmad/design.md`.

## Procedure

1. Confirm the requirement revision and approval state. For quick work, explicit user intent may be sufficient under client policy; do not silently assume feature/strategic approval.
2. Inspect affected repositories, local instructions, contracts, schemas/migrations, tests, infrastructure, and operations. Record evidence for current state.
3. Delegate bounded analysis only to affected frontend, backend, and/or infrastructure roles; provide each with relevant requirements and repository scope.
4. Describe technical target state and reconcile cross-boundary assumptions.
5. Write ADDED, MODIFIED, REMOVED, and RENAMED behavior, using `None` explicitly where a delta category is empty.
6. Define compatibility, migration, failure behavior, security/privacy, observability, rollout, rollback, and acceptance-linked validation.
7. Compare alternatives. Create an ADR only for a durable, hard-to-reverse decision under governance criteria; otherwise keep technical details with the change.
8. Normalize to the change-spec contract and mark ready artifacts `in-review`, never self-approved.

Stop for a human decision when alternatives materially change product scope, risk, data ownership, security, cost, or irreversible architecture.
