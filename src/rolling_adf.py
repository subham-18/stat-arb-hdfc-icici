import pandas as pd
from statsmodels.tsa.stattools import adfuller


def rolling_adf(path="data/processed/processed.parquet", window=252, alpha=0.05):
    df = pd.read_parquet(path)
    spread = df["spread"].dropna()

    p_values = []

    for i in range(len(spread)):
        if i < window:
            p_values.append(None)
        else:
            window_series = spread[i - window : i]
            pval = adfuller(window_series)[1]
            p_values.append(pval)

    df["adf_pvalue"] = p_values
    df["stationary"] = df["adf_pvalue"] < alpha

    df.to_parquet("data/processed/rolling_adf.parquet")

    print("Rolling ADF completed")
    return df


if __name__ == "__main__":
    rolling_adf()
