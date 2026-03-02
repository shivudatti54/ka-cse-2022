# **Probability Mass and Density Functions**

## **Introduction**

Probability mass and density functions are fundamental concepts in probability theory, used to describe random variables and their associated probabilities. In this section, we will explore the definitions, properties, and uses of these functions.

## **Probability Mass Function (PMF)**

A probability mass function (PMF) is a function that assigns a probability to each possible outcome of a discrete random variable.

### Definition

A random variable X is said to have a probability mass function PMF(x) if:

- PMF(x) is a function that maps each possible value of X to a non-negative real number (the probability)
- PMF(x) is defined for all possible values of X
- ∑PMF(x) = 1, where the sum is taken over all possible values of X

### Properties

- PMF(x) is a discrete function, meaning it takes on a finite number of values
- PMF(x) is non-negative, meaning PMF(x) ≥ 0 for all possible values of X
- PMF(x) is a probability distribution, meaning ∑PMF(x) = 1

### Examples

- A fair six-sided die has the following PMF:
  - P(X=1) = 1/6
  - P(X=2) = 1/6
  - P(X=3) = 1/6
  - P(X=4) = 1/6
  - P(X=5) = 1/6
  - P(X=6) = 1/6

- A coin toss has the following PMF:
  - P(X=0) = 0.5 (heads)
  - P(X=1) = 0.5 (tails)

## **Probability Density Function (PDF)**

A probability density function (PDF) is a function that assigns a probability density to each possible outcome of a continuous random variable.

### Definition

A random variable X is said to have a probability density function PDF(x) if:

- PDF(x) is a function that maps each possible value of X to a non-negative real number (the probability density)
- PDF(x) is defined for all possible values of X
- ∫PDF(x)dx = 1, where the integral is taken over all possible values of X

### Properties

- PDF(x) is a continuous function, meaning it takes on all real values between 0 and ∞
- PDF(x) is non-negative, meaning PDF(x) ≥ 0 for all possible values of X
- PDF(x) is a probability distribution, meaning ∫PDF(x)dx = 1

### Examples

- A normal distribution with mean 0 and variance 1 has the following PDF:
  - PDF(x) = (1/√(2π)) \* e^(-x^2/2) for all real x
- An exponential distribution with rate parameter λ has the following PDF:
  - PDF(x) = λ \* e^(-λx) for all x ≥ 0

## **Key Concepts**

- **Discrete random variable**: a random variable that takes on a finite number of values
- **Continuous random variable**: a random variable that takes on all real values between 0 and ∞
- **Probability mass function (PMF)**: a function that assigns a probability to each possible outcome of a discrete random variable
- **Probability density function (PDF)**: a function that assigns a probability density to each possible outcome of a continuous random variable
- **Non-negative**: a function or value that is greater than or equal to 0
- **Non-increasing**: a function that decreases as x increases
- **Non-decreasing**: a function that increases as x increases

## **Applications**

- **Random sampling**: PMFs are used to describe the distribution of random samples from a population
- **Random experiments**: PDFs are used to describe the probability of different outcomes in a random experiment
- **Quantitative risk analysis**: PMFs and PDFs are used to describe the probability of different outcomes in a quantitative risk analysis
- **Machine learning**: PMFs and PDFs are used in machine learning algorithms to describe the distribution of data.
