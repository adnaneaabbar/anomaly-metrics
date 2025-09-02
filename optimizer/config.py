THRESHOLDS = {
    "cpu_usage_high": 90,
    "memory_usage_high": 90,
    "latency_ms_high": 300,
    "disk_usage_high": 85,
    "io_wait_high": 10,
    "active_connections_high": 120,
    "error_rate_high": 0.10,
    "temperature_celsius_high": 85
}

Z_WINDOW = 10   # rolling window size
Z_SCORE = 2.5  # sensitivity for spike detection