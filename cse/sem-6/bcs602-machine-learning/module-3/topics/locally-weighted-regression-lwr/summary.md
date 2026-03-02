# Locally Weighted Regression (LWR)

## Overview

Locally Weighted Regression is a non-parametric method that performs regression around a query point by giving more weight to nearby training examples. Unlike global models that learn one function for entire dataset, LWR fits local models making it flexible for non-linear patterns.

## Key Points

- **Key Idea**: For each query point, fit a local model using nearby training points weighted by distance
- **Weighting Function**: Gaussian kernel w(i) = exp(-||x(i)-x||²/(2τ²)); τ (bandwidth) controls locality
- **Bandwidth τ**: Large τ → more global (like linear regression); Small τ → more local (follows data closely); optimal τ balances bias-variance
- **Non-Parametric**: No fixed number of parameters; model complexity grows with data size
- **Prediction**: For new point x, solve weighted least squares: minimize Σw(i)(y(i) - w^Tx(i))²
- **Computational Cost**: O(n) for each prediction (vs O(1) for parametric); must recompute for every query point

## Important Concepts

- Lazy learning: no explicit training phase; all computation happens at prediction time
- Bandwidth selection critical: cross-validation used to find optimal τ
- Captures non-linear relationships without specifying functional form
- Memory-intensive: must store all training data for predictions

## Notes

- Explain weighting function: points closer to query get higher weights (exponential decay with distance)
- Bandwidth τ effect: large (smooth, underfitting), small (wiggly, overfitting)
- Compare with linear regression: LWR is non-parametric, fits local models, higher computational cost
- Understand lazy learning: all work at prediction time, no training phase
