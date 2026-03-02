# Exponential Distribution

## Table of Contents

- [Exponential Distribution](#exponential-distribution)
- [Introduction](#introduction)
- [Definition](#definition)
  - [Verification that $f(x)$ is a valid PDF](#verification-that-fx-is-a-valid-pdf)
- [Cumulative Distribution Function (CDF)](#cumulative-distribution-function-cdf)
- [Mean and Variance](#mean-and-variance)
  - [Mean (Expected Value)](#mean-expected-value)
  - [Second Moment](#second-moment)
  - [Variance](#variance)
  - [Standard Deviation](#standard-deviation)
- [Moment Generating Function (MGF)](#moment-generating-function-mgf)
- [Memoryless Property](#memoryless-property)
  - [Statement](#statement)
  - [Proof](#proof)
- [Relationship to the Poisson Distribution](#relationship-to-the-poisson-distribution)
- [Worked Examples](#worked-examples)
  - [Example 1: Basic Probability Calculation](#example-1-basic-probability-calculation)
  - [Example 2: Memoryless Property Application](#example-2-memoryless-property-application)
  - [Example 3: Finding the Rate Parameter and Probabilities](#example-3-finding-the-rate-parameter-and-probabilities)
- [Applications of the Exponential Distribution](#applications-of-the-exponential-distribution)
  - [1. Queueing Theory](#1-queueing-theory)
  - [2. Reliability Engineering](#2-reliability-engineering)
  - [3. Network Traffic Analysis](#3-network-traffic-analysis)
  - [4. Radioactive Decay](#4-radioactive-decay)
  - [5. Survival Analysis](#5-survival-analysis)
- [Summary Table](#summary-table)
- [Exam Tips](#exam-tips)

## Introduction

The **exponential distribution** is one of the most important continuous probability distributions. It models the time between events in a Poisson process -- that is, a process where events occur continuously and independently at a constant average rate. If a Poisson random variable counts the number of events in a given interval, the exponential random variable measures the waiting time between consecutive events.

---

## Definition

A continuous random variable $X$ is said to follow an **exponential distribution** with parameter $\lambda > 0$ (written $X \sim \text{Exp}(\lambda)$) if its probability density function (PDF) is:

$$
f(x) = \begin{cases} \lambda e^{-\lambda x}, & x \geq 0 \\ 0, & x < 0 \end{cases}
$$

Here, $\lambda$ is called the **rate parameter** (the average number of events per unit time).

### Verification that $f(x)$ is a valid PDF

1. $f(x) \geq 0$ for all $x$ (since $\lambda > 0$ and $e^{-\lambda x} > 0$).
2. $\int_{0}^{\infty} \lambda e^{-\lambda x} \, dx = \left[-e^{-\lambda x}\right]_0^{\infty} = 0 - (-1) = 1$.

---

## Cumulative Distribution Function (CDF)

The CDF of the exponential distribution is obtained by integrating the PDF:

$$
F(x) = P(X \leq x) = \int_0^x \lambda e^{-\lambda t} \, dt = 1 - e^{-\lambda x}, \quad x \geq 0
$$

Therefore:

$$
F(x) = \begin{cases} 1 - e^{-\lambda x}, & x \geq 0 \\ 0, & x < 0 \end{cases}
$$

The **survival function** (complement of CDF) is:

$$
P(X > x) = 1 - F(x) = e^{-\lambda x}, \quad x \geq 0
$$

---

## Mean and Variance

### Mean (Expected Value)

$$
E(X) = \int_0^{\infty} x \cdot \lambda e^{-\lambda x} \, dx
$$

Using integration by parts (let $u = x$, $dv = \lambda e^{-\lambda x} dx$):

$$
E(X) = \left[-x e^{-\lambda x}\right]_0^{\infty} + \int_0^{\infty} e^{-\lambda x} \, dx = 0 + \frac{1}{\lambda} = \frac{1}{\lambda}
$$

### Second Moment

$$
E(X^2) = \int_0^{\infty} x^2 \cdot \lambda e^{-\lambda x} \, dx = \frac{2}{\lambda^2}
$$

### Variance

$$
\text{Var}(X) = E(X^2) - [E(X)]^2 = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \frac{1}{\lambda^2}
$$

### Standard Deviation

$$
\sigma = \frac{1}{\lambda}
$$

> **Note:** For the exponential distribution, the mean and the standard deviation are equal: $E(X) = \sigma = \frac{1}{\lambda}$.

---

## Moment Generating Function (MGF)

$$
M_X(t) = E(e^{tX}) = \frac{\lambda}{\lambda - t}, \quad t < \lambda
$$

---

## Memoryless Property

The exponential distribution is the **only continuous distribution** that possesses the memoryless property.

### Statement

For $s, t \geq 0$:

$$
P(X > s + t \mid X > s) = P(X > t)
$$

This means: given that an event has not occurred in the first $s$ time units, the probability of waiting an additional $t$ time units is the same as the probability of waiting $t$ time units from the start. The distribution "forgets" how long it has already been waiting.

### Proof

$$
P(X > s + t \mid X > s) = \frac{P(X > s + t \text{ and } X > s)}{P(X > s)}
$$

Since $\{X > s + t\} \subseteq \{X > s\}$, the intersection is simply $\{X > s + t\}$:

$$
= \frac{P(X > s + t)}{P(X > s)} = \frac{e^{-\lambda(s+t)}}{e^{-\lambda s}} = \frac{e^{-\lambda s} \cdot e^{-\lambda t}}{e^{-\lambda s}} = e^{-\lambda t} = P(X > t)
$$

Hence proved. $\blacksquare$

---

## Relationship to the Poisson Distribution

The exponential and Poisson distributions are intimately connected:

- If events occur according to a **Poisson process** with rate $\lambda$ (i.e., the number of events in time interval $t$ follows $\text{Poisson}(\lambda t)$), then the **time between consecutive events** (inter-arrival time) follows $\text{Exp}(\lambda)$.

- Conversely, if inter-arrival times are independent and identically distributed as $\text{Exp}(\lambda)$, then the number of arrivals in any interval of length $t$ follows $\text{Poisson}(\lambda t)$.

| Poisson Distribution                                | Exponential Distribution        |
| --------------------------------------------------- | ------------------------------- |
| Discrete (counts events)                            | Continuous (measures time)      |
| $P(X = k) = \frac{e^{-\lambda t}(\lambda t)^k}{k!}$ | $f(x) = \lambda e^{-\lambda x}$ |
| Number of events in interval $t$                    | Time between consecutive events |
| Mean = $\lambda t$                                  | Mean = $1/\lambda$              |

---

## Worked Examples

### Example 1: Basic Probability Calculation

**Problem:** The time (in minutes) between customer arrivals at a bank follows an exponential distribution with a mean of 5 minutes. Find the probability that the next customer arrives within 3 minutes.

**Solution:**

Given: Mean $= 1/\lambda = 5$, so $\lambda = 1/5 = 0.2$ per minute.

We need $P(X \leq 3)$:

$$
P(X \leq 3) = F(3) = 1 - e^{-\lambda \cdot 3} = 1 - e^{-0.2 \times 3} = 1 - e^{-0.6}
$$

$$
= 1 - 0.5488 = 0.4512
$$

**Answer:** The probability is approximately **0.4512** (or 45.12%).

---

### Example 2: Memoryless Property Application

**Problem:** The lifetime of a light bulb follows an exponential distribution with a mean lifetime of 1000 hours. Given that a bulb has already lasted 500 hours, what is the probability that it will last at least another 300 hours?

**Solution:**

Given: Mean $= 1/\lambda = 1000$ hours, so $\lambda = 0.001$ per hour.

By the memoryless property:

$$
P(X > 800 \mid X > 500) = P(X > 300)
$$

$$
= e^{-\lambda \times 300} = e^{-0.001 \times 300} = e^{-0.3} = 0.7408
$$

**Answer:** The probability is approximately **0.7408** (or 74.08%). Note how the past 500 hours of survival does not affect the future probability -- this is the memoryless property at work.

---

### Example 3: Finding the Rate Parameter and Probabilities

**Problem:** Calls arrive at a call center at an average rate of 12 per hour. The inter-arrival time follows an exponential distribution. Find:
(a) The probability that the time between two successive calls exceeds 10 minutes.
(b) The probability that the next call arrives between 3 and 7 minutes.

**Solution:**

Given: $\lambda = 12$ calls per hour $= 12/60 = 0.2$ calls per minute.

**(a)** $P(X > 10)$:

$$
P(X > 10) = e^{-\lambda \times 10} = e^{-0.2 \times 10} = e^{-2} = 0.1353
$$

**Answer (a):** Approximately **0.1353** (or 13.53%).

**(b)** $P(3 < X < 7)$:

$$
P(3 < X < 7) = F(7) - F(3) = (1 - e^{-0.2 \times 7}) - (1 - e^{-0.2 \times 3})
$$

$$
= e^{-0.6} - e^{-1.4} = 0.5488 - 0.2466 = 0.3022
$$

**Answer (b):** Approximately **0.3022** (or 30.22%).

---

## Applications of the Exponential Distribution

### 1. Queueing Theory

Models the inter-arrival times of customers at service counters, banks, hospitals, and similar systems. It is a key building block of the M/M/1 queue.

### 2. Reliability Engineering

Models the time to failure of components that have a constant failure rate (no aging effects). If $\lambda$ is the failure rate, the reliability at time $t$ is $R(t) = e^{-\lambda t}$.

### 3. Network Traffic Analysis

Models inter-arrival times of data packets in communication networks, enabling network capacity planning and performance analysis.

### 4. Radioactive Decay

The time between decay events of radioactive atoms follows an exponential distribution.

### 5. Survival Analysis

Used in medical statistics to model patient survival times under certain assumptions.

---

## Summary Table

| Property            | Formula / Value                                       |
| ------------------- | ----------------------------------------------------- |
| Notation            | $X \sim \text{Exp}(\lambda)$                          |
| Parameter           | $\lambda > 0$ (rate)                                  |
| PDF                 | $f(x) = \lambda e^{-\lambda x}, \quad x \geq 0$       |
| CDF                 | $F(x) = 1 - e^{-\lambda x}, \quad x \geq 0$           |
| Mean                | $E(X) = 1/\lambda$                                    |
| Variance            | $\text{Var}(X) = 1/\lambda^2$                         |
| Standard Deviation  | $\sigma = 1/\lambda$                                  |
| MGF                 | $M_X(t) = \lambda / (\lambda - t), \quad t < \lambda$ |
| Memoryless Property | $P(X > s+t \mid X > s) = P(X > t)$                    |
| Median              | $\ln(2) / \lambda \approx 0.693 / \lambda$            |
| Mode                | $0$                                                   |

---

## Exam Tips

1. **Always check units:** Ensure $\lambda$ and $x$ use consistent units (e.g., if $\lambda$ is per hour, then $x$ must be in hours).
2. **Mean vs. rate:** If a problem gives the mean, compute $\lambda = 1/\text{mean}$ first. If it gives the rate, use $\lambda$ directly.
3. **Memoryless property shortcut:** When a problem says "given that it has already lasted $s$ time," immediately apply $P(X > s + t \mid X > s) = P(X > t)$ to simplify.
4. **CDF for ranges:** For $P(a < X < b)$, compute $F(b) - F(a) = e^{-\lambda a} - e^{-\lambda b}$.
5. **Connection to Poisson:** frequently asks about the relationship. Remember: Poisson counts events, exponential measures time between events.
6. **Prove it is a valid PDF:** If asked, show $f(x) \geq 0$ and $\int_0^{\infty} f(x) \, dx = 1$.
7. **Derivation of mean and variance:** Practice deriving $E(X)$ and $\text{Var}(X)$ using integration by parts -- this is a common exam question.
