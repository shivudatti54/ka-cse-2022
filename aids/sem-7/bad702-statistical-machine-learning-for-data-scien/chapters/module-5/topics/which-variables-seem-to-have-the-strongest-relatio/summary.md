# **Revision Notes: Which Variables Seem to Have the Strongest Relationships**

**Definition:** In discriminant analysis, we want to identify the variables that have the strongest relationships with the target variable.

**Key Points:**

- **Covariance Matrix:** The covariance matrix measures the variance and covariance between each pair of variables. The diagonal elements represent the variance of each variable.
- **Fisher's Linear Discriminant (FLD):** FLD is a linear combination of variables that maximizes the separation between classes. It is calculated using the following formula:
  - `FLD = X^T * Σ^-1 * (μ1 - μ0)`, where:
    - `X` is the matrix of variables
    - `Σ` is the covariance matrix
    - `μ1` and `μ0` are the mean vectors of the two classes
- ** Eigenvectors and Eigenvalues:** FLD uses eigenvectors and eigenvalues from the covariance matrix to calculate the linear combination of variables.
- **Importance of Variables:** The importance of variables is determined by their contribution to the separation between classes.

**Theorem:** The FLD is a linear combination of variables that maximizes the separation between classes.

**Key Formulas:**

- `FLD = X^T * Σ^-1 * (μ1 - μ0)`
- `Σ^-1 = 1 / det(Σ) * adj(Σ)`

**Important Concepts:**

- **Variance:** Measures the spread of a variable.
- **Covariance:** Measures the linear relationship between two variables.
- **Eigenvectors:** Vectors that represent the directions of maximum variance.
- **Eigenvalues:** Scalars that represent the amount of variance explained by each eigenvector.

**Practice Questions:**

- Identify the variables with the strongest relationships with the target variable using FLD.
- Calculate the importance of variables using FLD.
- Interpret the results in the context of the problem.
