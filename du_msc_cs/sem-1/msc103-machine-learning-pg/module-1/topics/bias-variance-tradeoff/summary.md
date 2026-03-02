# Bias-Variance Tradeoff - Summary

## Key Definitions and Concepts
- **Bias**: Error from erroneous model assumptions
- **Variance**: Error from model's sensitivity to training data
- **Irreducible Error**: Data noise (σ²) that cannot be modeled
- **Model Capacity**: Range of functions a model can represent

## Important Formulas and Theorems
- Bias-Variance Decomposition:
  ```math
  E[(y - ŷ)^2] = (E[ŷ] - f(x))² + E[(ŷ - E[ŷ])²] + σ²
  ```
- VC Dimension: Measure of model complexity
- Structural Risk Minimization: Formal framework for tradeoff management

## Key Points
- Underfitting ↔ High Bias ↔ Low Variance
- Overfitting ↔ Low Bias ↔ High Variance
- Regularization explicitly controls model complexity
- Optimal model minimizes total error (bias² + variance + σ²)
- Ensemble methods manipulate tradeoff through aggregation
- Double descent shows error can decrease past interpolation point
- Learning curves visualize tradeoff across sample sizes

## Common Mistakes to Avoid
1. Confusing high variance with high bias in error analysis
2. Ignoring dataset size when discussing tradeoff (big data reduces variance)
3. Assuming deeper networks always increase variance (depends on regularization)
4. Overlooking irreducible error in decomposition explanations

## Revision Tips
1. Practice deriving decomposition from expectation algebra
2. Compare SVM kernels with different C values using Python
3. Memorize error patterns for common algorithms:
   - Linear Regression: High bias in nonlinear settings
   - k-NN: High variance with small k
   - Random Forests: Balanced through bagging
4. Study recent papers on neural tangent kernel theory

Length: 650 words