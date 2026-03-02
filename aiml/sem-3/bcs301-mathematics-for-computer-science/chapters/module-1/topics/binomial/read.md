# Binomial

### Introduction

In probability theory, the binomial distribution is a discrete probability distribution of the number of successes in a sequence of n independent experiments, each asking a yes–no question and having two possible outcomes (e.g. heads or tails). The binomial distribution is often used in computer science, particularly in machine learning and data analysis.

### Definition

A binomial experiment is defined by the following characteristics:

- There are n independent trials, each with a constant probability of success p.
- Each trial has only two possible outcomes: success or failure.
- The trials are independent, meaning the outcome of one trial does not affect the outcome of another trial.

### Key Concepts

- **Probability of Success (p)**: the probability of success in a single trial.
- **Number of Trials (n)**: the number of independent trials.
- **Number of Failures (q)**: the probability of failure in a single trial, where q = 1 - p.

### Binomial Probability Mass Function

The probability mass function (PMF) of a binomial distribution is given by:

P(X = k) = (nCk) \* (p^k) \* (q^(n-k))

where:

- P(X = k) is the probability of k successes.
- nCk is the binomial coefficient, which represents the number of ways to choose k successes from n trials.
- p^k is the probability of k successes.
- q^(n-k) is the probability of n-k failures.

### Examples

- **Coin Toss**: Suppose we toss a coin 5 times, with a probability of heads being 0.5. The probability of getting exactly 3 heads is:

  P(X = 3) = (5C3) \* (0.5^3) \* (0.5^(5-3))
  = 10 \* 0.125 \* 0.0625
  = 0.15625

- **Rolling Dice**: Suppose we roll a fair six-sided dice 10 times, with a probability of rolling a 6 being 1/6. The probability of getting exactly 2 sixes is:

  P(X = 2) = (10C2) \* (1/6)^2 \* (5/6)^(10-2)
  = 45 \* (1/36) \* (5/6)^8
  = 0.1298

### Applications

- **Binary Classification**: The binomial distribution can be used to model the probability of a binary classification task, such as spam vs. non-spam emails.
- **Quality Control**: The binomial distribution can be used to model the number of defects in a production process.
- **Insurance**: The binomial distribution can be used to model the number of claims in an insurance policy.

### Software Implementation

In Python, the binomial distribution can be implemented using the `math.comb` function and the `scipy.stats.binom` class.

```python
import math
import scipy.stats

# Define the parameters
n = 10  # number of trials
p = 0.5  # probability of success

# Calculate the probability of exactly k successes
k = 3
probability = scipy.stats.binom.pmf(k, n, p)

print(f"P(X = {k}) = {probability}")
```
