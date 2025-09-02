import numpy as np
import pandas as pd
from .config import Z_WINDOW

def enrich(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    # defining usage_index, network_index
    out["usage_index"] = (
        out["cpu_usage"] * 0.5 +
        out["memory_usage"] * 0.25 +
        out["disk_usage"] * 0.25
    )
    out["network_index"] = out["network_in_kbps"] + out["network_out_kbps"]

    # service status flags
    for service in ["database", "api_gateway", "cache"]:
        col = f"service_status.{service}"
        if col in out.columns:
            out[f"{service}_online"] = (out[col] == "online").astype(int)
            out[f"{service}_degraded"] = (out[col] == "degraded").astype(int)
            out[f"{service}_offline"] = (out[col] == "offline").astype(int)

    # rolling stats for spikes
    for metric in ["latency_ms", "cpu_usage", "memory_usage", "network_index", "error_rate"]:
        out[f"{metric}_roll_mean"] = out[metric].rolling(Z_WINDOW, min_periods=3).mean()
        out[f"{metric}_roll_std"] = out[metric].rolling(Z_WINDOW, min_periods=3).std(ddof=0)
        out[f"{metric}_z"] = (out[metric] - out[f"{metric}_roll_mean"]) / out[f"{metric}_roll_std"].replace(0, np.nan)

    return out
