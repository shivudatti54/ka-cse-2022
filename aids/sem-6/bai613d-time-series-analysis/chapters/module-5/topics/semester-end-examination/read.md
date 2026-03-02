# Module 5: Semester-End Examination Guide - Time Series Analysis

## Introduction

As you prepare for your semester-end examination in Time Series Analysis, this guide consolidates the core concepts typically covered under Module 5. This module often deals with advanced forecasting methods, model evaluation, and the application of time series models to real-world engineering problems. A firm grasp of these concepts is crucial for both your exam and practical applications in fields like signal processing, economic forecasting, and quality control.

## Core Concepts for Examination

### 1. Advanced Forecasting Techniques

Beyond the basic ARIMA models, you should be familiar with more sophisticated techniques.

*   **SARIMA (Seasonal ARIMA):** Used when data exhibits strong seasonal patterns. It is denoted as ARIMA(p,d,q)(P,D,Q)_s, where:
    *   `(P, D, Q)` are the seasonal AR, differencing, and MA terms.
    *   `s` is the number of time periods until the pattern repeats (e.g., `s=12` for monthly data with yearly seasonality).
    *   **Example:** Forecasting electricity demand, which has daily and yearly cycles.

*   **ARCH/GARCH Models (Autoregressive Conditional Heteroskedasticity):** These models are vital for forecasting volatility, not the mean value. They are extensively used in financial engineering and signal processing.
    *   **ARCH:** Models variance as a function of past error terms.
    *   **GARCH:** A generalized version that also includes past variances, making it more parsimonious and powerful. A GARCH(1,1) model is often sufficient: `σ²_t = ω + αε²_{t-1} + βσ²_{t-1}`

### 2. Model Evaluation and Selection

Choosing the best model among several candidates is a key exam question.

*   **AIC (Akaike Information Criterion) and BIC (Bayesian Information Criterion):** These are metrics used to compare models. You should **prefer the model with the lowest AIC or BIC value**. BIC imposes a stronger penalty for model complexity than AIC.
*   **Forecast Error Metrics:** Used to quantify a model's prediction accuracy on a test set.
    *   **Mean Absolute Error (MAE):** `MAE = (1/n) * Σ |Actual - Forecast|`
    *   **Root Mean Squared Error (RMSE):** `RMSE = √( (1/n) * Σ(Actual - Forecast)² )` - More sensitive to large errors.
    *   **Mean Absolute Percentage Error (MAPE):** `MAPE = (1/n) * Σ |(Actual - Forecast)/Actual| * 100%` - Useful for relative error interpretation.

### 3. Box-Jenkins Methodology (Recap and Application)

You will likely be asked to outline the steps of the Box-Jenkins approach for building an ARIMA model.
1.  **Identification:** Stationarize the series (via differencing, `d`). Identify potential `p` and `q` orders using ACF and PACF plots.
2.  **Estimation:** Estimate the parameters (φ, θ) of the chosen ARIMA(p,d,q) model using methods like Maximum Likelihood Estimation (MLE).
3.  **Diagnostic Checking:** Check if the residuals of the estimated model resemble white noise.
    *   **Ljung-Box Test:** A statistical test (Q-test) where a *p-value > 0.05* suggests the residuals are uncorrelated (good model fit).
4.  **Forecasting:** Use the fitted model to generate forecasts.

### 4. Application to Engineering Problems

Be prepared to discuss or apply time series analysis in an engineering context.
*   **Signal Processing:** Filtering noise from signals, trend removal.
*   **Structural Health Monitoring:** Analyzing vibration data from bridges or buildings to detect anomalies or predict maintenance needs.
*   **Network Traffic Forecasting:** Predicting data loads on servers or communication networks.

## Example Exam Question

**Q: A time series of vibration data from a machine is provided. Describe the steps you would take to model this data and build a forecasting system for predictive maintenance.**

**A:**
1.  **Visualization & Stationarity:** Plot the data to identify trends or seasonality. Apply differencing until the mean is stable (find `d`).
2.  **Model Identification:** Plot the ACF and PACF of the stationary data. The decay pattern will suggest candidate AR (`p`) or MA (`q`) terms. For seasonal patterns, consider a SARIMA model.
3.  **Parameter Estimation:** Fit the candidate models (e.g., ARIMA(1,1,1), ARIMA(2,1,0)) using software.
4.  **Diagnostics:** Select the model with the lowest AIC/BIC. Perform the Ljung-Box test on its residuals to ensure no pattern is left.
5.  **Forecasting & Application:** Use the validated model to forecast future vibration levels. Set a threshold; if the forecasted value (or the prediction interval) exceeds this threshold, it triggers a maintenance alert.

## Key Points & Summary

*   **SARIMA** extends ARIMA to handle **seasonal patterns**.
*   **GARCH** models are used for forecasting **volatility** (variance), common in financial and signal data.
*   Use **AIC/BIC** to select the best model; the **lowest value** is best.
*   Evaluate forecast accuracy with **MAE, RMSE, and MAPE**.
*   The **Ljung-Box test** checks if model residuals are white noise (a good fit).
*   The **Box-Jenkins Methodology** is a systematic four-step approach (Identify, Estimate, Diagnose, Forecast) for building ARIMA models.
*   Time series analysis has direct applications in crucial engineering domains like predictive maintenance and signal processing.

Focus on understanding these concepts conceptually and be ready to apply them to hypothetical datasets or describe the procedures in detail. Good luck with your examination