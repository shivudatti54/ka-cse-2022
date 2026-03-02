# **Covariance and Correlation Revision Notes**

**Definitions**

- **Covariance**: A measure of how much two random variables `X` and `Y` vary together. It is defined as:
  - `Cov(X, Y) = E[(X - E(X))(Y - E(Y))]`
- **Correlation**: A measure of the linear relationship between two random variables `X` and `Y`. It is defined as:
  - `Corr(X, Y) = Cov(X, Y) / (σ_X * σ_Y)`
  - where `σ_X` and `σ_Y` are the standard deviations of `X` and `Y`, respectively

**Important Formulas**

- `Covariance Matrix`: A matrix of covariances between pairs of random variables
  - `Σ = [Cov(X_i, X_j)]`
- `Correlation Matrix`: A matrix of correlations between pairs of random variables
  - `R = [Corr(X_i, X_j)]`

**Theorems**

- **Linearity of Expectation**: `E[aX + bY] = aE(X) + bE(Y)`
- **Independence**: If `X` and `Y` are independent, then `Cov(X, Y) = 0`

**Key Properties**

- **Symmetry**: `Cov(X, Y) = Cov(Y, X)`
- `Cov(aX + b, Y) = aCov(X, Y)`
- `Cov(X, aY + b) = aCov(X, Y)`
- `Corr(aX + b, Y) = aCorr(X, Y)`

**Key Concepts**

- **Positive Correlation**: `Corr(X, Y) > 0` means that `X` and `Y` tend to increase or decrease together
- **Negative Correlation**: `Corr(X, Y) < 0` means that `X` and `Y` tend to move in opposite directions
- `Correlation Coefficient`: A value between -1 and 1 that measures the strength and direction of the correlation between two variables
