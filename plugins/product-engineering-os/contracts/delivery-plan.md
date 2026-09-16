# Delivery plan contract v1

The normalized plan is `peos/changes/<change_id>/delivery-plan.md`.

Each delivery slice states outcome, scope, affected repositories, dependencies, owner lens, acceptance-criteria links, validation, rollout/rollback impact, and completion evidence. Prefer independently reviewable vertical slices over horizontal layer batches. Call out sequencing across repositories and temporary compatibility states.

The plan distinguishes prerequisite decisions, implementation slices, integration work, verification, publication, deployment, and live validation. A repository check passing is not equivalent to deployment or production verification.
