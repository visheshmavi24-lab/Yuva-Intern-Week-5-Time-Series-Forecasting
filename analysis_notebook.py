"""
Notebook-style starting point.
Open this file in VS Code or copy cells into a Jupyter notebook.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "aapl_ticker.csv")

print(df.head())
print(df.info())
print(df.isna().sum())

# Inspect the real column names before choosing columns for charts.
print("Columns:", list(df.columns))
