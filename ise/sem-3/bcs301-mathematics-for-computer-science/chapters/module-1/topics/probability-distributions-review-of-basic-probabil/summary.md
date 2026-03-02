# Probability Distributions: Review of Basic Probability Theory

## **Key Concepts**

- **Random Variable**: A function that assigns a probability distribution to each possible outcome of a random experiment.
- **Probability Distribution**: A function that describes the probability of each possible outcome of a random experiment.

## **Probability Theory**

- **Probability Mass Function (PMF)**: A function that describes the probability of each possible outcome of a discrete random variable.
  - Definition: P(X = x) = p(x)
- **Probability Density Function (PDF)**: A function that describes the probability of each possible outcome of a continuous random variable.
  - Definition: f(x) = p(x)
- **Expected Value (E)**: The long-run average of a random variable, calculated as the sum of each possible outcome multiplied by its probability.
  - Formula: E(X) = ∑xP(X = x) for discrete, E(X) = ∫xf(x)dx for continuous
- **Variance (σ^2)**: A measure of the spread of a random variable, calculated as the expected value of the squared difference between each possible outcome and the expected value.
  - Formula: σ^2 = E((X - E(X))^2)

## **Theorems**

- **The Law of Large Numbers (LLN)**: The long-run average of a random variable converges to its expected value.
  - Theorem: lim n→∞ (1/n) \* ∑xP(X = x) = E(X)
- **The Central Limit Theorem (CLT)**: The distribution of the sum of a large number of independent random variables converges to a normal distribution.
  - Theorem: lim n→∞ P(N(μ, σ) ≤ X ≤ N(μ, σ)) = 1

## **Important Formulas and Definitions**

- **Empirical Distribution Function (EDF)**: A function that describes the proportion of observations less than or equal to a given value.
- **Moment Generating Function (MGF)**: A function that describes the expected value of a random variable.
- **Chernoff Bound**: A bound on the probability of a random variable deviating from its expected value.
- **Markov Inequality**: A bound on the probability of a random variable exceeding a certain value.

Note: This summary is a concise review of the key concepts, formulas, and theorems in probability distributions. It is not an exhaustive list, and you should refer to additional resources for a more detailed understanding of each topic.
