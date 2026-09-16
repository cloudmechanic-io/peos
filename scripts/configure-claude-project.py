#!/usr/bin/env python3
"""Safely register PEOS and BMAD in a client's project-scoped Claude settings."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


if len(sys.argv) != 3:
    raise SystemExit("Usage: configure-claude-project.py <client-root> <github-owner/repository>")

client_root = Path(sys.argv[1]).expanduser().resolve()
repository = sys.argv[2]
if not client_root.is_dir():
    raise SystemExit(f"Client root does not exist: {client_root}")
if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
    raise SystemExit("GitHub source must use owner/repository format")

settings_dir = client_root / ".claude"
settings_path = settings_dir / "settings.json"
settings_dir.mkdir(exist_ok=True)

if settings_path.exists():
    try:
        settings = json.loads(settings_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Existing Claude settings are invalid JSON: {exc}") from exc
    if not isinstance(settings, dict):
        raise SystemExit("Existing Claude settings must contain a JSON object")
else:
    settings = {}

marketplaces = settings.setdefault("extraKnownMarketplaces", {})
enabled = settings.setdefault("enabledPlugins", {})
if not isinstance(marketplaces, dict) or not isinstance(enabled, dict):
    raise SystemExit("Existing extraKnownMarketplaces and enabledPlugins values must be objects")

desired_marketplaces = {
    "product-engineering-os": {
        "source": {"source": "github", "repo": repository}
    },
    "bmad": {
        "source": {"source": "github", "repo": "bmad-code-org/bmad-plugins"}
    },
}

for name, value in desired_marketplaces.items():
    existing = marketplaces.get(name)
    if existing is not None and existing != value:
        raise SystemExit(f"Refusing to replace conflicting marketplace {name!r} in {settings_path}")
    marketplaces[name] = value

enabled["product-engineering-os@product-engineering-os"] = True
enabled["bmad-method@bmad"] = True

temporary_path = settings_path.with_name("settings.json.peos-new")
temporary_path.write_text(json.dumps(settings, indent=2) + "\n", encoding="utf-8")
temporary_path.replace(settings_path)

print(f"Configured project-scoped Claude marketplaces in {settings_path}")
print("Commit this file after review; contributors will be prompted when they trust the repository.")
