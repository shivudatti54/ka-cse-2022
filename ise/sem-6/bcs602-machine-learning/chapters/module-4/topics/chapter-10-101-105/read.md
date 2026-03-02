# **Chapter-10: Bayesian Learning**

## **10.1 Introduction to Bayesian Learning**

Bayesian learning is a subfield of machine learning that utilizes Bayes' theorem to update the probability of a hypothesis based on new data. This approach is based on probability theory and is used to make predictions and decisions in a wide range of applications.

**Definition:**
Bayesian learning is an approach to machine learning that uses Bayes' theorem to update the probability of a hypothesis based on new data. It is based on probability theory and is used to make predictions and decisions in a wide range of applications.

## **10.2 Fundamentals of Bayes Theorem**

Bayes' theorem is a mathematical formula that describes the posterior probability of a hypothesis given new data. It is commonly used in Bayesian learning to update the probability of a hypothesis based on new data.

### Bayes' Theorem Formula:

P(H|D) = P(D|H) \* P(H) / P(D)

Where:

- P(H|D) is the posterior probability of the hypothesis given the data
- P(D|H) is the likelihood of the data given the hypothesis
- P(H) is the prior probability of the hypothesis
- P(D) is the prior probability of the data

## **10.3 Prior Probability**

The prior probability of a hypothesis is the probability of the hypothesis before any new data is observed. It is a subjective probability that is based on prior knowledge or experience.

### Example:

Suppose we want to determine the probability of a coin being heads or tails. We have no prior knowledge of the coin, so the prior probability of the coin being heads is 0.5 and the prior probability of the coin being tails is 0.5.

## **10.4 Likelihood**

The likelihood of the data given the hypothesis is the probability of observing the data if the hypothesis is true. It is a measure of how likely it is to observe the data given the hypothesis.

### Example:

Suppose we flip a coin and observe that it lands heads up. The likelihood of observing heads given that the coin is heads is 1, because if the coin is heads, it is certain to land heads up. The likelihood of observing heads given that the coin is tails is 0.5, because if the coin is tails, it is 50% likely to land heads up.

## **10.5 Posterior Probability**

The posterior probability of a hypothesis given new data is the probability of the hypothesis after observing the new data. It is calculated using Bayes' theorem.

### Example:

Suppose we have a hypothesis that a coin is biased towards heads, and we observe that it lands heads up 10 times in 20 flips. Using Bayes' theorem, we can update the prior probability of the hypothesis to be 0.7 (or 70%) and the posterior probability of the hypothesis to be 0.95 (or 95%).

**Key Concepts:**

- **Bayes' theorem**: a mathematical formula that describes the posterior probability of a hypothesis given new data
- **Prior probability**: the probability of a hypothesis before any new data is observed
- **Likelihood**: the probability of observing the data given the hypothesis
- **Posterior probability**: the probability of the hypothesis after observing the new data

**Example Problems:**

1. A coin is flipped 10 times and lands heads up 8 times. What is the prior probability of the coin being heads?
2. A coin is flipped 10 times and lands tails up 8 times. What is the likelihood of observing tails given that the coin is tails?
3. A coin is flipped 10 times and lands heads up 8 times. What is the posterior probability of the coin being heads?

**Answers:**

1. 0.8 (or 80%)
2. 0.5
3. 0.9 (or 90%)
