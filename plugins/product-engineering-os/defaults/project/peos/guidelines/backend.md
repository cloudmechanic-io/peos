# Backend guidelines

- Keep domain rules in one owned boundary and validate inputs at trust boundaries.
- Treat APIs, events, queues, schemas, and database changes as versioned contracts.
- Preserve compatibility for existing callers or provide an explicit consumer-aware migration.
- Define authorization, tenancy, data ownership, auditability, and privacy before persistence changes.
- Make retries, idempotency, ordering, concurrency, timeouts, and partial failure explicit for distributed work.
- Use transactions and consistency models deliberately; document invariants.
- Prefer bounded queries, indexed access paths, and migrations that are safe for live data volume.
- Emit actionable, structured, redacted telemetry with correlation identifiers.
- Test domain behavior, contract boundaries, failure paths, and migration behavior at the cheapest reliable level.
