import yfinance as yf
import pandas as pd
import os

def download_data(tickers, start_date="2019-01-01", end_date="2024-12-31"):
    print("Downloading data...")

    # auto_adjust=True ensures only a single price column per ticker
    data = yf.download(
        tickers, 
        start=start_date, 
        end=end_date, 
        auto_adjust=True
    )

    # If multi-column (for multiple tickers), keep only Close price
    if isinstance(data.columns, pd.MultiIndex):
        data = data["Close"]

    data = data.dropna()

    # Rename columns to clean names
    data.columns = ["HDFC", "ICICI"]

    # Create directory if missing
    os.makedirs("data/raw", exist_ok=True)

    # Save individual CSVs
    data["HDFC"].to_csv("data/raw/HDFCBANK.csv")
    data["ICICI"].to_csv("data/raw/ICICIBANK.csv")

    # Save combined file
    data.to_csv("data/raw/combined.csv")

    print("Data downloaded & saved successfully!")
    return data


if __name__ == "__main__":
    download_data(["HDFCBANK.NS", "ICICIBANK.NS"])
