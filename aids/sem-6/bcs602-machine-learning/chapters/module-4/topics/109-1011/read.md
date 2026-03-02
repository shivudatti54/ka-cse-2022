# **Bayesian Learning: Introduction to Probability-based Learning, Fundamentals of Bayes Theorem**

## **10.9-10.11: Bayesian Theory and Implementation**

### Introduction

Bayesian learning is a type of machine learning that uses Bayes' theorem to update the probability of a hypothesis based on new data. In this section, we will cover the fundamentals of Bayesian theory and its implementation.

### Bayes' Theorem

**Definition**

Bayes' theorem is a mathematical formula that describes the probability of a hypothesis given some new data. It is named after Reverend Thomas Bayes, who first described it in the 18th century.

P(H|D) = P(D|H) \* P(H) / P(D)

Where:

- P(H|D) is the probability of the hypothesis given the data
- P(D|H) is the probability of the data given the hypothesis
- P(H) is the prior probability of the hypothesis
- P(D) is the probability of the data

**Explanation**

Bayes' theorem states that the probability of a hypothesis given some new data can be calculated by multiplying the probability of the data given the hypothesis by the prior probability of the hypothesis, and then dividing by the probability of the data.

For example, suppose we want to determine whether a person is likely to own a car based on their age and income. We can use Bayes' theorem to update our prior probability of owning a car based on the new data.

### Prior Probability

**Definition**

The prior probability of a hypothesis is the probability of the hypothesis before any new data is observed.

For example, suppose we have a prior probability of P(Car) = 0.5, which means that we think it is equally likely that a person owns a car or not.

### Likelihood Function

**Definition**

The likelihood function is the probability of the data given the hypothesis.

For example, suppose we have a likelihood function P(D|Car) = 0.8, which means that if a person owns a car, then the probability of them having a certain type of insurance is 0.8.

### Posterior Probability

**Definition**

The posterior probability of a hypothesis is the probability of the hypothesis given some new data.

For example, suppose we have a prior probability of P(Car) = 0.5 and a likelihood function P(D|Car) = 0.8. Using Bayes' theorem, we can calculate the posterior probability of owning a car as follows:

P(Car|D) = P(D|Car) \* P(Car) / P(D)
= 0.8 \* 0.5 / P(D)

**Key Concepts**

- **Bayes' theorem**: a mathematical formula that describes the probability of a hypothesis given some new data
- **Prior probability**: the probability of a hypothesis before any new data is observed
- **Likelihood function**: the probability of the data given the hypothesis
- **Posterior probability**: the probability of the hypothesis given some new data

### Example

Suppose we want to determine whether a person is likely to own a car based on their age and income.

- **Prior probability**: P(Car) = 0.5 (we think it is equally likely that a person owns a car or not)
- **Likelihood function**: P(D|Car) = 0.8 (if a person owns a car, then the probability of them having a certain type of insurance is 0.8)
- **Posterior probability**: P(Car|D) = 0.8 \* 0.5 / P(D)

Using this example, we can see how Bayes' theorem can be used to update our prior probability of owning a car based on new data.
