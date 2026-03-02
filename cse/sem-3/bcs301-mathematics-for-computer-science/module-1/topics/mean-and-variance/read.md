# Probability Distributions

## Table of Contents

- [Probability Distributions](#probability-distributions)
- [Topic: Mean and Variance](#topic-mean-and-variance)
  - [Mean (Expected Value)](#mean-expected-value)
  - [Variance](#variance)
  - [Examples](#examples)
  - [Applications](#applications)

## Topic: Mean and Variance

In this module, we will delve into two important measures of a probability distribution: mean (also known as expected value) and variance. These metrics are fundamental in understanding probabilistic models used across various fields including computer science.

### Mean (Expected Value)

The **mean** or **expected value** of a discrete random variable \(X\) is the long-run average value that would be obtained if the experiment were repeated an infinite number of times. It can be calculated using the formula:
\[ E(X) = \sum\_{i} x_i P(x_i) \]
Where \(x_i\) are the possible values that \(X\) can take, and \(P(x_i)\) is the probability of \(X\) taking on value \(x_i\).

#### Key Concepts

- **Definition**: The mean captures the central tendency or typical value around which data points tend to cluster. It’s a weighted average where weights are the probabilities of each outcome.
- **Notation**: Often represented as \(\mu\) for a random variable \(X\).

### Variance

Variance measures how spread out the values in a dataset are from their mean. A higher variance indicates that the data points are more dispersed, while lower variance suggests they are closer to the mean.

The variance of a discrete random variable \(X\) is calculated using:
\[ \text{Var}(X) = E[(X - E(X))^2] \]
This can also be written as:
\[ \text{Var}(X) = \sum\_{i} (x_i - E(X))^2 P(x_i) \]

#### Key Concepts

- **Definition**: Variance quantifies the degree of variation or dispersion in a set of data. It’s calculated by taking the average of squared differences from the mean.
- **Notation**: Often represented as \(\sigma^2\) for variance, and \(s^2\) for sample variance.

### Examples

1. **Example: Binomial Distribution**
   Consider flipping a fair coin 5 times (each flip has two possible outcomes: heads or tails).

- The number of heads (\(X\)) follows a binomial distribution with parameters \(n = 5\) and \(p = 0.5\).

For \(x_i\) representing the number of heads, we calculate:
\[ E(X) = np = 5 \times 0.5 = 2.5 \]
The probability mass function for each \(x_i\) can be calculated using the binomial formula.

The variance is then computed as:
\[ \text{Var}(X) = np(1-p) = 5 \times 0.5 \times (1 - 0.5) = 5 \times 0.5 \times 0.5 = 1.25 \]

2. **Example: Uniform Distribution**
   Suppose you roll a six-sided die, where each face has an equal probability of appearing.

- The possible outcomes are \(X \in \{1, 2, 3, 4, 5, 6\}\).
- Mean (expected value) is:
  \[ E(X) = \frac{1+2+3+4+5+6}{6} = 3.5 \]
- Variance: First compute \(E(X^2)\):
  \[ E(X^2) = \frac{1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2}{6} = \frac{1+4+9+16+25+36}{6} = \frac{91}{6} \approx 15.167 \]
  Then use the shortcut formula:
  \[ \text{Var}(X) = E(X^2) - [E(X)]^2 = \frac{91}{6} - (3.5)^2 = \frac{91}{6} - \frac{49}{4} = \frac{182 - 147}{12} = \frac{35}{12} \approx 2.917 \]

### Applications

Understanding mean and variance helps in making predictions, assessing risk, and evaluating the performance of probabilistic models used extensively in machine learning algorithms like decision trees, clustering methods, and Bayesian networks.

In summary:

- **Mean** provides insights into central tendencies.
- **Variance** gives an idea about dispersion or spread within a dataset.

By mastering these concepts, you'll be better equipped to handle complex probabilistic scenarios in your studies and future projects.
