# Clustering: EM Algorithm

## Introduction
The Expectation-Maximization (EM) algorithm is a fundamental statistical tool for parameter estimation in probabilistic models with latent variables. In clustering contexts, it provides a principled framework for soft clustering through Gaussian Mixture Models (GMMs), addressing key limitations of hard-clustering methods like K-means. Its importance lies in handling incomplete data and providing probability estimates for cluster membership.

First introduced by Dempster, Laird, and Rubin in 1977, EM has become essential in modern machine learning for applications ranging from image segmentation to bioinformatics. Unlike K-means which makes hard assignments, EM allows for uncertainty quantification - critical in research domains like anomaly detection and multi-modal data analysis. Recent advances in scalable EM variants (e.g., Online EM, Variational EM) maintain its relevance in big data contexts.

## Key Concepts
1. **Latent Variable Model**: EM operates on models where observed data X is explained through unobserved latent variables Z
2. **Q-Function**: Expected complete-data log-likelihood 𝔼[log P(X,Z|θ)] 
3. **E-Step**: Computes posterior P(Z|X,θ⁰) using current parameters θ⁰
4. **M-Step**: Updates parameters θ¹ = argmax_θ Q(θ,θ⁰)
5. **GMM Components**:
   - π_k: Mixing coefficients
   - μ_k: Cluster means
   - Σ_k: Covariance matrices
6. **Convergence**: Monotonic likelihood improvement with possible local maxima
7. **Responsibilities**: γ(z_nk) = π_k N(x_n|μ_k,Σ_k) / Σ_j π_j N(x_n|μ_j,Σ_j)

## Examples

**Example 1: 1D GMM with Two Components**
Given data points {1, 2, 6, 7} with initial parameters:
- π₁=π₂=0.5
- μ₁=1, μ₂=6
- σ²=1 for both

*E-Step*:
Calculate responsibilities γ(z_nk):
γ(1,1) = 0.5*N(1|1,1) / [0.5*N(1|1,1) + 0.5*N(1|6,1)] ≈ 0.9997
Similarly compute for all points

*M-Step*:
Update parameters:
μ₁_new = (0.9997*1 + 0.9997*2 + 0.0025*6 + 0.0025*7)/(0.9997+0.9997+0.0025+0.0025) ≈ 1.5

**Example 2: Bivariate GMM**
For 2D data with initial clusters:
- μ₁=(0,0), μ₂=(5,5)
- Diagonal covariance matrices

After first iteration:
- Points near origin have γ(z_n1) ≈ 1
- Points near (5,5) have γ(z_n2) ≈ 1
Update Σ₂ using weighted covariance:
Σ₂ = Σ_n γ(z_n2)(x_n-μ₂)(x_n-μ₂)^T / Σ_n γ(z_n2)

**Example 3: Image Segmentation**
Using EM for pixel clustering:
1. Treat RGB values as 3D data points
2. Initialize 3 GMM components (background, object1, object2)
3. Iterate until convergence (<1% parameter change)
4. Assign pixels to max-responsibility cluster

## Exam Tips
1. **Derive E/M Steps**: Be ready to derive EM updates for GMM parameters from Q-function
2. **Compare with K-means**: EM reduces to K-means when variances approach zero
3. **Convergence Proofs**: Understand Jensen's inequality role in likelihood guarantee
4. **Missing Data Handling**: EM naturally accommodates missing features through marginalization
5. **Initialization Impact**: Multiple restarts needed due to local maxima
6. **Covariance Types**: Know effects of diagonal vs full covariance matrices
7. **Bayesian EM**: Mention Dirichlet prior extensions in viva