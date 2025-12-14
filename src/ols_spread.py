import pandas as pd
import numpy as np
import statsmodels.api as sm
import os

def create_OLS(
    path="data/raw/combined.csv", 
    outputPath="data/processed/processed.parquet"
):
    df = pd.read_csv(path, index_col=0, parse_dates=True)
    logp = np.log(df)

    # OLS regression
    X = sm.add_constant(logp["ICICI"])
    model = sm.OLS(logp["HDFC"], X).fit()

    alpha = model.params["const"]
    beta = model.params["ICICI"]

    print(f"Hedge Ratio β = {beta}")
    print(f"Intercept α = {alpha}")

    df["spread"] = logp["HDFC"] - beta * logp["ICICI"]

    os.makedirs(os.path.dirname(outputPath), exist_ok=True)
    df.to_parquet(outputPath)

    print("Spread computed & saved successfully!")
    return df, beta


if __name__ == '__main__':
    create_OLS()
