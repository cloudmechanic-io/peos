# PEOS native adapter: sync

Read `references/security-and-integrations.md` and client integration configuration. Determine source artifact, revision, approval state, destination, and requested create/update/preview action. If no authorized tool is available, produce a preview or exact next setup requirement; never simulate success.

When authorized, use the runtime’s existing Jira/Confluence or other approved connector. Apply the client mapping rather than a hard-coded `jira-confluence.yaml`. Read the remote item back, compare it with the source, and normalize the result to `contracts/sync-record.md`.
