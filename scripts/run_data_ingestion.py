"""
Run this script directly to pull (or refresh) the cached SPY dataset.

Usage:
    python scripts/run_data_ingestion.py
"""

import sys
import os

# Allows this script to import from the src/ folder when run directly.
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.data_ingestion import get_spy_data

if __name__ == "__main__":
    data = get_spy_data()
    print(data.head())
    print(data.tail())