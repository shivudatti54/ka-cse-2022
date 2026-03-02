# Gaussian Processes - Summary

## Key Definitions and Concepts
- **Gaussian Process**: Distribution over functions where any finite marginal is multivariate Gaussian
- **Kernel Trick**: Implicit mapping to high-dimensional space via covariance function \(k(\mathbf{x}, \mathbf{x'})\)
- **Nyström Approximation**: Low-rank matrix approximation for scalable GPs
- **Mercer's Theorem**: Basis for kernel eigen decomposition \(k(x,x') = \sum_i \lambda_i \phi_i(x)\phi_i(x')\)

## Important Formulas and Theorems
- **Predictive Distribution**:
  $$\mu_* = \mathbf{K}_{*X}(\mathbf{K}_{XX} + \sigma^2\mathbf{I})^{-1}\mathbf{y}$$
  $$\Sigma_* = \mathbf{K}_{**} - \mathbf{K}_{*X}(\mathbf{K}_{XX} + \sigma^2\mathbf{I})^{-1}\mathbf{K}_{X*}$$
- **Marginal Likelihood** (Evidence):
  $$\log p(\mathbf{y}|\mathbf{X}) = -\frac{1}{2}\mathbf{y}^\top(\mathbf{K} + \sigma^2\mathbf{I})^{-1}\mathbf{y} - \frac{1}{2}\log|\mathbf{K} + \sigma^2\mathbf{I}| + C$$

## Key Points
- GPs provide full predictive distributions, not just point estimates
- Kernel choice encodes prior knowledge about function properties
- Computational complexity scales cubically with data size \(n\)
- Sparse GPs use \(m \ll n\) inducing points for \(O(m^2n)\) scaling
- Bayesian optimization uses GP uncertainty for global optimization
- Deep GPs stack multiple GP layers for hierarchical feature learning
- Neural Tangent Kernels connect infinite-width NNs to GPs

## Common Mistakes to Avoid
- Using RBF kernel for non-smooth functions without considering Matérn
- Ignoring numerical stability in Cholesky decomposition (add jitter)
- Confusing prior covariance with posterior covariance
- Overlooking kernel hyperparameter initialization

## Revision Tips
1. Derive predictive distribution from joint Gaussian (key exam question)
2. Implement RBF kernel from scratch to understand Gram matrices
3. Study the connection between GPs and RKHS (Reproducing Kernel Hilbert Space)
4. Review recent papers on "GPyTorch" and "Sparse Gaussian Processes" (ICML 2023)