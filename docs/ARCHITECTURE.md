# Architecture

This document is also the development handover for PEOS maintainers. `README.md` explains how contributors use the product, and `FILE-MAP.md` inventories every shipped file. This guide explains how the layers execute together, which owner controls each layer, and how to evolve the framework without breaking its public workflow.

## System type

PEOS is a documentation-driven agent plugin, not an application service. Claude or Codex supplies the agent loop and tool execution. PEOS supplies stable capabilities, specialist roles, normalized contracts, lifecycle and approval policy, provider selection, client defaults, and integration boundaries.

The repository therefore treats its instruction files as runtime components:

- a **skill** is a stable capability and procedure;
- an **agent** is a role, reasoning boundary, and handoff contract;
- a **contract** defines provider-independent output and lifecycle semantics;
- a **provider adapter** implements a capability without changing its public meaning;
- a **reference** contains shared runtime policy;
- the **client overlay** contains organization-owned configuration, context, guidelines, templates, and artifacts.

There is no central PEOS service, database, or hidden workflow state. Durable state lives in Git artifacts and approved external projections.

## Ownership boundaries

| Zone | Owner | Change model |
| --- | --- | --- |
| PEOS distribution | PEOS maintainers | Versioned plugin release |
| BMAD or another external provider | Upstream provider maintainers | Separately installed and tested dependency |
| Client `peos/` overlay | Customer product and engineering owners | Normal client pull requests |
| Claude, Codex, connectors, and credentials | Client runtime/tool administrators | Existing platform authorization and policy |

`defaults/project/peos/` is copied once into a client repository. After scaffolding, the copied files belong to the client and are not overwritten by plugin upgrades. Likewise, `providers/bmad/` contains only PEOS-owned invocation and normalization glue; BMAD implementation remains outside this repository.

## Core decision

PEOS is an operating layer, not a competing implementation of BMAD, OpenSpec, Spec Kit, or Superpowers.

```text
people and agents
       |
       v
stable PEOS capabilities: guide / shape / design / plan / build / diagnose / verify / sync / learn
       |
       +--> lifecycle, approvals, normalized artifact contracts
       +--> role router --> product / architect / FE / BE / infra / reviewer
       +--> provider registry --> BMAD today / another provider later
       +--> client overlay --> organization rules and repository evidence
       +--> authorized integrations --> Jira / Confluence / AWS / logs / databases
```

The dependency arrows point inward: a public skill may read a capability contract and call a provider adapter; a provider adapter must not redefine the public workflow. Client configuration selects providers but must not require contributors to invoke them directly. BMAD is resolved at runtime from its separately installed plugin. Its implementation is never copied into PEOS; the `providers/bmad/` directory contains PEOS-owned glue only. See `DEPENDENCY-POLICY.md`.

## Request execution

A request normally traverses the system in this order:

```text
Claude or Codex marketplace
    -> platform plugin manifest
    -> public skill
    -> shared runtime, routing, governance, and security references
    -> normalized capability contract
    -> provider registry
    -> selected provider adapter
    -> affected role contracts and client guidelines
    -> repository or authorized operational evidence
    -> normalized artifact in the client peos/ overlay
```

For example, `shape` loads the product-requirement contract, the product role, client product guidance, and the configured provider. With the default provider, its BMAD adapter selects the appropriate BMAD discovery entrypoint. Provider output is then reduced to one PEOS requirement; it does not create a second provider-owned artifact hierarchy.

## Why BMAD plus delta specifications

BMAD provides broad product discovery, PRD, architecture, planning, implementation, and review workflows with distinct product and engineering perspectives. OpenSpec’s strongest contribution for this brownfield use case is the explicit change delta. PEOS therefore uses BMAD as the default provider and requires every normalized technical change to state ADDED, MODIFIED, REMOVED, and RENAMED behavior.

This is composition, not two parallel methodologies: the team sees one PEOS lifecycle and one artifact set.

## Runtime model

The lead is a router, not a universal expert with every rule permanently loaded. At each stage it loads:

1. the public capability contract;
2. the current artifact and lifecycle state;
3. the selected provider adapter;
4. only the affected specialist role and guideline files;
5. repository evidence needed for the decision.

This preserves distinct product, architecture, frontend, backend, infrastructure, and review reasoning while controlling context and token use.

## Artifact model

The durable system of record is Git. All artifacts carry a contract version, change identifier, status, ownership, approval, and provenance. Jira and Confluence are projections: `/sync` publishes an approved version and records the remote link, but the source remains reviewable beside the code.

An ADR records a durable decision, not every feature. It is required when a change introduces or reverses a hard-to-change system boundary, technology, data ownership rule, cross-repository contract, security model, or operational constraint. Small changes keep technical details in the ticket/change spec.

## Learning model

PEOS learns through explicit policy proposals:

```text
human review -> observed pattern -> proposed guideline diff -> owner review -> merge -> future runs
```

It never silently updates hidden memory from a reviewer comment. Product feedback updates product guidelines; implementation, security, and operational feedback update the corresponding engineering guideline. One-off preferences remain review notes unless a human promotes them.

