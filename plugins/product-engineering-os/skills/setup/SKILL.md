---
name: setup
description: Initialize or audit PEOS in an umbrella repository by mapping repositories, commands, guidelines, governance, providers, and disabled integrations without overwriting client files.
---

# Setup PEOS

Use this capability when a team first installs PEOS, opens a new umbrella repository, asks to initialize or map a workspace, or wants to audit its PEOS configuration.

## Required context

Read:

- `../../references/runtime-conventions.md`
- `../../references/security-and-integrations.md`
- `../../contracts/workspace.md`
- `../../providers/native/setup.md`
- `../../agents/product-engineering-lead.md`

## Procedure

1. Locate the common root and existing `peos/config.yaml`.
2. Discover top-level repositories and local instruction files. Inspect build manifests, test configuration, infrastructure directories, existing ADRs/specs, and ownership evidence. Prune generated and dependency directories.
3. If no overlay exists, use `../../defaults/project/peos/` as the exact starting structure when writes are authorized. Replace the organization marker. Never overwrite an existing `peos/` directory.
4. Populate only evidence-backed repository paths, repository types, owned capabilities, validation commands, and cross-repository contracts. Leave unknowns explicit.
5. Keep Jira, Confluence, AWS, logs, and database adapters disabled unless the user deliberately enables an already-authorized connection.
6. Validate the result against the workspace contract and scan it for secrets.

Finish with discovered scope, unknowns, configuration changes, and an invitation to run `guide`. Do not require the client to customize defaults before the first workflow.
