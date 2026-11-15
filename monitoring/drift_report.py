import os

import numpy as np
import pandas as pd
from evidently.metric_preset import DataDriftPreset
from evidently.report import Report

LOG_FILE = "logs/requests.csv"
OUTPUT = "reports/drift_report.html"
COLUMNS = ["a", "b", "result"]


def make_data(n, low, high, seed):
    rng = np.random.default_rng(seed)
    a = rng.uniform(low, high, n)
    b = rng.uniform(low, high, n)
    return pd.DataFrame({"a": a, "b": b, "result": a + b})


def load_current():
    """Use real API logs if there are enough rows, else simulate shifted data."""
    if os.path.exists(LOG_FILE):
        df = pd.read_csv(LOG_FILE)
        if len(df) >= 30:
            return df[COLUMNS]
    print("Not enough logged requests, using simulated current data.")
    return make_data(200, 50, 150, seed=7)  # shifted range -> drift


def main():
    os.makedirs("reports", exist_ok=True)
    reference = make_data(500, 0, 100, seed=42)
    current = load_current()

    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=reference, current_data=current)
    report.save_html(OUTPUT)
    print(f"Evidently report saved to {OUTPUT}")


if __name__ == "__main__":
    main()