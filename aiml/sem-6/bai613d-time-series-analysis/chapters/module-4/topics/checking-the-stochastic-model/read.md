# TIME SERIES ANALYSIS: Checking the Stochastic Model

## Introduction

In time series analysis, a stochastic model is a statistical model that represents a process as a collection of random variables. Checking the adequacy of a fitted stochastic model is crucial to ensure it accurately captures the underlying structure of the data. This process involves verifying that the model's residuals behave like white noise, meaning they are uncorrelated and normally distributed with zero mean and constant variance.

## Core Concepts

### 1. Residual Analysis
After fitting a model (like AR, MA, or ARIMA), we obtain residuals. These residuals should exhibit properties of white noise if the model is adequate.

**Key properties to check:**
- **Zero mean:** The average of residuals should be close to zero.
- **Constant variance (Homoscedasticity):** The spread of residuals should be consistent across all time points.
- **No autocorrelation:** Residuals should not be correlated with each other at any lag.

### 2. Graphical Methods
- **Residual Plot:** Plot residuals against time. Look for patterns (trends, cycles) which indicate model inadequacy.
- **ACF of Residuals:** Plot the autocorrelation function (ACF) of residuals. For a good model, all autocorrelations should be within the confidence bounds (approximately 95% within ±2/√N).
- **Q-Q Plot:** Check if residuals follow a normal distribution. Points should lie close to the straight line.

### 3. Statistical Tests
- **Ljung-Box Test:** A formal test for autocorrelation in residuals.
  - Null Hypothesis (H₀): Residuals are uncorrelated (white noise).
  - If p-value > 0.05, we fail to reject H₀, indicating no significant autocorrelation.
- **Jarque-Bera Test:** Tests for normality of residuals.
  - Null Hypothesis (H₀): Residuals are normally distributed.
- **Engle's ARCH Test:** Checks for heteroscedasticity (non-constant variance).

## Example

Suppose we fit an AR(1) model to a time series. The model is:
$$X_t = \phi X_{t-1} + \epsilon_t$$

After estimation, we get residuals $\hat{\epsilon}_t$. We then:
1. Plot residuals: If random scatter around zero, good.
2. Plot ACF of residuals: If no significant spikes, good.
3. Perform Ljung-Box test: If p-value > 0.05 for several lags, good.
4. Check normality: If Q-Q plot is linear and Jarque-Bera test p-value > 0.05, residuals are normal.

## Summary

- **Adequate model** residuals should be white noise: uncorrelated, normal, zero mean, constant variance.
- Use **graphical methods** (residual plot, ACF, Q-Q plot) for visual inspection.
- Use **statistical tests** (Ljung-Box, Jarque-Bera, ARCH) for objective evaluation.
- If residuals show patterns, the model may need improvement (e.g., higher order, different structure).

Proper model checking ensures reliable forecasts and inferences. Always validate your model before using it for prediction.