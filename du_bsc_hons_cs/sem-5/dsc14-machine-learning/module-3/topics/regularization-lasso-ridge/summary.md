# Regularization: Lasso and Ridge - Summary

## Key Definitions and Concepts

- **Regularization**: A technique to prevent overfitting by adding a penalty term to the loss function, constraining model complexity
- **Ridge Regression (L2)**: Adds penalty λΣβⱼ² to the loss function; shrinks coefficients toward zero but never makes them exactly zero
- **Lasso Regression (L1)**: Adds penalty λΣ|βⱼ| to the loss function; can set coefficients exactly to zero, performing feature selection
- **λ (Lambda)**: Regularization parameter controlling the strength of the penalty; larger λ = more regularization = simpler model

## Important Formulas and Theorems

- **Ridge Objective**: Minimize [RSS + λΣβⱼ²]
- **Lasso Objective**: Minimize [RSS + λΣ|βⱼ|]
- **Elastic Net**: Minimize [RSS + λ₁Σ|βⱼ| + λ₂Σβⱼ²]
- **Bias-Variance Tradeoff**: Total Error = Bias² + Variance + Irreducible Error
- **Feature Scaling**: x_standardized = (x - μ) / σ (required before regularization)

## Key Points

- Both methods add bias to reduce variance, improving generalization to unseen data
- Ridge excels when all features may be relevant; Lasso excels when sparse solutions are desired
- Always standardize features before applying regularization
- Use cross-validation to select optimal λ value
- Lasso creates "sparse" models (some coefficients = 0); Ridge keeps all features
- Ridge handles multicollinearity by stabilizing coefficient estimates
- Elastic Net combines strengths of both when features are correlated

## Common Mistakes to Avoid

1. **Forgetting to standardize features** — leads to unfair penalization of coefficients
2. **Choosing λ too large** — results in underfitting (all coefficients near zero)
3. **Choosing λ too small** — results in minimal regularization, overfitting persists
4. **Using Lasso with correlated features** — may arbitrarily eliminate one of correlated pair; use Elastic Net instead

## Revision Tips

1. **Quick comparison**: L2 = "shrink towards zero" (retain all); L1 = "set to zero" (select features)
2. **Remember geometric intuition**: Ridge = circles; Lasso = diamonds (with corners at axes)
3. **Practice**: Implement both methods on a small dataset and observe coefficient paths as λ varies
4. **Key insight**: The trade-off is between model complexity (fewer features, smaller coefficients) and training error