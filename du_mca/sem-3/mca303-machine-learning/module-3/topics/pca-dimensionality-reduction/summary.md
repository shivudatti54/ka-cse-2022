# Principal Component Analysis (PCA) - Summary

## Key Definitions and Concepts

- **Principal Component Analysis (PCA)**: An unsupervised linear dimensionality reduction technique that projects high-dimensional data onto a lower-dimensional subspace while preserving maximum variance (information).

- **Principal Components**: Linear combinations of original features representing directions of maximum variance; each component is orthogonal to all others.

- **Eigenvalues**: Quantify the variance captured by each principal component; larger eigenvalues indicate more important components.

- **Eigenvectors**: Define the direction of each principal component in the original feature space.

- **Covariance Matrix**: A symmetric d×d matrix capturing pairwise covariances between all features; the foundation for PCA computation.

## Important Formulas and Theorems

- **Standardization**: z = (x - μ) / σ (ensures zero mean, unit variance)

- **Covariance**: Cov(Xi, Xj) = Σ(xk,i - x̄i)(xkj - x̄j) / (n-1)

- **Eigenvalue equation**: Σv = λv

- **Variance explained by PCi**: λi / Σλj

- **Cumulative variance (k components)**: (Σᵢ₌₁ᵏ λi) / Σλj

- **Projection**: Znew = Z × W (where W contains selected eigenvectors)

## Key Points

- PCA identifies directions of maximum variance to reduce dimensionality while preserving information

- Always standardize data before applying PCA to prevent scale-dominated features

- Principal components are ordered by eigenvalues in descending variance capture

- The first k components with cumulative variance ≥95% typically provide adequate reduction

- PCA assumes linear relationships between features; it's not suitable for non-linear manifolds

- Orthogonality of principal components ensures no redundant information in the reduced space

- Computational approaches include covariance matrix eigendecomposition or SVD

## Common Mistakes to Avoid

1. **Skipping standardization**: Applying PCA without standardizing features leads to meaningless results dominated by large-scale features

2. **Choosing too many components**: Retaining components that contribute minimal variance increases complexity without significant benefit

3. **Ignoring information loss**: Reducing dimensions always loses some information; quantify and acknowledge this trade-off

4. **Misinterpreting components**: Principal components are abstract linear combinations, not directly interpretable as original features

## Revision Tips

1. Practice the complete PCA algorithm manually on small 2D or 3D datasets to solidify understanding

2. Memorize that eigenvalues represent variance and eigenvectors represent directions

3. Review scree plot examples to identify the "elbow" point visually

4. Remember that PCA is unsupervised—it doesn't use class labels in finding components

5. Know the practical Python implementation using scikit-learn's PCA class