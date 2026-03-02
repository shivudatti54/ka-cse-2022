# Module 2: Forecasting in Time Series Analysis

## Introduction

Forecasting is the cornerstone of Time Series Analysis. It is the process of using historical data to make informed predictions about future values of a time series. For engineering disciplines—be it predicting electricity load for power grid management, forecasting component failure rates in mechanical systems, or estimating future network traffic in telecommunications—accurate forecasting is critical for efficient planning, optimization, and decision-making. This module delves into the core concepts and methodologies used for forecasting time series data.

## Core Concepts of Forecasting

### 1. The Forecasting Objective

The primary goal is to predict future values of a series, $Z_{t+l}$, where $l$ is the **lead time** or **forecast horizon**. The forecast made at origin $t$ for lead time $l$ is denoted by $\hat{Z}_t(l)$.

### 2. Measures of Forecast Accuracy

To evaluate and compare different forecasting models, we need quantitative measures of accuracy. Common measures include:

*   **Mean Squared Error (MSE):** The average of the squared forecast errors.
    $\text{MSE} = \frac{1}{N} \sum_{t=1}^{N} (Z_t - \hat{Z}_t)^2$
*   **Mean Absolute Error (MAE):** The average of the absolute forecast errors.
    $\text{MAE} = \frac{1}{N} \sum_{t=1}^{N} |Z_t - \hat{Z}_t|$
*   **Mean Absolute Percentage Error (MAPE):** Expresses the error as a percentage of the actual values, making it scale-independent.
    $\text{MAPE} = \frac{100\%}{N} \sum_{t=1}^{N} \left| \frac{Z_t - \hat{Z}_t}{Z_t} \right|$

A lower value for these measures indicates a better forecast.

### 3. Forecasting with Moving Average (MA) Models

For an **MA(q)** model: $Z_t = a_t - \theta_1 a_{t-1} - \theta_2 a_{t-2} - ... - \theta_q a_{t-q}$

*   The forecast for lead time 1 is based on the current and past shocks (white noise terms, $a_t$).
*   Since future shocks ($a_{t+l}$ for $l>0$) are unknown and have an expected value of zero, the forecast for any lead time $l > q$ becomes zero. This is a key characteristic of MA models; their forecasts **cut off** after the order `q` of the model.

**Example:** For an **MA(1)** model: $Z_t = a_t - \theta a_{t-1}$
*   $\hat{Z}_t(1) = E[Z_{t+1}] = E[a_{t+1} - \theta a_t] = -\theta a_t$ (since $E[a_{t+1}]=0$ and $a_t$ is known)
*   $\hat{Z}_t(2) = E[Z_{t+2}] = E[a_{t+2} - \theta a_{t+1}] = 0$

### 4. Forecasting with Autoregressive (AR) Models

For an **AR(p)** model: $Z_t = \phi_1 Z_{t-1} + \phi_2 Z_{t-2} + ... + \phi_p Z_{t-p} + a_t$

*   Forecasting involves recursion. The forecast $\hat{Z}_t(l)$ is a linear combination of the *previous forecasts* and the *last `p` known observations*.
*   Unlike MA models, AR forecasts **do not cut off** but gradually decay toward the series mean (often zero if the series is stationary).

**Example:** For an **AR(1)** model: $Z_t = \phi Z_{t-1} + a_t$
*   $\hat{Z}_t(1) = E[Z_{t+1}] = \phi Z_t$ (the known current value)
*   $\hat{Z}_t(2) = E[Z_{t+2}] = \phi \hat{Z}_t(1) = \phi^2 Z_t$
*   $\hat{Z}_t(l) = \phi^l Z_t$
As `l` increases, this forecast decays to zero if $|\phi| < 1$.

### 5. Forecasting with ARMA Models

An **ARMA(p, q)** model combines both AR and MA components:
$Z_t = \phi_1 Z_{t-1} + ... + \phi_p Z_{t-p} + a_t - \theta_1 a_{t-1} - ... - \theta_q a_{t-q}$

The forecast is a weighted sum of:
1.  The last `p` observations ($Z_t, Z_{t-1}, ..., Z_{t-p+1}$),
2.  The last `q` forecasts ($\hat{Z}_t(1), \hat{Z}_{t-1}(1), ...$), and
3.  The last `q` shocks ($a_t, a_{t-1}, ..., a_{t-q+1}$).

The forecast function will generally exhibit a mixture of exponential decay and sinusoidal behavior, determined by the model's parameters.

### 6. The Forecast Error and Prediction Intervals

A point forecast ($\hat{Z}_t(l)$) is a single estimated value. It is equally important to quantify the uncertainty of this forecast.

*   The **forecast error** is $e_t(l) = Z_{t+l} - \hat{Z}_t(l)$.
*   The variance of this forecast error, $\sigma^2_e(l)$, can be derived from the model.
*   A **95% Prediction Interval** for the future value $Z_{t+l}$ is then given by:
    $\hat{Z}_t(l) \pm 1.96 \cdot \sigma_e(l)$

This interval provides a range of values within which the future observation is expected to fall with 95% probability, offering a crucial measure of forecast reliability.

## Key Points & Summary

*   **Purpose:** Forecasting uses historical time series data to predict future values, which is vital for engineering planning and optimization.
*   **Model Dependency:** The forecasting method is entirely dependent on the identified model (MA, AR, or ARMA). Each model type produces a distinct forecast pattern (e.g., MA cuts off, AR decays).
*   **Accuracy Measurement:** Use metrics like MSE, MAE, and MAPE to objectively evaluate and compare the performance of different forecasting models.
*   **Uncertainty Quantification:** A forecast is incomplete without a measure of its uncertainty. Always compute **prediction intervals** to understand the potential range of future outcomes.
*   **Recursive Nature:** Forecasting for AR and ARMA models is a recursive process, relying on both past observations and previous forecasted values.

Mastering these concepts allows engineers to not only generate predictions but also to critically assess their reliability, leading to more robust and data-driven decisions.