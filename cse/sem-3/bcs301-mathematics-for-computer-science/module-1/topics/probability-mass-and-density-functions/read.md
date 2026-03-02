# Probability Mass and Density Functions

## Table of Contents

- [Probability Mass and Density Functions](#probability-mass-and-density-functions)
- [Overview of Probability Distributions](#overview-of-probability-distributions)
- [Probability Mass Function (PMF)](#probability-mass-function-pmf)
  - [Definition](#definition)
  - [Notation](#notation)
  - [Properties of PMF](#properties-of-pmf)
  - [Example: Coin Toss](#example-coin-toss)
- [Probability Density Function (PDF)](#probability-density-function-pdf)
  - [Definition](#definition)
  - [Notation](#notation)
  - [Properties of PDF](#properties-of-pdf)
  - [Example: Normal Distribution](#example-normal-distribution)
- [Comparing PMF and PDF](#comparing-pmf-and-pdf)
  - [Key Differences](#key-differences)
  - [Example](#example)
- [Conclusion](#conclusion)

## Overview of Probability Distributions

Probability distributions describe the likelihood of occurrence of different outcomes from random experiments. In the field of computer science, we often use probability distribution functions to model various phenomena such as errors in algorithms or the execution time of programs.

In this material, we will focus on two specific types of probability functions: **probability mass function (PMF)** and **probability density function (PDF)**.

## Probability Mass Function (PMF)

### Definition

The **Probability Mass Function** is a function that provides the probability of occurrence for each possible outcome in a discrete random variable.

- A discrete random variable has a finite number or countably infinite number of distinct values.
- PMF, denoted as \( P(X = x) \), gives the probability that the random variable X takes on the value x.

### Notation

For a discrete random variable X with possible outcomes {x1, x2, ..., xn}, its PMF is defined by:
\[ P(X = x_i) \]

### Properties of PMF

- **Non-negativity**: For any outcome \( x_i \), the probability \( P(X = x_i) \geq 0 \).
- **Normalization**: The sum of all probabilities over all possible outcomes must equal 1.
  \[ \sum\_{i=1}^{n} P(X = x_i) = 1 \]

### Example: Coin Toss

Consider a fair coin toss experiment with two possible outcomes: heads (H) and tails (T). The PMF can be defined as:
\[ P(X = H) = \frac{1}{2}, \quad P(X = T) = \frac{1}{2} \]
Where \( X \) represents the outcome of a coin toss.

## Probability Density Function (PDF)

### Definition

The **Probability Density Function** is used for continuous random variables. Unlike discrete random variables, continuous variables can take on any value within an interval.

- A continuous random variable has uncountably infinite number of possible values.
- PDF, denoted as \( f(x) \), gives the probability density that the random variable X takes on a value within a specific interval.

### Notation

For a continuous random variable X with possible outcomes in the range [a, b], its PDF is defined by:
\[ f(X = x) \]

### Properties of PDF

- **Non-negativity**: For any value \( x \), the probability density \( f(x) \geq 0 \).
- **Normalization**: The integral of the PDF over all possible values must equal 1.
  \[ \int\_{-\infty}^{\infty} f(X = x) dx = 1 \]

### Example: Normal Distribution

The normal distribution is a common continuous probability distribution. Its PDF can be expressed as:
\[ f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \]
Where \( \mu \) is the mean and \( \sigma \) is the standard deviation.

## Comparing PMF and PDF

### Key Differences

- **Domain**:
- PMF applies to discrete variables (countable outcomes).
- PDF applies to continuous variables (unbounded, non-countable values).

- **Representation**:
- PMF uses a table or list to represent probabilities for specific discrete values.
- PDF uses an equation that represents the likelihood of values within intervals.

### Example

Consider two dice rolls:

#### Discrete Case: Dice Rolls

The possible outcomes are numbers between 1 and 6. The probability mass function:
\[ P(X = x) \]
Where \( X \) is the outcome of a single die roll.

#### Continuous Case: Heights of Adult Humans

The height of adult humans can vary from approximately 4 feet to over 8 feet, making it continuous. A PDF like the normal distribution would be used here instead.

## Conclusion

Understanding probability mass and density functions is crucial in analyzing data in computer science applications such as error analysis, reliability models, and statistical models. Comprehending how these concepts apply to discrete vs. continuous variables aids in choosing appropriate tools for modeling and predicting outcomes accurately.

This material provides a comprehensive introduction to the theory of PMF and PDFs with examples to illustrate key points.
