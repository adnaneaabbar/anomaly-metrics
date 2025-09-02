from pathlib import Path
from optimizer.pipeline import run
from optimizer.recommend import recommend_actions

if __name__ == "__main__":
    data_path = Path("data/rapport.json")
    out_dir = Path("output")
    paths = run(data_path, out_dir)
    
    print("Report generated at: ", paths["generated_report"])
    print("Anomalies CSV generated at: ", paths["anomalies_csv"])
    print("LLM Recommendations generated at: ", paths["recs_json"])