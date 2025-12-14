import pandas as pd
from statsmodels.tsa.stattools import adfuller


def test_stationary(path="data/processed/processed.parquet"):
    df = pd.read_parquet(path)
    spread = df["spread"].dropna()

    adf_result = adfuller(spread)

    print("ADF Statistic:", adf_result[0])
    print("p-value:", adf_result[1])

    if adf_result[1] < 0.05:
        print("Spread is STATIONARY → Good pair for mean-reversion")
    else:
        print("Spread is NOT stationary → Bad pair, strategy may fail")
        

if __name__ == '__main__':
    test_stationary()
