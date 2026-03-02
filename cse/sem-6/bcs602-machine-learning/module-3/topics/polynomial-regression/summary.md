# Polynomial Regression

## Overview

Polynomial regression extends linear regression by modeling non-linear relationships using polynomial functions. By transforming features to higher-degree terms (x², x³, etc.), it captures curved relationships while still using linear regression techniques for parameter estimation.

## Key Points

- **Model Form**: y = w₀ + w₁x + w₂x² + w₃x³ + ... + wₙxⁿ; where n is polynomial degree
- **Feature Transformation**: Create new features from existing ones: x → [x, x², x³, ...]; still linear in parameters despite non-linear in features
- **Degree Selection**: Low degree → underfitting (too simple); High degree → overfitting (too complex); optimal degree balances bias-variance
- **Overfitting Risk**: High-degree polynomials fit training noise; use cross-validation to select degree; regularization helps control overfitting
- **Implementation**: Transform features then apply standard linear regression: X_poly = [x, x², x³, ...], then Y = X_poly \* w
- **Applications**: Modeling growth curves, trajectory prediction, physical phenomena with non-linear relationships

## Important Concepts

- Still considered "linear regression" because model is linear in parameters (weights), not features
- Regularization (Ridge/Lasso) crucial for high-degree polynomials to prevent overfitting
- Cross-validation used to select optimal polynomial degree
- Feature scaling important: higher powers amplify magnitude differences between features

## Notes

- Understand it's linear in parameters despite polynomial features: y = w₀ + w₁x + w₂x² is linear in w
- Degree selection via cross-validation - plot validation error vs degree to find optimal
- High-degree polynomials prone to overfitting especially at boundaries - explain with diagram
- Know when to use polynomial vs linear: polynomial for curved relationships, linear for straight-line
