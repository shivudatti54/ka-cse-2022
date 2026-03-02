# Summary of Basic Probability Theory and Review of Probability Distributions

## Key Concepts:

### Definitions:

- **Sample Space (S)**: The set of all possible outcomes.
  - Example: Rolling a die, S = {1, 2, 3, 4, 5, 6}.
- **Event**: Subset of the sample space that represents some outcome or combination of outcomes.
  - Example: Getting an even number on a roll, Event A = {2, 4, 6}.

### Formulas:

- **Probability of an event E**:
  \[
  P(E) = \frac{\text{Number of favorable outcomes in } E}{\text{Total number of possible outcomes in the sample space}}
  \]

- **Complement Rule**:
  - Probability of non-E (the complement of E):
    \[
    P(\bar{E}) = 1 - P(E)
    \]

### Theorems:

- **Addition Rule for Mutually Exclusive Events**:
  If events A and B are mutually exclusive, the probability that either A or B occurs is:
  \[
  P(A \cup B) = P(A) + P(B)
  \]

- **Multiplication Rule (Conditional Probability)**:
  The probability of both A and B occurring is:
  \[
  P(A \cap B) = P(A|B)P(B) = P(B|A)P(A)
  \]
  Where \( P(A|B) \) denotes the conditional probability of A given B, which can also be expressed as:
  \[
  P(A|B) = \frac{P(A \cap B)}{P(B)}
  \]

### Distributions:

#### Uniform Distribution

- **Definition**: If every outcome in a sample space is equally likely.
- **Example**: Rolling a fair die.

#### Binomial Distribution

- **Definition**: Number of successes in a fixed number of independent Bernoulli trials with success probability p.
- **Formula**:
  \[
  P(X = k) = \binom{n}{k}p^k(1-p)^{n-k}, \quad k = 0, 1, 2, ..., n
  \]

Where \( \binom{n}{k} \) is the binomial coefficient.

#### Normal Distribution (Gaussian Distribution)

- **Definition**: Symmetric bell-shaped distribution with mean μ and variance σ².
- **Standardization**:
  - Standard Normal Variable Z:
    \[
    Z = \frac{X-\mu}{\sigma}
    \]
  - Probability Density Rule for Standardized Normal Distribution \(Z\) (using the standard normal table or software):
    \[
    P(Z < z) = \Phi(z)
    \]

### Important Formulas & Theorems

- **Expectation and Variance**:
  - **Expected Value**:
    For a discrete random variable X with probability distribution \(P(X)\), expected value E[X] is given by:
    \[
    E[X] = \sum_x x P(x)
    \]
  - **Variance**:
    The variance of X, Var(X), measures the spread of values around the mean. It can be expressed as:
    \[
    Var(X) = E[(X-E[X])^2]
    \]

- **Law of Large Numbers**: As the number of trials increases, the sample mean converges to the true population mean.

### Summary

This summary covers fundamental concepts in probability theory including definitions, formulas, theorems, and distributions. Understanding these principles is crucial for working with probability distributions effectively, which forms a core part of studying Mathematics for Computer Science.
