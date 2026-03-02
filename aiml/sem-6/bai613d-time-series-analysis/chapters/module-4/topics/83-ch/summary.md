# **8.3 Ch: Diagnostic Checking**

### Key Points

- **Checking the Stochastic Model**
  - Purpose: Verify if the model is correctly specified
  - Methods: Plotting methods (e.g., Q-Q plots, residual plots)
  - Important concepts:
    - Normality of residuals
    - Homoscedasticity
    - Linearity
- **Overfitting**
  - Definition: Model is too complex and fits noise rather than underlying patterns
  - Types:
    - Overfitting in time series
    - Overfitting in models with lagged variables
  - Methods to detect:
    - Cross-validation
    - Walk-forward optimization
  - Important concepts:
    - Model bias
    - Model variance
- **Diagnostic Plots**
  - Types:
    - Q-Q plots (Quantile-Quantile plots)
    - Residual plots
    - Autocorrelation plots
  - Important concepts:
    - Normality of residuals
    - Homoscedasticity
    - Autocorrelation

### Important Formulas and Definitions

- **Probability Plot Residuals (PPR)**
  - PPR = |e_t| \* Φ(-|e_t|)
  - where e_t is the residual at time t
- **Normality Test**
  - Two-sample t-test for normality of residuals
- **Autocorrelation Function (ACF)**
  - ACF = ρ(Δt) = cov(e*t, e*{t+Δt})
  - where Δt is the lag

### Important Theorems

- **Linearity Theorem**
  - If the model is correctly specified, then the residuals should be uncorrelated with the independent variables.
- **Homoscedasticity Theorem**
  - If the model is correctly specified, then the variance of the residuals should be constant across all levels of the independent variables.

### Quick Revision Tips

- Check the residuals for normality and homoscedasticity
- Use diagnostic plots to detect overfitting
- Use cross-validation and walk-forward optimization to evaluate model performance
- Verify model bias and variance
