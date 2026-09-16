#!/bin/sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
PLATFORM=${1:-both}

case "$PLATFORM" in
  claude|codex|both) ;;
  *) echo "Usage: $0 [claude|codex|both]" >&2; exit 2 ;;
esac

"$ROOT/scripts/validate.sh"

install_claude() {
  command -v claude >/dev/null 2>&1 || {
    echo "Claude CLI is not installed." >&2
    return 1
  }

  claude_marketplace_exists() {
    claude plugin marketplace list --json | python3 -c 'import json,sys; raise SystemExit(0 if any(item.get("name") == sys.argv[1] for item in json.load(sys.stdin)) else 1)' "$1"
  }
  claude_plugin_exists() {
    claude plugin list --json | python3 -c 'import json,sys; raise SystemExit(0 if any(item.get("id") == sys.argv[1] for item in json.load(sys.stdin)) else 1)' "$1"
  }

  if claude_marketplace_exists bmad; then
    claude plugin marketplace update bmad
  else
    claude plugin marketplace add bmad-code-org/bmad-plugins --scope user
  fi
  if claude_plugin_exists bmad-method@bmad; then
    claude plugin update bmad-method@bmad
  else
    claude plugin install bmad-method@bmad --scope user
  fi

  if claude_marketplace_exists product-engineering-os; then
    claude plugin marketplace update product-engineering-os
  else
    claude plugin marketplace add "$ROOT" --scope user
  fi
  if claude_plugin_exists product-engineering-os@product-engineering-os; then
    claude plugin update product-engineering-os@product-engineering-os
  else
    claude plugin install product-engineering-os@product-engineering-os --scope user
  fi

  echo "Installed PEOS and BMAD for Claude. Restart Claude Code before testing."
}

install_codex() {
  if command -v codex >/dev/null 2>&1; then
    CODEX_BIN=codex
  elif [ -x /Applications/ChatGPT.app/Contents/Resources/codex ]; then
    CODEX_BIN=/Applications/ChatGPT.app/Contents/Resources/codex
  else
    echo "Codex CLI is not installed." >&2
    return 1
  fi

  codex_marketplace_exists() {
    "$CODEX_BIN" plugin marketplace list --json | python3 -c 'import json,sys; data=json.load(sys.stdin); raise SystemExit(0 if any(item.get("name") == sys.argv[1] for item in data.get("marketplaces", [])) else 1)' "$1"
  }
  codex_plugin_exists() {
    "$CODEX_BIN" plugin list --json | python3 -c 'import json,sys; data=json.load(sys.stdin); raise SystemExit(0 if any(item.get("pluginId") == sys.argv[1] for item in data.get("installed", [])) else 1)' "$1"
  }

  if codex_marketplace_exists bmad; then
    "$CODEX_BIN" plugin marketplace upgrade bmad
  else
    "$CODEX_BIN" plugin marketplace add bmad-code-org/bmad-plugins
  fi
  if codex_plugin_exists bmad-method@bmad; then
    echo "BMAD is already installed in Codex."
  else
    "$CODEX_BIN" plugin add bmad-method@bmad
  fi

  if codex_marketplace_exists product-engineering-os; then
    echo "Local PEOS marketplace is already configured in Codex."
  else
    "$CODEX_BIN" plugin marketplace add "$ROOT"
  fi
  if codex_plugin_exists product-engineering-os@product-engineering-os; then
    echo "PEOS is already installed in Codex. Remove and re-add it only when testing cache behavior."
  else
    "$CODEX_BIN" plugin add product-engineering-os@product-engineering-os
  fi

  echo "Installed PEOS and BMAD for Codex. Restart Codex before testing."
}

case "$PLATFORM" in
  claude) install_claude ;;
  codex) install_codex ;;
  both) install_claude; install_codex ;;
esac
