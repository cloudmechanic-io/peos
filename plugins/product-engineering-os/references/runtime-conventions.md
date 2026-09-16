# Runtime conventions

Apply these rules for every PEOS capability.

## Context resolution

1. Follow platform, user, and repository instructions first.
2. Locate `peos/config.yaml` from the common repository root. If absent, explain that PEOS defaults apply and offer or invoke `setup` when workspace writes are authorized.
3. Load the capability contract and selected provider adapter from `providers/registry.json`.
4. Load only the client guideline files and specialist role contracts relevant to the affected scope.
5. Inspect repository evidence before making claims about current behavior.

Provider values `bmad` and `peos-native` resolve through the bundled registry. A client provider value may use `file:peos/providers/<adapter>.md`; resolve it only within the workspace, require it to name the same capability contract, and reject path traversal or contract/approval changes.

Do not preload all role files, all historical changes, or entire repositories. Summarize discovered context in `peos/context/system-map.md` only when it is durable and reviewed.

## Execution

- Prefer the smallest safe workflow class from `routing.md`.
- Ask only questions that materially change scope, product behavior, risk, or implementation.
- Distinguish observed facts, assumptions, decisions, and unresolved questions.
- Preserve existing behavior unless an approved delta changes it.
- Never invent test results, approvals, external links, or production state.
- Do not silently overwrite an approved artifact. Create a revision or move it back to draft with an explanation.
- Keep the user-facing capability name stable even when a provider is missing or changes.

## Specialist use

When subagents are supported, delegate a bounded task to the role described in `agents/`. When they are not supported, apply that file as a temporary reasoning lens. The lead owns integration; a specialist owns only its scoped analysis or implementation.

## Completion

Before completing a capability, check its contract postconditions, update lifecycle status, list evidence produced, list checks not run, and state the next safe capability. A document existing is not proof that a human approved it, code shipped, or an external system synchronized it.
