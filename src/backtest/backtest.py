import pandas as pd
import numpy as np


def backtest(path="data/processed/signals.parquet", cost_bps=10):
    df = pd.read_parquet(path)

    # Position = yesterday's signal
    df["position"] = df["signal"].shift(1).fillna(0)

    # Spread return
    df["spread_return"] = df["spread"].diff()

    # Gross PnL
    df["gross_pnl"] = df["position"] * df["spread_return"]

    # Transaction cost
    trades = df["position"].diff().abs()
    df["cost"] = trades * cost_bps * 1e-4

    # Net PnL
    df["net_pnl"] = df["gross_pnl"] - df["cost"]
    df["equity"] = df["net_pnl"].cumsum()

    df.to_parquet("data/processed/backtest.parquet")

    print("Backtest completed")
    print("Sharpe:", df["net_pnl"].mean() / df["net_pnl"].std() * np.sqrt(252))

    return df


if __name__ == "__main__":
    backtest()
