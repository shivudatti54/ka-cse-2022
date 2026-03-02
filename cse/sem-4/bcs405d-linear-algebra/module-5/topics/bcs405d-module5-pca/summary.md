# Dimensionality Reduction and PCA - Summary

## Key Definitions and Concepts

- **Dimensionality Reduction**: The process of reducing the number of features in a dataset while preserving essential information.
- **Principal Component Analysis (PCA)**: A linear unsupervised technique that transforms data to a new coordinate system defined by principal components (eigenvectors of covariance matrix).
- **Principal Components**: Orthogonal axes representing directions of maximum variance in the data; ordered by variance explained.
- **Eigenvalues**: Quantities representing the magnitude of variance in the direction of corresponding eigenvectors.
- **Eigenvectors**: Vectors that don't change direction during a linear transformation; represent principal component directions in PCA.
- **Covariance Matrix**: Symmetric matrix showing relationships between all pairs of variables in the dataset.

## Important Formulas and Theorems

- **Standardization**: Z = (X - μ) / σ
- **Covariance Matrix**: Σ = (1/(n-1)) × ZTZ where Z is the standardized data matrix
- **Variance Explained by PCi**: λi / Σλj (where λ represents eigenvalues)
- **Cumulative Variance**: Σ(λi for i=1 to k) / Σλj for first k components
- **Data Transformation**: Y = Z × Wk (standardized data × selected eigenvectors)

## Key Points

- PCA transforms correlated variables into uncorrelated principal components.
- The first principal component always captures the maximum variance.
- Principal components are orthogonal (perpendicular) to each other.
- Eigenvalues indicate the importance of each principal component.
- Typically retain components that explain 80-95% of total variance.
- Always standardize data before applying PCA to ensure fair feature contribution.
- PCA is computationally efficient using Singular Value Decomposition (SVD).
- The number of components is determined by eigenvalue magnitude or variance threshold.

## Common Mistakes to Avoid

1. **Forgetting to standardize**: Using raw data causes features with larger scales to dominate the analysis incorrectly.

2. **Keeping too many components**: Retaining components with very small eigenvalues adds noise rather than information.

3. **Ignoring cumulative variance**: Selecting components based only on individual variance percentages rather than cumulative explained variance.

4. **Misinterpreting components**: Principal components are linear combinations of original features, not new independent variables.

## Revision Tips

1. Practice computing PCA on small 2D/3D datasets manually to understand each step.

2. Remember: Eigenvectors show direction, eigenvalues show variance magnitude.

3. Review eigenvalue-eigenvector computation for symmetric matrices (covariance matrices are symmetric).

4. Know that PCA maximizes variance rather than minimizes reconstruction error (though mathematically equivalent).

5. Understand that PCA is a rotation of axes to new orthogonal positions aligned with data variance.
