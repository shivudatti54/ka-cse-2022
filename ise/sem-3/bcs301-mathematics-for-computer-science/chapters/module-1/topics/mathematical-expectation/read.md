# **Mathematical Expectation**

## **Introduction**

Mathematical expectation, also known as expected value, is a fundamental concept in probability theory that quantifies the average value of a random variable. It is a measure of the center of the distribution, and it is used to make predictions and decisions under uncertainty.

## **Definition**

The mathematical expectation of a random variable X, denoted by E(X), is defined as the sum of the product of each possible value of X and its probability:

E(X) = ∑xP(X=x)

where x is the possible value of X and P(X=x) is the probability of X taking on that value.

## **Properties**

- Linearity: E(aX + b) = aE(X) + b, where a and b are constants.
- Independence: E(X1 \* X2) = E(X1) \* E(X2), where X1 and X2 are independent random variables.
- Normalization: E(1) = 1, where 1 is the constant random variable that takes on the value 1 with probability 1.

## **Types of Expectation**

- **Discrete Expectation**: For a discrete random variable X, the expectation is calculated as the sum of the product of each possible value of X and its probability.
- **Continuous Expectation**: For a continuous random variable X, the expectation is calculated as the integral of the product of the function f(x) and the probability density function (pdf) of X.

## **Calculating Mathematical Expectation**

### Discrete Expectation

Let's consider a discrete random variable X that can take on the values 1, 2, and 3 with probabilities 1/4, 1/2, and 1/4, respectively.

To calculate the mathematical expectation of X, we multiply each possible value of X by its probability and sum the results:

E(X) = 1 \* (1/4) + 2 \* (1/2) + 3 \* (1/4)
= 1/4 + 1 + 3/4
= 2

### Continuous Expectation

Let's consider a continuous random variable X with a probability density function (pdf) f(x) = 2x, 0 ≤ x ≤ 1.

To calculate the mathematical expectation of X, we integrate the product of the function f(x) and the pdf of X:

E(X) = ∫[0,1] x \* 2x dx
= ∫[0,1] 2x^2 dx
= (2/3)x^3 | [0,1]
= (2/3)

## **Numerical Examples**

### Example 1: Discrete Expectation

Suppose we have a coin that lands on heads with probability 1/2 and tails with probability 1/2. If we flip the coin three times, what is the expected number of heads?

Let X be the random variable that represents the number of heads. X can take on the values 0, 1, 2, or 3. The probability of X taking on each value is as follows:

- P(X=0) = 1/8
- P(X=1) = 3/8
- P(X=2) = 3/8
- P(X=3) = 1/8

To calculate the mathematical expectation of X, we multiply each possible value of X by its probability and sum the results:

E(X) = 0 \* (1/8) + 1 \* (3/8) + 2 \* (3/8) + 3 \* (1/8)
= 0 + 3/8 + 6/8 + 3/8
= 6/4
= 1.5

### Example 2: Continuous Expectation

Suppose we have a random variable X that represents the height of a person in inches, measured with a standard error of 2 inches. If the height of a person is normally distributed with a mean of 68 inches and a standard deviation of 4 inches, what is the expected value of the height?

The probability density function (pdf) of X is given by:

f(x) = (1/√(2π\*16)) \* e^(-(x-68)^2/32)

To calculate the mathematical expectation of X, we integrate the product of the function f(x) and the pdf of X:

E(X) = ∫[0,∞] x \* (1/√(2π\*16)) \* e^(-(x-68)^2/32) dx

This integral can be solved numerically to give the expected value of the height.
