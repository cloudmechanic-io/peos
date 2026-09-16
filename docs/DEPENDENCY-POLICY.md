# Dependency policy

BMAD is an external runtime dependency. It is not part of the PEOS source tree.

## Allowed

- Declare the upstream marketplace and plugin in `providers/dependencies.json`.
- Install or update BMAD independently through its official marketplace.
- Keep thin PEOS adapter files that name public BMAD skills, select an appropriate upstream entrypoint, pass PEOS inputs, and normalize results to PEOS contracts.
- Test supported BMAD upgrades against PEOS evaluation scenarios before organization rollout.

## Forbidden

- Copy BMAD prompts, agents, workflows, templates, source files, generated installers, or documentation into this repository.
- Commit `_bmad`, `.bmad`, `bmad-method`, `bmad-toolbox`, vendored, or third-party source directories.
- Fork an upstream BMAD workflow merely to change PEOS behavior.
- Modify copied upstream content through a client overlay.
- Present BMAD content as PEOS-owned intellectual property.

## Adapter boundary

A provider adapter is glue, not a fork. It may contain only:

1. the PEOS capability and contract it implements;
2. the upstream public skill or entrypoint to invoke;
3. PEOS-specific routing inputs and postconditions;
4. normalization, provenance, and failure behavior.

If an upstream behavior must change, prefer configuration supported by BMAD, contribute upstream, or replace the capability provider through the stable PEOS contract. Do not copy and edit the upstream implementation.

## Installation and failure

`scripts/install-local.sh` and the Claude project configurator install/register BMAD from `bmad-code-org/bmad-plugins` as a separate plugin. Workspace administrators must import or install that marketplace independently. When BMAD is unavailable, dependent PEOS capabilities fail visibly with installation guidance; PEOS does not fall back to a hidden copy.

BMAD retains its own versioning, licensing, release process, and update channel. PEOS release artifacts contain only PEOS-owned adapters and contracts.
