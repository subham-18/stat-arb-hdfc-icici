Project: Regime-Aware Statistical Arbitrage on Indian Banking Stocks

Goal: 
    To study whether mean reversion between HDFC Bank and ICICI Bank exists consistently or only during certain market regimes.

Key Ideas:

    Spread construction using OLS

    Stationarity testing using ADF

    Regime detection via rolling ADF

Key Finding: 
    Mean reversion is not global but exists intermittently. Regime filtering is critical for robust statistical arbitrage.

How to Run:

    python src/download.py
    python src/ols_spread.py
    python src/rolling_adf.py
    python src/visualize_stationarity.py

Takeaway: Spread creates opportunity. Regime grants permission.