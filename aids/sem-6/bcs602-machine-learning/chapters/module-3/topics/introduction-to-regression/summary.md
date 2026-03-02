# Introduction to Regression - Summary

## Key Definitions and Concepts

Regression is a supervised learning technique used to predict continuous numerical values by establishing mathematical relationships between dependent and dependent variables. The dependent variable (Y) is what we want to predict, while independent variables (X) are the predictors used for prediction.

## Important Formulas and Theorems

Simple Linear Regression: Y = β₀ + β₁X + ε, where β₀ is the y-intercept, β₁ is the slope, and ε is the error term.

Slope Coefficient: β₁ = Σ(xᵢ - x̄)(yᵢ - ȳ) / Σ(xᵢ - x̄)²

Intercept Coefficient: β₀ = ȳ - β₁x̄

Coefficient of Determination: R² = Explained Variation / Total Variation

## Key Points

- Regression predicts continuous values while classification predicts discrete categories
- The line of best fit minimizes the sum of squared residuals using Ordinary Least Squares
- Simple linear regression uses one predictor; multiple linear regression uses multiple predictors
- R² ranges from 0 to 1, indicating how much variance is explained by the model
- Polynomial regression handles non-linear relationships by including higher-order terms
- Residual analysis helps identify model inadequacies and assumption violations

## Common Mistakes to Avoid

Confusing correlation with causation is a critical error. A strong regression relationship does not prove that X causes Y. Interpreting R² as the probability of model correctness is wrong; it only measures variance explained. Overlooking assumption violations can lead to invalid conclusions even with high R² values. Using the regression model for extrapolation beyond the range of training data is risky and often produces unreliable predictions.

## Revision Tips

Practice calculating regression coefficients from raw data multiple times until the process becomes automatic. Draw and label diagrams showing the regression line, residuals, and the concept of best fit. Create a comparison table distinguishing simple, multiple, and polynomial regression. Solve at least three numerical problems from previous year question papers to understand the exam pattern and common question types.