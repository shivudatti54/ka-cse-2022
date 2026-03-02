# Probability Distributions: Review of Basic Probability Theory

### Table of Contents

1. [Introduction](#introduction)
2. [Basic Probability Concepts](#basic-probability-concepts)
3. [Probability Distributions](#probability-distributions)
   - [Discrete Probability Distributions](#discrete-probability-distributions)
   - [Continuous Probability Distributions](#continuous-probability-distributions)
4. [Example 1: Fair Coin Toss](#example-1-fair-coin-toss)
5. [Example 2: Die Roll](#example-2-die-roll)
6. [Case Study: Fairness in Coin Toss](#case-study-fairness-in-coin-toss)
7. [Modern Developments](#modern-developments)
8. [Conclusion](#conclusion)
9. [Further Reading](#further-reading)

### Introduction

---

Probability is a branch of mathematics that deals with the study of chance events and their likelihood of occurrence. It provides a mathematical framework for analyzing and understanding random phenomena, which is essential in many fields, including computer science. Probability distributions are a fundamental concept in probability theory, and they play a crucial role in modeling random variables and their behavior.

### Basic Probability Concepts

---

#### 1. Experiment and Sample Space

An experiment is an action or a set of actions that can result in a specific outcome. The sample space is the set of all possible outcomes of an experiment.

#### 2. Event

An event is a subset of the sample space. Events can be simple (single outcome) or compound (combinations of outcomes).

#### 3. Probability of an Event

The probability of an event is a measure of the likelihood that the event will occur. It is defined as the ratio of the number of favorable outcomes to the total number of possible outcomes.

#### 4. Random Variable

A random variable is a variable that can take on different values, with each value associated with a probability. Random variables can be discrete or continuous.

### Probability Distributions

---

#### Discrete Probability Distributions

---

A discrete random variable can take on only a countable number of distinct values. The probability distribution of a discrete random variable is a function that assigns a probability to each possible value.

**Example:** A coin toss has two possible outcomes: heads (H) or tails (T). The probability distribution of a single toss is:

| Outcome | Probability |
| ------- | ----------- |
| H       | 1/2         |
| T       | 1/2         |

#### Continuous Probability Distributions

---

A continuous random variable can take on any value within a given interval or range. The probability distribution of a continuous random variable is a function that assigns a probability to each possible value.

**Example:** A die roll can take on any integer value between 1 and 6. The probability distribution of a single roll is:

| Value | Probability |
| ----- | ----------- |
| 1     | 1/6         |
| 2     | 1/6         |
| 3     | 1/6         |
| 4     | 1/6         |
| 5     | 1/6         |
| 6     | 1/6         |

### Example 1: Fair Coin Toss

---

Suppose we flip a fair coin three times. We want to calculate the probability of getting exactly two heads.

| Outcome | Probability |
| ------- | ----------- |
| HHH     | 1/8         |
| HHT     | 3/8         |
| HTH     | 3/8         |
| THH     | 3/8         |
| TTT     | 1/8         |
| HTT     | 3/8         |
| THT     | 3/8         |
| TTH     | 3/8         |

The probability of getting exactly two heads is:

P(2 heads) = P(HHT) + P(HTH) + P(THH) = 3/8 + 3/8 + 3/8 = 9/8

### Example 2: Die Roll

---

Suppose we roll a fair six-sided die. We want to calculate the probability of getting an even number.

| Value | Probability |
| ----- | ----------- |
| 1     | 1/6         |
| 2     | 1/6         |
| 3     | 1/6         |
| 4     | 1/6         |
| 5     | 1/6         |
| 6     | 1/6         |

The probability of getting an even number is:

P(even) = P(2) + P(4) + P(6) = 1/6 + 1/6 + 1/6 = 3/6 = 1/2

### Case Study: Fairness in Coin Toss

---

A coin toss is considered fair if the probability of getting heads is equal to the probability of getting tails, which is 1/2.

Suppose we have two coins, each with unknown probability of landing on heads. We want to determine if the coins are fair or not.

Let's say we flip the first coin 100 times and get 55 heads. The probability of getting heads is:

P(heads) = 55/100 = 0.55

We flip the second coin 100 times and get 50 heads. The probability of getting heads is:

P(heads) = 50/100 = 0.5

Since the probabilities of getting heads are not equal, the coins are not fair.

### Modern Developments

---

#### Bayesian Statistics

Bayesian statistics provides a framework for updating probabilistic models based on new data. This approach is widely used in machine learning and artificial intelligence.

#### Monte Carlo Methods

Monte Carlo methods involve using random sampling to approximate complex calculations. This approach is widely used in simulations and modeling.

#### Stochastic Processes

Stochastic processes describe the behavior of random systems over time. This approach is widely used in modeling and analysis of complex systems.

### Conclusion

---

Probability distributions are a fundamental concept in probability theory, and they play a crucial role in modeling random variables and their behavior. This review has covered the basics of probability theory, including discrete and continuous probability distributions, and provided examples and case studies to illustrate key concepts. Further reading is suggested in the final section.

### Further Reading

---

- [1] "Probability and Statistics" by James E. Freund
- [2] "Bayesian Statistics" by David J. Hand
- [3] "Monte Carlo Methods" by George P. Box
- [4] "Stochastic Processes" by Kenneth R. Sivakumar
- [5] "Probability Theory" by Churchman and Carlson

References:

- [1] Churchman, C. W., & Carlson, R. P. (1969). "Exploring and evaluating decision-rules." Prentice Hall.
- [2] Freund, J. E. (2011). "Probability and statistics for scientists and engineers." Prentice Hall.
- [3] Box, G. P., & Muller, M. E. (1958). "A general distribution for mixed random variables." Annals of Mathematics Statistics, 29(2), 377-391.
- [4] Sivakumar, K. R. (2011). "Stochastic processes: An introduction." Wiley.
