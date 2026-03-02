Of course. Here is a comprehensive educational note on Probability Mass Functions, Density Functions, and Mathematical Expectation for  Engineering students.

# Probability Distributions: PMF, PDF, and Expectation

## Introduction

In the realm of Mathematics for Computer Science, probability theory provides the fundamental language for dealing with uncertainty, randomness, and noise—elements inherent in algorithms, networks, data analysis, and machine learning. A probability distribution describes how the probabilities of a random variable are distributed over its values. To understand and work with these distributions, we need precise mathematical tools: the **Probability Mass Function (PMF)** for discrete variables and the **Probability Density Function (PDF)** for continuous variables. Building upon these, **Mathematical Expectation** gives us a way to find the average or expected value of a random variable, a crucial concept for decision-making and predictions.

## Core Concepts

### 1. Probability Mass Function (PMF)

A PMF is used for **discrete random variables**—variables whose possible values are countable (e.g., the number of packets arriving at a router, the result of a die roll, or the number of bugs in a code module).

For a discrete random variable \( X \) taking possible values \( x_1, x_2, x_3, \ldots \), the probability mass function \( p(x) \) is defined as:
\[
p(x_i) = P(X = x_i)
\]

**Properties of a PMF:**
1. **Non-negativity:** \( p(x_i) \geq 0 \) for all \( i \).
2. **Summation to 1:** The sum of all probabilities must be 1: \( \sum_{i} p(x_i) = 1 \).

**Example:** Consider the random variable \( X \) representing the outcome of a fair die roll.
The PMF is: \( p(x) = \frac{1}{6} \) for \( x = 1, 2, 3, 4, 5, 6 \), and \( p(x) = 0 \) for all other values.
You can verify: \( \sum_{x=1}^{6} p(x) = 6 \times \frac{1}{6} = 1 \).

### 2. Probability Density Function (PDF)

A PDF is used for **continuous random variables**—variables that can take an uncountable number of values within an interval (e.g., the time between two incoming network packets, the execution time of an algorithm, or the voltage level in a circuit).

For a continuous random variable \( X \), the probability density function \( f(x) \) is a function such that the probability that \( X \) falls in the interval \([a, b]\) is given by the area under the curve of \( f(x) \) from \( a \) to \( b \):
\[
P(a \leq X \leq b) = \int_{a}^{b} f(x) \, dx
\]

**Crucial Note:** For a continuous variable, \( P(X = a) = 0 \) for any specific value \( a \). Probability is only defined over an interval.

**Properties of a PDF:**
1. **Non-negativity:** \( f(x) \geq 0 \) for all \( x \).
2. **Integral to 1:** The total area under the PDF curve must be 1: \( \int_{-\infty}^{\infty} f(x) \, dx = 1 \).

**Example:** The time (in seconds) a server takes to respond is modeled by a continuous random variable with PDF \( f(x) = e^{-x} \) for \( x \geq 0 \). The probability the response takes between 1 and 2 seconds is:
\[
P(1 \leq X \leq 2) = \int_{1}^{2} e^{-x} \, dx = [-e^{-x}]_{1}^{2} = -e^{-2} + e^{-1} \approx 0.233
\]

### 3. Mathematical Expectation

The expectation, or expected value, of a random variable \( X \) is a weighted average of all its possible values, where the weights are their respective probabilities. It represents the long-run average value of the variable if the experiment is repeated infinitely.

*   **For a discrete variable** with PMF \( p(x) \):
    \[
    E[X] = \sum_{i} x_i \cdot p(x_i)
    \]
*   **For a continuous variable** with PDF \( f(x) \):
    \[
    E[X] = \int_{-\infty}^{\infty} x \cdot f(x) \, dx
    \]

Expectation is a **linear operator**. For any constants \( a \) and \( b \), and random variables \( X \) and \( Y \):
\[
E[aX + b] = aE[X] + b
\]
\[
E[X + Y] = E[X] + E[Y]
\]

**Example (Discrete):** The expected value of the fair die roll is:
\[
E[X] = \sum_{x=1}^{6} x \cdot \frac{1}{6} = \frac{1+2+3+4+5+6}{6} = 3.5
\]

**Example (Continuous):** For the server response time with PDF \( f(x) = e^{-x}, x \geq 0 \), the expected response time is:
\[
E[X] = \int_{0}^{\infty} x \cdot e^{-x} \, dx = 1 \quad \text{(using integration by parts)}
\]

## Key Points & Summary

| Concept | Applies to | Definition | Key Property |
| :--- | :--- | :--- | :--- |
| **PMF - p(x)** | Discrete RVs | \( p(x_i) = P(X = x_i) \) | \( \sum_{\text{all } i} p(x_i) = 1 \) |
| **PDF - f(x)** | Continuous RVs | \( P(a \leq X \leq b) = \int_a^b f(x)dx \) | \( \int_{-\infty}^{\infty} f(x)dx = 1 \) |
| **Expectation - E[X]** | All RVs | Average value weighted by probability | \( E[aX + b] = aE[X] + b \) (Linearity) |

*   **PMF** gives the probability at a **point**.
*   **PDF** gives the probability **density**; area under the curve between two points gives the probability.
*   **Mathematical Expectation** provides a single measure of the "center" of a distribution and is fundamental for making predictions and optimizing systems, from network throughput to algorithm performance.