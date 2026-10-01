"""
Feature engineering module for the SPY volatility regime detection project.

This module turns raw price data into the two things every model in this
project actually needs: daily log returns, and a rolling realized
volatility measure. See DECISIONS.md for why log returns and rolling
standard deviation were chosen over the alternatives.
"""

import os
import numpy as np
import pandas as pd


PROCESSED_DATA_PATH = "data/processed/spy_features.parquet"

VOLATILITY_WINDOW = 22


def compute_log_returns(data, price_column="Adj Close"):
    """
    Computes daily log returns from the Adjusted Close price.
    """
    prices = data[price_column]
    log_returns = np.log(prices / prices.shift(1))
    return log_returns


def compute_realized_volatility(log_returns, window=VOLATILITY_WINDOW):
    """
    Computes rolling realized volatility: the standard deviation of daily
    log returns over a trailing window of days.
    """
    realized_vol = log_returns.rolling(window=window).std()
    return realized_vol


def build_feature_dataset(raw_data, price_column="Adj Close"):
    """
    Builds the full feature dataset: log returns and realized volatility.
    """
    features = pd.DataFrame(index=raw_data.index)
    features["log_return"] = compute_log_returns(raw_data, price_column)
    features["realized_volatility"] = compute_realized_volatility(
        features["log_return"]
    )
    return features


def save_features(features, path=PROCESSED_DATA_PATH):
    """
    Saves the engineered features to a local Parquet file.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    features.to_parquet(path)


def load_cached_features(path=PROCESSED_DATA_PATH):
    """
    Loads cached features from disk, if they exist. Returns None if not.
    """
    if os.path.exists(path):
        return pd.read_parquet(path)
    return None


def get_features(raw_data, force_refresh=False):
    """
    Main entry point other code should use to get the engineered features.
    """
    if not force_refresh:
        cached = load_cached_features()
        if cached is not None:
            print(f"Loaded cached features from {PROCESSED_DATA_PATH} ({cached.shape[0]} rows)")
            return cached

    print("Computing fresh features...")
    features = build_feature_dataset(raw_data)
    save_features(features)
    print(f"Saved fresh features to {PROCESSED_DATA_PATH} ({features.shape[0]} rows)")
    return features