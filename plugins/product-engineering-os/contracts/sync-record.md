# Synchronization contract v1

`peos/changes/<change_id>/sync-record.md` records each authorized projection:

- source artifact path, revision/commit, and approval state;
- destination system, tenant/site/project, content type, and identifier;
- action (`create`, `update`, or `read-only preview`);
- time, acting identity when observable, and canonical link;
- read-back result and any divergence;
- next synchronization responsibility.

Synchronization never changes the source approval state and never occurs merely because an artifact reached `approved`.
