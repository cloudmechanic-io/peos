---
name: learn
description: Convert repeated human review and delivery outcomes into minimal evidence-backed proposals for product or engineering guidelines without silent memory or self-approval.
---

# Learn from human review

Use when a user explicitly asks PEOS to learn, capture a repeated review correction, update engineering/product guidance, or analyze delivery feedback for a reusable rule.

## Required context

Read:

- `../../references/runtime-conventions.md`
- `../../references/governance.md`
- `../../contracts/learning-proposal.md`
- `../../providers/native/learn.md`
- the relevant client guideline and supplied/authorized review evidence.

## Procedure

1. Restate the observed review or outcome without exposing sensitive data.
2. Classify it as one-off, change-specific, or reusable. Look for repetition, impact, scope, counterexamples, and conflicts with existing guidance.
3. For one-off feedback, retain it in the review/change artifact and do not create a global rule.
4. For reusable feedback, choose the narrowest product, engineering, frontend, backend, infrastructure, security, or quality guideline.
5. Draft a minimal diff and a learning proposal with evidence, examples, counterexamples, owner, review criteria, and removal condition.
6. Run relevant validation and present the Git diff for human review. Leave approval empty.

Never modify installed plugin defaults or claim the model has been trained. Learning becomes effective only when humans merge the client guideline change.
