# **8.3 Ch: Checking the Stochastic Model**

### Key Points

- **Definition**: Checking the stochastic model is a crucial step in time series analysis to ensure that the model is properly specified and to detect potential issues.
- **Objectives**:
  - Verify that the model is correctly specified
  - Detect overfitting and underfitting
  - Evaluate the model's assumptions
- **Diagnostic Checks**:
  - Autocorrelation Function (ACF)
  - Partial Autocorrelation Function (PACF)
  - Quasi-Maximum Likelihood Estimation (QMLE)
  - Bayesian Information Criterion (BIC)
  - Akaike Information Criterion (AIC)

### Important Formulas and Definitions

- **Autocorrelation Function (ACF)**: measures the correlation between a time series and a lagged version of itself
- **Partial Autocorrelation Function (PACF)**: measures the correlation between a time series and a lagged version of itself, while controlling for other lags
- **Quasi-Maximum Likelihood Estimation (QMLE)**: a method for estimating model parameters
- **Bayesian Information Criterion (BIC)**: a measure of model fit, which balances model complexity and data fit
- **Akaike Information Criterion (AIC)**: a measure of model fit, which balances model complexity and data fit

### Important Theorems

- **Breusch-Godfrey Test**: tests for autocorrelation in residuals
- **Hausman Test**: tests for endogeneity in the error term

### Revision Notes

- Use diagnostic checks to verify model specification
- Avoid overfitting by selecting a parsimonious model
- Use BIC or AIC to evaluate model fit
- Test for autocorrelation and endogeneity in residuals
- Report results in a clear and concise manner
