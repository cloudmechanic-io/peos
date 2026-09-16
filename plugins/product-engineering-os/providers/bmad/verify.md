# BMAD adapter: verify

Use `bmad-code-review` for adversarial implementation review and `bmad-qa-generate-e2e-tests` when end-to-end coverage is relevant. Combine these with repository-defined validation commands and PEOS review gates; BMAD output alone is not a pass.

Use an independent reviewer context or subagent when available. Trace implementation to acceptance criteria and change deltas, then assess automated checks, QA, architecture, security/privacy, dependencies, infrastructure, backwards compatibility, migration, rollback, observability, and operational readiness. Normalize to `contracts/review-report.md` and state checks not run.

If BMAD is unavailable, report the missing provider and installation command without changing the public capability.
