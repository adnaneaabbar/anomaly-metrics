import json
from pathlib import Path
import pandas as pd

def generate(report, df: pd.DataFrame, out_dir: Path, recs=None):
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
    if recs:
        try:
            # if recommendations is a JSON string, parse it
            rec_json = json.loads(recs)
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