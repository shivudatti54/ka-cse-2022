# **Statistical Machine Learning for Data Science: Discriminant Analysis**

### Overview

---

- **Covariance Matrix**: A square matrix representing the variance and covariance of a multivariate distribution.
- **Fisher's Linear Discriminant**: A linear combination of features that maximizes the ratio of between-class variance to within-class variance.

### Key Concepts

---

- **Covariance Matrix Formula**: `Cov(X) = E[(X - E(X))(X - E(X))^T]`
- **Fisher's Linear Discriminant Formula**: `F(X) = (X - E(X))^T * Cov^-1(X) * (X - E(X))`
- **Generalized Linear Models**: A class of linear models that allow for non-normal response variables.
- **Interpreting Discriminant Analysis**: Understanding the importance of each feature in separating classes.

### Important Formulas and Definitions

---

- **Covariance**: A measure of how much a variable changes when another variable changes.
- **Covariance Matrix Inversion**: Used to compute the weights in Fisher's Linear Discriminant.
- **Eigenvalues and Eigenvectors**: Used to diagonalize the covariance matrix.

### Theorems and Assumptions

---

- **Spectral Decomposition Theorem**: Used to diagonalize the covariance matrix.
- **Assumption of Linearity**: Required for most discriminant analysis algorithms.
- **Independence Assumption**: Required for most discriminant analysis algorithms.

### Quick Revision Notes

---

- **Key Takeaways**:
  - Covariance matrices and Fisher's Linear Discriminant are used for classification tasks.
  - Generalized Linear Models are used for regression tasks.
  - Interpretation is crucial for understanding the importance of each feature.
- **Formulae and Definitions**:
  - Covariance: `Cov(X) = E[(X - E(X))(X - E(X))^T]`
  - Fisher's Linear Discriminant: `F(X) = (X - E(X))^T * Cov^-1(X) * (X - E(X))`
- **Important Theorems and Assumptions**:
  - Spectral Decomposition Theorem
  - Assumption of Linearity
  - Independence Assumption
