import pandas as pd
import numpy as np


def generate_daily_signal(
    path="data/processed/rolling_adf.parquet",
    lookback=60,
    entry_z=2.0,
    exit_z=0.5,
):
    df = pd.read_parquet(path)

    # Use only data available up to today (important)
    df = df.dropna()

    # Compute z-score
    spread = df["spread"]
    mean = spread.rolling(lookback).mean()
    std = spread.rolling(lookback).std()
    zscore = (spread - mean) / std

    df["zscore"] = zscore

    # Get latest row (TODAY)
    latest = df.iloc[-1]

    signal = "FLAT"
    reason = ""

    if latest["stationary"]:
        if latest["zscore"] > entry_z:
            signal = "SHORT SPREAD"
            reason = f"z={latest['zscore']:.2f} > {entry_z} and regime=stationary"

        elif latest["zscore"] < -entry_z:
            signal = "LONG SPREAD"
            reason = f"z={latest['zscore']:.2f} < -{entry_z} and regime=stationary"

        else:
            signal = "FLAT"
            reason = f"z={latest['zscore']:.2f} within no-trade band"

    else:
        signal = "FLAT"
        reason = "Regime is non-stationary (no mean reversion)"

    # Output
    print("\n===== DAILY TRADING DECISION =====")
    print(f"Date        : {latest.name.date()}")
    print(f"Signal      : {signal}")
    print(f"Z-Score     : {latest['zscore']:.2f}")
    print(f"Stationary  : {latest['stationary']}")
    print(f"Reason      : {reason}")
    print("=================================\n")

    return signal


if __name__ == "__main__":
    generate_daily_signal()
