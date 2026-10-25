"""
ts_mcp - Timestamp MCP server

Provides accurate temporal grounding for LLM contexts via MCP.

Transport: stdio (runs as subprocess from MCP host)
"""

import json
import os
import socket
import time
from datetime import datetime, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ts_mcp")

DEFAULT_TZ = os.environ.get("DEFAULT_TZ", "UTC")
# Which body answered. TS_HOST overrides the kernel hostname (e.g. inside a container).
HOST = os.environ.get("TS_HOST") or socket.gethostname()


@mcp.tool()
async def get_current_time(tz: str = DEFAULT_TZ) -> str:
    """
    Returns the current accurate timestamp.

    Args:
        tz (str): IANA timezone string. Defaults to DEFAULT_TZ env var (fallback: UTC).
                  Examples: "America/New_York", "UTC", "Europe/London"

    Returns:
        str: JSON with unix, iso_utc, local datetime, day_of_week, timezone, host.
    """
    try:
        now_local = datetime.now(ZoneInfo(tz))
    except ZoneInfoNotFoundError:
        now_local = datetime.now(ZoneInfo(DEFAULT_TZ))

    return json.dumps({
        "unix": int(time.time()),
        "iso_utc": datetime.now(timezone.utc).isoformat(),
        "local": now_local.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "day_of_week": now_local.strftime("%A"),
        "timezone": tz,
        "host": HOST,
    }, indent=2)


if __name__ == "__main__":
    mcp.run()
