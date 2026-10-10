from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "aapl_ticker.csv"

df = pd.read_csv(DATA_PATH)
print("\n--- Dataset shape ---")
print(df.shape)
print("\n--- Column names and data types ---")
print(df.dtypes)
print("\n--- First 5 rows ---")
print(df.head())
print("\n--- Missing values ---")
print(df.isna().sum())
print("\n--- Numeric summary ---")
print(df.describe(include="all").T)

date_candidates = ["date", "datetime", "timestamp", "time"]
date_col = next((c for c in df.columns if c.lower() in date_candidates), None)
if date_col:
    parsed_dates = pd.to_datetime(df[date_col], errors="coerce")
    print(f"\nDate column detected: {date_col}")
    print("Date range:", parsed_dates.min(), "to", parsed_dates.max())
else:
    print("\nNo standard date column detected. Review the column names manually.")
