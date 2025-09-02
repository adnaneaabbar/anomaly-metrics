## Input

### JSON file snippet:

```json
{ "timestamp": "2023-10-01T12:00:00Z", "cpu_usage": 85, "memory_usage": 70, "latency_ms": 250, "disk_usage": 65, "network_in_kbps": 1200, "network_out_kbps": 900, "io_wait": 5, "thread_count": 150, "active_connections": 45, "error_rate": 0.02, "uptime_seconds": 360000, "temperature_celsius": 65, "power_consumption_watts": 250, "service_status": { ‘database’: "online", "api_gateway": "degraded", ‘cache’: "online" }
```

### Input file: [rapport.json](/data/rapport.json)

## Module

Module `optimizer` contains the nodes:
1. Ingest [ingest](/optimizer/ingest.py)
2. Enrich [enrich](/optimizer/enrich.py)
3. Detect anomalies [detect_anomalies](/optimizer/detect_anomalies.py)
4. Analyse [analyse](/optimizer/analyse.py)
5. Recommend [recommend](/optimizer/recommend.py)
6. Generate [generate](/optimizer/generate.py)

## How to run:

```bash
# install deps
pip install -r requirements.txt

python app.py
```

or you can run everything inside a docker container
```bash
# build image
docker build -t anomaly-metrics .

# run container
docker run --rm \                
  -v $(pwd)/data:/app/data \
  -v $(pwd)/output:/app/output \
  anomaly-metrics
```

## Output

### Anomalies file: [anomalies.csv](/output/anomalies.csv)
### Generated JSON report: [generated_report.json](/output/generated_report.json)
### Generated JSON recommendations: [recs.json](/output/recs.json)

### Trace of the run: [RunnableSequence](https://smith.langchain.com/public/2c7fb5d0-a56a-49ca-96af-254a7f19aa4f/r)