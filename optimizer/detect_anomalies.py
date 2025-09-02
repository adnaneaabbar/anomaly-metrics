import pandas as pd
from .config import THRESHOLDS, Z_SCORE

def detect_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    # threshold anomalies
    out["anomaly_cpu"] = out["cpu_usage"] >= THRESHOLDS["cpu_usage_high"]
    out["anomaly_memory"] = out["memory_usage"] >= THRESHOLDS["memory_usage_high"]
    out["anomaly_disk"] = out["disk_usage"] >= THRESHOLDS["disk_usage_high"]
    out["anomaly_latency"] = out["latency_ms"] >= THRESHOLDS["latency_ms_high"]
    out["anomaly_error_rate"] = out["error_rate"] >= THRESHOLDS["error_rate_high"]
    out["anomaly_temp"] = out["temperature_celsius"] >= THRESHOLDS["temperature_celsius_high"]

    # service anomalies
    out["anomaly_db_offline"] = out.get("database_offline", 0) == 1
    out["anomaly_api_degraded"] = out.get("api_gateway_degraded", 0) == 1
    out["anomaly_cache_degraded"] = out.get("cache_degraded", 0) == 1

    # spike anomalies on rolling windows
    for metric in ["latency_ms", "cpu_usage", "memory_usage", "network_index", "error_rate"]:
        out[f"anomaly_spike_{metric}"] = out[f"{metric}_z"].abs() >= Z_SCORE

    # severity score
    def severity(row):
        if row["anomaly_db_offline"] or (row["anomaly_cpu"] and row["anomaly_memory"] and row["anomaly_disk"] and row["anomaly_temp"]):
            return 2
        if row["anomaly_cpu"] or row["anomaly_cache_degraded"] or row["anomaly_api_degraded"]:
            return 1
        return 0

    # apply severity score to each row of the dataframe
    out["severity"] = out.apply(severity, axis=1)

    return out
