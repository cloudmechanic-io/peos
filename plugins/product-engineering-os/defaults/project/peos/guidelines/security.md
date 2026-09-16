# Security guidelines

- Identify trust boundaries, actors, assets, abuse cases, and privilege changes for affected behavior.
- Enforce authentication and authorization server-side and preserve tenant isolation.
- Minimize data collection, exposure, retention, logging, and third-party transfer.
- Use approved secret stores and redact credentials, tokens, personal data, and customer payloads.
- Pin or review dependencies according to client policy; investigate material vulnerability and supply-chain changes.
- Validate input, encode output, parameterize queries, and constrain file/network/process operations at boundaries.
- Use least-privilege, short-lived, auditable identities for cloud and database diagnostics.
- Treat security tools as evidence sources, not automatic proof of safety.
- Escalate critical findings; do not weaken a gate to complete a workflow.
