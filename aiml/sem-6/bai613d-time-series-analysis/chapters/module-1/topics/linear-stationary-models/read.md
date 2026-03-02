# Linear Stationary Models in Time Series Analysis

## Introduction

Time Series Analysis is a crucial statistical tool for engineers, enabling them to analyze data points collected or recorded at specific time intervals. From predicting electrical load demand to analyzing signal processing outputs or forecasting production rates in manufacturing, understanding the underlying structure of time-dependent data is paramount. The first step in this analysis is often to model the data, and **Linear Stationary Models** form the foundational building block for this purpose. This module focuses on understanding these core models, their characteristics, and their applications.

Stationarity is a key concept. A time series is said to be **stationary** if its statistical properties—such as its mean, variance, and autocorrelation—are constant over time. This implies the series lacks trends or seasonal variations, making it easier to model and forecast. Most real-world data is non-stationary, but we can often transform it (e.g., through differencing) to achieve stationarity before applying these linear models.

## Core Concepts

### 1. White Noise Process

The most basic stationary time series model is the **White Noise** process. It is a sequence of random variables with a constant mean (usually zero), constant variance (σ²), and no correlation between observations at different times.

*   **Mathematical Representation:** `{εₜ}`, where:
    *   `E(εₜ) = 0` for all `t` (mean zero).
    *   `Var(εₜ) = σ²` for all `t` (constant variance).
    *   `Cov(εₜ, εₜ₊ₖ) = 0` for all `t` and `k ≠ 0` (no autocorrelation).

White noise is the "innovations" or "error" process in more complex models. It represents the unpredictable shock or randomness in the system at time `t`.

**Example:** The random electrical signal (static) you might see on a television screen with no input is a classic example of a white noise process.

### 2. Moving Average (MA) Model

A Moving Average model expresses the present value of the series, `Xₜ`, as a linear combination of the current and past white noise shocks (`εₜ`, `εₜ₋₁`, ...).

*   **MA(q) Model:** An MA model of order `q` is defined as:
    `Xₜ = μ + εₜ + θ₁εₜ₋₁ + θ₂εₜ₋₂ + ... + θ_qεₜ₋_q`
    where `μ` is the mean of the series, and `θ₁, θ₂, ..., θ_q` are the model parameters.

*   **Key Property:** An MA(q) model has a memory of only `q` time steps. This means the correlation between `Xₜ` and `Xₜ₊ₖ` cuts off abruptly after lag `k = q`. This is a crucial signature used for model identification.

**Example:** Consider a manufacturing process where the diameter of a produced bearing (`Xₜ`) deviates from the mean (`μ`) due to random shocks in the machine. A shock today (`εₜ`) and a shock from the previous hour (`εₜ₋₁`) might both influence the current bearing's measurement. This could be modeled as an MA(1) process: `Xₜ = μ + εₜ + θ₁εₜ₋₁`.

### 3. Autoregressive (AR) Model

An Autoregressive model expresses the present value of the series, `Xₜ`, as a linear combination of its own past values (`Xₜ₋₁`, `Xₜ₋₂`, ...) plus a white noise shock.

*   **AR(p) Model:** An AR model of order `p` is defined as:
    `Xₜ = c + φ₁Xₜ₋₁ + φ₂Xₜ₋₂ + ... + φ_pXₜ₋_p + εₜ`
    where `c` is a constant, and `φ₁, φ₂, ..., φ_p` are the model parameters.

*   **Key Property:** The AR model has an infinite memory. The effect of a past shock decays exponentially but influences all future values. The Autocorrelation Function (ACF) of an AR(p) model tails off gradually rather than cutting off.

**Example:** The temperature in a room (`Xₜ`) is highly dependent on what it was one hour ago (`Xₜ₋₁`) and two hours ago (`Xₜ₋₂`). The current temperature is essentially a weighted sum of these past values, plus some random change due to a door opening or a sudden draft (`εₜ`). This is the essence of an autoregressive process.

### 4. Autoregressive Moving Average (ARMA) Model

The ARMA model is a hybrid approach that combines both the Autoregressive (AR) and Moving Average (MA) components, providing a more parsimonious model (one that uses fewer parameters to describe the same process).

*   **ARMA(p, q) Model:**
    `Xₜ = c + φ₁Xₜ₋₁ + ... + φ_pXₜ₋_p + εₜ + θ₁εₜ₋₁ + ... + θ_qεₜ₋_q`
    This model states that the current value `Xₜ` depends on both its own past values and the past random shocks.

ARMA models are powerful tools for describing a wide range of stationary time series behaviors encountered in engineering applications.

## Key Points / Summary

| Concept | Model | Equation | Key Property |
| :--- | :--- | :--- | :--- |
| **White Noise** | - | `Xₜ = εₜ` | Zero mean, constant variance, no correlation. |
| **Moving Average** | **MA(q)** | `Xₜ = μ + εₜ + θ₁εₜ₋₁ + ... + θ_qεₜ₋_q` | Memory of `q` steps. ACF cuts off after lag `q`. |
| **Autoregressive** | **AR(p)** | `Xₜ = c + φ₁Xₜ₋₁ + ... + φ_pXₜ₋_p + εₜ` | Infinite memory. ACF tails off gradually. |
| **ARMA** | **ARMA(p, q)** | `Xₜ = c + Σφ_iXₜ₋_i + εₜ + Σθ_jεₜ₋_j` | Combines AR and MA for a more efficient model. |

*   **Foundation:** These linear models are the foundation for analyzing and forecasting stationary time series.
*   **Prerequisite:** Stationarity is a required assumption for these standard ARMA models.
*   **Identification:** The behavior of the Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) is used to identify the appropriate model (AR, MA, or ARMA) and its order (`p` or `q`).
*   **Building Block:** Understanding these models is essential before advancing to more complex models like ARIMA (which handles non-stationary data) and SARIMA (which handles seasonality).