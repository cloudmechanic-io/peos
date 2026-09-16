#!/usr/bin/env python3
"""Validate PEOS packaging and cross-platform invariants using only stdlib."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "product-engineering-os"
NAME = "product-engineering-os"
DESCRIPTION = "A governed product-engineering operating layer for human-agent teams."
CAPABILITIES = {
    "setup",
    "guide",
    "shape",
    "design",
    "plan",
    "build",
    "diagnose",
    "verify",
    "sync",
    "learn",
}

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def load_json(relative: str) -> dict:
    path = ROOT / relative
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing JSON file: {relative}")
        return {}
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {relative}: {exc}")
        return {}
    if not isinstance(value, dict):
        fail(f"expected JSON object in {relative}")
        return {}
    return value


codex_manifest = load_json("plugins/product-engineering-os/.codex-plugin/plugin.json")
claude_manifest = load_json("plugins/product-engineering-os/.claude-plugin/plugin.json")
codex_marketplace = load_json(".agents/plugins/marketplace.json")
claude_marketplace = load_json(".claude-plugin/marketplace.json")
registry = load_json("plugins/product-engineering-os/providers/registry.json")
dependencies = load_json("plugins/product-engineering-os/providers/dependencies.json")

manifests = {
    "Codex manifest": codex_manifest,
    "Claude manifest": claude_manifest,
}
for label, manifest in manifests.items():
    if manifest.get("name") != NAME:
        fail(f"{label} name must be {NAME!r}")
    if manifest.get("description") != DESCRIPTION:
        fail(f"{label} description must match the canonical description")
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?", str(manifest.get("version", ""))):
        fail(f"{label} has an invalid semantic version")

versions = {
    codex_manifest.get("version"),
    claude_manifest.get("version"),
    claude_marketplace.get("metadata", {}).get("version"),
}
for entry in claude_marketplace.get("plugins", []):
    if entry.get("name") == NAME:
        versions.add(entry.get("version"))
if len(versions) != 1:
    fail(f"manifest and marketplace versions differ: {sorted(str(v) for v in versions)}")

codex_entries = codex_marketplace.get("plugins", [])
if len(codex_entries) != 1 or codex_entries[0].get("name") != NAME:
    fail("Codex marketplace must contain exactly the PEOS plugin")
else:
    source = codex_entries[0].get("source", {})
    if source.get("source") != "local" or source.get("path") != "./plugins/product-engineering-os":
        fail("Codex marketplace must use the repository-local plugin path")

claude_entries = claude_marketplace.get("plugins", [])
if len(claude_entries) != 1 or claude_entries[0].get("name") != NAME:
    fail("Claude marketplace must contain exactly the PEOS plugin")
elif claude_entries[0].get("source") != "./plugins/product-engineering-os":
    fail("Claude marketplace must use the repository-local plugin path")

skills_dir = PLUGIN / "skills"
actual_skills = {path.parent.name for path in skills_dir.glob("*/SKILL.md")}
if actual_skills != CAPABILITIES:
    fail(f"skill set mismatch: expected {sorted(CAPABILITIES)}, got {sorted(actual_skills)}")

frontmatter_name = re.compile(r"^name:\s*([^\s]+)\s*$", re.MULTILINE)
frontmatter_description = re.compile(r"^description:\s*(.+)\s*$", re.MULTILINE)
for skill in sorted(actual_skills):
    path = skills_dir / skill / "SKILL.md"
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---\n") or "\n---\n" not in content[4:]:
        fail(f"{path.relative_to(ROOT)} has invalid YAML frontmatter")
        continue
    frontmatter = content.split("---", 2)[1]
    name_match = frontmatter_name.search(frontmatter)
    description_match = frontmatter_description.search(frontmatter)
    if not name_match or name_match.group(1) != skill:
        fail(f"{path.relative_to(ROOT)} name must match its directory")
    if not description_match or len(description_match.group(1).strip()) < 30:
        fail(f"{path.relative_to(ROOT)} needs a meaningful description")

registered = set(registry.get("capabilities", {}))
if registered != CAPABILITIES:
    fail(f"provider registry capabilities differ from skills: {sorted(registered ^ CAPABILITIES)}")
for capability, definition in registry.get("capabilities", {}).items():
    for key in ("contract", "default_provider", "adapter"):
        if not definition.get(key):
            fail(f"provider registry {capability!r} is missing {key!r}")
    for key in ("contract", "adapter"):
        target = PLUGIN / definition.get(key, "missing")
        if not target.is_file():
            fail(f"provider registry {capability!r} references missing {key}: {target.relative_to(ROOT)}")

dependency_entries = dependencies.get("dependencies", [])
bmad_dependencies = [item for item in dependency_entries if item.get("id") == "bmad"]
if len(bmad_dependencies) != 1:
    fail("dependencies.json must declare exactly one BMAD dependency")
else:
    bmad_dependency = bmad_dependencies[0]
    expected_dependency_fields = {
        "distribution": "external-plugin",
        "repository": "bmad-code-org/bmad-plugins",
        "marketplace": "bmad",
        "plugin": "bmad-method",
        "vendored": False,
        "missing_dependency_behavior": "fail-closed-with-install-guidance",
    }
    for key, expected in expected_dependency_fields.items():
        if bmad_dependency.get(key) != expected:
            fail(f"BMAD dependency field {key!r} must be {expected!r}")
    if set(bmad_dependency.get("required_for", [])) != {"shape", "design", "plan", "build", "verify"}:
        fail("BMAD dependency consumers must match the BMAD-backed capabilities")

bmad_adapter_dir = PLUGIN / "providers" / "bmad"
expected_bmad_adapters = {"shape.md", "design.md", "plan.md", "build.md", "verify.md"}
actual_bmad_entries = {path.name for path in bmad_adapter_dir.iterdir()} if bmad_adapter_dir.is_dir() else set()
if actual_bmad_entries != expected_bmad_adapters:
    fail(f"BMAD adapter directory may contain only thin adapter files: {sorted(actual_bmad_entries)}")

forbidden_provider_directories = {".bmad", "_bmad", "bmad-method", "bmad-toolbox", "vendor", "vendors", "third_party", "third-party"}
for path in ROOT.rglob("*"):
    if ".git" in path.parts:
        continue
    if any(part.lower() in forbidden_provider_directories for part in path.relative_to(ROOT).parts):
        fail(f"vendored provider directory is forbidden: {path.relative_to(ROOT)}")

required_paths = [
    "plugins/product-engineering-os/references/runtime-conventions.md",
    "plugins/product-engineering-os/references/routing.md",
    "plugins/product-engineering-os/references/governance.md",
    "plugins/product-engineering-os/defaults/project/peos/config.yaml",
    "plugins/product-engineering-os/defaults/project/peos/context/system-map.md",
]
for relative in required_paths:
    if not (ROOT / relative).is_file():
        fail(f"missing required file: {relative}")

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    if path.is_symlink():
        fail(f"symbolic links are not allowed in the distribution: {path.relative_to(ROOT)}")
        continue
    if path.suffix.lower() not in {".md", ".json", ".yaml", ".yml", ".py", ".sh"}:
        continue
    text = path.read_text(encoding="utf-8")
    unresolved_markers = ("[" + "TODO", "TODO" + ":")
    if any(marker in text for marker in unresolved_markers):
        fail(f"unresolved placeholder marker in {path.relative_to(ROOT)}")

if errors:
    print("PEOS validation failed:", file=sys.stderr)
    for error in errors:
        print(f"  - {error}", file=sys.stderr)
    raise SystemExit(1)

print(f"PEOS {next(iter(versions))} passed cross-platform validation ({len(CAPABILITIES)} skills).")
