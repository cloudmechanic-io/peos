---
name: guide
description: Route a product-engineering request or active change to the smallest safe PEOS workflow, required specialist lenses, current lifecycle state, and next decision.
---

# Guide the change

Use this as the normal front door when a contributor describes an idea, bug, feature, pivot, review request, or unfinished change and does not know which PEOS capability comes next.

## Required context

Read:

- `../../references/runtime-conventions.md`
- `../../references/routing.md`
- `../../references/governance.md`
- `../../contracts/guide.md`
- `../../providers/native/guide.md`
- `../../agents/product-engineering-lead.md`

## Procedure

1. Parse the requested outcome and locate any `peos/changes/<change-id>/` artifacts.
2. Classify the work as quick, feature, or strategic using risk, ambiguity, and reversibility.
3. Identify risk signals and only the specialist lenses that are materially affected.
4. Determine the current lifecycle state without inventing approvals or completion.
5. Return the normalized guide decision.
6. If the user already requested execution and no material decision is missing, continue immediately into `shape`, `design`, `plan`, `build`, `diagnose`, or `verify`. Use `sync` and `learn` only from explicit intent.

Do not create extra ceremony. A clear local change should take the quick path; hidden compatibility, security, data, or cross-repository risk must escalate it.
