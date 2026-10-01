"""
Run this script directly to compute (or refresh) log returns and realized volatility
from the cached SPY datasets.
"""
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.data_ingestion import get_spy_data
from src.feature_engineering import get_features

if __name__ == "__main__":
    raw_data = get_spy_data()
    features = get_features(raw_data)
    print(features.head(30))
    print(features.tail())