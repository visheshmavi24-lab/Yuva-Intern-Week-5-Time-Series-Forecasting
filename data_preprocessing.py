from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "aapl_ticker.csv"
OUTPUT_PATH = ROOT / "data" / "aapl_ticker_cleaned.csv"

df = pd.read_csv(DATA_PATH)
df.columns = [c.strip() for c in df.columns]

date_candidates = ["date", "datetime", "timestamp", "time"]
date_col = next((c for c in df.columns if c.lower() in date_candidates), None)
if date_col:
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df = df.dropna(subset=[date_col]).sort_values(date_col)

before = len(df)
df = df.drop_duplicates()
removed_duplicates = before - len(df)

# Convert numeric-looking columns where possible, while leaving text columns intact.
for col in df.columns:
    if col != date_col and df[col].dtype == "object":
        converted = pd.to_numeric(df[col].astype(str).str.replace(",", "", regex=False), errors="coerce")
        if converted.notna().mean() >= 0.8:
            df[col] = converted

df.to_csv(OUTPUT_PATH, index=False)
print(f"Saved cleaned dataset: {OUTPUT_PATH}")
print(f"Rows after cleaning: {len(df)}")
print(f"Duplicate rows removed: {removed_duplicates}")
print("Missing values remaining by column:")
print(df.isna().sum())
