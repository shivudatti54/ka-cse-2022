# Introduction to Linear Regression

## Overview

Linear regression is a fundamental supervised learning algorithm that models the relationship between input features and continuous output as a straight line. It assumes a linear relationship and finds the best-fit line that minimizes prediction error using least squares method.

## Key Points

- **Model Equation**: y = mx + b (simple) or y = w₀ + w₁x₁ + w₂x₂ + ... + wₙxₙ (multiple); where w = weights, b = bias/intercept
- **Objective**: Minimize loss function (typically MSE) by finding optimal weights using gradient descent or normal equation
- **Normal Equation**: w = (X^TX)⁻¹X^Ty; provides closed-form solution for optimal weights
- **Gradient Descent**: Iterative optimization: w = w - α\*∇L(w); learning rate α controls step size
- **Assumptions**: Linearity (linear relationship), independence (observations independent), homoscedasticity (constant variance), normality (residuals normally distributed)
- **Evaluation**: R² (0 to 1, higher better), MSE/RMSE (lower better), residual analysis (check patterns)

## Important Concepts

- Ordinary Least Squares (OLS): minimize sum of squared residuals Σ(yi - ŷi)²
- Coefficient interpretation: for unit increase in feature, target changes by coefficient amount
- Multicollinearity: high correlation between features causes unstable coefficients
- Residuals: difference between actual and predicted values; should be randomly distributed

## Notes

- Memorize model equation y = w₀ + w₁x₁ + ... + wₙxₙ and normal equation w = (X^TX)⁻¹X^Ty
- Explain gradient descent update rule with learning rate effect
- Know assumptions: linearity, independence, homoscedasticity, normality
- Practice interpreting coefficients and R² values
- Understand difference between simple (one feature) and multiple (many features) linear regression
