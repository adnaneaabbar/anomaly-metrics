from pathlib import Path
from optimizer.pipeline import run

if __name__ == "__main__":
    data_path = Path("data/rapport.json")
    out_dir = Path("output")
    report, paths = run(data_path, out_dir)
    
    print("Report generated at:", paths["generated_report"])
    print("Anomalies CSV at:", paths["anomalies_csv"])
    print("Report Overview:", report["overview"])
    print("Current Service Status:", report["current_service_status"])
    print("KPIs:", report["kpis"])