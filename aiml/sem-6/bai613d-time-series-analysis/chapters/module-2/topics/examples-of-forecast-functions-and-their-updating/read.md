# Module 2: Examples of Forecast Functions and Their Updating

## Introduction

In Time Series Analysis, a forecast function is the mathematical formula we use to generate predictions for future values of a time series. Once a model (like ARIMA) is fitted, its forecast function provides the means to project the series forward. However, as new data becomes available, these forecasts must be updated efficiently without refitting the entire model from scratch. This process is called **forecast updating** or **forecast revision**. This module explores common forecast functions and the mechanics behind their updating.

## Core Concepts

### 1. The General Form of a Forecast Function

For a general ARIMA(p,d,q) model, $\phi(B)\nabla^d z_t = \theta(B)a_t$, the forecast function $\hat{z}_t(l)$ for lead time $l$ is the conditional expectation of the future value $z_{t+l}$ given all information up to time $t$. The solution to this difference equation, for $l > q$, is a function that depends solely on the **Autoregressive (AR)** and **Differencing** components.

The general solution takes the form:
$$\hat{z}_t(l) = C_1(t)f_1(l) + C_2(t)f_2(l) + ... + C_p(t)f_p(l)$$
where $f_i(l)$ are functions of the lead time $l$ (e.g., polynomials, exponentials, sines/cosines) determined by the model's **characteristic equation**. The coefficients $C_i(t)$ are **adaptive coefficients** that are updated as new observations $z_{t+1}$ become available.

### 2. The Principle of Updating Forecasts

The key idea is that when we move from time $t$ to $t+1$, we gain a new observation $z_{t+1}$. This new data point is compared to its one-step-ahead forecast made at time $t$, which is $\hat{z}_t(1)$. The difference between the actual value and this forecast is the **forecast error** $a_{t+1} = z_{t+1} - \hat{z}_t(1)$.

This forecast error contains new information about the process. Updating incorporates this new information by revising the adaptive coefficients $C_i(t)$ to $C_i(t+1)$, leading to revised forecasts for all future lead times.

## Examples of Forecast Functions and Their Updating

### Example 1: ARIMA(0,1,0) or the Random Walk Model

This is one of the simplest non-stationary models: $\nabla z_t = a_t$ or $z_t = z_{t-1} + a_t$.

*   **Forecast Function:** The forecast function is trivial. The best forecast for any future value is simply the last observed value.
    $$\hat{z}_t(l) = z_t \quad \text{for all } l \geq 1$$
*   **Updating:** When a new observation $z_{t+1}$ arrives, the entire forecast function is updated to a new constant level.
    $$\hat{z}_{t+1}(l) = z_{t+1} \quad \text{for all } l \geq 1$$
    The forecast error $a_{t+1} = z_{t+1} - z_t$ is directly incorporated into the new forecast.

### Example 2: ARIMA(0,2,0) or the Linear Growth Model

This model involves second differences: $\nabla^2 z_t = a_t$, implying a local linear trend.

*   **Forecast Function:** The solution is a linear function in $l$:
    $$\hat{z}_t(l) = b_0^{(t)} + b_1^{(t)}l$$
    Here, $b_0^{(t)}$ is the estimated level at time $t$, and $b_1^{(t)}$ is the estimated slope at time $t$.
*   **Updating:** The coefficients are updated using the new forecast error $a_{t+1} = z_{t+1} - \hat{z}_t(1)$. The common updating equations (similar to Holt's linear method) are:
    $$
    \begin{aligned}
    b_0^{(t+1)} &= z_{t+1} \\
    b_1^{(t+1)} &= b_1^{(t)} + (z_{t+1} - \hat{z}_t(1)) \\
    \end{aligned}
    $$
    More precisely, the updating equations can be derived as:
    $$
    \begin{aligned}
    b_0^{(t+1)} &= b_0^{(t)} + b_1^{(t)} + a_{t+1} \\
    b_1^{(t+1)} &= b_1^{(t)} + a_{t+1} \\
    \end{aligned}
    $$
    The new forecast function becomes $\hat{z}_{t+1}(l) = b_0^{(t+1)} + b_1^{(t+1)}l$.

### Example 3: ARIMA(0,1,1) Model

This model is $\nabla z_t = a_t - \theta a_{t-1}$ and is equivalent to Simple Exponential Smoothing.

*   **Forecast Function:** The forecast function is constant for all lead times.
    $$\hat{z}_t(l) = C_1(t) \quad \text{for all } l \geq 1$$
    Where $C_1(t)$ is the smoothed level at time $t$.
*   **Updating:** The coefficient is updated using the one-step-ahead forecast error. The updating equation is:
    $$C_1(t+1) = \hat{z}_{t+1}(l) = z_{t+1} + (1-\theta)a_{t+1} = (1-\theta)z_{t+1} + \theta \hat{z}_t(1)$$
    This shows how the new level is a weighted average of the new observation and the old forecast, which is the essence of exponential smoothing.

## Key Points & Summary

*   **Forecast Function Purpose:** Provides the mathematical form for generating out-of-sample predictions from a fitted time series model.
*   **Determining Components:** The form of the forecast function (constant, linear, quadratic, damped, etc.) is determined by the **Autoregressive (AR)** and **Differencing** parts of the ARIMA model.
*   **Adaptive Coefficients:** The function contains coefficients ($C_i(t)$) that are "weights" or "states" updated with each new observation.
*   **Update Mechanism:** Forecasts are updated using the **one-step-ahead forecast error** ($a_{t+1} = z_{t+1} - \hat{z}_t(1)$). This error carries the new information.
*   **Efficiency:** This method allows for efficient, recursive updating of forecasts for all future time periods without the computational burden of re-estimating the entire model.
*   **Link to Smoothing:** The updating procedure for many ARIMA models (like ARIMA(0,1,1)) is directly equivalent to classical exponential smoothing techniques.

Understanding these principles allows engineers to not only generate forecasts but also to design efficient systems for maintaining and updating predictive models in real-time applications like signal processing, load forecasting, and economic indicator prediction.