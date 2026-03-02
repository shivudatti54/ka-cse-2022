# Module 4: Some Aspects of More General Seasonal ARIMA Models

## Introduction

Welcome,  Engineering students! In our previous modules, we explored the foundational concepts of ARIMA (Autoregressive Integrated Moving Average) models for non-seasonal time series data. However, many real-world engineering phenomena—from power grid load and river flow to traffic patterns and sensor data—exhibit strong seasonal or periodic behavior. This module extends the standard ARIMA framework to model these complex seasonal patterns effectively. We will delve into the structure, notation, and interpretation of more general Seasonal ARIMA (SARIMA) models.

## Core Concepts

### 1. The Need for Seasonality in ARIMA

A standard ARIMA model is denoted as ARIMA(p, d, q), where:
*   `p`: order of the Autoregressive (AR) part
*   `d`: degree of differencing for making the series stationary
*   `q`: order of the Moving Average (MA) part

This model is powerful but assumes that any patterns are non-seasonal. Seasonal effects repeat every `S` time steps (e.g., S=12 for monthly data, S=4 for quarterly data, S=24 for hourly data with daily seasonality). To capture this, we need to incorporate seasonal components into the ARIMA structure, leading to the **Seasonal ARIMA** or **SARIMA** model.

### 2. SARIMA Notation

A general SARIMA model is succinctly expressed as:
**ARIMA(p, d, q)×(P, D, Q)<sub>S</sub>**

Let's break down the new seasonal components:
*   **`S`**: The number of time periods until the season repeats (the seasonal period).
*   **`P`**: Seasonal Autoregressive (SAR) order. It models how an observation is related to observations from *previous seasons*. For example, the current month's temperature might be correlated with the temperature from the same month last year.
*   **`D`**: Seasonal Differencing order. This is used to remove seasonal non-stationarity. A seasonal difference of order 1 is calculated as `z_t = y_t - y_{t-S}`.
*   **`Q`**: Seasonal Moving Average (SMA) order. It incorporates the impact of past seasonal forecast errors (white noise terms) into the model.

The `(p, d, q)` part is often called the **non-seasonal** or **regular** part of the model, handling short-term dependencies and trends.

### 3. The Backshift Operator in SARIMA

The backshift operator, `B`, where `B y_t = y_{t-1}`, is crucial for writing the model's equation compactly. A seasonal lag of `S` is written as `B^S`, so `B^S y_t = y_{t-S}`.

The general form of a SARIMA(p, d, q)×(P, D, Q)<sub>S</sub> model is defined by the equation:

**φ<sub>p</sub>(B) Φ<sub>P</sub>(B<sup>S</sup>) (1 - B)<sup>d</sup>(1 - B<sup>S</sup>)<sup>D</sup> y<sub>t</sub> = θ<sub>q</sub>(B) Θ<sub>Q</sub>(B<sup>S</sup>) ε<sub>t</sub>**

Where:
*   `φ_p(B)` is the regular AR polynomial of order `p`.
*   `Φ_P(B^S)` is the seasonal AR polynomial of order `P`.
*   `(1 - B)^d` is the regular differencing operator.
*   `(1 - B^S)^D` is the seasonal differencing operator.
*   `θ_q(B)` is the regular MA polynomial of order `q`.
*   `Θ_Q(B^S)` is the seasonal MA polynomial of order `Q`.
*   `ε_t` is the white noise error term.

### 4. Example: Interpreting a SARIMA Model

Let's interpret a specific model: **SARIMA(1, 1, 1)×(0, 1, 1)<sub>12</sub>** for monthly data (`S=12`).

1.  **Non-seasonal part (1,1,1)**:
    *   `d=1`: We take a first difference to remove a linear trend: `y'_t = y_t - y_{t-1}`.
    *   `p=1`: There is one regular AR term. The current value depends on its immediately previous value.
    *   `q=1`: There is one regular MA term. The current shock depends on the previous shock.

2.  **Seasonal part (0,1,1)₁₂**:
    *   `D=1`: We take a *seasonal* difference of order 1. Combined with the regular difference, the full transformation is: `z_t = (y_t - y_{t-1}) - (y_{t-12} - y_{t-13})`.
    *   `P=0`: There is no seasonal autoregressive component.
    *   `Q=1`: There is one seasonal moving average term. This means the model accounts for the shock that occurred one full season (12 months) ago.

In simpler terms, this model predicts the current value based on its previous value, its previous error, and the error from the same month in the previous year, after removing both trend and seasonal trend.

## Key Points and Summary

*   **Purpose**: SARIMA models extend ARIMA to handle time series data with strong **seasonal patterns**.
*   **Notation**: A SARIMA model is denoted as **ARIMA(p, d, q)×(P, D, Q)<sub>S</sub>**, where the lowercase letters represent the non-seasonal components and the uppercase letters represent the seasonal components.
*   **`S` is Critical**: The seasonal period `S` must be correctly identified based on the data context (e.g., 12 for monthly, 24 for hourly).
*   **Differencing**: Two types are used: **Regular differencing (`d`)** to remove trend and **Seasonal differencing (`D`)** to remove seasonal trends.
*   **Model Building**: The Box-Jenkins methodology (Identification, Estimation, Diagnostic Checking) applies to SARIMA as well. The ACF and PACF plots are analyzed for both regular and seasonal lags to identify potential `p, q, P, Q` values.
*   **Application**: SARIMA is widely used in engineering forecasts, including **predicting energy demand, network traffic, environmental data, and resource allocation**.

Mastering SARIMA models equips you with a powerful tool to analyze and forecast the complex, seasonal data prevalent in countless engineering systems.