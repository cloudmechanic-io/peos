# Testing

## Static validation

Run `./scripts/validate.sh`. It checks both platform manifests, marketplace references, version consistency, skill frontmatter, the provider registry, required files, and unresolved placeholders. If Claude Code is installed, it also runs Claude’s native plugin validator.

## Behavioral smoke test

Install locally, reload the client, and run each scenario in `evals/scenarios.md` in a new session. Confirm that:

- Claude and Codex choose the same change class and produce equivalent normalized artifacts;
- product discovery asks business questions before technical design;
- technical design inspects the current repository before describing target state;
- unrelated specialist rules are not loaded;
- no agent claims a human approval or publishes externally without explicit authority;
- `/learn` creates a reviewable proposal instead of silently changing policy.

## Upgrade test

Create a temporary client overlay, edit one guideline, install the next PEOS version, and verify the client file is untouched. Resume an in-flight change and confirm contract-version handling is explicit.
