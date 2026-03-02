# GD Variants - Summary

## Types

- Batch: entire dataset
- Stochastic: one sample
- Mini-batch: small batch (32-512)

## Key Formulas

SGD: θ = θ - α∇J(θ; xᵢ)
Momentum: v = βv + α∇J(θ)

## Exam Tips

1. Mini-batch is standard in deep learning
2. Smaller batch = more noise = regularization
3. Momentum accelerates convergence
