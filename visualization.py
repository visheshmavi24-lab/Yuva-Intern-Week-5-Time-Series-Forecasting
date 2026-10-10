from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "aapl_ticker_cleaned.csv"
if not DATA_PATH.exists():
    DATA_PATH = ROOT / "data" / "aapl_ticker.csv"
OUT_DIR = ROOT / "reports"
OUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)
date_candidates = ["date", "datetime", "timestamp", "time"]
close_candidates = ["close", "adj close", "adj_close", "adjusted_close", "closing_price"]
volume_candidates = ["volume"]

date_col = next((c for c in df.columns if c.lower().strip() in date_candidates), None)
close_col = next((c for c in df.columns if c.lower().strip() in close_candidates), None)
volume_col = next((c for c in df.columns if c.lower().strip() in volume_candidates), None)

if not date_col:
    raise ValueError(f"Could not detect a date column. Available columns: {list(df.columns)}")
if not close_col:
    raise ValueError(f"Could not detect a closing-price column. Available columns: {list(df.columns)}")

df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
df[close_col] = pd.to_numeric(df[close_col], errors="coerce")
df = df.dropna(subset=[date_col, close_col]).sort_values(date_col)

plt.figure(figsize=(11, 5))
plt.plot(df[date_col], df[close_col])
plt.title("AAPL Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.tight_layout()
plt.savefig(OUT_DIR / "aapl_closing_price.png", dpi=150)
plt.close()

if volume_col:
    df[volume_col] = pd.to_numeric(df[volume_col], errors="coerce")
    plt.figure(figsize=(11, 5))
    plt.plot(df[date_col], df[volume_col])
    plt.title("AAPL Trading Volume Over Time")
    plt.xlabel("Date")
    plt.ylabel("Volume")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "aapl_trading_volume.png", dpi=150)
    plt.close()

print(f"Charts saved in: {OUT_DIR}")
