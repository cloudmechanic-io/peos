---
name: plan
description: Convert an approved requirement and technical change into small dependency-aware delivery slices with owners, validation, compatibility, rollout, and completion evidence.
---

# Plan delivery

Use when a feature or strategic design is ready to sequence, or a quick change needs concise implementation steps. Planning does not automatically create Jira items.

## Required context

Read:

- `../../references/runtime-conventions.md`
- `../../references/governance.md`
- `../../contracts/lifecycle.md`
- `../../contracts/delivery-plan.md`
- `../../agents/product-engineering-lead.md`

Resolve the provider through `../../providers/registry.json`; the default adapter is `../../providers/bmad/plan.md`.

## Procedure

1. Confirm the source requirement and change-spec revisions and record unresolved approvals or decisions.
2. Identify dependency order, cross-repository contracts, migrations, temporary compatibility, and release constraints.
3. Slice vertically around demonstrable outcomes. Keep a quick change as one compact slice; avoid artificial epics.
4. For each slice, state scope, repositories, owner lens, acceptance links, validation, rollout/rollback impact, and completion evidence.
5. Separate implementation, integration, external publication, deployment, and live verification.
6. Normalize to `peos/changes/<change-id>/delivery-plan.md` and mark it `in-review` when human sequencing approval is required.

Recommend `build` for the next approved slice. Use `sync` only when the user requests Jira/Confluence publication.
