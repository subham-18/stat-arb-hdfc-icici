import pandas as pd
import numpy as np


def generate_signals(
    path="data/processed/rolling_adf.parquet",
    entry_z=2.0,
    exit_z=0.5,
):
    df = pd.read_parquet(path)

    # Compute z-score of spread
    df["spread_mean"] = df["spread"].rolling(60).mean()
    df["spread_std"] = df["spread"].rolling(60).std()
    df["zscore"] = (df["spread"] - df["spread_mean"]) / df["spread_std"]

    # Initialize signal column
    df["signal"] = 0

    # Entry rules (ONLY when stationary)
    df.loc[(df["zscore"] > entry_z) & (df["stationary"]), "signal"] = -1
    df.loc[(df["zscore"] < -entry_z) & (df["stationary"]), "signal"] = 1

    # Exit
    df.loc[df["zscore"].abs() < exit_z, "signal"] = 0

    df = df.dropna()
    df.to_parquet("data/processed/signals.parquet")

    print("Trading signals generated")
    return df


if __name__ == "__main__":
    generate_signals()
