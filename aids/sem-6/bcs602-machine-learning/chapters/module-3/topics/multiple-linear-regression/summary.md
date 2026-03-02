# Multiple Linear Regression - Summary

## Key Definitions and Concepts

- MULTIPLE LINEAR REGRESSION: A statistical method that models the relationship between two or more predictor variables and a continuous response variable
- REGRESSION COEFFICIENT (βᵢ): The change in the dependent variable for a one-unit change in predictor Xᵢ, holding all other variables constant
- ORDINARY LEAST SQUARES (OLS): The estimation method that minimizes the sum of squared residuals
- RESIDUAL (ε): The difference between observed and predicted values
- MULTICOLLINEARITY: High correlation among predictor variables that inflates coefficient variance estimates

## Important Formulas and Theorems

- Model: Y = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ + ε
- OLS Solution: β = (X'X)⁻¹X'Y
- R² = 1 - (SS_res / SS_tot)
- Adjusted R² = 1 - [(1 - R²)(n - 1) / (n - k - 1)]
- VIFᵢ = 1 / (1 - R²ᵢ)
- t-statistic: t = βᵢ / SE(βᵢ)

## Key Points

1. Multiple linear regression extends simple linear regression by including multiple predictor variables
2. Five assumptions must be satisfied: linearity, independence, homoscedasticity, normality, and no multicollinearity
3. OLS estimation provides the best linear unbiased estimates (BLUE) under classical assumptions
4. Adjusted R² penalizes for adding insignificant predictors, unlike regular R²
5. VIF values greater than 5 or 10 indicate problematic multicollinearity
6. Coefficient interpretation requires the ceteris paribus condition
7. Both individual t-tests and overall F-test are used for hypothesis testing
8. The model assumes linear relationships; non-linear patterns require transformations or polynomial regression

## Common Mistakes to Avoid

1. Interpreting coefficients without mentioning "holding other variables constant"
2. Using R² alone to compare models with different numbers of predictors
3. Ignoring multicollinearity when interpreting individual coefficient significance
4. Assuming correlation implies causation in regression relationships
5. Overlooking assumption violations that invalidate statistical inference

## Revision Tips

1. Practice deriving the OLS solution using matrix operations
2. Work through at least three numerical examples to understand coefficient interpretation
3. Create a checklist of all five assumptions and how to test each
4. Memorize the threshold values for VIF and understand implications
5. Review hypothesis testing procedures and distinguish between t-tests and F-tests
6. Connect this topic to related regression techniques covered in the module