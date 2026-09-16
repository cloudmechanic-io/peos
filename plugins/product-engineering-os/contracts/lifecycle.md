# Lifecycle contract v1

Every artifact begins with YAML frontmatter:

```yaml
peos:
  contract: product-requirement/v1
  change_id: example-change
  classification: quick
  status: draft
  owners: []
  approvals: []
  provider: bmad
  generated_at: 2026-01-01T00:00:00Z
  source_artifacts: []
```

Allowed classifications are `quick`, `feature`, and `strategic`. Allowed statuses and transitions are defined in `references/governance.md`. An approval entry needs a human identity, role, time, artifact revision or commit, and optional conditions. Agents leave `approvals` empty unless reading already-recorded evidence.

Use lowercase, hyphenated `change_id` values. Store change artifacts in `peos/changes/<change_id>/` and ADRs in `peos/decisions/`.
