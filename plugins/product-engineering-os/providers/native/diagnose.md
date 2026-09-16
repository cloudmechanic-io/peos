# PEOS native adapter: diagnose

Read client system context, security/integration rules, and the diagnostic contract. Verify the exact account/environment, service or dataset, time window, authorization, and data-sensitivity boundary before using connected tools.

Start from symptoms and a hypothesis tree. Use repository evidence plus the smallest bounded read-only AWS, log, observability, or database query that can distinguish hypotheses. Prefer metadata and aggregates before payloads; redact sensitive values. Re-check assumptions when evidence conflicts.

Normalize material work to `contracts/diagnostic-report.md`. Stop after evidence, root-cause confidence, safe mitigations, and follow-up options. A code or infrastructure fix routes through `guide`/`shape`/`design`/`build`; production or database mutation requires separate explicit authority.
