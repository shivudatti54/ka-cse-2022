# Expectation (Mathematics for Computer Science)

## Key Points

### Expected Value of Joint Probability Distribution

- **Formula:** \( E[X] = \sum\_{x} xP(X=x) \)
  - Where, \( X \) is a discrete random variable.
- **Example Application:** Calculating the expected outcome in games or systems with multiple states.

### Conditional Expectation

- **Definition:** The expectation of one random variable given another. \( E[X|Y=y] = \sum\_{x} xP(X=x|Y=y) \)
  - \( Y \) is a conditioning event.
- **Example Application:** Estimating expected outcomes in scenarios where the probability depends on previous states.

### Expectation Properties

- **Linearity of Expectations:**
  - \( E[aX + b] = aE[X] + b \), for constants \( a, b \)
  - \( E[X_1 + X_2 + ... + X_n] = E[X_1] + E[X_2] + ... + E[X_n] \) if random variables are independent.

### Conditional Expectation Properties

- **Properties of Conditional Expectations:**
  - \( E[E[X|Y]] = E[X] \)
  - If \( X \perp Y \), then \( E[XY] = E[X]E[Y] \)

## Theorems and Definitions

### Law of Total Expectation (Tower Property)

- **Theorem:** \( E[E[X|Y]] = E[X] \)

### Markov's Inequality

- **Inequality:** For any non-negative random variable \( X \) and any positive constant \( c \):
  - \( P(X \geq c) \leq \frac{E[X]}{c} \)

### Chebyshev's Inequality

- **Inequality:** For any random variable \( X \) with finite mean \( \mu_X \) and variance \( \sigma_X^2 \), for any positive constant \( k \):
  - \( P(|X-\mu_X| \geq k\sigma_X) \leq \frac{1}{k^2} \)

## Important Formulas

- **Law of Total Expectation (Tower Property):**
  - \( E[X] = E[E[X|Y]] \)
- **Markov's Inequality:**
  - \( P(X \geq c) \leq \frac{E[X]}{c} \)

- **Chebyshev's Inequality:**
  - \( P(|X-\mu_X| \geq k\sigma_X) \leq \frac{1}{k^2} \)

## Summary

In the context of Mathematics for Computer Science, especially in understanding joint probability distribution and Markov chain concepts within Probability and Statistics, expectation plays a crucial role. It is defined as \( E[X] = \sum\_{x} xP(X=x) \), and its application can range from simple games to complex systems where probabilities depend on previous states. Properties of expectations such as linearity help in simplifying calculations involving multiple variables. Conditional expectations further refine these, especially when the probability of events depends on others, and properties like Markov's and Chebyshev’s inequalities provide bounds for probabilistic outcomes. Understanding these concepts is essential for analyzing stochastic processes and making predictions in computer science applications.
