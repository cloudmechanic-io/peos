# Quality guidelines

- Trace every test and review gate to approved acceptance criteria or an identified engineering risk.
- Use the test pyramid appropriate to the system; prefer fast deterministic coverage and add end-to-end tests for critical journeys and integration risk.
- Cover happy path, boundaries, permissions, failure, recovery, compatibility, and migration behavior.
- Run repository-native format, lint, type, unit, integration, build, security, and infrastructure checks when relevant.
- Review architecture consistency and duplicated rules across repositories, not only local code style.
- Record exact commands, scope, outcomes, skipped checks, flakiness, and residual risk.
- Separate “checks passed” from “deployed” and “verified live.”
- A failing or missing critical gate blocks readiness; it does not silently become not applicable.
