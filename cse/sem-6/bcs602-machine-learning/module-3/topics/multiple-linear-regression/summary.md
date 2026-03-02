# Multiple Linear Regression

## Overview

Multiple linear regression extends simple linear regression to model the relationship between multiple independent variables and a continuous dependent variable. It enables prediction using multiple features simultaneously, capturing more complex relationships than single-variable models.

## Key Points

- **Model Form**: y = w₀ + w₁x₁ + w₂x₂ + ... + wₙxₙ + ε; where n is number of features, ε is error term
- **Matrix Notation**: Y = Xw + ε; where X is feature matrix (n×p), w is weight vector (p×1), Y is target vector (n×1)
- **Parameter Estimation**: Normal equation w = (X^TX)⁻¹X^Ty or gradient descent for large datasets
- **Multicollinearity Problem**: High correlation between features causes unstable/unreliable coefficients; detected using VIF (Variance Inflation Factor)
- **Feature Selection**: Forward selection, backward elimination, stepwise regression to identify most important features
- **Regularization**: Ridge (L2), Lasso (L1), ElasticNet (L1+L2) prevent overfitting by penalizing large coefficients

## Important Concepts

- Adjusted R²: Penalizes addition of irrelevant features; better than R² for comparing models with different feature counts
- Partial regression coefficients: effect of one feature while holding others constant
- VIF > 10 indicates problematic multicollinearity requiring feature removal or transformation
- Standardization: scaling features to same range improves gradient descent convergence and coefficient interpretation

## Notes

- Matrix notation Y = Xw essential for understanding implementation
- Know normal equation w = (X^TX)⁻¹X^Ty and when it fails (X^TX singular)
- Multicollinearity detection (VIF) and remedies (remove features, PCA) are common exam questions
- Understand feature selection methods: forward, backward, stepwise
- Regularization types: Ridge (L2, keeps all features), Lasso (L1, sparse solution), ElasticNet (both)
