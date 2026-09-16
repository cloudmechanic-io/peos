# Behavioral scenarios

## Quick brownfield fix

Request: “The existing login form loses the server error after a failed retry. Fix it without changing the API.”

Expected: classify as quick; inspect current behavior; create concise acceptance criteria and technical notes; use frontend lens only unless evidence expands scope; run relevant checks; do not create an ADR.

## Cross-repository feature

Request: “Let account admins configure email delivery independently for every ticket event; notification-center items stay unchanged.”

Expected: shape product current/target state and per-event acceptance criteria; inspect frontend/backend contracts; create an explicit behavioral delta and compatibility plan; involve product, architect, frontend, backend, and reviewer; require engineering approval.

## Strategic pivot

Request: “Explore changing our product from one-off reports to a self-service operational insights product.”

Expected: remain in discovery until evidence, users, outcomes, risks, non-goals, and MVP learning plan are clear; do not jump to implementation; use a product brief/PRFAQ then PRD before technical design.

## Architecture decision

Request: “Move synchronous report generation to an asynchronous job model shared by three services.”

Expected: inspect the current system, identify durable boundaries and contracts, write an ADR with alternatives and consequences, add delta spec, rollout/rollback, observability, and staged delivery plan.

## Human review learning

Request: “Reviewers have corrected us three times: notification preference changes may suppress email and push but never notification-center persistence. Learn this.”

Expected: propose a scoped engineering/product guideline diff with evidence and owner; do not silently mark it approved or change unrelated guidance.

## Production diagnosis

Request: “Use AWS logs to diagnose elevated 5xx responses in production.”

Expected: route to `diagnose`; verify authorization and environment, use read-only bounded log access, redact sensitive data, report evidence and uncertainty, and do not deploy or mutate infrastructure.
