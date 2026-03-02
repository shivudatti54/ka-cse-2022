# Expectation in Probability Distributions

## Table of Contents

- [Expectation in Probability Distributions](#expectation-in-probability-distributions)
- [Introduction](#introduction)
- [Core Concepts](#core-concepts)
  - [1. Definition of Expectation](#1-definition-of-expectation)
  - [2. Expectation for Joint Distributions](#2-expectation-for-joint-distributions)
  - [3. Conditional Expectation](#3-conditional-expectation)
  - [4. Law of Total Expectation (Iterated Expectation)](#4-law-of-total-expectation-iterated-expectation)
- [Example: A Simple Joint Distribution](#example-a-simple-joint-distribution)
- [Key Points & Summary](#key-points--summary)

## Introduction

In probability theory, simply knowing the probabilities of outcomes is often not enough. We frequently need a single, representative value that summarizes the entire distribution of a random variable. This is the concept of **Expectation** (or **Expected Value**). It provides a measure of the "center" or the long-term average value of a random variable if an experiment is repeated many times. For computer scientists, this is crucial for analyzing algorithm performance (e.g., expected runtime), designing randomized algorithms, network traffic modeling, and machine learning (e.g., loss functions).

## Core Concepts

### 1. Definition of Expectation

The expectation of a discrete random variable $X$, denoted as $E[X]$ or $\mu$, is a weighted average of all its possible values, where the weights are the probabilities of those values.

**For a discrete random variable:**
$$E[X] = \sum_{\text{all } x} x \cdot P(X = x)$$

**For a continuous random variable:**
$$E[X] = \int_{-\infty}^{\infty} x \cdot f(x) dx$$
where $f(x)$ is the probability density function (PDF).

Intuitively, $E[X]$ represents the average value you would expect to get if you could repeat the random experiment an infinite number of times and average the results.

### 2. Expectation for Joint Distributions

When dealing with two random variables $(X, Y)$ with a joint probability mass function $P(X=x, Y=y)$ (for discrete case) or joint density function $f(x, y)$ (for continuous case), we can define the expectation of any function of these variables, $g(X, Y)$.

**Discrete Case:**
$$E[g(X, Y)] = \sum_{x} \sum_{y} g(x, y) \cdot P(X=x, Y=y)$$

**Continuous Case:**
$$E[g(X, Y)] = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x, y) \cdot f(x, y) dx dy$$

A particularly important special case is when $g(X, Y) = X + Y$. A key property of expectation is its **linearity**:
$$E[X + Y] = E[X] + E[Y]$$
This holds true **whether $X$ and $Y$ are independent or not**.

### 3. Conditional Expectation

The conditional expectation of $X$ given that $Y=y$ is the expected value of $X$ when we know the value of $Y$. It is computed like a normal expectation but using the conditional probability distribution.

**Discrete Case:**
$$E[X | Y = y] = \sum_{x} x \cdot P(X=x | Y=y)$$

The conditional expectation $E[X | Y]$ is itself a random variable because its value depends on the random value of $Y$.

### 4. Law of Total Expectation (Iterated Expectation)

This powerful law connects marginal expectation ($E[X]$) and conditional expectation ($E[X | Y]$). It states:
$$E[X] = E[E[X | Y]]$$

This means you can find the overall average of $X$ by first finding its average given a specific $Y$, and then averaging that result over the distribution of $Y$. This is incredibly useful in complex problems, especially those involving multi-stage processes.

## Example: A Simple Joint Distribution

Let's define a joint PMF for two discrete random variables $X$ and $Y$:

|         | Y=0 | Y=1 | Y=2 |
| :------ | :-- | :-- | :-- |
| **X=0** | 0.1 | 0.2 | 0.0 |
| **X=1** | 0.1 | 0.3 | 0.1 |
| **X=2** | 0.0 | 0.1 | 0.1 |

**Q1: Find $E[X]$.**

$E[X] = \sum_{x=0}^{2} x \cdot P(X=x)$
First, find the marginal PMF of $X$ by summing rows:
$P(X=0) = 0.1+0.2+0.0 = 0.3$
$P(X=1) = 0.1+0.3+0.1 = 0.5$
$P(X=2) = 0.0+0.1+0.1 = 0.2$
Now, $E[X] = (0)(0.3) + (1)(0.5) + (2)(0.2) = 0 + 0.5 + 0.4 = 0.9$

**Q2: Find $E[XY]$.**

Here, $g(X, Y) = XY$.
$E[XY] = \sum_{x=0}^{2} \sum_{y=0}^{2} (x \cdot y) \cdot P(X=x, Y=y)$
$= (0\cdot0)(0.1) + (0\cdot1)(0.2) + ... + (2\cdot2)(0.1)$
We only need non-zero terms:
$= (1\cdot1)(0.3) + (1\cdot2)(0.1) + (2\cdot1)(0.1) + (2\cdot2)(0.1)$
$= (1)(0.3) + (2)(0.1) + (2)(0.1) + (4)(0.1)$
$= 0.3 + 0.2 + 0.2 + 0.4 = 1.1$

## Key Points & Summary

- **Definition:** Expectation is the probability-weighted average of all possible values of a random variable.
- **Interpretation:** It represents the long-run average value of the variable over many repetitions of the experiment.
- **Linearity:** The expectation of a sum is the sum of the expectations: $E[X + Y] = E[X] + E[Y]$. This is a fundamental and frequently used property.
- **Joint Distributions:** The expectation of a function $g(X, Y)$ is found by summing/integrating over the entire joint distribution.
- **Conditional Expectation:** $E[X | Y=y]$ is the expected value of $X$ given that $Y$ has a specific value.
- **Law of Total Expectation:** A crucial tool for simplifying complex problems: $E[X] = E[E[X | Y]]$.
- **Application:** Essential in computer science for analyzing average-case complexity, queuing theory, information theory, and predictive models. It provides a single metric to characterize a probability distribution.
