import pandas as pd
import matplotlib.pyplot as plt


def plot_stationarity(path="data/processed/rolling_adf.parquet"):
    df = pd.read_parquet(path)

    plt.figure(figsize=(14, 6))

    plt.plot(df.index, df["spread"], label="Spread", color="black", alpha=0.6)

    # Highlight stationary regimes
    stationary = df["stationary"] == True
    plt.scatter(
        df.index[stationary],
        df.loc[stationary, "spread"],
        color="red",
        s=5,
        label="Stationary Regime",
    )

    plt.title("Spread with Stationary Regimes (Rolling ADF)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    plot_stationarity()
