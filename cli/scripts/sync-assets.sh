#!/bin/bash

# Sync data and scripts from .shared to cli/assets
# Templates are managed separately in cli/assets/templates/

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLI_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$CLI_DIR")"
ASSETS_DIR="$CLI_DIR/assets"
SHARED_DIR="$ROOT_DIR/.shared/backend-architect-skill"

echo "🔄 Syncing assets from .shared to cli/assets..."

# Preserve templates folder
TEMP_DIR=$(mktemp -d)
if [ -d "$ASSETS_DIR/templates" ]; then
    cp -r "$ASSETS_DIR/templates" "$TEMP_DIR/templates"
fi

# Remove old assets and recreate
rm -rf "$ASSETS_DIR"
mkdir -p "$ASSETS_DIR"

# Restore templates
if [ -d "$TEMP_DIR/templates" ]; then
    cp -r "$TEMP_DIR/templates" "$ASSETS_DIR/templates"
fi
rm -rf "$TEMP_DIR"

# Copy data folder from .shared
if [ -d "$SHARED_DIR/data" ]; then
    echo "  📁 Copying data/..."
    cp -r "$SHARED_DIR/data" "$ASSETS_DIR/data"
else
    echo "  ⚠️ Warning: .shared/backend-architect-skill/data/ not found"
fi

# Copy scripts folder from .shared
if [ -d "$SHARED_DIR/scripts" ]; then
    echo "  📁 Copying scripts/..."
    cp -r "$SHARED_DIR/scripts" "$ASSETS_DIR/scripts"
else
    echo "  ⚠️ Warning: .shared/backend-architect-skill/scripts/ not found"
fi

# Count files
FILE_COUNT=$(find "$ASSETS_DIR" -type f | wc -l | tr -d ' ')
echo "✅ Assets synced successfully!"
echo "   Total: $FILE_COUNT files"
