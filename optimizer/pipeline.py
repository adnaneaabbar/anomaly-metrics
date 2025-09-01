from pathlib import Path
from datetime import datetime, timezone
from . import ingest, generate

def run(data_path: Path, out_dir: Path):
    df = ingest.ingest(data_path)

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        # placeholder for actual work
        "overview": {
            "num_records": len(df),
            "columns": df.columns.tolist(),
        }
    }
    paths = generate.generate(report, df, out_dir)
    
    return report, paths["generated_report"]