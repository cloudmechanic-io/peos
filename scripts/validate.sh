#!/bin/sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)

python3 "$ROOT/scripts/validate.py"

if command -v claude >/dev/null 2>&1; then
  claude plugin validate "$ROOT/plugins/product-engineering-os"
  claude plugin validate "$ROOT/.claude-plugin/marketplace.json"
else
  echo "Claude CLI not found; skipped Claude's native validator."
fi

echo "Validation complete."
