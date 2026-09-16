#!/bin/sh
set -eu

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <semantic-version>" >&2
  exit 2
fi

VERSION=$1
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)

cd "$ROOT"
git rev-parse --is-inside-work-tree >/dev/null
[ -z "$(git status --porcelain)" ] || {
  echo "Working tree must be clean before preparing a release." >&2
  exit 1
}
[ "$(git branch --show-current)" = "main" ] || {
  echo "Prepare releases from main." >&2
  exit 1
}

git pull --ff-only
git switch -c "release/v$VERSION"
python3 "$ROOT/scripts/set-version.py" "$VERSION"
"$ROOT/scripts/validate.sh"
git add CHANGELOG.md .claude-plugin/marketplace.json plugins/product-engineering-os/.claude-plugin/plugin.json plugins/product-engineering-os/.codex-plugin/plugin.json
git commit -m "release: v$VERSION"
git push -u origin "release/v$VERSION"

if command -v gh >/dev/null 2>&1; then
  gh pr create --base main --head "release/v$VERSION" --title "release: v$VERSION" --body "Prepare Product Engineering Operating System v$VERSION."
else
  echo "Open a pull request from release/v$VERSION to main, review it, and merge it."
fi
