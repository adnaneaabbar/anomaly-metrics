import json
from pathlib import Path
import pandas as pd

def generate(report, df: pd.DataFrame, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "generated_report.json"

    with json_path.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, default=str)

    return {"generated_report": str(json_path)}