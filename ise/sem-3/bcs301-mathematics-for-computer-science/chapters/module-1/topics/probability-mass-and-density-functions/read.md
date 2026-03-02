# **Probability Mass and Density Functions**

## **Introduction**

Probability mass and density functions are fundamental concepts in probability theory, used to describe the probability distributions of random variables. In this study material, we will explore these concepts, including their definitions, properties, and examples.

## **Definition and Notation**

- **Probability Mass Function (PMF)**: A function that assigns a probability mass to each value in a discrete random variable. The PMF is often denoted as `p(x)` or `f(x)` and is defined as:
  - `p(x) = P(X = x)`
- **Probability Density Function (PDF)**: A function that assigns a probability density to each value in a continuous random variable. The PDF is often denoted as `f(x)` and is defined as:
  - `f(x) = P(X ≤ x)`
- **Random Variable**: A variable that can take on different values with different probabilities.

## **Properties of PMFs and PDFs**

### Properties of PMFs

- **Normalizing Property**: The sum of all probabilities in a PMF should be equal to 1:
  - `∑[p(x)] = 1`
- **Non-Negativity Property**: The probability of each value in a PMF should be non-negative:
  - `p(x) ≥ 0`
- **Discrete Uniqueness Property**: Each value in a PMF can only have one probability assigned to it:
  - `p(x) = 0` for all `x ≠ x_i`
- **Countable Additivity Property**: The probability of a union of disjoint events in a PMF can be calculated by summing the probabilities of each event:
  - `P(A ∪ B) = P(A) + P(B)` if `A` and `B` are disjoint

### Properties of PDFs

- **Non-Negativity Property**: The probability density of each value in a PDF should be non-negative:
  - `f(x) ≥ 0`
- **Normalization Property**: The integral of the PDF over all possible values should be equal to 1:
  - `∫[f(x)] dx = 1`
- **Continuous Uniqueness Property**: Each value in a PDF can only have one probability density assigned to it:
  - `f(x) = 0` for all `x ≠ x_i`
- **Additivity Property**: The probability of a union of disjoint events in a PDF can be calculated by integrating the PDF over each event:
  - `P(A ∪ B) = ∫[f(x)] dx` if `A` and `B` are disjoint

## **Examples**

### Discrete Random Variable

Suppose we have a discrete random variable `X` that can take on the values 0, 1, and 2, with the following probabilities:

| `x` | `p(x)` |
| --- | ------ |
| 0   | 1/3    |
| 1   | 2/3    |
| 2   | 1/3    |

The PMF of `X` is given by `p(x) = 1/3` for `x = 0, 1, 2`.

### Continuous Random Variable

Suppose we have a continuous random variable `X` that follows a uniform distribution over the interval [0, 1], with the following PDF:

| `x`    | `f(x)` |
| ------ | ------ |
| (0, 1) | 1      |

The PDF of `X` is given by `f(x) = 1` for `0 ≤ x ≤ 1`.

## **Conclusion**

Probability mass and density functions are fundamental concepts in probability theory, used to describe the probability distributions of random variables. Understanding the properties and examples of PMFs and PDFs is crucial for modeling and analyzing random phenomena in mathematics and computer science.
