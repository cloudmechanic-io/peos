#!/bin/sh
set -eu

if [ "$#" -lt 1 ] || [ "$#" -gt 2 ]; then
  echo "Usage: $0 <client-umbrella-directory> [organization-name]" >&2
  exit 2
fi

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
SOURCE="$ROOT/plugins/product-engineering-os/defaults/project/peos"
TARGET_ROOT=$1
ORG_NAME=${2:-Client organization}

[ -d "$TARGET_ROOT" ] || {
  echo "Client umbrella directory does not exist: $TARGET_ROOT" >&2
  exit 1
}

TARGET_ROOT=$(CDPATH= cd -- "$TARGET_ROOT" && pwd)
TARGET="$TARGET_ROOT/peos"

[ ! -e "$TARGET" ] || {
  echo "Refusing to overwrite existing client overlay: $TARGET" >&2
  exit 1
}

mkdir "$TARGET"
cp -R "$SOURCE/." "$TARGET/"

ORG_ESCAPED=$(printf '%s' "$ORG_NAME" | sed 's/[\\/&]/\\&/g')
sed "s/__ORGANIZATION_NAME__/$ORG_ESCAPED/g" "$TARGET/config.yaml" > "$TARGET/config.yaml.new"
mv "$TARGET/config.yaml.new" "$TARGET/config.yaml"

echo "Created client overlay at $TARGET"
echo "Next: review config.yaml and context/system-map.md, then commit the overlay through a pull request."
