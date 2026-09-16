# Infrastructure guidelines

- Infrastructure as code is the source of truth; avoid undocumented console drift.
- Separate accounts, environments, regions, identities, state, and blast radius explicitly.
- Apply least privilege and make trust relationships, network paths, encryption, secrets, and egress reviewable.
- Prefer reversible, staged changes and retain rollback or replacement paths.
- Estimate capacity, quotas, availability, recovery objectives, and cost impact for material changes.
- Define logs, metrics, traces, alarms, dashboards, and ownership before rollout.
- Validate syntax, plans/synthesis, deployment, and live behavior as distinct stages.
- Never infer production state from repository configuration alone.
- Avoid embedding credentials or environment-specific secrets in code, artifacts, logs, or agent prompts.
