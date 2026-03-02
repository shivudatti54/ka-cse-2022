# Regression Analysis

## Overview

Regression analysis is a statistical method for examining relationships between variables. It identifies the strength and nature of relationships between dependent and independent variables, provides predictive models, and enables inference about the underlying data-generating process.

## Key Points

- **Purpose**: Model relationships, make predictions, test hypotheses, identify important predictors, quantify variable effects
- **Types**: Simple (one predictor), Multiple (many predictors), Linear (straight line), Non-linear (curves), Polynomial (higher powers)
- **Assumptions**: Linearity, independence, homoscedasticity (constant variance), normality of residuals, no multicollinearity
- **Residual Analysis**: Residuals should be randomly distributed, centered at zero, constant variance; patterns indicate model problems
- **Goodness of Fit**: R² (proportion variance explained), Adjusted R² (penalizes extra predictors), AIC/BIC (model comparison)
- **Hypothesis Testing**: Test if coefficients significantly different from zero; p-values < 0.05 typically considered significant

## Important Concepts

- Residuals = actual - predicted; check via residual plots (should show random scatter)
- R² = 1 - (SS_residual/SS_total); ranges 0 to 1; higher indicates better fit but can be misleading with many predictors
- Standard error of coefficients measures uncertainty; used to construct confidence intervals
- F-statistic tests overall model significance (all coefficients = 0)

## Notes

- Know all regression assumptions and how to test them
- Residual analysis is crucial - explain residual plots and what patterns indicate
- Understand R² interpretation and limitations; Adjusted R² better for model comparison
- Be able to interpret regression output: coefficients, p-values, R², F-statistic
