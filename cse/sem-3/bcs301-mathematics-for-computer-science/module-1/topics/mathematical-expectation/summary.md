# Mathematical Expectation Revision Notes

## Definition

The mathematical expectation (or expected value) of a discrete random variable \(X\) is denoted by \(\mathbb{E}[X]\) and calculated as:
\[
\mathbb{E}[X] = \sum\_{x} x P(X=x)
\]
where the sum is taken over all possible values \(x\) that \(X\) can take, and \(P(X=x)\) is the probability of \(X\) taking value \(x\).

## Properties

1. **Linearity of Expectation:**
   \[
   \mathbb{E}[aX + b] = a\mathbb{E}[X] + b
   \]
2. **Expected Value for Summations:**
   If \(Y\) is another random variable such that \(Y = X_1 + X_2 + \ldots + X_n\), then:
   \[
   \mathbb{E}[Y] = \mathbb{E}[X_1 + X_2 + \ldots + X_n] = \mathbb{E}[X_1] + \mathbb{E}[X_2] + \ldots + \mathbb{E}[X_n]
   \]

## Important Theorem

**Law of Total Expectation:**
If \(Y\) is an additional random variable and given that:
\[
X = x \implies Y = y(x)
\]
then the expected value of \(X\) can be calculated as:
\[
\mathbb{E}[X] = \sum_x x P(X=x) = \sum_y y(x)P(Y=y)
\]

## Formula and Theorem Recap

- **Linearity:** \(\mathbb{E}[aX + b] = a\mathbb{E}[X] + b\)
- **Law of Total Expectation:** \(\mathbb{E}[X] = \sum_x x P(X=x) = \sum_y y(x)P(Y=y)\)

## Applications

1. In probability and statistics, it is used to model expected outcomes.
2. It helps in making predictions based on past data.

## Conclusion

The mathematical expectation is a fundamental concept that underpins many of the probabilistic analyses in computer science, providing a way to compute the central tendency (or most likely value) of random variables. Understanding and applying these properties and theorems effectively are crucial for solving complex problems involving randomness and uncertainty.

---

This concise summary covers key points about mathematical expectation, formulas, and important theorems, suitable for quick revision before exams in Mathematics for Computer Science.
