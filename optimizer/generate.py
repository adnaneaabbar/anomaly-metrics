import json
from pathlib import Path
import pandas as pd
from . import recommend

def generate(report, df: pd.DataFrame, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "generated_report.json"
    anomalies_path = out_dir / "anomalies.csv"
    rec_path = out_dir / "recs.json"

    # save report
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, default=str)

    # save anomalies
    df[df["severity"] > 0].to_csv(anomalies_path, index=False)

    # save recommendations
    recs = recommend.recommend_actions(report, anomalies_path)
    try:
        # remove code block markers if present
        cleaned_recs = recs.strip()
        if cleaned_recs.startswith("```json"):
            cleaned_recs = cleaned_recs[len("```json"):].strip()
        if cleaned_recs.endswith("```"):
            cleaned_recs = cleaned_recs[:-3].strip()
        rec_json = json.loads(cleaned_recs)
    except Exception:
        # if not, save as plain text
        rec_json = {"raw": recs}
    with rec_path.open("w", encoding="utf-8") as f:
        json.dump(rec_json, f, indent=4, default=str)

    paths = {
        "generated_report": str(json_path),
        "anomalies_csv": str(anomalies_path),
        "recs_json": str(rec_path)
    }

    return paths