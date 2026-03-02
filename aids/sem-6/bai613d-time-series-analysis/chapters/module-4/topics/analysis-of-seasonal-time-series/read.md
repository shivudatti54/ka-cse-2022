Of course. Here is a comprehensive educational note on the Analysis of Seasonal Time Series for  engineering students.

# Module 4: Analysis of Seasonal Time Series

## 1. Introduction

In the real world, many time series data exhibit patterns that repeat over fixed intervals. For example, electricity consumption peaks during summer afternoons, retail sales surge during festival seasons, and river levels rise during monsoons. These repeating patterns are called **seasonality**. A seasonal time series is one that contains this systematic, calendar-related variation. Analyzing such series requires specialized techniques to decompose these patterns, understand the underlying structure, and build accurate forecasting models. This module focuses on the core methods for analyzing and modeling seasonal time series.

## 2. Core Concepts

### a) What is Seasonality?

**Seasonality** is a component of a time series that repeats at regular intervals over time. The key characteristic is that the pattern's period is fixed and known.
*   **Period (s):** The number of time periods after which the seasonality repeats. For monthly data with an annual pattern (e.g., ice cream sales), the period `s = 12`. For quarterly data, `s = 4`. For daily data with a weekly pattern (e.g., website traffic), `s = 7`.

### b) The Multiplicative and Additive Models

To analyze a seasonal series, we break it down into its constituent components. The two primary models are:

1.  **Additive Model:**
    `Y(t) = T(t) + S(t) + C(t) + R(t)`
    *   **Y(t):** Observed value at time `t`
    *   **T(t):** Trend component (long-term direction)
    *   **S(t):** Seasonal component (repeating pattern)
    *   **C(t):** Cyclical component (long-term, non-fixed cycles)
    *   **R(t):** Random/Irregular component (noise)

    **Use Case:** The additive model is appropriate when the magnitude of the seasonal fluctuations **does not change** with the level of the series. The seasonal effect is roughly constant over time.
    *Example: The number of toys sold might always increase by ~50,000 units in December, regardless of the overall annual sales trend.*

2.  **Multiplicative Model:**
    `Y(t) = T(t) * S(t) * C(t) * R(t)`
    *   **Use Case:** The multiplicative model is used when the seasonal variation **increases or decreases** with the level of the trend. The seasonal effect is proportional to the trend.
    *Example: Sales of a growing company might increase by 20% every quarter. The 20% is a multiplier, so the absolute increase gets larger as the company's sales grow.*

### c) Seasonal Differencing

A powerful technique to remove seasonal non-stationarity from a series is **seasonal differencing**. While first differencing (`y'(t) = Y(t) - Y(t-1)`) removes a linear trend, seasonal differencing removes a seasonal trend.

*   **Formula:** The seasonal difference with period `s` is calculated as:
    `∇sY(t) = Y(t) - Y(t-s)`

*   **Example:** For monthly data (`s=12`), the seasonal difference would be:
    `Y(Jan 2023) - Y(Jan 2022)`
    `Y(Feb 2023) - Y(Feb 2022)`, and so on.
    This compares values in the same season across different years, effectively removing the seasonal pattern and stabilizing the mean of the series.

### d) The Seasonal ARIMA (SARIMA) Model

The ARIMA model (AutoRegressive Integrated Moving Average) can be extended to explicitly incorporate seasonality. This extended model is called **SARIMA**, denoted as **ARIMA(p, d, q)(P, D, Q)s**.

*   **Non-Seasonal Part (p, d, q):** Same as standard ARIMA.
    *   `p`: Order of the AutoRegressive (AR) term.
    *   `d`: Degree of non-seasonal differencing.
    *   `q`: Order of the Moving Average (MA) term.

*   **Seasonal Part (P, D, Q)s:** The new, seasonal parameters.
    *   `P`: Order of the **seasonal** AutoRegressive (SAR) term.
    *   `D`: Degree of **seasonal differencing** (usually 1).
    *   `Q`: Order of the **seasonal** Moving Average (SMA) term.
    *   `s`: The number of periods per season (e.g., 12 for monthly data).

**Interpretation Example:** An `ARIMA(1,1,1)(0,1,1)12` model for monthly data implies:
*   `(1,1,1)`: A non-seasonal AR(1) term, one non-seasonal difference, and a non-seasonal MA(1) term.
*   `(0,1,1)12`: **No** seasonal autoregressive term, **one** seasonal difference (`s=12`), and a seasonal MA(1) term.

## 3. Example: Analyzing Monthly Electricity Demand

Imagine a time series of monthly electricity consumption for a city.

1.  **Visualization:** Plotting the data would likely show a strong annual pattern (`s=12`) with peaks every summer and winter.
2.  **Model Identification:** The seasonal pattern appears to grow over time as the city expands, suggesting a **multiplicative** model might be appropriate.
3.  **Differencing:** To make the series stationary, we might need both a first difference (`d=1`) to remove the overall trend and a seasonal difference (`D=1`, `s=12`) to remove the seasonal trend.
4.  **Model Fitting:** After examining the ACF and PACF plots, we might identify a `SARIMA(0,1,1)(0,1,1)12` model. This model would use a non-seasonal MA term, a seasonal MA term, and one of each type of differencing to effectively capture and forecast the seasonal pattern.

## 4. Key Points & Summary

*   **Seasonality** is a fixed-period, repeating pattern in a time series (e.g., monthly, quarterly).
*   The two primary decomposition models are **Additive** (constant seasonal swings) and **Multiplicative** (swings proportional to the trend).
*   **Seasonal Differencing** (`Y(t) - Y(t-s)`) is a crucial technique for removing seasonal patterns and achieving stationarity.
*   The **SARIMA model** `ARIMA(p,d,q)(P,D,Q)s` is the standard tool for modeling and forecasting seasonal time series, combining both non-seasonal and seasonal components.
*   The analysis process always starts with **visualization** to identify the seasonality period (`s`) and its nature (additive/multiplicative), followed by differencing and model identification using ACF/PACF plots.