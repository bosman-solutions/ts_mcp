# ts_mcp

A minimal MCP server that gives LLM contexts an accurate clock.

One tool: **`get_current_time`** — unix timestamp, ISO datetime, local time, day of week.

---

## Install

```bash
git clone https://github.com/bosman-solutions/ts_mcp.git
cd ts_mcp
bash install.sh
```

---

## Claude Desktop Config

`~/.config/Claude/claude_desktop_config.json` (Linux) or
`~/Library/Application Support/Claude/claude_desktop_config.json` (macOS):

```json
{
  "mcpServers": {
    "ts_mcp": {
      "command": "/path/to/ts_mcp/.venv/bin/python",
      "args": ["/path/to/ts_mcp/server.py"],
      "env": {
        "DEFAULT_TZ": "America/New_York"
      }
    }
  }
}
```

Replace `/path/to/ts_mcp` with your actual install path and `DEFAULT_TZ` with your
IANA timezone string. Falls back to `UTC` if unset. Restart Claude Desktop after editing.

### Location (optional)

Every response includes `host`. Add these to `env` to say where the clock lives:

| var | example | adds |
|---|---|---|
| `TS_HOST` | `gaspar` | overrides the hostname (set it in containers) |
| `TS_LOCATION` | `home-lab` | `location` |
| `TS_LAT` / `TS_LON` | `40.71` / `-74.01` | `coords` |

All values come from env; ts_mcp makes no network lookups.

---

> **Note:** Installing this server makes the tool *available* — it does not make
> the model *use* it. To ensure consistent timestamp grounding, you must instruct
> the model to call `get_current_time` in your system prompt. Without that instruction,
> tool use will be inconsistent or absent.

---

## License

MIT
