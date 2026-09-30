"""
Data ingestion module for the SPY volatility regime detection project.

This module is responsible for one job only: getting SPY price history from yfinanceand saving it locally, 
so we do not have to download it everytime we run the analysis. Keeping this logic sepeate from 
any analysis code means we can run it in notebooks, scripts, or later pipelines stages without 
copy-pasting.
"""

import os
import yfinance as yf
import pandas as pd

# Where the cached data dile will live. Using a constant here means every part of the prject
# refers to the same file path, so if we ever move it, we only change it in one place. 

RAW_DATA_PATH = "data/raw/spy_ohlc.parquet"

def fetch_spy_data(start_date = "2000-01-01"):
    """
    Download SPY daily price history from yfinance.
    We keep auto_adjust=False so that yfinance gives us BOTH the raw
    Close price and the Adjusted Close price as separate columns.
    We need both available for reference, even though our decision
    log (see DECISIONS.md) says only Adjusted Close will be used for
    actual volatility calculations.
    """
    data = yf.download("SPY", start=start_date, auto_adjust=False)
    return data

def save_raw_data(data, path = RAW_DATA_PATH):
    """
    Saves the price data to a local Parquet file.

    Parquet is used instead of CSV because it preserves the exact
    data types (dates stay dates, numbers stay numbers) and keeps
    file size smaller for the same data. This matches the caching
    decision recorded in DECISIONS.md.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data.to_parquet(path)

def load_cached_data(path=RAW_DATA_PATH):
    """
    Loads the cached price data from disk, if it exists.

    Returns None if no cached file is found yet, so the calling code
    can decide whether to fetch fresh data instead.
    """
    if os.path.exists(path):
        return pd.read_parquet(path)
    return None


def get_spy_data(start_date="2000-01-01", force_refresh=False):
    """
    Main entry point other code should use to get SPY data.

    By default, this checks for a cached file first and only hits
    the yfinance API if no cache exists, or if force_refresh=True
    is explicitly requested. This avoids unnecessary API calls every
    time a script or notebook runs.
    """
    if not force_refresh:
        cached = load_cached_data()
        if cached is not None:
            print(f"Loaded cached data from {RAW_DATA_PATH} ({cached.shape[0]} rows)")
            return cached

    print("Fetching fresh data from yfinance...")
    data = fetch_spy_data(start_date=start_date)
    save_raw_data(data)
    print(f"Saved fresh data to {RAW_DATA_PATH} ({data.shape[0]} rows)")
    return data
