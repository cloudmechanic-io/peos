# Architecture

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

The dependency arrows point inward: a public skill may read a capability contract and call a provider adapter; a provider adapter must not redefine the public workflow. Client configuration selects providers but must not require contributors to invoke them directly.

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
- `providers/bmad/*.md`: exact BMAD invocation and normalization rules.
- `providers/native/*.md`: small PEOS-owned operations where no external method is needed.
- `agents/*.md`: role goals, tensions, scope, and handoff expectations.
- `defaults/project/peos/`: upgrade-safe client overlay scaffold.
- `references/*.md`: shared runtime rules deliberately not duplicated in every skill.

## Versioning

Plugin versions use semantic versioning. Capability contract revisions are explicit within artifacts. A breaking contract change requires a major plugin release and migration notes; adding an optional field is minor; wording and bug fixes are patch changes.
