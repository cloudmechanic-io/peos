# Client PEOS overlay

This directory contains organization-owned configuration, context, guidelines, artifacts, and decisions. It overrides bundled PEOS defaults and remains unchanged when the plugin upgrades.

- `config.yaml`: repositories, providers, governance, validation, and integration switches.
- `context/system-map.md`: evidence-based boundaries and commands for the umbrella project.
- `guidelines/`: product and discipline-specific rules loaded only when relevant.
- `templates/`: client-adjustable normalized artifact layouts.
- `providers/`: optional custom adapters that preserve public capability contracts.
- `changes/`: one folder per active or completed change.
- `diagnostics/`: bounded read-only incident and data investigations.
- `decisions/`: durable architecture decisions.

All changes to this overlay should use the same pull-request and ownership controls as production code. Never store secrets here.
