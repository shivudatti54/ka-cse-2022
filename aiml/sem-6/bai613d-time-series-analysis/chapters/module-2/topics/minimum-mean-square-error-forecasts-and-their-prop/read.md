# Module 2: Minimum Mean Square Error (MMSE) Forecasts and Their Properties

## Introduction

In the realm of Time Series Analysis, the ultimate goal is often to predict future values of a series based on its past behavior. Among various forecasting methods, the **Minimum Mean Square Error (MMSE)** forecast stands out as a powerful and theoretically sound approach. It provides the "best" forecast in a very specific and useful sense: it minimizes the expected value of the square of the forecast error. This module delves into the core concepts, derivation, and crucial properties of MMSE forecasts, which form the bedrock of many advanced forecasting techniques.

## Core Concepts

### 1. The Forecast Function and the Criterion

Let `z_t` be a stationary time series. Suppose at time `t` we have all observations `{..., z_{t-1}, z_t}` and wish to forecast the value `l` steps ahead, i.e., `z_{t+l}`.

We denote the forecast as `ẑ_t(l)`. The **forecast error** is defined as:
`e_t(l) = z_{t+l} - ẑ_t(l)`

The **Mean Square Error (MSE)** of this forecast is:
`MSE = E[ (e_t(l))^2 ] = E[ (z_{t+l} - ẑ_t(l))^2 ]`

The **Minimum Mean Square Error (MMSE)** forecast is the function `ẑ_t(l)` that minimizes this MSE.

### 2. Derivation of the MMSE Forecast

It can be proven using calculus and properties of expectations that the function of the observed data `{..., z_{t-1}, z_t}` that minimizes `E[ (z_{t+l} - ẑ_t(l))^2 ]` is the **conditional expectation**:
`ẑ_t(l) = E[ z_{t+l} | z_t, z_{t-1}, z_{t-2}, ... ]`

This makes intuitive sense: the best prediction (in the MSE sense) of a future value is the average (or expected value) of all its possible realizations, given everything we have observed up to the present.

### 3. Practical Calculation using ARIMA Models

For a general linear process, the MMSE forecast can be derived by expressing the model in its **random shock form** (infinite MA representation). Consider an `ARIMA(p, d, q)` model that has been differenced `d` times to become stationary, effectively an `ARMA(p, q)` model `φ(B)z_t = θ(B)a_t`, where `a_t` is white noise.

The optimal forecast `ẑ_t(l)` is obtained by writing the model for the future time `t+l` and then taking the conditional expectation at time `t`.

**The rules for taking conditional expectations `E_t[.]` are:**
*   `E_t[ z_{t-k}] = z_{t-k}` for `k ≥ 0` (past and present are known)
*   `E_t[ z_{t+k}] = ẑ_t(k)` for `k > 0` (future values are forecasts)
*   `E_t[ a_{t-k}] = a_{t-k}` for `k ≥ 0` (past shocks are known, calculated from the model)
*   `E_t[ a_{t+k}] = 0` for `k > 0` (future shocks are unknown, and their best prediction is their mean, zero)

**Example: Forecasting with an AR(1) Model**

Let `z_t = φ z_{t-1} + a_t`, where `|φ| < 1`.
To find the 1-step-ahead forecast `ẑ_t(1)`:
`z_{t+1} = φ z_t + a_{t+1}`
Take conditional expectation:
`E_t[z_{t+1}] = E_t[φ z_t] + E_t[a_{t+1}]`
`ẑ_t(1) = φ z_t + 0 = φ z_t`

To find the 2-step-ahead forecast `ẑ_t(2)`:
`z_{t+2} = φ z_{t+1} + a_{t+2}`
`E_t[z_{t+2}] = φ E_t[z_{t+1}] + E_t[a_{t+2}]`
`ẑ_t(2) = φ (φ z_t) + 0 = φ^2 z_t`

In general, for an AR(1) model, `ẑ_t(l) = φ^l z_t`.

## Key Properties of MMSE Forecasts

1.  **Unbiasedness:** The forecast is unbiased. The expected value of the forecast error is zero: `E[e_t(l)] = 0`.
    *   *Interpretation:* On average, over many forecasts, we are neither over-predicting nor under-predicting.

2.  **Forecast Errors are Uncorrelated:** The forecast errors for *different lead times* (`e_t(l)` and `e_t(l+v)` for `v ≠ 0`) are uncorrelated.
    *   *Interpretation:* An error in forecasting, say, next month's value provides no linear information about the error you will make in forecasting the value six months from now.

3.  **Variance of Forecast Errors:** The variance of the forecast errors increases as the forecast horizon `l` increases. For a linear model, it converges to the variance of the time series itself as `l → ∞`.
    *   *Interpretation:* The further into the future we predict, the less certain we become. The forecast interval will widen accordingly.

4.  **Updating:** As new data becomes available, forecasts can be updated efficiently using the latest forecast error. For example, in the AR(1) case:
    `ẑ_{t+1}(l) = φ^{l} z_{t+1} = φ^{l} (φ z_t + a_{t+1}) = φ^{l+1} z_t + φ^{l} a_{t+1} = φ ẑ_t(l) + φ^{l} a_{t+1}`

## Summary

*   The **MMSE forecast** `ẑ_t(l)` is the forecast that minimizes the expected squared prediction error.
*   It is given by the **conditional expectation** `E[ z_{t+l} | z_t, z_{t-1}, ... ]`.
*   In practice, it is calculated from an ARIMA model by applying simple **rules of conditional expectation** to the model's random shock form.
*   Its key properties ensure it is **unbiased**, its errors are **uncorrelated across lead times**, and its **uncertainty (variance) increases with the forecast horizon**.
*   These properties make MMSE forecasting a cornerstone of modern time series prediction, providing a strong theoretical foundation for generating and interpreting predictions.