# Probability Distributions: Review of Basic Probability Theory

## Table of Contents

1. [Introduction](#introduction)
2. [Historical Context](#historical-context)
3. [Basic Probability Theory](#basic-probability-theory)
   - [Random Variables](#random-variables)
   - [Probability Mass Functions](#probability-mass-functions)
   - [Probability Density Functions](#probability-density-functions)
   - [Expectation and Variance](#expectation-and-variance)
4. [Discrete Probability Distributions](#discrete-probability-distributions)
   - [Bernoulli Distribution](#bernoulli-distribution)
   - [Binomial Distribution](#binomial-distribution)
   - [Poisson Distribution](#poisson-distribution)
   - [Geometric Distribution](#geometric-distribution)
5. [Continuous Probability Distributions](#continuous-probability-distributions)
   - [Uniform Distribution](#uniform-distribution)
   - [Exponential Distribution](#exponential-distribution)
   - [Normal Distribution](#normal-distribution)
   - [Gamma Distribution](#gamma-distribution)
6. [Applications and Case Studies](#applications-and-case-studies)
7. [Modern Developments](#modern-developments)
8. [Conclusion](#conclusion)
9. [Further Reading](#further-reading)

## Introduction

Probability distributions are mathematical models that describe the likelihood of different outcomes in a random experiment. They are a fundamental concept in probability theory and have numerous applications in computer science, statistics, engineering, and other fields. In this review, we will cover the basic probability theory, discrete and continuous probability distributions, applications, and modern developments.

## Historical Context

Probability theory has a rich history that dates back to ancient civilizations. The ancient Greeks, such as Aristotle and Epicurus, discussed the concept of chance and randomness. In the 17th century, Pierre de Fermat and Blaise Pascal developed the theory of probability, which laid the foundation for modern probability theory.

In the 19th century, the development of calculus by Isaac Newton and Gottfried Wilhelm Leibniz enabled the derivation of probability distributions. The work of mathematicians such as Abraham de Moivre, Pierre-Simon Laplace, and Carl Friedrich Gauss further advanced the field of probability theory.

## Basic Probability Theory

### Random Variables

A random variable is a function that assigns a real number to each outcome of a random experiment. It can be discrete or continuous, and its value is determined by the outcome of the experiment.

### Probability Mass Functions

A probability mass function (PMF) is a function that assigns a probability to each possible outcome of a discrete random variable. It is defined as:

P(X = x) = P(x)

where P(X = x) is the probability of the outcome x.

### Probability Density Functions

A probability density function (PDF) is a function that assigns a probability to each possible outcome of a continuous random variable. It is defined as:

f(x) = P(x)

where f(x) is the probability density function of the random variable x.

### Expectation and Variance

The expectation of a random variable X, denoted by E(X), is the long-run average value of X. It is calculated as:

E(X) = ∑xP(X = x)

The variance of a random variable X, denoted by Var(X), is a measure of its spread or dispersion. It is calculated as:

Var(X) = E((X - E(X))^2)

## Discrete Probability Distributions

### Bernoulli Distribution

The Bernoulli distribution is a discrete probability distribution that models a random variable X that takes on only two values: 0 and 1. It is defined by the PMF:

P(X = 0) = p
P(X = 1) = 1 - p

where p is the probability of success.

### Binomial Distribution

The binomial distribution is a discrete probability distribution that models the number of successes in a fixed number of independent trials. It is defined by the PMF:

P(X = k) = (nCk)p^k(1-p)^(n-k)

where n is the number of trials, k is the number of successes, and p is the probability of success.

### Poisson Distribution

The Poisson distribution is a discrete probability distribution that models the number of events occurring in a fixed interval of time or space. It is defined by the PMF:

P(X = k) = (e^(-λ)λ^k)/k!

where λ is the average rate of events.

### Geometric Distribution

The geometric distribution is a discrete probability distribution that models the number of trials until the first success. It is defined by the PMF:

P(X = k) = (1-p)^k p

where p is the probability of success.

## Continuous Probability Distributions

### Uniform Distribution

The uniform distribution is a continuous probability distribution that models a random variable X that takes on values in a fixed interval. It is defined by the PDF:

f(x) = 1/(b-a)

where a and b are the lower and upper bounds of the interval.

### Exponential Distribution

The exponential distribution is a continuous probability distribution that models the time between events in a Poisson process. It is defined by the PDF:

f(x) = λe^(-λx)

where λ is the average rate of events.

### Normal Distribution

The normal distribution is a continuous probability distribution that models a random variable X that follows a Gaussian distribution. It is defined by the PDF:

f(x) = (1/σ√(2π))e^(-((x-μ)^2)/(2σ^2))

where μ is the mean and σ is the standard deviation.

### Gamma Distribution

The gamma distribution is a continuous probability distribution that models the sum of independent exponential random variables. It is defined by the PDF:

f(x) = (1/Γ(α))x^(α-1)e^(-x/β)

where α is the shape parameter and β is the scale parameter.

## Applications and Case Studies

### Coin Tosses

Consider a fair coin toss. The outcome can be heads or tails, each with a probability of 0.5. We can model this using a Bernoulli distribution with p = 0.5.

### Medical Trials

Suppose we conduct a medical trial to test the effectiveness of a new treatment. We want to know the probability that the treatment is effective. We can model this using a binomial distribution with n trials and p = 0.5.

### Stock Prices

Suppose we want to model the stock price of a company. We can use a normal distribution with mean μ and standard deviation σ.

## Modern Developments

### Monte Carlo Methods

Monte Carlo methods are a class of numerical algorithms that rely on random sampling to solve mathematical problems. They are widely used in finance, engineering, and computer science.

### Bayesian Statistics

Bayesian statistics is a branch of statistics that combines probability theory and statistics to model complex data. It is widely used in machine learning, data analysis, and artificial intelligence.

## Conclusion

Probability distributions are a fundamental concept in probability theory and have numerous applications in computer science, statistics, engineering, and other fields. In this review, we covered the basic probability theory, discrete and continuous probability distributions, applications, and modern developments.

## Further Reading

- [Kendall and Babkin, 1943] Kendall, N. G., & Babkin, B. (1943). A Course in the Theory of Statistics. Hafner Publishing Company.
- [Karlin and Rubin, 1956] Karlin, S., & Rubin, H. (1956). The Theory of Statistics. Prentice-Hall.
- [Feller, 1966] Feller, W. (1966). An Introduction to Probability Theory and Its Applications. John Wiley & Sons.
- [Ross, 2014] Ross, S. (2014). Simulation. Academic Press.
- [Gilks et al., 2019] Gilks, W. R., et al. (2019). Bayesian Statistics and Machine Learning. John Wiley & Sons.
