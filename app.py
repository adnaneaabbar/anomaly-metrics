from pathlib import Path
from optimizer.pipeline import run

if __name__ == "__main__":
    data_path = Path("data/rapport.json")
    out_dir = Path("output")
    report, report_path = run(data_path, out_dir)
    
    print("Report generated at:", report_path)
    print("Report Overview:", report["overview"])