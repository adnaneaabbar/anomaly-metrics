import json
import pandas as pd
from pathlib import Path

def ingest(path: Path) -> pd.DataFrame:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    df = pd.json_normalize(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)

    # sorting by timestamp just to make sure everything is in chronological order
    return df.sort_values("timestamp").reset_index(drop=True)