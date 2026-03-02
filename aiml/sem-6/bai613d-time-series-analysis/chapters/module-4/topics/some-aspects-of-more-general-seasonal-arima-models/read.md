# Some Aspects of More General Seasonal ARIMA Models

## Introduction

Welcome,  engineering students! In our previous modules, we explored fundamental ARIMA (AutoRegressive Integrated Moving Average) models for non-seasonal time series data. However, many real-world engineering phenomena—from monthly power grid loads and quarterly water reservoir levels to hourly traffic flow data—exhibit strong seasonal patterns. The standard ARIMA model falls short in capturing these periodic behaviors. This module extends the ARIMA framework by incorporating seasonal components, leading us to the powerful **Seasonal ARIMA** model, often denoted as **SARIMA**.

## Core Concepts of SARIMA Models

A general Seasonal ARIMA model is formally specified as **ARIMA(p, d, q)×(P, D, Q)ₛ**. This notation might look daunting, but it logically extends the standard ARIMA model.

*   **Standard (Non-Seasonal) Components:**
    *   `p`: Order of the non-seasonal AutoRegressive (AR) term.
    *   `d`: Degree of non-seasonal Differencing.
    *   `q`: Order of the non-seasonal Moving Average (MA) term.

*   **Seasonal Components:**
    *   `P`: Order of the **seasonal** AutoRegressive (SAR) term.
    *   `D`: Degree of **seasonal** Differencing (often 1, differencing at lag s).
    *   `Q`: Order of the **seasonal** Moving Average (SMA) term.
    *   `s`: The number of time periods until the pattern repeats, i.e., the **seasonal period** (e.g., `s=12` for monthly data, `s=4` for quarterly data).

### The Backshift Operator Notation

The beauty of the SARIMA model is best expressed using the backshift operator (`B`), where `BᵏYₜ = Yₜ₋ₖ`.

The general multiplicative SARIMA model is written as:
**Φₚ(Bˢ) φₚ(B) (1 - Bˢ)ᴰ (1 - B)ᵈ Yₜ = θq(B) ΘQ(Bˢ) εₜ**

Let's break this down:
1.  **Differencing Polynomial:** `(1 - Bˢ)ᴰ (1 - B)ᵈ Yₜ` applies both seasonal and non-seasonal differencing to make the series stationary.
2.  **AR Polynomial:** `Φₚ(Bˢ) φₚ(B)` models the dependency between observations. This includes:
    *   `φₚ(B)`: Standard AR component (e.g., `φ₁Yₜ₋₁`).
    *   `Φₚ(Bˢ)`: Seasonal AR component (e.g., `Φ₁Yₜ₋₁₂` for monthly data).
3.  **MA Polynomial:** `θq(B) ΘQ(Bˢ)` models the dependency between error terms (shocks). This includes:
    *   `θq(B)`: Standard MA component (e.g., `θ₁εₜ₋₁`).
    *   `ΘQ(Bˢ)`: Seasonal MA component (e.g., `Θ₁εₜ₋₁₂`).

## Example: Building a SARIMA Model

Imagine you are an engineer analyzing **monthly electricity consumption** (`s=12`) for a city. The data shows a clear yearly cycle and a positive trend.

**Step 1: Make the Series Stationary**
*   The data has a trend, so you apply first-order non-seasonal differencing: `d=1`.
*   A strong seasonal pattern remains. You apply first-order seasonal differencing at lag 12: `D=1`.
    *   The transformed series becomes: `Wₜ = (1 - B)(1 - B¹²)Yₜ = (Yₜ - Yₜ₋₁) - (Yₜ₋₁₂ - Yₜ₋₁₃)`

**Step 2: Identify Model Orders (p, q, P, Q)**
You analyze the ACF and PACF plots of the differenced series `Wₜ`:
*   The ACF shows a significant spike *only* at lag 12. This suggests a Seasonal Moving Average (SMA) term of order 1: `Q=1`.
*   The PACF shows a significant spike *only* at lag 1. This suggests a non-seasonal AutoRegressive (AR) term of order 1: `p=1`.
*   No other significant seasonal or non-seasonal correlations are evident, so you set `P=0` and `q=0`.

**Step 3: Specify and Fit the Model**
You have identified an **ARIMA(1, 1, 0)×(0, 1, 1)₁₂** model.
In equation form, this model is:
`(1 - φ₁B)(1 - B)(1 - B¹²)Yₜ = (1 - Θ₁B¹²)εₜ`

This model intuitively states that the current electricity consumption is:
*   Related to its value from the previous month (via the `φ₁` term).
*   Affected by a "shock" or unusual event that happened during the same month in the previous year (via the `Θ₁` term).

## Key Points and Summary

*   **Purpose:** SARIMA models are essential for forecasting time series data that contains both trends and **seasonal patterns**.
*   **Model Notation:** ARIMA**(p, d, q)×(P, D, Q)ₛ**. Mastery of this notation is key to understanding and specifying models.
*   **The `s` Parameter:** The seasonal period `s` is critical and is determined by the data context (e.g., 12 for monthly, 4 for quarterly, 24 for hourly daily patterns).
*   **Model Building Process:** The standard workflow involves:
    1.  **Visualization:** Plot the data to identify trend and seasonality.
    2.  **Differencing:** Apply non-seasonal (`d`) and seasonal (`D`) differencing to achieve stationarity.
    3.  **Order Identification:** Use ACF/PACF plots of the differenced series to identify `p`, `q`, `P`, and `Q`.
    4.  **Parameter Estimation & Diagnostics:** Fit the model, check residuals for randomness, and refine if necessary.
*   **Engineering Application:** From predicting network traffic and structural vibrations to forecasting renewable energy output, SARIMA provides a robust statistical framework for modeling and predicting cyclical engineering data.