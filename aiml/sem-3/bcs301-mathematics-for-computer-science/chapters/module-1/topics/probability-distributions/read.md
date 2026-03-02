# Probability Distributions for Computer Science

## Introduction

In Computer Science, we constantly deal with uncertainty and randomness—from the time it takes to execute an algorithm and the arrival of data packets in a network, to the likelihood of a bit flipping in memory or a user clicking a button. Probability distributions provide the essential mathematical framework to model, analyze, and make predictions about these random phenomena. Understanding them is crucial for fields like machine learning, randomized algorithms, performance modeling, and network simulation.

## Core Concepts

### 1. Random Variable

A **random variable** is a variable whose possible values are numerical outcomes of a random phenomenon. It acts as a bridge between random physical events and numbers. We denote it by a capital letter, like `X`. Its actual measured value is denoted by a lowercase letter, `x`.

*   **Discrete Random Variable**: Takes on a countable number of distinct values (e.g., number of errors in a code, number of requests to a server).
*   **Continuous Random Variable**: Takes on an infinite number of possible values within a given range (e.g., time between interrupts, latency of a network connection).

### 2. Probability Distribution

A probability distribution describes how probabilities are distributed over the values of the random variable. The way we describe this depends on whether the variable is discrete or continuous.

#### For Discrete Variables: Probability Mass Function (PMF)

The PMF, denoted as `P(X = x)`, gives the probability that a discrete random variable `X` is exactly equal to some value `x`. It must satisfy two conditions:
1.  `0 ≤ P(X = x) ≤ 1` for all `x`
2.  `∑ P(X = x) = 1` over all possible `x`

**Example:** The number of heads (`X`) in two fair coin tosses.
*   Possible values: `x = {0, 1, 2}`
*   PMF: `P(X=0) = 1/4`, `P(X=1) = 1/2`, `P(X=2) = 1/4`

#### For Continuous Variables: Probability Density Function (PDF)

For continuous variables, the probability at a single point is effectively zero. Instead, we use a PDF, `f(x)`. The probability that `X` lies between two points `a` and `b` is found by calculating the *area under the curve* of the PDF between those points.

`P(a ≤ X ≤ b) = ∫(a to b) f(x) dx`

The PDF must satisfy:
1.  `f(x) ≥ 0` for all `x`
2.  `∫ f(x) dx = 1` over all possible `x`

### 3. Cumulative Distribution Function (CDF)

The CDF, `F(x)`, gives the probability that the random variable `X` is less than or equal to a value `x`. This definition applies to both discrete and continuous variables.

*   **For Discrete:** `F(x) = P(X ≤ x) = ∑ P(X = k)` for all `k ≤ x`
*   **For Continuous:** `F(x) = P(X ≤ x) = ∫(-∞ to x) f(t) dt`

The CDF is a non-decreasing function that ranges from 0 to 1.

## Common Distributions (A Preview)

While Module 1 will cover these in detail, here are two fundamental distributions:

**1. Binomial Distribution (Discrete)**
*   **Models:** The number of successes in `n` independent trials, each with a probability `p` of success.
*   **Computer Science Application:** Modeling the number of corrupted bits in a data packet, the number of successful responses from `n` servers.

**2. Normal (Gaussian) Distribution (Continuous)**
*   **Models:** Naturally occurring phenomena where data tends to cluster around a mean (μ) with a certain spread (standard deviation σ). The classic "bell curve."
*   **Computer Science Application:** Modeling measurement errors (e.g., sensor data), noise in signals, and the distribution of averages (Central Limit Theorem).

## Key Points & Summary

| Concept | Description | Application |
| :--- | :--- | :--- |
| **Random Variable (X)** | A numerical outcome of a random process. | The foundation for quantifying randomness. |
| **PMF (Discrete)** | `P(X=x)`. Probability that a discrete variable equals a value `x`. | Counting events: errors, requests, successes. |
| **PDF (Continuous)** | `f(x)`. Defines the density. Probability is the area under the curve. | Measuring continuous quantities: time, length, volume. |
| **CDF (F(x))** | `P(X ≤ x)`. The probability that the variable is at most `x`. | Useful for calculating percentiles and probabilities. |

*   Probability distributions are not just abstract math; they are **practical tools** for building and analyzing stochastic computer systems.
*   The choice of which distribution to use depends on the nature of the data you are modeling (discrete/continuous) and the underlying random process.
*   Mastery of these concepts is a prerequisite for understanding more advanced topics like statistical inference, queueing theory, and machine learning algorithms.