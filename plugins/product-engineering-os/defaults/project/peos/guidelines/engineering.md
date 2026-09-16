# Engineering guidelines

- Inspect existing code, contracts, tests, migrations, and operations before designing a target state.
- Preserve backwards compatibility or provide an explicit staged migration and rollback.
- Prefer small, reversible vertical slices with clear ownership and observable behavior.
- Keep domain boundaries and sources of truth explicit; avoid duplicate business rules.
- Treat API, event, schema, configuration, and infrastructure changes as contracts.
- Design failure behavior, idempotency, concurrency, retries, timeouts, and observability where applicable.
- Do not conflate validation, deployment, and live verification.
- Preserve unrelated human work and avoid broad rewrites without an approved reason.
- Record durable, hard-to-reverse decisions in ADRs; keep local implementation notes with the change.
- State assumptions, residual risk, and checks not run.
