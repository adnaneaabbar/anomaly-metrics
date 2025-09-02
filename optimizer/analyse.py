import pandas as pd
from typing import Dict, Any

def analyse(df: pd.DataFrame) -> Dict[str, Any]:
    # number of records
    total = len(df)
    critical = int((df["severity"] == 2).sum())
    warnings = int((df["severity"] == 1).sum())

    last = df.iloc[-1]

    return {
        "overview": {
            "records": total,
            "warning_events": warnings,
            "critical_events": critical,
            "time_start_utc": df["timestamp"].iloc[0].isoformat(),
            "time_end_utc": df["timestamp"].iloc[-1].isoformat(),
        },
        "current_service_status": {
            "database": last.get("service_status.database"),
            "api_gateway": last.get("service_status.api_gateway"),
            "cache": last.get("service_status.cache")
        },
        "kpis": {
            "latency_ms_p95": float(df["latency_ms"].quantile(0.95)),
            "error_rate_p95": float(df["error_rate"].quantile(0.95)),
            "peak_cpu_percent": float(df["cpu_usage"].max()),
            "peak_memory_percent": float(df["memory_usage"].max()),
            "peak_disk_percent": float(df["disk_usage"].max()),
            "peak_temperature": float(df["temperature_celsius"].max())
        }
    }
