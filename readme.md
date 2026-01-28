# Regime-Aware Statistical Arbitrage System (Indian Banking Stocks)

## Overview

This project implements a **regime-aware statistical arbitrage trading system**
for Indian banking equities (HDFC Bank & ICICI Bank).

The system exploits **intermittent mean-reversion** in price spreads while
explicitly avoiding non-stationary market regimes, incorporating
transaction costs, risk controls, and capital scalability analysis.

The focus is on **robustness and scalability**, not short-term trading frequency.

---

## Motivation

Classical statistical arbitrage assumes persistent mean reversion.
Empirical evidence shows this assumption often breaks down.

This project demonstrates that:

> **Mean reversion is regime-dependent, not global.**

Trading only when statistical conditions are valid is critical
for long-term capital deployment.

---

## System Architecture

### 1. Data

- Daily adjusted close prices
- Instruments: HDFC Bank, ICICI Bank
- Source: Yahoo Finance
- Frequency: End-of-day

---

### 2. Signal Generation

- Log-price spread constructed via OLS hedge ratio
- Stationarity tested using Augmented Dickey-Fuller (ADF)
- Rolling ADF used to detect time-varying regimes

---

### 3. Regime Filter

- Trades enabled only during statistically stationary regimes
- Regime information used as a **permission layer**, not a prediction

---

### 4. Trading Strategy

- Z-score based mean-reversion entries
- Symmetric exits when spread normalizes
- Market-neutral long/short construction

---

### 5. Backtesting & Risk

- No look-ahead bias (positions lagged by one period)
- Transaction cost modeling (bps-based)
- Equity curve, Sharpe ratio, drawdown analysis

---

### 6. Capital Scaling Analysis

- Performance evaluated under increasing capital assumptions:
  - ₹10L → ₹25L → ₹50L → ₹1Cr
- Explicit cost drag added with scale
- Strategy behavior remains stable under higher capital due to:
  - Low turnover
  - High-liquidity instruments

---

### 7. Live Signal (Pseudo-Live)

- Daily signal generation using latest available data
- Outputs LONG / SHORT / FLAT decisions with rationale
- Designed to mirror real quant research workflows prior to deployment

---

## Key Insight

> **Spread creates opportunity.  
> Regime grants permission.  
> Risk grants survival.**

---

## How to Run

- python src/download.py
- python src/ols_spread.py
- python src/rolling_adf.py
- python src/strategy/mean_reversion.py
- python src/backtest/backtest.py
- python src/backtest/capital_scaling.py
- python src/visualize_pnl.py
- python src/live/daily_signal.py
