import json
import pandas as pd
from pathlib import Path

'''
JSON file snippet

{
    "timestamp": "2023-10-01T12:00:00Z",
    "cpu_usage": 93,
    "memory_usage": 86,
    "latency_ms": 334,
    "disk_usage": 89,
    "network_in_kbps": 2541,
    "network_out_kbps": 2137,
    "io_wait": 12,
    "thread_count": 143,
    "active_connections": 126,
    "error_rate": 0.12,
    "uptime_seconds": 360000,
    "temperature_celsius": 84,
    "power_consumption_watts": 356,
    "service_status": {
      "database": "online",
      "api_gateway": "degraded",
      "cache": "online"
    }
  }
'''

def ingest(path: Path) -> pd.DataFrame:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    df = pd.json_normalize(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)

    # sorting by timestamp just to make sure everything is in chronological order
    return df.sort_values("timestamp").reset_index(drop=True)