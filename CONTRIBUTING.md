# Contributing

PEOS uses trunk-based development. `main` must remain releasable.

## Working agreement

1. Pull the current `main` and create a short-lived branch.
2. Make one coherent, reviewable change. Prefer branches that live for hours, not weeks.
3. Run `./scripts/validate.sh`.
4. Add or update a scenario in `evals/scenarios.md` when behavior changes.
5. Open a pull request. Use feature flags when incomplete runtime behavior must merge incrementally.
6. Obtain the required product or engineering ownership approval. Engineers retain final approval for code, architecture, security, and operations.
7. Squash-merge promptly and delete the branch.

Do not create long-lived `develop`, integration, or release branches. Release preparation happens on a short-lived `release/vX.Y.Z` branch; publishing tags the already-merged commit on `main`.

## Compatibility expectations

- Public capability names and artifact contracts are versioned APIs.
- A provider change must not change the user-facing workflow or silently rewrite approved artifacts.
- New defaults must remain useful without client configuration.
- Client overlays take precedence over bundled defaults and must survive plugin upgrades.
- Provider-specific instructions belong under `providers/`; never leak them into public capability names.
- BMAD and other workflow providers remain external dependencies. Do not copy their prompts, agents, workflows, templates, source, or documentation into PEOS. Adapter files may reference public provider entrypoints and normalize outputs only.

## Pull-request checklist

- [ ] The change is scoped and backwards compatible, or migration is documented.
- [ ] Claude and Codex manifests still validate.
- [ ] Skills have valid frontmatter and load only necessary context.
- [ ] Security boundaries and human approvals are preserved.
- [ ] Documentation and changelog are current.
- [ ] `./scripts/validate.sh` passes.
- [ ] No provider implementation or upstream-owned content was vendored.
