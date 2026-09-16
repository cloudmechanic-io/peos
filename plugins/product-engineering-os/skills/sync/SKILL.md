---
name: sync
description: Preview or publish approved PEOS requirements, ADRs, delivery plans, epics, and tickets to configured Jira, Confluence, or wiki adapters with explicit authority and read-back.
---

# Synchronize approved artifacts

Use only when the user asks to create, update, preview, or reconcile external Jira/Confluence or other configured work-management/wiki content.

## Required context

Read:

- `../../references/runtime-conventions.md`
- `../../references/governance.md`
- `../../references/security-and-integrations.md`
- `../../contracts/sync-record.md`
- `../../providers/native/sync.md`

## Procedure

1. Confirm the exact source artifact/revision, approval state, destination, content type, and create/update/preview intent.
2. Read client integration configuration. Never assume a universal Jira/Confluence schema; resolve project, space, issue types, fields, hierarchy, and mappings from the client adapter or ask for the missing material choice.
3. Produce a preview when writes are disabled, tools are absent, or approval is insufficient.
4. When explicitly authorized and connected, perform the smallest external write.
5. Read the result back, compare it with the source, and record canonical identifiers, links, timestamps, and divergence in `sync-record.md`.

Do not treat synchronization as product approval, merge, deployment, or completion. Never publish secrets or unnecessary internal implementation detail.
