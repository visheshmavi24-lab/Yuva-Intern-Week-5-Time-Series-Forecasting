# Apple (AAPL) Stock Data Analysis

A beginner-friendly Python project for exploring Apple (AAPL) historical stock data and building a baseline time-series forecasting workflow.

## Project goals
- Explore the dataset and understand its columns and date range.
- Clean and prepare the data for time-series analysis.
- Visualize closing prices and trading volume.
- Check stationarity and compare simple forecasting baselines.
- Document results and limitations.

## Dataset
The file `data/aapl_ticker.csv` is the dataset supplied for this project. Check the actual column names in the file before running the scripts; the code attempts to identify common date and closing-price column names.

## Repository structure
```text
aapl_stock_analysis_repository/
├── data/
│   └── aapl_ticker.csv
├── notebooks/
│   └── analysis_notebook.py
├── reports/
│   └── report_template.md
├── src/
│   ├── data_exploration.py
│   ├── data_preprocessing.py
│   ├── visualization.py
│   └── forecasting_baseline.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup
Python 3.10+ recommended.

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Run the project
From the repository root:

```bash
python src/data_exploration.py
python src/data_preprocessing.py
python src/visualization.py
python src/forecasting_baseline.py
```

Output charts and cleaned data are written to `reports/` and `data/`.

## Important notes
- This is an educational analysis project, not investment advice.
- Forecasts are uncertain and should not be used alone to make trading decisions.
- The baseline forecast script uses a chronological holdout split to avoid shuffling time-series data.
