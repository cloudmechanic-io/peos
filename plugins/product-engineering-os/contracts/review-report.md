# Verification report contract v1

The normalized report is `peos/changes/<change_id>/review-report.md`.

It includes:

- reviewed revision and approved artifact revisions;
- acceptance-criteria traceability;
- automated test, lint, type, build, and static-analysis results;
- QA scenarios and observed results;
- architecture and cross-repository consistency checks;
- security, privacy, abuse, dependency, secret, and infrastructure checks as applicable;
- API/data/event backwards-compatibility and migration checks;
- rollout, rollback, monitoring, and operational-readiness checks;
- findings ranked by severity with evidence and ownership;
- explicit `PASS`, `FAIL`, `OPEN`, or `NOT APPLICABLE` decision for each gate;
- checks not run and residual risk.

Review must be independent from implementation reasoning where the runtime supports a separate context or subagent. A passing report does not merge, deploy, or approve on behalf of a human.
