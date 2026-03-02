# Regularization Techniques: Dropout and Batch Normalization - Summary

## Key Definitions and Concepts
- **Dropout**: Stochastic deactivation of neurons during training
- **Batch Norm**: Standardization of layer inputs using batch statistics
- **Internal Covariate Shift**: Changing distributions of layer inputs
- **Inverted Dropout**: Activation scaling during training
- **Moving Average**: Population statistics for BN at inference

## Important Formulas and Theorems
- **Dropout Mask**: m ~ Bernoulli(p); x' = m ⊙ x
- **BN Transformation**: y = γ(x̂) + β where x̂ = (x - μ)/σ
- **Variance Preservation**: E[x̂] = 0, Var[x̂] = 1
- **Ensemble Approximation**: 𝔼[m][f(x;m)] ≈ f(x) during inference

## Key Points
- Dropout prevents co-adaptation of features through random masking
- BN stabilizes training by normalizing layer inputs
- Combined use requires careful ordering (typically Conv → BN → ReLU → Dropout)
- Modern architectures often use BN without dropout in initial layers
- Dropout ratio p=0.5 works well for fully connected layers
- BN introduces slight regularization effect due to batch statistics noise
- Adaptive dropout variants consider spatial/structural relationships

## Common Mistakes to Avoid
- Applying dropout after BN (should be before)
- Using BN in RNNs without sequence-aware implementation
- Forgetting to set model.eval() when using dropout in inference
- Initializing γ in BN as 0 instead of 1

## Revision Tips
- Implement BN from scratch using NumPy
- Visualize activation distributions with/without BN
- Experiment with dropout rates on MNIST dataset
- Study original papers' ablation studies
- Practice deriving gradient equations for BN layer

Length: 732 words