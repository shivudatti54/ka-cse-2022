# Chapter-3 (3.3) Revision Notes

### Multivariate Gaussian Distribution

- A multivariate Gaussian distribution (also known as a multivariate normal distribution) is a probability distribution that describes a continuous random variable with multiple variables.
- It is characterized by its mean vector μ and covariance matrix Σ.
- The probability density function (PDF) of a multivariate Gaussian distribution is given by:
  ```
  f(x | μ, Σ) = (1/√(|Σ|)) \* exp(-0.5 \* (x-μ)^T \* (Σ)^-1 \* (x-μ))
  ```
- Where:
  - x is a vector of random variables
  - μ is the mean vector
  - Σ is the covariance matrix
  - |Σ| is the determinant of the covariance matrix
  - (x-μ)^T is the transpose of the vector (x-μ)
  - (Σ)^-1 is the inverse of the covariance matrix

### Multivariate Normal Distribution Theorems

- **Theorem 1:** If X ~ N(μ, Σ) and Y ~ N(ν, Ω), then X + Y ~ N(μ + ν, Σ + Ω)
- **Theorem 2:** If X ~ N(μ, Σ) and c is a constant, then cX ~ N(cμ, c^2Σ)

### Correlation Coefficient

- The correlation coefficient ρ between two random variables X and Y is given by:
  ```
  ρ(X, Y) = cov(X, Y) / (√cov(X)\*√cov(Y))
  ```
- Where:
  - cov(X, Y) is the covariance between X and Y
  - cov(X) and cov(Y) are the variances of X and Y, respectively

### Regression Analysis

- Linear regression analysis is a statistical method used to establish a relationship between two or more variables.
- The regression equation is given by:
  ```
  y = β0 + β1x + ε
  ```
- Where:
  - y is the dependent variable
  - x is the independent variable
  - β0 is the intercept
  - β1 is the slope
  - ε is the error term

### Other Important Formulas

- **Cholesky decomposition:** A matrix Σ can be decomposed into the product of a lower triangular matrix L and its transpose L^T:
  ```
  Σ = L \* L^T
  ```
- **Eigenvalue decomposition:** A matrix Σ can be decomposed into the product of an orthogonal matrix P, a diagonal matrix Λ, and the transpose of P:
  ```
  Σ = P \* Λ \* P^T
  ```
