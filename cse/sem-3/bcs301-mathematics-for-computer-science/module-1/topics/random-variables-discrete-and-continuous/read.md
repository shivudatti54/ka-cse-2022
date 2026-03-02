# Random Variables (Discrete and Continuous)

## Table of Contents

- [Random Variables (Discrete and Continuous)](#random-variables-discrete-and-continuous)
- [Introduction to Probability Distributions](#introduction-to-probability-distributions)
  - [Definition of Probability Distribution](#definition-of-probability-distribution)
- [Random Variables: Discrete vs Continuous](#random-variables-discrete-vs-continuous)
  - [Discrete Random Variables](#discrete-random-variables)
  - [Continuous Random Variables](#continuous-random-variables)
- [Probability Distributions for Discrete Random Variables](#probability-distributions-for-discrete-random-variables)
  - [Binomial Distribution](#binomial-distribution)
  - [Poisson Distribution](#poisson-distribution)
- [Probability Distributions for Continuous Random Variables](#probability-distributions-for-continuous-random-variables)
  - [Normal Distribution (Gaussian Distribution)](#normal-distribution-gaussian-distribution)
  - [Exponential Distribution](#exponential-distribution)
  - [Example: Time Between Customer Arrivals](#example-time-between-customer-arrivals)
- [Conclusion and Next Steps](#conclusion-and-next-steps)

## Introduction to Probability Distributions

Probability distributions are fundamental to understanding how randomness affects our data. They provide us with a framework to predict outcomes of random events, making them essential tools for modeling uncertainty in computer science applications.

### Definition of Probability Distribution

A probability distribution is a function that provides the probability of occurrence for different possible values of an event. For random variables (discrete or continuous), we define such distributions over their respective sample spaces.

## Random Variables: Discrete vs Continuous

In this section, we introduce two types of random variables - discrete and continuous.

### Discrete Random Variables

A discrete random variable takes on distinct, separate values within its domain. These values are often integers (whole numbers), or categories like "Yes" or "No." The probability distribution function describes the likelihood of each value occurring.

#### Key Concepts for Discrete RVs:

- **Support**: The set of all possible values taken by a discrete random variable.
- **Probability Mass Function (PMF)**: Represents the probability that the discrete random variable takes on any particular value in its support. Mathematically, \( P(X = x_i) \).

#### Example: Coin Toss

If we flip a coin and count the number of heads as our outcome, this is a simple example of a discrete random variable (the possible values are 0 or 1).

### Continuous Random Variables

A continuous random variable can take on any value within an interval. This type of randomness often arises when measuring physical quantities like height, weight, temperature, etc., where the results vary continuously.

#### Key Concepts for Continuous RVs:

- **Support**: The set of all possible values that a continuous random variable can take.
- **Probability Density Function (PDF)**: Unlike discrete distributions which use PMFs, continuous distributions describe probabilities over intervals rather than specific points.

#### Example: Heights and Weights

Height or weight measurements are often modeled as continuous RVs because these quantities can vary continuously within reasonable bounds.

## Probability Distributions for Discrete Random Variables

### Binomial Distribution

The binomial distribution describes the probability of having exactly \(k\) successes in \(n\) independent trials, where each trial has two possible outcomes and a constant success probability. Commonly used when we are interested in the number of times an event happens within a fixed number of attempts.

#### Formula:

\[ P(X = k) = \binom{n}{k} p^k (1-p)^{n-k} \]

Where:

- \( n \): Number of trials
- \( p \): Probability of success on each trial
- \( \binom{n}{k} \): Binomial coefficient

#### Example: Coin Toss Experiment

If you flip a coin 5 times and want to find the probability that it lands heads up exactly 3 times, this would be modeled using the binomial distribution.

### Poisson Distribution

The Poisson distribution models the number of events (occurrences) in a fixed interval of time or space. It is often used to model rare events like customer arrivals at a store or failures occurring during a certain period.

#### Formula:

\[ P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!} \]

Where:

- \( \lambda \): Average number of events expected in the interval
- \( e \): Base of natural logarithm (approximately 2.71828)

#### Example: Customer Arrivals at Store

If we know that, on average, there are 2 customers arriving at a store every hour, what is the probability that exactly 3 customers arrive within one hour?

## Probability Distributions for Continuous Random Variables

### Normal Distribution (Gaussian Distribution)

The normal distribution or Gaussian distribution is often used to model real-world phenomena such as heights and weights. It is characterized by its bell-shaped curve.

#### Formula:

\[ f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \]

Where:

- \( \mu \): Mean
- \( \sigma \): Standard deviation

#### Properties of Normal Distribution:

- Symmetrical and centered at the mean.
- Empirical Rule: Approximately 68% of data falls within one standard deviation, approximately 95% within two standard deviations, and approximately 99.7% within three.

### Exponential Distribution

The exponential distribution describes the time between events in a Poisson point process, i.e., the time (or interval) that elapses before some event occurs.

#### Formula:

\[ f(x) = \lambda e^{-\lambda x} \]

Where:

- \( \lambda > 0 \): Rate parameter; measure of frequency.

### Example: Time Between Customer Arrivals

If the average number of customers arriving at a store is 2 per hour, we can use an exponential distribution to model the time between arrivals (the interarrival times).

## Conclusion and Next Steps

Understanding the different types of probability distributions for both discrete and continuous random variables is crucial in various applications within computer science. This knowledge forms the basis for more advanced concepts like hypothesis testing or machine learning algorithms that make probabilistic predictions.

In subsequent studies, we will explore how these distributions are used in more complex models and computational methods to analyze data with uncertainty.
