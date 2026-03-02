# Probability Mass Functions, Density Functions, and Mathematical Expectation

## Introduction

In the realm of Mathematics for Computer Science, probability theory provides the foundational language for dealing with uncertainty. This is critical for fields like machine learning, randomized algorithms, network analysis, and performance modeling. Two fundamental concepts to master are the **Probability Mass Function (PMF)** for discrete data and the **Probability Density Function (PDF)** for continuous data. Closely related is the concept of **Mathematical Expectation**, which provides a measure of the "center" or average value of a random variable. This module will explore these core ideas in detail.

## Core Concepts

### 1. Probability Mass Function (PMF)

A **Probability Mass Function** is used for **discrete random variables**—variables whose possible values can be counted (e.g., the number of heads in coin tosses, the number of packets arriving at a router, or the roll of a die).

**Definition:** The PMF, often denoted as $p_X(x)$ or simply $P(X=x)$, gives the probability that a discrete random variable $X$ takes on a specific value $x$.
$$ p_X(x) = P(X = x) $$

**Properties of a PMF:**

1.  $0 \leq p_X(x) \leq 1$ for any value $x$.
2.  The sum of probabilities over all possible values must equal 1: $\sum_{\text{all } x} p_X(x) = 1$.

**Example:** Consider the random variable $X$ representing the outcome of a fair six-sided die roll. The PMF is:
$p_X(x) = P(X = x) = \frac{1}{6}$ for $x = 1, 2, 3, 4, 5, 6$.

We can represent this in a table:
| $x$ | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $p_X(x)$ | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 |

### 2. Probability Density Function (PDF)

A **Probability Density Function** is used for **continuous random variables**—variables that can take on an uncountably infinite number of values within an interval (e.g., the time between two interrupts, the height of a student, or the voltage in a circuit).

**Definition:** The PDF, denoted as $f_X(x)$, is a function such that the probability that $X$ falls in any interval $[a, b]$ is found by integrating the PDF over that interval.
$$ P(a \leq X \leq b) = \int\_{a}^{b} f_X(x) dx $$

**Crucial Note:** For a continuous random variable, $P(X = x) = 0$ for any specific point $x$. Probability is only defined over intervals. The PDF itself **is not a probability**; it is a density. The area under the curve of the PDF represents probability.

**Properties of a PDF:**

1.  $f_X(x) \geq 0$ for all $x$.
2.  The total area under the entire PDF curve must be 1: $\int_{-\infty}^{\infty} f_X(x)  dx = 1$.

**Example:** The time (in hours) a server runs before failure, $T$, follows an exponential distribution with parameter $\lambda = 0.5$. Its PDF is:
$f_T(t) = 0.5e^{-0.5t}$ for $t \geq 0$ (and 0 otherwise).
The probability the server fails between 1 and 2 hours is:
$P(1 \leq T \leq 2) = \int_{1}^{2} 0.5e^{-0.5t}  dt \approx 0.1447$.

### 3. Mathematical Expectation (Expected Value)

The **Mathematical Expectation** or **Expected Value** of a random variable $X$ is its long-term average value. It is a weighted average of all possible values, where the weights are their respective probabilities.

**For a Discrete Random Variable:**
$$ E[X] = \sum\_{\text{all } x} x \cdot p_X(x) $$

**For a Continuous Random Variable:**
$$ E[X] = \int\_{-\infty}^{\infty} x \cdot f_X(x) dx $$

The expectation is a linear operator. For any constants $a$ and $b$ and random variables $X$ and $Y$:
$$ E[aX + b] = aE[X] + b $$
$$ E[X + Y] = E[X] + E[Y] $$

**Example (Discrete):** For the fair die roll, the expected value is:
$E[X] = (1)(\frac{1}{6}) + (2)(\frac{1}{6}) + (3)(\frac{1}{6}) + (4)(\frac{1}{6}) + (5)(\frac{1}{6}) + (6)(\frac{1}{6}) = 3.5$

**Example (Continuous):** For a random variable $X$ uniformly distributed on $[a, b]$ (PDF: $f_X(x) = \frac{1}{b-a}$ for $a \leq x \leq b$), the expected value is:
$E[X] = \int_{a}^{b} x \cdot \frac{1}{b-a}  dx = \frac{a + b}{2}$
This correctly gives the midpoint of the interval.

## Key Points & Summary

| Feature               | Probability Mass Function (PMF) | Probability Density Function (PDF)                |
| :-------------------- | :------------------------------ | :------------------------------------------------ |
| **Variable Type**     | Discrete                        | Continuous                                        |
| **Gives Probability** | $P(X=x)$ directly               | $P(a \leq X \leq b)$ via **area** under the curve |
| **Key Property**      | $\sum p_X(x) = 1$               | $\int f_X(x) dx = 1$                              |
| **Expectation**       | $E[X] = \sum x \cdot p_X(x)$    | $E[X] = \int x \cdot f_X(x) dx$                   |

- **PMF** is for countable outcomes; it gives the probability at a point.
- **PDF** is for measured outcomes; the area under its curve within an interval gives probability.
- **Mathematical Expectation** ($E[X]$) is the theoretical average and a fundamental measure of the center of a distribution. Its linearity property is extremely powerful for solving complex problems.
- Mastering these functions and the concept of expectation is essential for progressing to more advanced topics like variance, moment generating functions, and stochastic processes.
