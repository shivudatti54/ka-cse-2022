# Time Series Analysis: Linear Nonstationary Models

## Introduction

In Module 1, we explored stationary models where the mean, variance, and autocorrelation structure remain constant over time. However, most real-world engineering and economic data (like stock prices, sensor readings from a non-controlled environment, or electricity demand) exhibit trends, cycles, or other forms of nonstationarity. **Linear Nonstationary Models** form a cornerstone of classical time series analysis, providing the tools to model, understand, and forecast such data. This module focuses on the most important family of these models: the Autoregressive Integrated Moving Average (ARIMA) models.

## Core Concepts

### 1. The Principle of Differencing

The fundamental idea behind handling nonstationarity is to transform a nonstationary series into a stationary one through a simple operation called **differencing**.

*   **First Differencing:** For a time series `Y_t`, the first difference is defined as:
    `∇Y_t = Y_t - Y_{t-1}`
    This operation often removes a linear trend. For instance, if `Y_t` increases by a constant amount each time period (e.g., `Y_t = β₀ + β₁*t`), then `∇Y_t` becomes a constant (`β₁`), which is stationary.

*   **Second Differencing:** If first differencing doesn't achieve stationarity (e.g., the series has a quadratic trend), we can apply differencing a second time:
    `∇²Y_t = ∇(∇Y_t) = (Y_t - Y_{t-1}) - (Y_{t-1} - Y_{t-2}) = Y_t - 2Y_{t-1} + Y_{t-2}`
    Second differencing can remove quadratic trends.

*   **Seasonal Differencing:** For data with a seasonal pattern (e.g., monthly temperature data), differencing at the seasonal period `s` can be applied:
    `∇_s Y_t = Y_t - Y_{t-s}`

The number of times (`d`) a series must be differenced to become stationary is a key parameter.

### 2. The ARIMA Model

The **Autoregressive Integrated Moving Average (ARIMA)** model combines Autoregressive (AR) and Moving Average (MA) components with an **Integrated** (I) component, which represents the differencing step. An ARIMA model is denoted as **ARIMA(p, d, q)**.

*   **p**: The order of the Autoregressive (AR) part. It signifies how many past values (`Y_{t-1}, Y_{t-2}, ..., Y_{t-p}`) are used to predict the current value.
*   **d**: The order of Integration (differencing). This is the number of times the raw data needs to be differenced to achieve stationarity (`d = 0` implies a stationary ARMA model).
*   **q**: The order of the Moving Average (MA) part. It signifies how many past error terms (`ε_{t-1}, ε_{t-2}, ..., ε_{t-q}`) are used to predict the current value.

The general form of an ARIMA(p, d, q) model is:
`∇^d Y_t = c + Φ₁∇^d Y_{t-1} + ... + Φ_p ∇^d Y_{t-p} + ε_t + θ₁ε_{t-1} + ... + θ_q ε_{t-q}`
Where `∇^d Y_t` is the differenced series (which is stationary), `ε_t` is white noise, and the `Φ` and `θ` are model coefficients.

### 3. The Random Walk Model

A **Random Walk** is the simplest nonstationary model and a special case of ARIMA. It is defined as:
`Y_t = Y_{t-1} + ε_t`
where `ε_t` is white noise. This implies that the current value is simply the previous value plus a random shock. Its first difference, `∇Y_t = ε_t`, is stationary (white noise). Therefore, a Random Walk is an **ARIMA(0, 1, 0)** model.

**Example:** Modelling the daily closing price of a stock. It's often difficult to predict the price itself, but the *change* in price from one day to the next (`∇Price`) may appear random, making the Random Walk a useful baseline model.

### 4. The ARIMA Model-Building Process (Box-Jenkins Methodology)

Fitting an ARIMA model to data is a systematic process:
1.  **Identification:** Use plots (time series plot, ACF, PACF) to determine the appropriate differencing order `d` to achieve stationarity. Then, use the ACF and PACF of the *stationary* series to suggest potential `p` and `q` orders.
2.  **Estimation:** Use statistical software (like R or Python's `statsmodels`) to estimate the coefficients (`Φ`s and `θ`s) for the candidate model.
3.  **Diagnostic Checking:** Analyze the residuals (the differences between the actual values and the model's predictions). If the model is good, the residuals should resemble white noise (no discernible patterns). If not, return to step 1.

## Key Points & Summary

*   **Purpose:** Linear nonstationary models, primarily ARIMA, are used to analyze and forecast time series data that exhibit trends or other nonstationary behavior.
*   **Core Mechanism:** **Differencing** is the key operation to transform a nonstationary series into a stationary one, which can then be modeled using ARMA components.
*   **ARIMA(p,d,q):** The general model where:
    *   `p` is the autoregressive order.
    *   `d` is the differencing order.
    *   `q` is the moving average order.
*   **Random Walk:** A fundamental ARIMA(0,1,0) model where the current value equals the previous value plus a random step. Its first difference is white noise.
*   **Methodology:** The Box-Jenkins approach provides a structured framework (Identify-Estimate-Diagnose) for building and selecting the best ARIMA model for a given dataset.
*   **Engineering Relevance:** These models are crucial for forecasting in various engineering domains, including predicting network traffic, power load demand, sensor drift, and structural health monitoring data.