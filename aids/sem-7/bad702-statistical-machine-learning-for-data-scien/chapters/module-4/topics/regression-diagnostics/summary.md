# Regression Diagnostics

### Key Points

- **Definition:** Regression diagnostics are used to evaluate the assumptions of linear regression and diagnose potential issues with the model.
- **Key Assumptions:**
  - Linearity
  - Independence
  - Homoscedasticity
  - Normality
  - No multicollinearity
- **Common Issues:**
  - Outliers
  - Non-normality
  - Heteroscedasticity
  - Multicollinearity
- **Techniques:**
  - Plotting (residual plot, Q-Q plot)
  - Tests (normality, heteroscedasticity)
  - Transformations (log, square root)
  - Feature selection

### Important Formulas

- **Normality Test:**
  - Shapiro-Wilk test: W = (n/∑(xi - x̄)^2)^{(n-1)/n} \* √(n/σ^2)
- **Heteroscedasticity Test:**
  - Breusch-Pagan test: F(1, n-k-1) = F\_{α, n-k-1} (where k is the number of predictors)
- **Multicollinearity Test:**
  - Variance Inflation Factor (VIF): VIF = 1 / (1 - R^2)

### Important Definitions

- **Residual Plot:** a plot of the residuals against the fitted values
- **Q-Q Plot:** a plot of the residuals against the quantiles of the standard normal distribution
- **Homoscedasticity:** the assumption that the variance of the residuals is constant across all levels of the independent variable

### Important Theorems

- **Central Limit Theorem:** the distribution of the sample mean converges to the population mean as the sample size increases.
- **Law of Large Numbers:** the average of the sample is close to the population mean as the sample size increases.

### Quick Revision Tips

- Plot residual plots and Q-Q plots to diagnose issues
- Use normality and heteroscedasticity tests to evaluate assumptions
- Apply transformations and feature selection to address issues
- Remember the key assumptions and common issues in regression diagnostics
