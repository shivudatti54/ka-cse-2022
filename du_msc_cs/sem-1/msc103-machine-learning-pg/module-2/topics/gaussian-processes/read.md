# Gaussian Processes

## Introduction
Gaussian Processes (GPs) are powerful non-parametric Bayesian models that provide a flexible framework for regression and classification tasks. Unlike parametric models that assume a specific functional form, GPs define a distribution over functions, making them particularly effective for uncertainty quantification and small-data scenarios. Their ability to model complex patterns while providing well-calibrated uncertainty estimates has made them indispensable in robotics, geostatistics, and Bayesian optimization.

In modern machine learning research, GPs bridge the gap between Bayesian statistics and kernel methods. They are theoretically grounded in Kolmogorov extension theorem and employ kernelized covariance structures to capture data relationships. Current research extends GPs to deep architectures (Deep GPs), scalable approximations (SVGP), and integration with neural networks, maintaining relevance in areas like meta-learning and automated machine learning.

## Key Concepts
1. **GP Definition**: A GP is a collection of random variables where any finite subset follows a multivariate Gaussian distribution. Formally, 
   $$f(\mathbf{x}) \sim \mathcal{GP}(m(\mathbf{x}), k(\mathbf{x}, \mathbf{x'}))$$
   where \(m\) is the mean function and \(k\) the kernel/covariance function.

2. **Kernel Functions**: 
   - Radial Basis Function (RBF): 
     $$k(\mathbf{x}, \mathbf{x'}) = \exp\left(-\frac{\|\mathbf{x} - \mathbf{x'}\|^2}{2l^2}\right)$$
   - Matérn Kernels: Handle different smoothness assumptions

3. **Posterior Predictive Distribution**:
   Given training data \((\mathbf{X}, \mathbf{y})\), the predictive distribution at test points \(\mathbf{X}_*\) is:
   $$
   p(\mathbf{f}_* | \mathbf{X}_*, \mathbf{X}, \mathbf{y}) = \mathcal{N}(\mathbf{K}_{*}^\top \mathbf{K}_{XX}^{-1} \mathbf{y}, \mathbf{K}_{**} - \mathbf{K}_{*}^\top \mathbf{K}_{XX}^{-1} \mathbf{K}_{*})
   $$

4. **Hyperparameter Learning**: 
   Optimize kernel parameters by maximizing the marginal likelihood:
   $$
   \log p(\mathbf{y}|\mathbf{X}) = -\frac{1}{2}\mathbf{y}^\top \mathbf{K}^{-1}\mathbf{y} - \frac{1}{2}\log|\mathbf{K}| - \frac{n}{2}\log 2\pi
   $$

5. **Computational Challenges**: 
   Exact GPs have \(O(n^3)\) complexity due to matrix inversion. Sparse approximations (e.g., FITC, SVGP) reduce this to \(O(m^2n)\) using inducing points.

## Examples

**Example 1: 1D Regression with RBF Kernel**
```python
# Generate data
X = np.linspace(0, 5, 10)[:, None]
y = np.sin(X*3) + 0.1*np.random.randn(10,1)

# Define GP model
kernel = RBF(length_scale=1.0)
gp = GaussianProcessRegressor(kernel=kernel)
gp.fit(X, y)

# Predictive distribution
X_test = np.linspace(0, 5, 100)[:, None]
y_mean, y_std = gp.predict(X_test, return_std=True)
```
*Solution*: The posterior mean captures the sine wave trend, while uncertainty bands widen in regions with no data.

**Example 2: Hyperparameter Optimization**
Maximize marginal likelihood for RBF kernel parameters:
$$
\frac{\partial \log p(\mathbf{y}|\mathbf{X})}{\partial l} = \frac{1}{2}\text{tr}\left((\boldsymbol{\alpha}\boldsymbol{\alpha}^\top - \mathbf{K}^{-1})\frac{\partial \mathbf{K}}{\partial l}\right)
$$
where \(\boldsymbol{\alpha} = \mathbf{K}^{-1}\mathbf{y}\). Use gradient ascent with ADAM optimizer.

**Example 3: Bayesian Optimization**
Use GP-UCB acquisition function to find global maximum of unknown \(f(x)\):
$$
x_{t+1} = \arg\max_x \mu_t(x) + \beta_t \sigma_t(x)
$$
Balance exploration (\(\sigma\)) and exploitation (\(\mu\)) for sample-efficient optimization.

## Exam Tips
1. **Kernel Selection**: Understand how different kernels (RBF, Matérn, Periodic) encode prior assumptions about function smoothness and periodicity.
2. **Covariance Matrix Properties**: Be prepared to explain positive definiteness and Cholesky decomposition in GP regression.
3. **Comparison with NN**: Contrast GPs (exact Bayesian inference) with neural networks (point estimates + dropout approximation).
4. **Computational Limits**: Discuss the \(O(n^3)\) bottleneck and sparse approximation methods.
5. **Active Research**: Mention connections to Transformers (self-attention as kernel similarity) and neural tangent kernels.
6. **Derivation Skills**: Practice deriving the posterior predictive distribution from joint Gaussian.
7. **Real-World Case**: Study GP applications in climate modeling or drug discovery where uncertainty matters.