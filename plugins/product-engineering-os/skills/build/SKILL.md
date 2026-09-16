---
name: build
description: Implement an approved PEOS delivery slice in existing repositories using only affected specialist lenses while preserving contracts, user changes, and verification evidence.
---

# Build an approved slice

Use when the user asks to implement a shaped quick change or an approved delivery slice. This capability changes code; it does not expand product scope or approve its own result.

## Required context

Read:

- `../../references/runtime-conventions.md`
- `../../references/governance.md`
- `../../contracts/lifecycle.md`
- `../../contracts/implementation-record.md`
- the approved product requirement, change spec, and selected plan slice;
- only affected client guidelines and specialist role contracts.

Resolve the provider through `../../providers/registry.json`; the default adapter is `../../providers/bmad/build.md`.

## Procedure

1. Verify scope, approval, repository state, branch/worktree policy, and acceptance criteria. Route missing or ambiguous intent back through `guide`.
2. Inspect the exact implementation area and current tests before editing. Preserve unrelated changes.
3. Delegate bounded frontend, backend, or infrastructure work only when the slice crosses those boundaries. The lead owns contract consistency and integration.
4. Implement the smallest coherent slice. Preserve compatibility and rollback assumptions; flag a material design deviation before proceeding.
5. Add or update tests with the code and run the cheapest relevant repository checks.
6. Maintain `implementation.md` for non-trivial work with files, contract/migration impact, deviations, command evidence, checks not run, and remaining work.
7. Mark the slice `implemented`, not `verified`, after implementation checks succeed.

Finish by recommending independent `verify`. Do not merge, deploy, publish externally, or claim live behavior unless separately requested and directly evidenced.
