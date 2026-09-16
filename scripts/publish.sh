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
  echo "Working tree must be clean before publishing." >&2
  exit 1
}
[ "$(git branch --show-current)" = "main" ] || {
  echo "Publish only from main after the release pull request is merged." >&2
  exit 1
}

git pull --ff-only
python3 -c 'import json,sys; value=json.load(open("plugins/product-engineering-os/.codex-plugin/plugin.json"))["version"]; sys.exit(0 if value == sys.argv[1] else f"Manifest version {value} does not match {sys.argv[1]}")' "$VERSION"
"$ROOT/scripts/validate.sh"

if git rev-parse "v$VERSION" >/dev/null 2>&1; then
  echo "Tag v$VERSION already exists." >&2
  exit 1
fi

git tag -a "v$VERSION" -m "Product Engineering Operating System v$VERSION"
git push origin "v$VERSION"
echo "Published v$VERSION. Workspace marketplaces can now synchronize this revision."
