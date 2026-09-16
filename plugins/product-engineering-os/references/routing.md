# Workflow routing

Use risk and ambiguity, not word count, to select the workflow.

## Quick

Use when the desired behavior is clear, the change is local, no durable architectural decision is introduced, and rollback is straightforward. Produce acceptance criteria and concise technical notes in one product requirement, then build and verify. An ADR is normally unnecessary.

Escalate out of quick when repository inspection reveals cross-service contracts, data migration, security/privacy impact, public API compatibility, uncertain product behavior, or difficult rollback.

## Feature

Use for a meaningful new or changed user capability within the existing product. Produce a PRD with product current/target state, a technical change spec with explicit deltas, an ADR only when the decision meets ADR criteria, and a sliced delivery plan.

## Strategic

Use for pivots, new product surfaces, high ambiguity, major platform or data ownership changes, or investments requiring discovery before commitment. Start with brainstorming/research and a product brief or PR/FAQ. Approve the PRD before detailed technical design.

## Specialist routing

| Evidence or affected surface | Required lens |
| --- | --- |
| User problem, scope, KPI, experiment, acceptance criteria | Product |
| Cross-repository boundary, contract, data ownership, durable tradeoff | Architect |
| UI, React, accessibility, client state, browser/mobile behavior | Frontend |
| API, domain logic, persistence, asynchronous processing | Backend |
| Cloud, IAM, networking, CI/CD, observability, IaC | Infrastructure |
| Any implementation before completion | Reviewer |

Use multiple specialists only when the evidence crosses those boundaries. The product lens should challenge excess scope; the architecture lens should challenge unsafe shortcuts. The lead resolves the tension against approved outcomes and governance.
