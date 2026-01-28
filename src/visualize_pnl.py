import pandas as pd
import matplotlib.pyplot as plt


def plot_equity(path="data/processed/backtest.parquet"):
    df = pd.read_parquet(path)

    plt.figure(figsize=(14, 6))
    plt.plot(df.index, df["equity"], label="Equity Curve")
    plt.title("Regime-Aware Stat Arb Equity Curve")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    plot_equity()
