# Module 2: Autoregressive Integrated Moving Average (ARIMA) Processes

## Introduction

In the previous module, you were introduced to fundamental time series concepts like stationarity, autocorrelation, and basic models like AR(p) and MA(q). The **Autoregressive Integrated Moving Average (ARIMA)** model is a powerful generalization that combines these concepts to model a much wider range of non-stationary time series data commonly encountered in engineering fields, such as signal processing, economic forecasting, and vibration analysis. It is arguably one of the most widely used time series forecasting techniques.

## Core Concepts Explained

An ARIMA model is characterized by three order parameters: `(p, d, q)`. Understanding these parameters is key to understanding the model itself.

*   **AR (Autoregressive part - `p`)**: This component of the model regresses the variable against its own prior values. The order `p` represents the number of lag observations included in the model. It captures the momentum and mean-reversion effects in the data.
    *   **Formula for AR(p):** $Y_t = c + \phi_1Y_{t-1} + \phi_2Y_{t-2} + ... + \phi_pY_{t-p} + \epsilon_t$
    *   **Example:** Predicting tomorrow's power grid load based on the loads of the previous `p` days.

*   **I (Integrated part - `d`)**: This refers to the **differencing** degree applied to the time series to make it **stationary**. Differencing removes changes in the level of a time series, eliminating trend and seasonality. The order `d` is the number of times the raw data is differenced.
    *   **First Difference:** $\nabla Y_t = Y_t - Y_{t-1}$
    *   **Second Difference:** $\nabla^2 Y_t = \nabla(Y_t - Y_{t-1}) = (Y_t - Y_{t-1}) - (Y_{t-1} - Y_{t-2})$
    *   **Why it's crucial:** ARMA models (AR + MA) assume stationarity. The "I" in ARIMA allows us to model non-stationary data by first transforming it into a stationary series through differencing. If a series is already stationary, `d=0`.

*   **MA (Moving Average part - `q`)**: This component models the error term as a linear combination of past error terms. The order `q` represents the number of lagged forecast errors to include. It captures the effect of sudden "shocks" or innovations to the series.
    *   **Formula for MA(q):** $Y_t = \mu + \epsilon_t + \theta_1\epsilon_{t-1} + \theta_2\epsilon_{t-2} + ... + \theta_q\epsilon_{t-q}$
    *   **Example:** Modeling a system's output where the current state depends not just on its previous state but also on random, unobserved "shocks" from the previous `q` time steps.

An ARIMA model is typically denoted as **ARIMA(p, d, q)**. For example, a model specified as ARIMA(1, 1, 1) would mean:
*   `p=1`: It contains one autoregressive lag.
*   `d=1`: The time series was differenced once to achieve stationarity.
*   `q=1`: It contains one moving average lag.

### The General ARIMA(p,d,q) Model

A stationary series after differencing `d` times (let's call it $W_t = \nabla^d Y_t$) is modeled as:
$$W_t = c + \phi_1W_{t-1} + ... + \phi_pW_{t-p} + \epsilon_t + \theta_1\epsilon_{t-1} + ... + \theta_q\epsilon_{t-q}$$
This is essentially an ARMA(p, q) model applied to the differenced data. The model predicts the next value based on:
1.  Its own past values (AR component).
2.  The cumulative past forecast errors (MA component).

### The Box-Jenkins Methodology

Building an ARIMA model is not a blind guess of `(p, d, q)`. It follows a structured, iterative approach known as the **Box-Jenkins Methodology**:
1.  **Identification**: Use plots (time series plot, ACF, PACF) to determine if the data is stationary and guess appropriate values for `p`, `d`, and `q`.
    *   **Determine `d`**: Difference the series until it appears stationary (constant mean and variance).
    *   **Determine `p` and `q`**: Analyze the ACF and PACF plots of the *stationary* (differenced) data. The patterns in these plots suggest orders for the AR and MA parts.
2.  **Estimation**: Use computational methods (e.g., Maximum Likelihood Estimation) to estimate the coefficients ($\phi$'s and $\theta$'s) for the chosen `(p, d, q)` order.
3.  **Diagnostic Checking**: Validate the model. Check if the residuals (the difference between actual and forecasted values) resemble white noise (no autocorrelation). If not, return to step 1 and try a different order.

## Example

Imagine a non-stationary time series of monthly semiconductor sales with a clear upward trend.

1.  **Identification**: The raw data is non-stationary. We apply first differencing (`d=1`). The differenced data now has a constant mean (looks stationary).
2.  **Analyze ACF/PACF**: The ACF of the differenced data shows a sharp cutoff after lag 1, and the PACF shows a gradual decay. This is a classic signature of an MA(1) process.
3.  **Model Selection**: We hypothesize an ARIMA(0, 1, 1) model for the original sales data.
4.  **Estimation & Forecasting**: The model is fitted, and forecasts are generated. The forecasts will follow the trend of the original data because the model was built on the changes (differences).

## Key Points & Summary

*   **ARIMA** combines Autoregression (AR), Differencing (I), and Moving Average (MA) components.
*   The model is defined by its **order (p, d, q)**:
    *   `p`: Order of the Autoregressive part (number of AR terms).
    *   `d`: Degree of Differencing (number of times data is differenced to achieve stationarity).
    *   `q`: Order of the Moving Average part (number of MA terms).
*   The **"I" (Integrated)** component is what allows ARIMA to model **non-stationary** data, making it extremely versatile.
*   Model building is guided by the **Box-Jenkins Methodology** (Identification, Estimation, Diagnostic Checking).
*   **ACF and PACF plots** are essential tools for identifying the potential orders `p` and `q` after making the series stationary.
*   ARIMA is a foundational model for understanding more complex models like SARIMA (which adds seasonal components) and is widely applied in forecasting and system modeling.