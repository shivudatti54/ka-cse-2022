# Module 1: Linear Stationary Models in Time Series Analysis

## Introduction

Welcome to the foundation of Time Series Analysis. In many engineering domains—from signal processing and environmental monitoring to forecasting energy demand—we encounter data points indexed in time order. A **Time Series** is precisely this: a sequence of observations recorded sequentially over time. The primary goal of time series analysis is to understand the underlying structure and patterns within this data to build models for description, explanation, and, crucially, forecasting.

A fundamental concept in this pursuit is **stationarity**. For a time series to be easily modeled, its statistical properties should be stable over time. **Linear Stationary Models** are a class of models that assume this stationarity and express the current value of the series as a linear combination of past values, past shocks (random errors), or both.

## Core Concepts

### 1. Stationarity

A time series ${Z_t}$ is said to be **stationary** if its mean, variance, and autocovariance are time-invariant. Formally:

*   **Constant Mean:** $E(Z_t) = \mu$ for all $t$
*   **Constant Variance:** $Var(Z_t) = E[(Z_t - \mu)^2] = \sigma^2$ for all $t$
*   **Constant Autocovariance:** $Cov(Z_t, Z_{t+k}) = \gamma_k$ depends only on the lag $k$, not on time $t$

Why is this important? Modeling non-stationary data (e.g., with trends or seasonal patterns) is like hitting a moving target. Stationary series are more predictable and their properties can be reliably estimated from a single historical record.

### 2. Autocorrelation Function (ACF)

The **Autocorrelation Function (ACF)** is a vital tool for identifying stationary processes and selecting the right model. It measures the linear correlation between a time series and a lagged version of itself. For lag $k$, the ACF is defined as:

$$\rho_k = \frac{Cov(Z_t, Z_{t+k})}{\sqrt{Var(Z_t)Var(Z_{t+k})}} = \frac{\gamma_k}{\gamma_0}$$

Since we assume stationarity, $\gamma_0$ is the constant variance. The plot of $\rho_k$ against $k$ (the lag) is called a **correlogram** and is the fingerprint of a time series process.

### 3. Key Linear Stationary Models

Three basic models form the building blocks for more complex models: MA, AR, and ARMA.

#### a) Moving Average (MA) Model

An **MA(q)** model expresses the current value $Z_t$ as a linear combination of the *current and past random shock terms (a_t)*. The shock $a_t$ is a white noise process with mean 0 and constant variance $\sigma_a^2$.

$$Z_t = \mu + a_t - \theta_1 a_{t-1} - \theta_2 a_{t-2} - ... - \theta_q a_{t-q}$$

*   **Example:** `MA(1)` Model: $Z_t = \mu + a_t - \theta_1 a_{t-1}$
*   **Key Property:** The ACF of an MA(q) process "cuts off" after lag $q$. This means $\rho_k \approx 0$ for all $k > q$. This is a crucial identifier for MA models.

#### b) Autoregressive (AR) Model

An **AR(p)** model expresses the current value $Z_t$ as a linear combination of its *own past values* plus a random shock.

$$Z_t = c + \phi_1 Z_{t-1} + \phi_2 Z_{t-2} + ... + \phi_p Z_{t-p} + a_t$$

*   **Example:** `AR(1)` Model: $Z_t = c + \phi_1 Z_{t-1} + a_t$
*   **Key Property:** The ACF of an AR process decays exponentially or in a sinusoidal manner; it "tails off" slowly. Conversely, its **Partial ACF (PACF)**, which measures the correlation between $Z_t$ and $Z_{t-k}$ after removing the effects of intermediate lags, "cuts off" after lag $p$.

#### c) Autoregressive Moving Average (ARMA) Model

An **ARMA(p, q)** model is a hybrid, combining both Autoregressive and Moving Average components.

$$Z_t = c + \phi_1 Z_{t-1} + ... + \phi_p Z_{t-p} + a_t - \theta_1 a_{t-1} - ... - \theta_q a_{t-q}$$

This model provides a parsimonious representation (fewer parameters) for a wider range of stationary time series patterns. The ACF and PACF of an ARMA process both tail off, providing clues for model selection.

## Summary & Key Points

*   **Stationarity is Key:** The assumption of constant mean, variance, and autocovariance is fundamental for building linear time series models. Non-stationary data often requires differencing to achieve stationarity.
*   **ACF is the Fingerprint:** The Autocorrelation Function plot is the primary tool for identifying the type of process (MA, AR, or ARMA) based on its cutting-off or tailing-off behavior.
*   **Model Definitions:**
    *   **MA(q):** Model based on past forecast errors (shocks). ACF cuts off at lag `q`.
    *   **AR(p):** Model based on past values of the series itself. PACF cuts off at lag `p`.
    *   **ARMA(p, q):** A powerful combination of AR and MA components. Both ACF and PACF tail off.
*   **Building a Model:** The general approach involves:
    1.  Ensuring the series is stationary.
    2.  Plotting the ACF/PACF to identify potential `p` and `q` orders.
    3.  Estimating the model parameters ($\phi$'s, $\theta$'s).
    4.  Performing diagnostic checks on the model residuals.

These linear stationary models form the essential toolkit for any engineer beginning their work in time series forecasting and analysis.