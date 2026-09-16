# Diagnostic report contract v1

Store a material investigation as `peos/diagnostics/<diagnostic-id>.md` or link it from the active change.

It contains scope, environment, time window, authorization boundary, symptoms and impact, current known architecture, observations with timestamps/sources, hypothesis tree, bounded queries or commands with sensitive values redacted, findings separated from inference, root cause confidence, immediate safe mitigations, proposed durable follow-up, residual risk, and checks/data not available.

Diagnosis is read-only by default. A recommendation is not an implemented fix, deployment, database mutation, or verified recovery.
