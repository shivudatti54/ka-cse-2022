# Multiple Linear Regression - Summary

## Key Definitions and Concepts

- **Multiple Linear Regression (MLR)**: An extension of simple linear regression that models the relationship between one dependent variable and two or more independent variables.

- **Regression Coefficients (β)**: Parameters that represent the expected change in the dependent variable for a one-unit increase in an independent variable, holding all other variables constant.

- **Ordinary Least Squares (OLS)**: A method that estimates regression coefficients by minimizing the sum of squared residuals (differences between observed and predicted values).

- **Multicollinearity**: A condition where independent variables are highly correlated with each other, causing unstable coefficient estimates and unreliable significance tests.

## Important Formulas and Theorems

- **MLR Model**: Y = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ + ε

- **OLS Estimation (Matrix Form)**: β = (X'X)⁻¹X'Y

- **Coefficient of Determination**: R² = 1 - (SSE/SST)

- **Adjusted R²**: R² adjusted = 1 - [(1-R²)(n-1)/(n-k-1)]

- **Variance Inflation Factor (VIF)**: VIFⱼ = 1/(1-R²ⱼ), where VIF > 10 indicates serious multicollinearity

- **F-statistic**: F = (SSR/k) / (SSE/(n-k-1))

## Key Points

1. Multiple linear regression extends simple linear regression by including multiple predictor variables to explain variation in a single response variable.

2. The five assumptions—linearity, independence, homoscedasticity, normality, and no multicollinearity—must be satisfied for valid inference.

3. Each coefficient represents the effect of one variable while controlling for all other variables in the model.

4. R² always increases with additional predictors; Adjusted R² accounts for the number of predictors and can decrease with irrelevant variables.

5. Multicollinearity is detected through VIF (>10 indicates problem) and correlation matrices; remedies include removing variables or using regularization.

6. The overall F-test evaluates whether the model provides significant explanatory power; individual t-tests evaluate each coefficient's significance.

7. Point predictions give expected values; confidence intervals estimate mean response, while prediction intervals estimate individual observations.

## Common Mistakes to Avoid

1. **Ignoring multicollinearity**: Failing to check for correlated predictors leads to unreliable coefficient estimates and incorrect conclusions.

2. **Incorrect coefficient interpretation**: Never interpret a coefficient without specifying "holding other variables constant"—this is a common exam error.

3. **Using R² alone for model comparison**: Always use Adjusted R² when comparing models with different numbers of predictors.

4. **Assuming correlation implies causation**: Significant regression coefficients indicate association, not necessarily causal relationships.

5. **Ignoring assumption violations**: Applying MLR without checking linearity, homoscedasticity, or normality can lead to invalid results.

## Revision Tips

1. Practice writing the regression equation from raw data and interpreting each coefficient in context.

2. Memorize the five assumptions and be ready to explain how you would test each one.

3. Work through numerical examples calculating predicted values, residuals, and fit statistics.

4. Review the difference between confidence and prediction intervals—know when each is appropriate.

5. Solve previous year DU examination questions on multiple linear regression to understand the exam pattern and important topics.