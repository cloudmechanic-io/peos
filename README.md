# Product Engineering Operating System

> A governed product-engineering operating layer for human-agent teams.

PEOS gives product engineers, product owners, and coding agents one brownfield-first workflow from idea to verified change. It packages once for **Claude Code/Claude Teams and Codex/ChatGPT workspaces** while keeping the actual operating model independent of either platform.

BMAD is the default workflow provider for discovery, requirements, design, planning, implementation, and review. It is installed separately as an external plugin dependency: **no BMAD prompts, agents, workflows, templates, or source files are copied into this repository**. PEOS exposes only thin provider adapters and stable capability contracts, so BMAD can be upgraded or replaced without retraining the team or changing the lifecycle. See the [dependency policy](docs/DEPENDENCY-POLICY.md).

## Start here

### Maintainer smoke test

```sh
git clone YOUR_GITHUB_REPOSITORY_URL
cd product-engineering-os
./scripts/validate.sh
./scripts/install-local.sh both
```

Reload Claude Code and Codex after installation. In an umbrella repository, start with:

- Claude: `/product-engineering-os:setup`, then `/product-engineering-os:guide`
- Codex: `$setup`, then `$guide`, or ask “Use PEOS to guide this change.”

The setup capability creates a small `peos/` overlay in the umbrella root. It does not copy the plugin or vendor BMAD.

### Client rollout

From this cloned distribution repository:

```sh
./scripts/scaffold-client.sh /absolute/path/to/client-umbrella "Client Name"
./scripts/configure-claude-project.py /absolute/path/to/client-umbrella YOUR_ORG/product-engineering-os
```

