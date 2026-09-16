# Governance

## Decision rights

- Product contributors may draft requirements, acceptance criteria, prioritization, and evidence.
- Named product owners approve product intent when client policy permits.
- Engineers approve code, technical design, architecture, data, security, operations, and release readiness.
- Agents may recommend status transitions but never impersonate a human approver.

## Artifact states

`draft -> in-review -> approved -> implementing -> implemented -> verified -> closed`

`blocked` may be used from any active state with a reason and owner. A material scope change returns affected approved artifacts to `draft` or creates a revision. Verification failure returns work to `implementing` or `blocked`; it does not weaken the acceptance criteria.

## Change control

- Git is the authoritative review and audit trail.
- An ADR is required only for a durable, hard-to-reverse decision involving system boundaries, technology, data ownership, security model, public contracts, or operational constraints.
- Generated Jira and Confluence items are projections of approved Git artifacts.
- External writes, deployments, merges, production commands, and data mutation require explicit user intent and applicable human controls.

## Learning

Human review is evidence, not automatically a rule. `/learn` classifies feedback as one-off, change-specific, or reusable; proposes the smallest guideline diff; cites source review or outcome; chooses a product or engineering owner; and leaves the proposal unapproved until reviewed through Git.
