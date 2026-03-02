# Mathematical Expectation

## Table of Contents

- [Mathematical Expectation](#mathematical-expectation)
- [Definition and Basic Concepts of Mathematical Expectation](#definition-and-basic-concepts-of-mathematical-expectation)
  - [Definition:](#definition)
  - [Properties of Mathematical Expectation:](#properties-of-mathematical-expectation)
  - [Examples and Applications](#examples-and-applications)
  - [Exercises](#exercises)
- [Expectation in More Complex Scenarios](#expectation-in-more-complex-scenarios)
  - [Conditional Mathematical Expectation](#conditional-mathematical-expectation)
  - [Variance and Standard Deviation](#variance-and-standard-deviation)
- [Summary](#summary)

## Definition and Basic Concepts of Mathematical Expectation

Mathematical expectation, also known as expected value or mean, is a fundamental concept in probability theory. It quantifies the average outcome of an experiment over many trials.

### Definition:

The mathematical expectation (or expected value) of a discrete random variable \(X\) with possible values \(x_1, x_2, \ldots, x_n\) and corresponding probabilities \(P(X = x_i)\) is given by:

\[
E[X] = \sum\_{i=1}^{n} x_i P(X = x_i)
\]

or for a continuous random variable with probability density function (pdf) \(f(x)\):

\[
E[X] = \int\_{-\infty}^{\infty} x f(x) dx
\]

### Properties of Mathematical Expectation:

1. **Linearity**:

- For any two random variables \(X\) and \(Y\), and constants \(a\) and \(b\):
  \[
  E[aX + bY] = aE[X] + bE[Y]
  \]

2. **Expected Value of Sum**:

- For any two random variables \(X\) and \(Y\) (independence is NOT required):
  \[
  E[X + Y] = E[X] + E[Y]
  \]
- Note: Independence IS required for \(E[XY] = E[X] \cdot E[Y]\), but NOT for sums.

3. **Non-Negativity**:

- For any random variable \(X\), if \(P(X \geq 0) = 1\):
  \[
  E[X] \geq 0
  \]

### Examples and Applications

#### Example 1: Discrete Random Variable

Consider a game where you roll two six-sided dice. Let \(X\) be the sum of the numbers on the top faces.

- Possible values for \(X\): \(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\)
- Probabilities:
- Probability of getting a sum of 2: \(\frac{1}{36}\) (only one way to get this: \(1+1\))
- Probability of getting a sum of 3: \(\frac{2}{36} = \frac{1}{18}\) (two ways to get this: \(1+2, 2+1\))

Calculate the expected value:
\[
E[X] = 2 \cdot \frac{1}{36} + 3 \cdot \frac{2}{36} + 4 \cdot \frac{3}{36} + 5 \cdot \frac{4}{36} + 6 \cdot \frac{5}{36} + 7 \cdot \frac{6}{36} + 8 \cdot \frac{5}{36} + 9 \cdot \frac{4}{36} + 10 \cdot \frac{3}{36} + 11 \cdot \frac{2}{36} + 12 \cdot \frac{1}{36}
\]
\[
= \frac{2 + 6 + 12 + 20 + 30 + 42 + 40 + 36 + 30 + 22 + 12}{36} = \frac{252}{36} = 7
\]

Therefore, the expected sum when rolling two dice is **7**.

#### Example 2: Continuous Random Variable

Suppose \(X\) is a continuous random variable with probability density function:
\[
f(x) =
\begin{cases}
\frac{1}{4}, & \text{if } x \in [0,4] \\
0, & \text{otherwise}
\end{cases}
\]

Calculate the expected value \(E[X]\):
\[
E[X] = \int\_{-\infty}^{\infty} x f(x) dx = \int_0^4 x \cdot \frac{1}{4} dx
\]
\[
= \frac{1}{4} \left[ \frac{x^2}{2} \right]\_0^4 = \frac{1}{4} \left( \frac{16}{2} - 0 \right) = 2
\]

### Exercises

1. **Expected Value of a Simple Random Variable**:

- Suppose \(X\) is the outcome of rolling a six-sided die, where \(P(X = x_i)\) are uniformly distributed.
- Calculate \(E[X]\).

2. **Application in Computer Science**:

- Consider an algorithm that generates random numbers between 0 and 1 using a uniform distribution. Compute its expected value.

## Expectation in More Complex Scenarios

### Conditional Mathematical Expectation

In certain scenarios, we might want to calculate the expectation of \(X\) given another random variable \(Y\):
\[
E[X \mid Y = y]
\]

This is defined as:
\[
E[X \mid Y = y] = \sum\_{i} x_i P(X = x_i \mid Y = y)
\]

### Variance and Standard Deviation

Variance measures the spread of a distribution around its mean. It is given by:

\[
Var(X) = E[(X - E[X])^2]
\]

Standard deviation is simply the square root of variance.

## Summary

Mathematical expectation, or expected value, is crucial in probability theory and has numerous applications in computer science, including algorithm analysis, simulations, and machine learning. Understanding how to calculate and apply mathematical expectations can help you make informed decisions based on probabilities and predict outcomes more accurately.
