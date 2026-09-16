# Customizing clients

PEOS is convention over configuration: a client can install it and use the defaults immediately. Customization is an overlay in the client’s umbrella repository, never a fork of the plugin.

## Bootstrap

```sh
./scripts/scaffold-client.sh /absolute/path/to/client-umbrella "Client Name"
```

Commit the resulting `peos/` directory to the client repository. Product and engineering owners should review the initial pull request.

For a plug-and-play Claude prompt in that repository, also run:

```sh
./scripts/configure-claude-project.py /absolute/path/to/client-umbrella YOUR_ORG/product-engineering-os
```

The script merges PEOS and BMAD marketplace entries without replacing unrelated Claude settings, and refuses conflicting entries. Review and commit `.claude/settings.json`. Codex/ChatGPT distribution is normally workspace-admin managed, so it does not require a client repository file.

## What to customize first

### 1. System map and commands

Edit `peos/config.yaml` and `peos/context/system-map.md` with:

- repository paths and owned capabilities;
- build, lint, test, type-check, security, and infrastructure validation commands;
- API/event/data contracts shared across repositories;
- owners and approval rules;
- change-size and risk thresholds.

Do not put secrets, tokens, jump-host keys, connection strings, or personal paths in these files.

### 2. Product guidelines

Use `peos/guidelines/product.md` for customer, market, terminology, analytics, accessibility, experimentation, and scope principles. This is where product review learning lands.

### 3. Engineering guidelines

Keep cross-cutting rules in `engineering.md`. Put React/component rules only in `frontend.md`, API/data rules only in `backend.md`, AWS/IaC rules only in `infrastructure.md`, and independent gates in `security.md` and `quality.md`. The router loads only relevant files.

### 4. Approval policy

Tune `governance` in `config.yaml`. Product contributors may approve product intent when the client allows it. Engineering owners always control code, architecture, security, data, and production operations.

### 5. Providers and integrations

Defaults use BMAD for lifecycle work and PEOS native adapters for routing, sync, and learning. To replace one capability:

1. Copy `peos/providers/provider.example.md` to a client-owned adapter file.
2. Preserve the referenced capability’s inputs, output contract, status transitions, and approval semantics.
3. Point only that capability’s `provider` value in `peos/config.yaml` to `file:peos/providers/<adapter>.md`.
4. Add evaluation scenarios and migrate in-flight artifacts deliberately.

Client customization must not copy or modify BMAD internals. Configure the external provider, contribute a needed change upstream, or replace the PEOS capability adapter while preserving its contract.

Jira, Confluence, AWS, logs, and database access are disabled until the runtime already has an approved connection and `config.yaml` enables the adapter. Enabling an adapter does not grant credentials or bypass tool permissions.

## Resolution and upgrades

PEOS resolves instructions in this order:

1. client `peos/` overlay;
2. evidence and local instruction files discovered in the affected repository;
3. bundled PEOS defaults.

Do not edit installed plugin cache files. Plugin upgrades can replace bundled files, while the client overlay remains in Git. When a new plugin version adds a default, compare it deliberately and adopt only the parts the client wants.

## Multi-repository umbrella guidance

Keep one overlay at the common root when the agent session can see all repositories. Map each repository with a type (`frontend`, `backend`, `infrastructure`, or `mixed`) and its commands. Repository-specific instruction files remain authoritative for local implementation details; the umbrella overlay owns cross-repository product and architecture policies.

If repositories cannot share a filesystem session, copy the minimal relevant overlay into each repository and make one repository the source of truth for cross-system ADRs.

## Recommended ownership

- Product guideline changes: product owner plus engineering representative.
- Architecture and cross-repository guidelines: architecture owner.
- Frontend/backend/infrastructure rules: respective code owners.
- Security policy: security or designated engineering owner.
- Provider adapters and capability contracts: PEOS maintainers.
