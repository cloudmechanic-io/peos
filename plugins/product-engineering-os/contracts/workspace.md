# Workspace setup contract v1

Setup must produce or validate:

- `peos/config.yaml` with organization name, repository map, providers, governance, validation, and disabled-by-default integrations;
- `peos/context/system-map.md` with evidence-based repository and contract boundaries;
- scoped product, engineering, frontend, backend, infrastructure, security, and quality guidelines;
- `peos/changes/` and `peos/decisions/` documentation;
- no secrets and no overwrite of existing client files.

Setup reports what was discovered, what remains unknown, any conflicting repository instructions, and the first recommended workflow. It may create the overlay only when workspace writes are authorized.
