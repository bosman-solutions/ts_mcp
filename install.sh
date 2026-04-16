#!/usr/bin/env bash
# ts_mcp install script
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "→ Creating virtualenv..."
python3 -m venv .venv

echo "→ Installing dependencies..."
.venv/bin/pip install -q -r requirements.txt

echo ""
echo "✓ Done. Add to your MCP host config:"
echo ""
echo "  \"ts_mcp\": {"
echo "    \"command\": \"$SCRIPT_DIR/.venv/bin/python\","
echo "    \"args\": [\"$SCRIPT_DIR/server.py\"],"
echo "    \"env\": { \"DEFAULT_TZ\": \"Your/Timezone\" }"
echo "  }"
echo ""
echo "Replace Your/Timezone with a valid IANA timezone string (e.g. America/New_York)."
echo "Restart Claude Desktop after editing the config."
