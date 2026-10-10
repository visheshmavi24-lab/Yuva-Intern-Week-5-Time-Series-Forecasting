from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
from statsmodels.tsa.stattools import adfuller

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "aapl_ticker_cleaned.csv"
if not DATA_PATH.exists():
    DATA_PATH = ROOT / "data" / "aapl_ticker.csv"

df = pd.read_csv(DATA_PATH)
date_candidates = ["date", "datetime", "timestamp", "time"]
close_candidates = ["close", "adj close", "adj_close", "adjusted_close", "closing_price"]
date_col = next((c for c in df.columns if c.lower().strip() in date_candidates), None)
close_col = next((c for c in df.columns if c.lower().strip() in close_candidates), None)

if not date_col or not close_col:
    raise ValueError(
        f"Could not detect date/closing-price columns. Available columns: {list(df.columns)}"
    )

df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
df[close_col] = pd.to_numeric(df[close_col], errors="coerce")
series = df.dropna(subset=[date_col, close_col]).sort_values(date_col)[close_col].reset_index(drop=True)

if len(series) < 20:
    raise ValueError("At least 20 valid observations are recommended for this baseline.")

split = int(len(series) * 0.8)
train, test = series.iloc[:split], series.iloc[split:]

# Naive baseline: each prediction equals the most recent observed training/test value.
predictions = []
last_value = float(train.iloc[-1])
for actual in test:
    predictions.append(last_value)
    last_value = float(actual)

mae = mean_absolute_error(test, predictions)
rmse = np.sqrt(mean_squared_error(test, predictions))
print(f"Observations: {len(series)} | Train: {len(train)} | Test: {len(test)}")
print(f"Naive baseline MAE: {mae:.4f}")
print(f"Naive baseline RMSE: {rmse:.4f}")

try:
    result = adfuller(series.diff().dropna())
    print(f"ADF test on first differences: statistic={result[0]:.4f}, p-value={result[1]:.6f}")
except Exception as exc:
    print("ADF test could not be computed:", exc)