Then publish this repository to private GitHub and follow [Team distribution](#team-distribution). The MVP ships sensible guidelines and routing defaults, so client customization is optional rather than a prerequisite.

## The workflow

```text
                       small, clear change
                  +--------------------------+
                  |                          v
idea -> GUIDE -> SHAPE -> DESIGN -> PLAN -> BUILD -> VERIFY -> SYNC
          |         |        |        |        |        |        |
          |         PRD      ADR /    slices   code     report   Jira /
          |                  change                              Confluence
          |                  spec
          +----------------------------------------------------------+
                                LEARN proposes guideline improvements

incident/data question -> GUIDE -> DIAGNOSE -> evidence -> shape/design/build only if a change is requested
```

`guide` selects the smallest safe path:

| Change class | Product artifact | Technical artifact | Delivery |
| --- | --- | --- | --- |
| Quick | Acceptance criteria | Ticket technical notes | Build and verify; no ADR by default |
| Feature | PRD with current/target state | Change spec; ADR only for durable decisions | Sliced plan, build, verify |
| Strategic | Product brief or PR/FAQ, then PRD | Architecture and ADRs | Staged plan, build, verify |

Every technical change spec uses an OpenSpec-inspired delta: **ADDED, MODIFIED, REMOVED, and RENAMED** behavior, plus compatibility, migration, rollout, rollback, observability, and validation. This preserves the part of OpenSpec that is most valuable for an existing system without forcing a second end-to-end process beside BMAD.

## Capabilities

| Stable capability | Business outcome | Default provider | Primary lens |
| --- | --- | --- | --- |
| `setup` | Bootstrap or inspect a client workspace | PEOS native | Lead |
| `guide` | Route work and show the next decision | PEOS native | Lead |
| `shape` | Discover the problem and produce requirements | BMAD | Product |
| `design` | Produce current/target technical design, delta spec, and ADR when warranted | BMAD | Architect + affected specialists |
| `plan` | Produce thin, dependency-aware delivery slices | BMAD | Architect + delivery |
| `build` | Implement an approved slice | BMAD | Frontend, backend, and/or infrastructure |
| `diagnose` | Investigate production behavior, logs, AWS, or data read-only | PEOS native adapter | Affected specialist |
| `verify` | Run and report tests, QA, security, architecture, and compatibility checks | BMAD + local tools | Independent reviewer |
| `sync` | Publish approved artifacts to Jira/Confluence when authorized | PEOS native adapter | Lead |
| `learn` | Turn human review into governed guideline proposals | PEOS native | Lead + owners |

These names are the product API. Provider mappings live in `providers/registry.json` and provider adapter files.

## Roles and subagents

PEOS does not use four always-present agents. `product-engineering-lead` is the front door and invokes only the specialist lenses needed for the current stage:

- Product optimizes problem clarity, value, scope, evidence, and MVP learning.
- Architect protects system integrity, boundaries, compatibility, operability, and reversibility.
- Frontend, backend, and infrastructure specialists load their own rules only when affected.
- Reviewer independently checks the approved intent against the implementation and evidence.

Claude can expose these as native plugin agents. Codex skills use the same files as role contracts and may delegate to subagents when the runtime supports it. In both cases, roles are reasoning boundaries; skills are repeatable capabilities.

## Artifact lifecycle and approvals

Work lives under `peos/changes/<change-id>/`. Draft artifacts may be edited collaboratively by product and engineering contributors. Approval fields are explicit. An agent must not mark human approval, silently change an approved requirement, or merge/publish on someone’s behalf.

Product contributors can shape work and open pull requests. Engineers make final decisions and approvals for implementation, architecture, security, data, and operations. `/learn` never trains an opaque memory: it proposes a normal Git diff to product or engineering guidelines, with evidence and an owner review.

## Team distribution

### Claude Code and Claude Teams

Host this repository on GitHub. Developers can add and install it with:

```text
/plugin marketplace add YOUR_ORG/product-engineering-os
/plugin install product-engineering-os@product-engineering-os
```

For a client repository, `configure-claude-project.py` safely merges the project-scoped marketplace and enabled-plugin settings into `.claude/settings.json`; review and commit that file. When developers trust the folder, Claude prompts them to install the approved marketplaces/plugins. See [the client customization guide](docs/CUSTOMIZING-CLIENTS.md). For managed organizations, use Claude’s plugin marketplace controls to restrict approved sources. Private repositories use each developer’s existing Git credentials.

### Codex and ChatGPT workspaces

For individual local testing:

```sh
codex plugin marketplace add /absolute/path/to/product-engineering-os
codex plugin add product-engineering-os@product-engineering-os
```

For workspace rollout, an admin opens **Manage → Plugins → Add → Import marketplace**, selects this GitHub repository, and leaves the path empty because `.agents/plugins/marketplace.json` is at the repository root. The admin then chooses whether PEOS is available or installed for each role. GitHub can be private, and workspace synchronization supplies updates after changes reach the configured branch.

PEOS does not bundle MCP servers in the MVP. That keeps the plugin usable beyond desktop-only runtimes and prevents accidental credential distribution.

## Releasing

Prepare a version on a short-lived branch:

```sh
./scripts/prepare-release.sh 0.2.0
```

Review and merge that pull request. Then, from a clean, current `main`:

```sh
./scripts/publish.sh 0.2.0
```

The publish script validates the package and pushes an annotated Git tag. It does not create or configure a GitHub repository for you.

## Customizing a client

Customize the generated `peos/` overlay, not the plugin copy. The normal order is:

1. Map repositories, boundaries, commands, owners, and risk thresholds in `peos/config.yaml`.
2. Edit product and discipline guidelines in `peos/guidelines/`.
3. Add templates or provider adapters only when the defaults are insufficient.
4. Protect the client overlay through `CODEOWNERS` and pull-request checks.

Resolution order is **client overlay → detected repository evidence → bundled defaults**. Secrets and database credentials never belong in PEOS configuration. Full examples and upgrade rules are in [Customizing clients](docs/CUSTOMIZING-CLIENTS.md).

## Repository map

| Path | Purpose |
| --- | --- |
| `.claude-plugin/marketplace.json` | Claude marketplace catalog for the repository |
| `.agents/plugins/marketplace.json` | Codex/ChatGPT workspace marketplace catalog |
| `plugins/product-engineering-os/.claude-plugin/plugin.json` | Claude plugin manifest and native-agent exposure |
| `plugins/product-engineering-os/.codex-plugin/plugin.json` | Codex plugin manifest and shared-skill exposure |
| `plugins/product-engineering-os/skills/` | Stable user-facing capability wrappers |
| `plugins/product-engineering-os/agents/` | Specialist role contracts; native agents in Claude and role lenses elsewhere |
| `plugins/product-engineering-os/contracts/` | Versioned normalized artifact and lifecycle contracts |
| `plugins/product-engineering-os/providers/` | Replaceable BMAD/native mappings behind the wrappers |
| `plugins/product-engineering-os/defaults/project/peos/` | Sensible, copyable client overlay |
| `plugins/product-engineering-os/references/` | Runtime, routing, governance, and security instructions |
| `docs/` | Architecture, client customization, rollout, and testing guides |
| `scripts/` | Validate, install, scaffold, version, and publish automation |
| `evals/` | Human-readable acceptance scenarios for framework behavior |

For dependency direction, read [Architecture](docs/ARCHITECTURE.md). For the responsibility of every shipped file, read the [File map](docs/FILE-MAP.md). For rollout and platform administration, read [Rollout](docs/ROLLOUT.md).

## Current boundaries

- BMAD must be installed separately; `install-local.sh` does this for supported CLIs.
- BMAD is never vendored or redistributed by PEOS; its versioning, licensing, and updates remain upstream-owned.
- Jira, Confluence, AWS, logs, and database access are adapters, not embedded credentials. The agent uses only tools already authorized in the user’s runtime. `/diagnose` provides the governed read-only procedure when those adapters are enabled.
- External writes require explicit user intent and a read-back. Production infrastructure and database mutation are never implied by a PEOS workflow stage.
- The initial release is private/internal and intentionally has no open-source license. Choose a license before public redistribution.
