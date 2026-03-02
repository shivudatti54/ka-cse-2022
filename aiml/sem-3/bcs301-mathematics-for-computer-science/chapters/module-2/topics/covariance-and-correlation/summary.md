# Covariance and Correlation

## Definitions

- **Covariance**: A measure of how much two random variables vary together. It is calculated as the expected value of the product of the deviations from the mean.
- **Correlation**: A statistical measure that calculates the strength and direction of the linear relationship between two random variables.
- **Covariance Formula**: $\text{Cov}(X, Y) = E[(X - E(X))(Y - E(Y))]$
- **Correlation Formula**: $r(X, Y) = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}$, where $\sigma_X$ and $\sigma_Y$ are the standard deviations of $X$ and $Y$ respectively.

## Important Theorems

- **Properties of Covariance**:

* $\text{Cov}(aX + b, Y) = a\text{Cov}(X, Y)$
* $\text{Cov}(X, aY + b) = a\text{Cov}(X, Y)$

- **Spherical Symmetry Property**: $\text{Cov}(X, Y) = \text{Cov}(Y, X)$
- **Independence Property**: $\text{Cov}(X, Y) = 0$ if and only if $X$ and $Y$ are independent

## Types of Correlation

- **Positive Correlation**: $r(X, Y) > 0$ when $X$ and $Y$ tend to increase together.
- **Negative Correlation**: $r(X, Y) < 0$ when $X$ and $Y$ tend to decrease together.
- **No Correlation**: $r(X, Y) = 0$ when $X$ and $Y$ are unrelated.

## Key Points

- Covariance measures the linear relationship between two random variables, while correlation measures the strength and direction of this relationship.
- Covariance is calculated using the expected value of the product of the deviations from the mean.
- Correlation is calculated using the covariance and the standard deviations of the two variables.
- Positive correlation indicates a strong positive linear relationship, negative correlation indicates a strong negative linear relationship, and no correlation indicates no linear relationship.
