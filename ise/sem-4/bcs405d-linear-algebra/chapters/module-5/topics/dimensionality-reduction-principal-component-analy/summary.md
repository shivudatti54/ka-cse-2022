# Dimensionality Reduction – Principal Component Analysis

### Overview

- Dimensionality reduction is a technique used to reduce the number of features or variables in a dataset while preserving most of the information.
- Principal Component Analysis (PCA) is a widely used dimensionality reduction technique.

### Key Points

- **Definition:** PCA is a linear transformation that projects a dataset onto a new coordinate system such that the resulting variables are uncorrelated and explain most of the variance in the data.
- **Objective:** To find the linear combination of the original features that captures the most variance in the data.
- **Assumptions:**
  - Data is multivariate normal
  - Correlation between features is equal

### Formulas

- **Principal Component Loadings:** `λ_i`, `v_i`, where `λ_i` is the variance explained by the `i`-th principal component and `v_i` is the corresponding eigenvector.
- **Principal Component Scores:** `X_p = U^T X`, where `X_p` is the projected data, `U` is the matrix of principal component loadings, and `X` is the original data.

### Theorems

- **Covariance Matrix:** The covariance matrix of the principal component scores is diagonal, i.e., `Cov(X_p) = Σv_i v_i^T`.
- **Orthogonality:** The principal components are orthogonal, i.e., `X_p^T X_p = I`.

### Important Concepts

- **Eigenvectors:** Non-zero vectors that, when multiplied by the covariance matrix, result in a scaled version of themselves.
- **Eigenvalues:** Scalars that represent the amount of variance explained by each principal component.
- **Singular Value Decomposition (SVD):** A factorization of the covariance matrix into three matrices: `U`, `Σ`, and `V^T`.

### Important Formulas (continued)

- **Eigenvalue Equation:** `X^T X v = λ v`, where `v` is the eigenvector and `λ` is the eigenvalue.
- **Singular Value Decomposition (SVD):** `X = U Σ V^T`, where `U` and `V` are orthogonal matrices, and `Σ` is a diagonal matrix containing the singular values.

### Key Takeaways

- PCA is a widely used dimensionality reduction technique that projects data onto a new coordinate system.
- The resulting principal components are uncorrelated and explain most of the variance in the data.
- PCA is based on the eigenvectors and eigenvalues of the covariance matrix.
