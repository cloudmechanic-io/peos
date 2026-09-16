---
name: diagnose
description: Investigate incidents, AWS and application logs, observability signals, or database questions through bounded read-only evidence gathering with redaction and explicit environment controls.
---

# Diagnose behavior and data

Use when the user asks why a system behaves a certain way, requests production/log/AWS investigation, or wants to query operational data through an approved connection. Diagnosis does not imply implementation.

## Required context

Read:

- `../../references/runtime-conventions.md`
- `../../references/security-and-integrations.md`
- `../../contracts/diagnostic-report.md`
- `../../providers/native/diagnose.md`
- only affected backend and/or infrastructure role contracts and client guidelines.

## Procedure

1. Confirm symptoms or question, impact, environment/account, service or data domain, time window, and authorization. Resolve any production-versus-test ambiguity before querying.
2. Inspect the client system map and repository evidence needed to interpret telemetry or schemas. Do not assume conventional tables, fields, services, or regions.
3. Build a small hypothesis tree and identify the cheapest safe evidence that distinguishes each branch.
4. Use only enabled, already-authorized adapters. Bound time, result volume, query cost, fields, and account/region. Prefer read-only metadata or aggregates and redact sensitive data.
5. Separate observations from inference, update hypotheses, and stop when evidence supports a useful conclusion or the next access/data requirement is clear.
6. Normalize material investigations to `peos/diagnostics/<diagnostic-id>.md`, including exact sanitized queries/commands, confidence, limitations, and residual risk.

Return root cause or ranked hypotheses, evidence, safe immediate mitigations, and durable follow-up. Route an authorized code change through `guide`; never mutate production or a database as part of diagnosis.
