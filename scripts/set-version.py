#!/usr/bin/env python3
"""Set one PEOS version consistently across native manifests."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path


if len(sys.argv) != 2 or not re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?", sys.argv[1]):
    raise SystemExit("Usage: set-version.py <semantic-version>")

version = sys.argv[1]
root = Path(__file__).resolve().parents[1]
paths = [
    root / "plugins/product-engineering-os/.codex-plugin/plugin.json",
    root / "plugins/product-engineering-os/.claude-plugin/plugin.json",
]

for path in paths:
    document = json.loads(path.read_text(encoding="utf-8"))
    document["version"] = version
    path.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")

marketplace_path = root / ".claude-plugin/marketplace.json"
marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
marketplace.setdefault("metadata", {})["version"] = version
for plugin in marketplace.get("plugins", []):
    if plugin.get("name") == "product-engineering-os":
        plugin["version"] = version
marketplace_path.write_text(json.dumps(marketplace, indent=2) + "\n", encoding="utf-8")

changelog_path = root / "CHANGELOG.md"
changelog = changelog_path.read_text(encoding="utf-8")
match = re.search(r"^## Unreleased\s*\n(?P<body>.*?)(?=^## |\Z)", changelog, flags=re.MULTILINE | re.DOTALL)
if not match:
    raise SystemExit("CHANGELOG.md must contain an '## Unreleased' section")
body = match.group("body").strip()
if not body:
    raise SystemExit("CHANGELOG.md has no unreleased entries")
released = f"## Unreleased\n\n## {version} - {date.today().isoformat()}\n\n{body}\n\n"
changelog = changelog[: match.start()] + released + changelog[match.end() :].lstrip("\n")
changelog_path.write_text(changelog, encoding="utf-8")

print(f"Set PEOS version to {version}.")
