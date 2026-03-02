# **Random Variables (Discrete and Continuous)**

## **Introduction**

In probability theory, a random variable is a function that assigns a real value to each outcome of a random experiment. It is a mathematical representation of the uncertainty associated with a random event. In this study material, we will explore both discrete and continuous random variables.

## **Discrete Random Variables**

### Definition

A discrete random variable is a random variable that can take on a finite or countable number of distinct values.

### Properties

- Each outcome of the random experiment corresponds to a single value.
- The set of possible outcomes is countable.
- The probability of each outcome is non-negative.

### Examples

- A coin toss can result in either heads (H) or tails (T), which are two distinct outcomes.
- A roll of a fair six-sided die can result in a value between 1 and 6, which are six distinct outcomes.

### Types of Discrete Random Variables

- **Bernoulli Random Variable**: A discrete random variable that can take on only two values, typically 0 and 1.
- **Binomial Random Variable**: A discrete random variable that represents the number of successes in a fixed number of independent trials.
- **Poisson Random Variable**: A discrete random variable that represents the number of events occurring in a fixed interval of time or space.

### Key Concepts

- **Mean (μ)**: The expected value of the random variable.
- **Variance (σ^2)**: The average of the squared differences between each outcome and the mean.
- **Standard Deviation (σ)**: The square root of the variance.

### Example

Consider a fair six-sided die. Let X be the random variable representing the outcome of a single roll. The possible outcomes are 1, 2, 3, 4, 5, and 6. The probability of each outcome is 1/6. The mean of the random variable is:

μ = (1 + 2 + 3 + 4 + 5 + 6) / 6 = 21/6 = 3.5

The variance of the random variable is:

σ^2 = [(1 - 3.5)^2 + (2 - 3.5)^2 + (3 - 3.5)^2 + (4 - 3.5)^2 + (5 - 3.5)^2 + (6 - 3.5)^2] / 6
= [(2.5)^2 + (1.5)^2 + (0.5)^2 + (0.5)^2 + (1.5)^2 + (2.5)^2] / 6
= 15.5 / 6
= 2.58

The standard deviation of the random variable is:

σ = √(2.58) ≈ 1.6

## **Continuous Random Variables**

### Definition

A continuous random variable is a random variable that can take on any value within a given interval or range.

### Properties

- Each outcome of the random experiment corresponds to a continuous interval.
- The set of possible outcomes is uncountable.
- The probability of each outcome is non-negative.

### Examples

- The height of a person can be any value within a given range, such as 0 to 2 meters.
- The time it takes to complete a task can be any value within a given range, such as 1 to 10 minutes.

### Types of Continuous Random Variables

- **Uniform Random Variable**: A continuous random variable that has a uniform probability distribution over a given interval.
- **Normal Random Variable**: A continuous random variable that has a normal probability distribution, also known as a Gaussian distribution.
- **Exponential Random Variable**: A continuous random variable that has an exponential probability distribution.

### Key Concepts

- **Mean (μ)**: The expected value of the random variable.
- **Variance (σ^2)**: The average of the squared differences between each outcome and the mean.
- **Standard Deviation (σ)**: The square root of the variance.

### Example

Consider a normal random variable X with a mean of 5 and a standard deviation of 2. The probability density function of the random variable is:

f(x) = (1/√(2π)) \* e^(-(x-5)^2 / (2 \* 2^2))

The probability of X being between 3 and 7 is:

P(3 < X < 7) = ∫[3,7] f(x) dx
= ∫[3,7] (1/√(2π)) \* e^(-(x-5)^2 / 8) dx
= 0.5

In conclusion, random variables are a fundamental concept in probability theory, and understanding both discrete and continuous random variables is essential for modeling and analyzing real-world phenomena.
