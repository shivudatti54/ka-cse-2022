# Random Variables (Discrete and Continuous)

## Discrete Random Variables

- **Definition:** A random variable \( X \) is discrete if it can take on only a countable number of distinct values.
- **Probability Mass Function (PMF):**
  - For \( X = x_i \), the probability mass function \( P(X=x_i) \) gives \( P(x_1), P(x_2), \ldots, P(x_n) \).
  - Summation: \( \sum\_{i} P(X=x_i) = 1 \)
- **Expected Value (Mean):**
  - Discrete random variable: \( E[X] = \sum_x xP(x) \)

## Continuous Random Variables

- **Definition:** A random variable \( Y \) is continuous if it can take on any value within a given interval.
- **Probability Density Function (PDF):**
  - For an interval, the probability density function \( f_Y(y) = P(a < Y \le b) \).
  - Area under the curve: \( \int_a^b f_Y(y) dy = 1 \)
- **Cumulative Distribution Function (CDF):**
  - \( F*Y(y) = P(Y \le y) = \int*{-\infty}^{y} f_Y(t) dt \)
- **Expected Value (Mean):**
  - Continuous random variable: \( E[Y] = \int\_{-\infty}^{\infty} yf_Y(y) dy \)

## Important Theorems and Formulas

- Law of Large Numbers:
  - For large sample sizes, the sample mean approaches the expected value.
  - \( \bar{X} \to E(X) \)
- Central Limit Theorem:
  - For a sufficiently large n, the distribution of sample means approximates a normal distribution with mean \( E(X) \) and variance \( \frac{\sigma^2}{n} \).
  - \( \sqrt{n}\left( \bar{X} - E(X)\right) \to N(0, \sigma^2) \)
- Chebyshev's Inequality:
  - For any random variable \( X \) with mean \( \mu \):
    - \( P(|X-\mu| \ge k\sigma) \le \frac{1}{k^2} \)

## Summary

- **Discrete Random Variables:** Use PMF, expected value is summation of products of values and their probabilities.
- **Continuous Random Variables:** Use PDF, expected value is integral of the variable multiplied by its density function.
- **Theorems and Inequalities:**
  - Law of Large Numbers
  - Central Limit Theorem
  - Chebyshev's Inequality
