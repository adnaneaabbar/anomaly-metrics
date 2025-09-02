from pathlib import Path
from datetime import datetime, timezone
from . import ingest, enrich, detect_anomalies, analyse, recommend, generate

def run(data_path: Path, out_dir: Path):
    # ingest, enrich, detect anomalies
    df = ingest.ingest(data_path)
    df_enriched = enrich.enrich(df)
    df_anoms = detect_anomalies.detect_anomalies(df_enriched)
    
    # generate summary and report
    summary = analyse.analyse(df_anoms)

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        # placeholder for actual work
        **summary
    }

    # get LLM recommendations
    anomalies_csv_path = out_dir / "anomalies.csv"
    recommendations = recommend.recommend_actions(report, anomalies_csv_path)

    paths = generate.generate(report, df_anoms, out_dir, recommendations)
    
    return paths