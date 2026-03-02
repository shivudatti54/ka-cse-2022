# Chapter 3.3: Multivariate Data and Multivariate Statistics

### Key Concepts

- **Multivariate Data**: Data that has more than two variables.
- **Multivariate Statistics**: Statistical analysis of data with more than two variables.
- **Multivariate Distribution**: Probability distribution of a vector of random variables.
- **Correlation Coefficient**: Measures the linear relationship between two variables.

### Important Formulas and Theorems

- **Covariance Formula**: Cov(X, Y) = E[(X - E(X))(Y - E(Y))]
- **Correlation Coefficient Formula**: ρ(X, Y) = Cov(X, Y) / (σ_X \* σ_Y)
- **Multivariate Normal Distribution**: f(x | μ, Σ) = (1 / (2π)^n \* |Σ|^(1/2)) \* exp(-((x - μ)^T Σ^(-1) (x - μ))/2)
- **Hotelling's T-Square**: T^2 = (n - 1) \* (Σ^(-1) (X - μ)^T (X - μ)) / (n - k)

### Definitions

- **Sum of Squares**: Σ = X^T X
- **Covariance Matrix**: Σ = E[(X - E(X))(X - E(X))^T]
- **Variance-Covariance Matrix**: Ω = E[(X - E(X))(X - E(X))^T] = Σ^(-1)

### Theorems

- **Multivariate Regression**: Least Squares Estimator of β is given by β̂ = (X^T X)^(-1) X^T Y
- **Multivariate Analysis of Variance (MANOVA)**: Tests the hypothesis that two or more groups have equal covariance matrices.
