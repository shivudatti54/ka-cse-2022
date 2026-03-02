# Summary: Mean and Variance

## Definitions:

- **Mean (Expected Value)**: The mean of a random variable \(X\) is denoted as \(\mu\) or \(E[X]\) and calculated using:
  \[
  \mu = E[X] = \sum*{i} x_i P(X=x_i)
  \]
  For a continuous distribution, it becomes:
  \[
  \mu = E[X] = \int*{-\infty}^{\infty} x f(x) dx
  \]

- **Variance**: The variance of a random variable \(X\) is denoted as \(\sigma^2\) or \(Var(X)\) and calculated using:
  \[
  Var(X) = E[(X - \mu)^2] = \sum*{i} (x_i - \mu)^2 P(X=x_i)
  \]
  For a continuous distribution, it becomes:
  \[
  Var(X) = E[(X - \mu)^2] = \int*{-\infty}^{\infty} (x - \mu)^2 f(x) dx
  \]

## Important Formulas:

1. **Variance of a Sum**: If \(X\) and \(Y\) are two independent random variables, then:
   \[
   Var(X + Y) = Var(X) + Var(Y)
   \]

2. **Standard Deviation**: The standard deviation is the square root of the variance:
   \[
   \sigma_X = \sqrt{Var(X)}
   \]

## Key Points:

- Mean and Variance are fundamental statistical measures.
- Mean represents the expected value or average of a random variable, while variance quantifies the dispersion or spread around this mean.

- Variance can be expanded as:
  \[
  Var(X) = E[X^2] - (E[X])^2
  \]
  This is useful when the direct calculation using summation/integration is cumbersome.

## Theorems:

1. **Chebyshev's Inequality**: For any random variable \(X\) with mean \(\mu\) and variance \(\sigma^2\), for all \(k > 0\):
   \[
   P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}
   \]
   This theorem provides a bound on the probability that a random variable deviates from its mean by at least \(k\) times the standard deviation.

## Example:

Given two independent random variables \(X\) and \(Y\) with means 3 and 5 respectively, and variances 4 and 9:

- Their combined variance is:
  \[
  Var(X + Y) = Var(X) + Var(Y) = 4 + 9 = 13
  \]
- The mean of their sum is the sum of their means:
  \[
  E[X+Y] = E[X] + E[Y] = 3 + 5 = 8
  \]

## Conclusion:

Understanding and calculating both mean and variance are crucial in probability theory. They provide insight into the central tendency (mean) and spread (variance) of a distribution, which is essential for further statistical analysis and machine learning applications.
