import pandas as pd
import matplotlib.pyplot as plt


def capital_scaling(
    path="data/processed/backtest.parquet",
    base_capital=10_00_000,  # 10L
    capitals=[10_00_000, 25_00_000, 50_00_000, 1_00_00_000],
    extra_cost_bps_per_10L=1,  # liquidity impact
):
    df = pd.read_parquet(path)

    pnl = df["net_pnl"]

    plt.figure(figsize=(14, 6))

    for cap in capitals:
        scale = cap / base_capital

        # extra slippage as capital increases
        extra_cost = (cap / 10_00_000) * extra_cost_bps_per_10L * 1e-4
        scaled_pnl = pnl * scale - extra_cost

        equity = scaled_pnl.cumsum()

        label = f"Capital ₹{cap/1e5:.1f}L"
        plt.plot(equity, label=label)

    plt.title("Capital Scaling Analysis (Cost-Aware)")
    plt.xlabel("Time")
    plt.ylabel("Equity")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()


if __name__ == "__main__":
    capital_scaling()
