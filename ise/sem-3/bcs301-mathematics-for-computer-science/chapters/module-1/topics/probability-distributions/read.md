# Probability Distributions in Computer Science

## Introduction

Probability distributions are fundamental to computer science, providing the mathematical backbone for modeling uncertainty, randomness, and variability. From designing randomized algorithms and analyzing their performance to building machine learning models and simulating complex network traffic, understanding how data is distributed is crucial. This module introduces the core concepts of probability distributions, focusing on the essential types you will encounter in your field.

## Core Concepts

### 1. What is a Random Variable?

A **random variable** is not a traditional variable but a function that assigns a numerical value to each outcome in a sample space of a random experiment. It's the bridge between random physical (or digital) events and numerical probabilities.

- **Discrete Random Variable**: Takes on a countable number of distinct values (e.g., number of heads in coin tosses, number of packets arriving at a router).
- **Continuous Random Variable**: Takes on an uncountable infinite number of values (e.g., time between packet arrivals, execution time of an algorithm).

### 2. What is a Probability Distribution?

A probability distribution describes how probabilities are distributed over the values of a random variable. It defines the likelihood of different outcomes.

- For **discrete** variables, we define a **Probability Mass Function (PMF)**, denoted as `P(X = x)`. This gives the probability that a discrete random variable is exactly equal to some value.
- For **continuous** variables, we use a **Probability Density Function (PDF)**, denoted as `f(x)`. The probability for a continuous variable is defined over an interval and is calculated as the area under the PDF curve for that interval.

The **Cumulative Distribution Function (CDF)**, `F(x) = P(X ≤ x)`, is a universal concept that applies to both discrete and continuous random variables, representing the probability that the variable takes a value less than or equal to `x`.

## Key Discrete Distributions

### 1. Bernoulli Distribution

Models a single trial with exactly two outcomes: **success** (1) with probability `p` and **failure** (0) with probability `q = 1 - p`.

- **PMF**: `P(X = x) = p^x * (1-p)^(1-x)` for `x ∈ {0, 1}`
- **Example**: Modeling a single bit transmission (0 or 1) over a noisy channel where `p` is the probability of a bit flip.

### 2. Binomial Distribution

Models the number of successes (`k`) in a fixed number (`n`) of independent Bernoulli trials.

- **PMF**: `P(X = k) = C(n, k) * p^k * (1-p)^(n-k)`
- **Example**: The number of errored packets in a batch of `n` transmitted packets, where each packet has an independent probability `p` of being corrupted.

### 3. Poisson Distribution

Models the number of events occurring in a fixed interval of time or space, given a constant average rate (`λ`) of occurrence.

- **PMF**: `P(X = k) = (e^{-λ} * λ^k) / k!`
- **Example**: Modeling the number of requests hitting a web server per second or the number of typos per page of code.

## Key Continuous Distributions

### 1. Uniform Distribution

All outcomes in a continuous interval [`a, b`] are equally likely. It represents maximum uncertainty.

- **PDF**: `f(x) = 1/(b - a)` for `a ≤ x ≤ b`
- **Example**: Generating random numbers for simulations or randomizing algorithm behavior.

### 2. Exponential Distribution

Models the time _between_ events in a Poisson process. It is memoryless, meaning the probability of an event occurring in the next instant is independent of how much time has already elapsed.

- **PDF**: `f(x) = λe^{-λx}` for `x ≥ 0`
- **Example**: Modeling the inter-arrival time of network packets or the lifetime of hardware components.

### 3. Normal (Gaussian) Distribution

The ubiquitous "bell-shaped curve." It is fundamental due to the Central Limit Theorem, which states that the sum of many independent random variables tends to follow a normal distribution.

- **PDF**: `f(x) = (1 / (σ√(2π))) * e^{-(x-μ)²/(2σ²)}`
- **Example**: Modeling measurement errors, noise in data, and the distribution of sample means. Extensively used in machine learning (e.g., as prior distributions).

## Key Points & Summary

| Concept              | Description                                              | Computer Science Application                                  |
| :------------------- | :------------------------------------------------------- | :------------------------------------------------------------ |
| **Random Variable**  | A function mapping outcomes to numbers.                  | Quantifying random events (e.g., latency, packet count).      |
| **PMF (Discrete)**   | Gives probability at a specific point.                   | Analyzing counts of events (successes, errors, arrivals).     |
| **PDF (Continuous)** | Must be integrated to find probability over an interval. | Modeling continuous metrics like time, duration, and amounts. |
| **CDF**              | Probability that a variable is ≤ a value `x`.            | Useful for calculating percentiles and thresholds.            |
| **Bernoulli**        | Single trial, two outcomes.                              | Binary data, single event success/failure.                    |
| **Binomial**         | Number of successes in `n` trials.                       | Batch processing reliability, error-correcting codes.         |
| **Poisson**          | Events in fixed interval with known rate.                | Network traffic analysis, server request modeling.            |
| **Exponential**      | Time between events.                                     | Queueing theory, scheduling, reliability analysis.            |
| **Normal**           | Sum of many small effects.                               | Noise modeling, machine learning algorithms, statistics.      |

Understanding these distributions allows you to move from simply observing data to _modeling_ it, enabling prediction, simulation, and the design of robust computer systems.