## Integration boundary

The plugin contains no credentials and grants no authority. An adapter may use an already-authorized connector, MCP server, CLI, or API. Default permissions are read-only for AWS/log/database diagnostics. Mutations, Jira/Confluence publication, deployments, and database writes require explicit user intent and the controls of the underlying tool.

## File responsibilities

- `skills/*/SKILL.md`: stable capability entrypoints and postconditions.
- `contracts/*.md`: provider-independent output shape and lifecycle semantics.
- `providers/registry.json`: capability-to-provider selection and fallback metadata.
- `providers/dependencies.json`: external provider identity, distribution, ownership, and failure policy.
- `providers/bmad/*.md`: exact BMAD invocation and normalization rules.
- `providers/native/*.md`: small PEOS-owned operations where no external method is needed.
- `agents/*.md`: role goals, tensions, scope, and handoff expectations.
- `defaults/project/peos/`: upgrade-safe client overlay scaffold.
- `references/*.md`: shared runtime rules deliberately not duplicated in every skill.

See `FILE-MAP.md` for every shipped file and the exact responsibility of each one.

## Maintaining the framework

### Choose the correct layer

| Intended change | Owning layer |
| --- | --- |
| Public capability behavior, required context, or postcondition | `skills/` |
| Artifact shape, lifecycle, approval, or provenance | `contracts/` |
| BMAD entrypoint selection or output normalization | `providers/bmad/` |
| PEOS-owned setup, routing, diagnosis, synchronization, or learning procedure | `providers/native/` |
| Specialist objective, concerns, boundaries, or handoff | `agents/` |
| Rule shared by multiple capabilities | `references/` |
| Defaults for newly scaffolded clients | `defaults/project/peos/` |
| Organization-specific rule | Client-owned `peos/` overlay |
| Platform discovery and presentation | Marketplace/plugin manifests |
| Package and release automation | Root `scripts/` |

Do not solve a client customization by changing global runtime policy, or solve provider behavior by leaking provider commands into a public skill.

### Add a public capability

Adding a capability changes the product API. A complete addition requires:

1. `skills/<capability>/SKILL.md` with valid frontmatter and postconditions;
2. a normalized output contract;
3. a default provider adapter;
4. a registry mapping from capability to contract/provider/adapter;
5. the capability in `CAPABILITIES` inside `scripts/validate.py`;
6. client configuration when provider selection is configurable;
7. behavioral scenarios and documentation;
8. a semantic-version decision.

A command without artifact, lifecycle, approval, validation, and failure semantics is not a complete PEOS capability.

### Change a provider

Keep the public capability name and contract stable. Change the thin adapter and dependency declaration where required, then test in-flight artifacts and behavioral scenarios. Provider-native temporary output should not become a second permanent document set.

Never copy an upstream implementation into PEOS to make customization easier. Configure the provider, contribute upstream, or replace the adapter.

### Change a role

Define the role's objective, tensions, evidence expectations, boundaries, and return shape. Update routing evidence and only the skills that need it. Discipline conventions belong in client guidelines rather than being duplicated in the role contract.

### Change a client default

Test a freshly scaffolded overlay. Existing client overlays do not receive the default automatically. Provide a deliberate migration or learning proposal when an existing organization should adopt the change.

### Add an integration

An integration needs an authorized runtime connector, client-owned mapping, least-privilege and environment controls, bounded operations, redaction, read-back for writes, visible no-access behavior, and evaluation scenarios. A configuration flag does not grant authority, and credentials never belong in PEOS files.

### Change a contract

Treat contracts as APIs. Identify in-flight artifacts and templates, preserve interpretation of old revisions or publish migration guidance, and never silently rewrite an approved artifact to a new revision.

## Validation and release handover

`scripts/validate.py` proves package structure and invariants: manifests, version consistency, skills, registry references, required files, BMAD dependency/no-vendoring rules, symlink restrictions, and unresolved markers. `scripts/validate.sh` also invokes Claude's native validation when available.

Static validation does not prove agent behavior. Run relevant cases from `evals/scenarios.md` in fresh Claude and Codex sessions and perform the overlay upgrade test in `TESTING.md` when defaults, contracts, or provider behavior changes.

PEOS uses trunk-based development. `main` stays releasable. `scripts/prepare-release.sh` creates a short-lived release branch after updating versions and the changelog; after review and merge, `scripts/publish.sh` validates `main` and publishes an annotated tag. The scripts require a configured Git remote, clean current `main`, push access, and a non-empty `Unreleased` changelog section.

Before merging a framework change, confirm that it belongs in the selected layer, preserves the provider-neutral API and client overlays, keeps human approvals explicit, updates behavioral scenarios where necessary, and does not turn validation, publication, deployment, or live verification into interchangeable claims.

## Versioning

Plugin versions use semantic versioning. Capability contract revisions are explicit within artifacts. A breaking contract change requires a major plugin release and migration notes; adding an optional field is minor; wording and bug fixes are patch changes.
