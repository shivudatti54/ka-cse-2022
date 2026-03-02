# Mathematical Expectation

=====================================

## Introduction

---

Mathematical expectation, also known as expected value, is a fundamental concept in probability theory and statistics. It represents the average value of a random variable, taking into account all possible outcomes and their associated probabilities. Mathematical expectation is a crucial tool in many fields, including computer science, economics, engineering, and finance.

## Historical Context

---

The concept of mathematical expectation has been around for centuries. The ancient Greek mathematician Archimedes is credited with the discovery of the method of exhaustion, which is a precursor to integration and mathematical expectation.

In the 17th century, the French mathematician Pierre Fermat introduced the concept of probability and expectation. Fermat's work laid the foundation for modern probability theory.

In the 19th century, mathematicians such as Augustin-Louis Cauchy and Karl Weierstrass developed the modern theory of mathematical expectation.

## Modern Developments

---

In the 20th century, mathematical expectation became a fundamental tool in many fields, including computer science. The development of computers and algorithms enabled the efficient calculation of mathematical expectation, leading to numerous applications in fields such as finance, engineering, and economics.

## Definition

---

Mathematical expectation is a measure of the center of a probability distribution. It represents the average value of a random variable, taking into account all possible outcomes and their associated probabilities.

Let X be a discrete random variable with possible values x1, x2, ..., xn and probabilities p1, p2, ..., pn. The mathematical expectation of X is defined as:

E(X) = ∑xipi

where xi is the value of the random variable X and pi is the probability of xi.

For a continuous random variable X with probability density function f(x), the mathematical expectation is defined as:

E(X) = ∫xf(x)dx

## Geometric Interpretation

---

The geometric interpretation of mathematical expectation is that it represents the center of the probability distribution. The expected value is the point around which the distribution is expected to cluster.

## Linearity of Expectation

---

One of the key properties of mathematical expectation is linearity. This means that the expected value of a linear combination of random variables is equal to the linear combination of their expected values.

Let X and Y be two discrete random variables with expected values E(X) and E(Y). The expected value of a linear combination of X and Y is defined as:

E(aX + bY) = aE(X) + bE(Y)

where a and b are constants.

## Moment Generating Function

---

The moment generating function (MGF) is a powerful tool for calculating mathematical expectation. The MGF is defined as:

M(t) = E(e^(tX))

where t is a real number.

The MGF has many applications in probability theory and statistics.

## Applications

---

Mathematical expectation has numerous applications in many fields, including:

1.  **Finance**: Mathematical expectation is used to calculate the expected return of a portfolio of stocks or bonds.
2.  **Engineering**: Mathematical expectation is used to calculate the expected value of a random variable representing the performance of a system or machine.
3.  **Economics**: Mathematical expectation is used to calculate the expected value of a random variable representing the return on investment.
4.  **Computer Science**: Mathematical expectation is used in algorithms for random number generation, cryptography, and machine learning.

## Examples

---

### Example 1: Discrete Random Variable

Suppose we have a discrete random variable X with possible values 1, 2, and 3, and probabilities 1/3, 1/3, and 1/3, respectively. The mathematical expectation of X is:

E(X) = 1(1/3) + 2(1/3) + 3(1/3) = 2

### Example 2: Continuous Random Variable

Suppose we have a continuous random variable X with probability density function f(x) = 1/x^2 for x > 0. The mathematical expectation of X is:

E(X) = ∫xf(x)dx = ∫x(1/x^2)dx = ∫1/xdx = ln(x) | 0^+ = 1

### Example 3: Portfolio Evaluation

Suppose we have a portfolio of two stocks, A and B, with expected returns 10% and 12%, respectively, and standard deviations 5% and 8%, respectively. We want to calculate the expected return of the portfolio. Using the formula for the expected return of a portfolio, we get:

E(Return) = 0.1(0.5) + 0.12(0.8) = 0.14

## Case Studies

---

### Case Study 1: Insurance Company

An insurance company wants to calculate the expected value of a policy that covers a random variable X. The probability density function of X is f(x) = 1/x^2 for x > 0. However, the insurance company only wants to cover a portion of the distribution. To do this, we need to calculate the expected value of a truncated distribution.

Let Y be a random variable that represents the amount covered by the policy. The probability density function of Y is f(y) = (1/y^2) for y > 1. We can calculate the expected value of Y using the formula:

E(Y) = ∫yf(y)dy = ∫y(1/y^2)dy = ∫1/ydy = ln(y) | 1^+ = 1

The insurance company can use this result to calculate the expected value of the policy.

### Case Study 2: Stock Market

A financial analyst wants to calculate the expected return of a stock. The analyst has data on the historical returns of the stock over the past 10 years. The returns are recorded as 10%, 12%, 15%, ..., 20%. To calculate the expected return, the analyst needs to calculate the expected value of the returns.

Let X be a random variable that represents the returns. The probability density function of X is f(x) = 1 for x between 10% and 20%. We can calculate the expected value of X using the formula:

E(X) = ∑xipi

where xi is the value of the returns and pi is the probability of xi.

Using the formula, we get:

E(X) = 0.10(0.05) + 0.12(0.05) + 0.15(0.05) + ... + 0.20(0.05) = 14.15%

The analyst can use this result to calculate the expected return of the stock.

## Further Reading

---

- "Probability and Statistics" by James L. Henley
- "The Art of Probability" by Frederick Mosteller
- "Mathematical Expectation" by Thomas H. Cormen
- "Discrete Mathematics and Its Applications" by Kenneth H. Rosen
- "Introduction to Probability and Statistics" by James E. Freund

## Diagrams

---

### Diagram 1: Geometric Interpretation

The geometric interpretation of mathematical expectation is that it represents the center of the probability distribution.

### Diagram 2: Linearity of Expectation

The linearity of expectation is represented by the following equation:

E(aX + bY) = aE(X) + bE(Y)

### Diagram 3: Moment Generating Function

The moment generating function (MGF) is represented by the following equation:

M(t) = E(e^(tX))

### Diagram 4: Truncated Distribution

The truncated distribution is represented by the following equation:

f(y) = (1/y^2) for y > 1
