# Rollout

## Phase 1: maintainers

1. Run `./scripts/validate.sh`.
2. Run `./scripts/install-local.sh both` on a maintainer machine.
3. Test the scenarios in `evals/scenarios.md` in fresh Claude and Codex sessions.
4. Record platform differences as adapter defects, not client workflow changes.

## Phase 2: pilot client

1. Put this repository in a private GitHub organization accessible to the pilot.
2. Run `scaffold-client.sh` against the umbrella repository.
3. Run `configure-claude-project.py` when the client uses Claude Code, then review the generated project settings.
4. Add repository mappings and real validation commands; leave all external integrations disabled.
5. Pilot one quick change, one feature, and one production diagnosis with two or three contributors.
6. Use `/learn` only for repeated, accepted feedback; review all proposed guideline changes.

## Phase 3: organization distribution

### Claude

- Add the GitHub repository as a Claude plugin marketplace.
- Install `product-engineering-os@product-engineering-os` for pilot users.
- Install `bmad-method@bmad` from `bmad-code-org/bmad-plugins`.
- For repository-scoped discovery, commit `.claude/settings.json` with approved `extraKnownMarketplaces` and `enabledPlugins` values after testing the exact source syntax with the client’s authentication model.
- Use organization policy to restrict marketplaces when central governance is required.

### Codex and ChatGPT

- In the workspace administration UI, import the GitHub repository as a marketplace.
- Leave the marketplace path empty because the manifest is at `.agents/plugins/marketplace.json` in the root.
- Configure installation per role in the workspace; repository policy fields are suggestions and are not automatically applied during workspace import.
- Import or install the BMAD marketplace separately.

## Phase 4: integrations

Enable one adapter at a time. Start with read-only Jira/Confluence, then AWS/logs, then read-only database diagnostics if required. Use least-privilege identities, auditable access, redaction, environment allowlists, bounded queries, and explicit write approval.

## Success measures

- elapsed time from problem statement to approved requirement;
- percentage of implemented changes traceable to approved acceptance criteria;
- review escape rate and rollback rate;
- human edits required per normalized artifact;
- token/context use per change class;
- frequency and acceptance rate of `/learn` proposals;
- provider portability demonstrated by one capability swap in a test environment.
