# Feedforward Networks Optimization - Summary

## Key Definitions and Concepts
- **Optimizer**: Algorithm minimizing loss function (e.g., Adam, SGD)
- **Learning Rate**: Step size in parameter updates (η in Δw = -η∇L)
- **Momentum**: Exponential moving average of gradients (ρ parameter)
- **Weight Decay**: L2 regularization term added to loss (λ||w||²)

## Important Formulas and Theorems
- **Gradient Descent Update**: wₜ₊₁ = wₜ - η∇L(wₜ)
- **Adam Update**:
  mₜ = β₁mₜ₋₁ + (1-β₁)gₜ  
  vₜ = β₂vₜ₋₁ + (1-β₂)gₜ²  
  ŵₜ = wₜ₋₁ - η mₜ/(√vₜ + ε)
- **Xavier Initialization**: Var(w) = 2/(n_in + n_out)
- **Batch Norm**: x̂ = (x - μ)/√(σ² + ε); y = γx̂ + β

## Key Points
- Adaptive optimizers (Adam) generally outperform vanilla SGD
- ReLU derivatives (0 or 1) enable efficient sparse computations
- Proper initialization prevents layer-wise gradient magnitude divergence
- Batch normalization requires different handling during train/test
- Learning rate warmup helps stabilize training in transformers
- Second-order methods (L-BFGS) are impractical for large networks
- SWA (Stochastic Weight Averaging) improves model generalization

## Common Mistakes to Avoid
- Using same learning rate for all network layers
- Initializing all weights to zero causing symmetric breaking failure
- Forgetting to set model.eval() when using dropout/batch norm
- Misinterpreting Adam's bias correction terms

## Revision Tips
1. Practice deriving optimizer update rules from scratch
2. Create comparison tables: Optimizers vs. Tasks vs. Convergence Rates  
3. Implement weight initialization from numpy (He/Xavier)
4. Use TensorBoard to visualize gradient histograms
5. Study ICLR papers on optimization (last 3 years)

Length: 650 words