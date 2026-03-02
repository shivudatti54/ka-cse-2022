# Use of Residuals to Modify the Model in Time Series Analysis

## Introduction

In time series analysis, building a model is rarely a one-step process. A model is first identified and its parameters estimated based on the available data. However, a crucial step in ensuring the model's adequacy and reliability is the **diagnostic checking** phase. This is where the analysis of **residuals** becomes paramount. Residuals are the differences between the observed values and the values predicted by the fitted model. They hold the key to understanding what the model has failed to capture. This module focuses on how these residuals are used to detect inadequacies and guide modifications to improve the model.

## Core Concepts

### 1. What are Residuals?

In the context of an ARIMA(p,d,q) model, where the time series $Z_t$ has been differenced to achieve stationarity, creating $W_t = \nabla^d Z_t$, the residuals ($a_t$) are defined as:
$$
a_t = W_t - \hat{W}_t
$$
where $\hat{W}_t$ is the one-step-ahead forecast from the model. Essentially, if our model is perfect, the residuals should be nothing but **white noise**—a sequence of uncorrelated random shocks with a mean of zero and constant variance.

### 2. The Principle of Diagnostic Checking

The fundamental idea is simple: **If the model is adequate, the residuals should behave like white noise.** Therefore, any systematic pattern or structure left in the residuals indicates that the model has not fully captured the underlying process. The goal of diagnostic checking is to test the null hypothesis that the residuals are white noise.

### 3. How to Analyze Residuals?

We use two primary tools to analyze residuals:

*   **Autocorrelation Function (ACF) Plot of Residuals:** We calculate the sample autocorrelations of the residuals ($r_k(a)$) for various lags $k$. For a white noise series, we expect all autocorrelations to be close to zero. Formally, we check if the correlations fall within the approximate confidence bounds of $\pm 2/\sqrt{N}$ (where $N$ is the number of observations). Any significant spike outside these bounds (e.g., at lag 2 or 5) suggests a pattern that the model missed.

*   **Ljung-Box Test (Q-Statistic):** This is a portmanteau test that collectively tests whether the first $m$ autocorrelations of the residuals are significantly different from zero. The test statistic is:
    $$
    Q = N(N+2) \sum_{k=1}^{m} \frac{r_k^2(a)}{N-k}
    $$
    Under the null hypothesis of model adequacy, $Q$ follows a $\chi^2$ distribution with $(m - p - q)$ degrees of freedom. A high $Q$ value (low p-value, typically < 0.05) leads us to reject the null hypothesis, concluding that the residuals are not white noise and the model is inadequate.

### 4. Using Findings to Modify the Model

The patterns in the residual ACF provide direct clues on how to modify the model:

*   **Example 1: Missed AR Component**
    *   **Symptom:** The residual ACF shows significant spikes that **tail off** (perhaps a slow decay).
    *   **Diagnosis:** This suggests a systematic autoregressive component remains in the data that the model did not account for.
    *   **Modification:** Increase the order of the AR part (`p`). For instance, if you fitted an ARIMA(1,1,0) model and the residuals have a significant spike at lag 2, try an ARIMA(2,1,0) model.

*   **Example 2: Missed MA Component**
    *   **Symptom:** The residual ACF shows a **significant spike at a specific lag** (e.g., at lag 3) and cuts off thereafter.
    *   **Diagnosis:** This suggests a moving average component remains.
    *   **Modification:** Increase the order of the MA part (`q`). If the spike is at lag 3, adding an MA(3) term might be necessary. For example, upgrade from ARIMA(0,1,1) to ARIMA(0,1,2).

*   **Example 3: Heteroscedasticity (Non-Constant Variance)**
    *   **Symptom:** The variance of the residuals is not constant over time. A plot of residuals vs. time might show the spread increasing or decreasing.
    *   **Diagnosis:** The assumption of constant variance is violated.
    *   **Modification:** Apply a variance-stabilizing transformation (like a logarithmic transformation) to the original data before building the ARIMA model.

This process is iterative. After modifying the model, you must re-estimate its parameters and again analyze the *new* residuals from the modified model to check for further improvements.

## Key Points / Summary

*   **Residuals** are the differences between observed and model-predicted values.
*   The primary goal of **diagnostic checking** is to verify that the residuals are **white noise** (uncorrelated with zero mean and constant variance).
*   The main tools for analysis are the **Residual ACF Plot** and the **Ljung-Box test**.
*   **Significant spikes in the residual ACF** indicate that the model has not captured all the available information and needs modification.
*   The pattern of these spikes (e.g., cutting off or tailing off) provides a direct guide on whether to **increase the AR (`p`) or MA (`q`) order** in the model.
*   **Non-constant variance** in residuals suggests a need for transforming the original time series data.
*   Model building is an **iterative process** (Identify -> Estimate -> Diagnose -> Modify) that relies heavily on the analysis of residuals to achieve an optimal and adequate model.