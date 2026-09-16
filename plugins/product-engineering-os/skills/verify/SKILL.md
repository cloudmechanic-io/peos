---
name: verify
description: Independently verify a PEOS implementation against requirements, technical deltas, tests, QA, architecture, security, compatibility, migration, and operational readiness.
---

# Verify the change

Use for pre-merge review, quality gates, security and architecture checks, backwards-compatibility review, QA, or release-readiness assessment.

## Required context

Read:

- `../../references/runtime-conventions.md`
- `../../references/governance.md`
- `../../references/security-and-integrations.md`
- `../../contracts/lifecycle.md`
- `../../contracts/review-report.md`
- `../../agents/reviewer.md`
- relevant client security, quality, and affected discipline guidelines.

Resolve the provider through `../../providers/registry.json`; the default adapter is `../../providers/bmad/verify.md`.

## Procedure

1. Use a fresh reviewer context or bounded reviewer subagent when available. Review the actual diff/revision, not the implementer’s summary alone.
2. Trace every acceptance criterion and technical delta to implementation and evidence.
3. Run authorized repository-native format, lint, type, unit, integration, build, static-analysis, dependency, secret, security, and infrastructure checks as applicable.
4. Exercise user journeys, boundary conditions, permissions, failure/recovery, migration, compatibility, rollback, and observability proportional to risk.
5. Check architecture and business-rule consistency across affected repositories.
6. Rank findings by severity with exact evidence and ownership. Never lower severity to obtain a pass.
7. Normalize to `review-report.md`, giving each gate `PASS`, `FAIL`, `OPEN`, or `NOT APPLICABLE`, and list checks not run and residual risk.

Only mark lifecycle status `verified` when all required gates pass. Human code and release approvals remain separate.
