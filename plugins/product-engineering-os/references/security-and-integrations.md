# Security and integrations

PEOS carries process, not credentials or implicit authority.

## Default posture

- Jira, Confluence, AWS, log, and database adapters are disabled in the client overlay by default.
- Use identities and connections already authorized by the runtime and user.
- Diagnose production systems read-only first. Bound time ranges, accounts, regions, services, result counts, and query cost.
- Redact secrets, tokens, personal data, customer data, payload bodies, and connection details from artifacts and logs.
- Never place credentials, private keys, database URLs, jump-host commands containing secrets, or cloud session tokens in PEOS files.

## Database access

Prefer read replicas or read-only roles, approved tunnels, statement timeouts, row limits, explicit schemas, and queries grounded in actual migrations/entities. Explain query impact before broad scans. Database writes are outside diagnostic scope unless separately and explicitly authorized.

## Publication

Before creating or updating Jira/Confluence content, confirm the destination and artifact version. After writing, read the item back, record its canonical link and synchronization timestamp, and report any divergence. Do not treat publication as approval or deployment.

## Cloud and delivery

Inspect before changing. Separate repository validation, infrastructure plan/synthesis, deployment, and live verification as different claims. Preserve rollback paths and environment boundaries. Do not infer production access from an enabled adapter.
