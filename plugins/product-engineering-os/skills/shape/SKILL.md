---
name: shape
description: Facilitate brainstorming and product discovery, then create a normalized quick acceptance brief, PRD, product brief, or PRFAQ with current and target product state.
---

# Shape product intent

Use when the problem, user outcome, scope, MVP, acceptance criteria, or product direction needs discovery or definition. This is the requirements-gathering capability for product and engineering contributors.

## Required context

Read:

- `../../references/runtime-conventions.md`
- `../../references/routing.md`
- `../../references/governance.md`
- `../../contracts/lifecycle.md`
- `../../contracts/product-requirement.md`
- `../../agents/product.md`

Resolve the configured provider through `../../providers/registry.json`; the default adapter is `../../providers/bmad/shape.md`.

## Discovery loop

1. Frame the problem, affected users, desired outcome, evidence, constraints, and why now. Separate facts from assumptions.
2. Establish current product behavior from product context, existing artifacts, and repository evidence where available.
3. Ask focused questions one decision at a time when answers change scope or success. Do not interrogate for information that can be discovered safely.
4. Diverge before converging: consider no-change, process/manual, smallest experiment, and fuller solution options. Explain value, learning speed, cost, and risk.
5. Choose a quick, feature, or strategic path. Define target behavior, scope, non-goals, user scenarios, success measure, guardrails, and observable acceptance criteria.
6. Run a product challenge: look for solution-first framing, unsupported demand, hidden actors, edge/failure experience, analytics, accessibility, privacy, and oversized MVP scope.
7. Normalize provider output to `peos/changes/<change-id>/product-requirement.md`. For strategic work, preserve a linked brief or PR/FAQ when useful; for quick work, keep only the concise required sections.
8. Mark the artifact `in-review` when ready for a human. Never self-approve it.

Finish with key decisions, assumptions, open product questions, approval owner, and whether `design` can start.
