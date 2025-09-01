from pathlib import Path
from datetime import datetime, timezone
from . import ingest, enrich, generate

def run(data_path: Path, out_dir: Path):
    df = ingest.ingest(data_path)
    df_enriched = enrich.enrich(df)

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        # placeholder for actual work
        "overview": {
            "num_columns": len(df_enriched.columns),
            "columns": df_enriched.columns.tolist(),
        }
    }
    paths = generate.generate(report, df_enriched, out_dir)
    
    return report, paths["generated_report"]