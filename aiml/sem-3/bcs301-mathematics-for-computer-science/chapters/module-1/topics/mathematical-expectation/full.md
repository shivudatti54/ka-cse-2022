# Mathematical Expectation

### Introduction

Mathematical expectation, also known as expected value, is a fundamental concept in probability theory and statistics. It is used to measure the average value or outcome of a random variable or a set of random variables. In this topic, we will delve into the concept of mathematical expectation, its historical context, and its applications in computer science.

## History of Mathematical Expectation

The concept of mathematical expectation dates back to the 17th century when it was first introduced by French mathematician Blaise Pascal. However, it was not until the 19th century that mathematician Abraham de Moivre and mathematician Augustin-Louis Cauchy developed the concept further. The modern definition of mathematical expectation was given by mathematician Norbert Wiener in the 20th century.

## Definition of Mathematical Expectation

Mathematical expectation is defined as the long-run average value of a random variable or a set of random variables. It is calculated using the following formula:

E(X) = ∑xP(X = x)

where E(X) is the mathematical expectation, x is the value of the random variable, and P(X = x) is the probability of the random variable taking on the value x.

## Types of Mathematical Expectation

There are two types of mathematical expectation:

1. **Discrete Expectation**: This type of expectation is used when the random variable can take on only a finite number of values. The mathematical expectation is calculated using the formula:

E(X) = ∑xP(X = x)

2. **Continuous Expectation**: This type of expectation is used when the random variable can take on any value within a given range. The mathematical expectation is calculated using the formula:

E(X) = ∫xf(x)dx

where f(x) is the probability density function of the random variable.

## Properties of Mathematical Expectation

Mathematical expectation has several properties, including:

1. **Linearity**: The mathematical expectation of a linear combination of random variables is equal to the linear combination of their individual mathematical expectations.

E(aX + bY) = aE(X) + bE(Y)

2. **Homogeneity**: The mathematical expectation of a random variable is equal to the random variable multiplied by a constant.

E(cX) = cE(X)

3. **Translation**: The mathematical expectation of a random variable is equal to the random variable shifted by a constant.

E(X + c) = E(X) + c

## Calculating Mathematical Expectation

There are several methods to calculate mathematical expectation, including:

1. **Direct Calculation**: This method involves calculating the mathematical expectation directly using the formula for discrete or continuous expectation.

2. **Monte Carlo Method**: This method involves simulating the random variable many times and calculating the average value of the simulation.

3. **Analytical Methods**: This method involves using analytical techniques, such as integration, to calculate the mathematical expectation.

## Applications of Mathematical Expectation

Mathematical expectation has many applications in computer science, including:

1. **Risk Analysis**: Mathematical expectation is used to calculate the expected payout of a random variable, which can be used to analyze risk.

2. **Portfolio Optimization**: Mathematical expectation is used to calculate the expected return of a portfolio of assets, which can be used to optimize the portfolio.

3. **Machine Learning**: Mathematical expectation is used in machine learning algorithms, such as neural networks, to calculate the expected output of a model.

4. **Computer Networks**: Mathematical expectation is used to calculate the expected delay of a message in a computer network.

5. **Finance**: Mathematical expectation is used to calculate the expected return of a financial instrument, which can be used to analyze risk.

## Case Study: Calculating Mathematical Expectation

Suppose we have a random variable X that can take on values of 1, 2, or 3 with probabilities of 1/3, 1/3, and 1/3, respectively. We want to calculate the mathematical expectation of X.

Using the formula for discrete expectation, we get:

E(X) = 1(1/3) + 2(1/3) + 3(1/3)
= 1/3 + 2/3 + 1
= 8/3

This means that the expected value of X is 8/3.

## Example 1: Calculating Mathematical Expectation for a Continuous Random Variable

Suppose we have a continuous random variable X with a probability density function f(x) = 2x for 0 ≤ x ≤ 1. We want to calculate the mathematical expectation of X.

Using the formula for continuous expectation, we get:

E(X) = ∫xf(x)dx
= ∫x(2x)dx
= ∫2x^2 dx
= (2/3)x^3 |0^1
= 2/3

This means that the expected value of X is 2/3.

## Example 2: Calculating Mathematical Expectation for a Discrete Random Variable

Suppose we have a discrete random variable X with values of 0, 1, and 2 with probabilities of 1/3, 1/3, and 1/3, respectively. We want to calculate the mathematical expectation of X.

Using the formula for discrete expectation, we get:

E(X) = 0(1/3) + 1(1/3) + 2(1/3)
= 0 + 1/3 + 2/3
= 3/3
= 1

This means that the expected value of X is 1.

## Diagram: Calculating Mathematical Expectation

The following diagram illustrates the calculation of mathematical expectation for a discrete random variable.

```
  +---------------+
  |  Discrete    |
  |  Random Variable|
  +---------------+
           |
           |
           v
  +---------------+
  |  Values        |
  |  (0, 1, 2)     |
  +---------------+
           |
           |
           v
  +---------------+
  |  Probabilities  |
  |  (1/3, 1/3, 1/3)|
  +---------------+
           |
           |
           v
  +---------------+
  |  Mathematical  |
  |  Expectation  |
  |  (E(X) = 1)    |
  +---------------+
```

## Further Reading

- "Probability and Statistics for Dummies" by Jeffery Bennett
- "Introduction to Probability and Statistics" by James R. Royall
- "The Elements of Statistical Learning" by Trevor Hastie, Robert Tibshirani, and Jerome Friedman
- "Probability and Statistics for Computer Scientists" by David J. Culler
- "Mathematical Expectation" by Wikipedia
