# Probability Distributions: Mass, Density, and Expectation

**Subject:** Mathematics for Computer Science
**Module:** Module 1: Probability Distributions
**Topic:** Probability Mass and Density Functions & Mathematical Expectation

## Introduction

Probability theory is the bedrock of numerous computer science fields, from designing randomized algorithms and machine learning models to analyzing network traffic and performance. At the heart of this theory lie probability distributions, which describe how probabilities are distributed over the values of a random variable. Understanding the two fundamental types of functions that define these distributions—the Probability Mass Function (PMF) for discrete data and the Probability Density Function (PDF) for continuous data—is crucial. Furthermore, the concept of **Mathematical Expectation** provides a powerful tool to summarize these distributions into a single, predictive value, such as the long-term average.

## Core Concepts

### 1. Probability Mass Function (PMF)

A **PMF** applies to **discrete random variables**—variables whose possible values can be counted (e.g., the number of heads in 10 coin tosses, the number of packets arriving at a router per second).

*   **Definition:** The PMF, denoted as $p_X(x)$ or simply $P(X=x)$, gives the probability that a discrete random variable $X$ takes on a specific value $x$.
    $$p_X(x) = P(X = x)$$

*   **Properties:**
    1.  $0 \leq p_X(x) \leq 1$ for every possible value $x$.
    2.  $\sum_{\text{all } x} p_X(x) = 1$ (The sum of all probabilities must be 1).

**Example:** Consider the random variable $X$ representing the outcome of a fair six-sided die roll. Its PMF is:
$$p_X(x) = P(X = x) = \frac{1}{6}, \quad \text{for } x = 1, 2, 3, 4, 5, 6$$

### 2. Probability Density Function (PDF)

A **PDF** applies to **continuous random variables**—variables that can take on any value within an interval (e.g., the time between two incoming network requests, the height of a student).

*   **Definition:** The PDF, denoted as $f_X(x)$, defines the relative likelihood for a continuous random variable $X$ to take on a given value. **Crucially, the probability at a single point is zero** ($P(X = a) = 0$). Probability is instead defined over an interval.
    $$P(a \leq X \leq b) = \int_a^b f_X(x)  dx$$

*   **Properties:**
    1.  $f_X(x) \geq 0$ for all $x$ (Density is never negative).
    2.  $\int_{-\infty}^{\infty} f_X(x)  dx = 1$ (The total area under the curve is 1).

**Example:** Suppose the time (in seconds) for a server to respond, $T$, is modeled by the PDF $f_T(t) = 0.5e^{-0.5t}$ for $t \geq 0$. The probability the response takes between 1 and 3 seconds is:
$$P(1 \leq T \leq 3) = \int_1^3 0.5e^{-0.5t}  dt \approx 0.383$$

### 3. Mathematical Expectation (Expected Value)

The **expected value** $E[X]$ of a random variable $X$ is a measure of its central tendency—a long-run average if its experiment is repeated infinitely.

*   **For a Discrete Variable (using PMF):**
    $$E[X] = \sum_{\text{all } x} x \cdot p_X(x)$$
    It is a weighted average of all possible values, weighted by their probabilities.

*   **For a Continuous Variable (using PDF):**
    $$E[X] = \int_{-\infty}^{\infty} x \cdot f_X(x)  dx$$

**Example (Discrete):** The expected value of the fair die roll is:
$$E[X] = (1)(\frac{1}{6}) + (2)(\frac{1}{6}) + (3)(\frac{1}{6}) + (4)(\frac{1}{6}) + (5)(\frac{1}{6}) + (6)(\frac{1}{6}) = 3.5$$

**Linearity of Expectation:** A profoundly useful property states that for any random variables $X$ and $Y$ (even if they are dependent) and constants $a$ and $b$:
$$E[aX + bY] = aE[X] + bE[Y]$$
This property is extensively used in the average-case analysis of algorithms.

## Key Points & Summary

| Aspect | Discrete Random Variable ($X$) | Continuous Random Variable ($X$) |
| :--- | :--- | :--- |
| **Defining Function** | **Probability Mass Function (PMF)**<br>$p_X(x) = P(X = x)$ | **Probability Density Function (PDF)**<br>$f_X(x)$ |
| **Probability Calculation** | $P(a \leq X \leq b) = \sum_{x=a}^b p_X(x)$ | $P(a \leq X \leq b) = \int_a^b f_X(x)  dx$ |
| **Normalization** | $\sum_{\text{all } x} p_X(x) = 1$ | $\int_{-\infty}^{\infty} f_X(x)  dx = 1$ |
| **Expected Value** | $E[X] = \sum x \cdot p_X(x)$ | $E[X] = \int x \cdot f_X(x)  dx$ |
| **Probability at a point** | $P(X=a)$ can be $>0$ | $P(X=a) = 0$ |

*   **PMF** is used for countable, distinct outcomes. **PDF** is used for measurable, continuous outcomes.
*   **Mathematical Expectation ($E[X]$)** is the theoretical mean of the probability distribution, representing the center of mass.
*   **Linearity of Expectation** is a powerful and versatile tool for simplifying complex calculations.
*   These concepts form the foundation for more advanced topics like variance, common distributions (Binomial, Poisson, Normal, Exponential), and stochastic processes.