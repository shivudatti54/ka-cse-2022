# Module 1: Probability Distributions

## Table of Contents

- [Module 1: Probability Distributions](#module-1-probability-distributions)
- [A Review of Basic Probability Theory and Random Variables](#a-review-of-basic-probability-theory-and-random-variables)
  - [Introduction](#introduction)
  - [1. Core Probability Theory](#1-core-probability-theory)
  - [2. Random Variables](#2-random-variables)
  - [Key Points & Summary](#key-points--summary)

## A Review of Basic Probability Theory and Random Variables

### Introduction

For computer scientists, probability is not just an abstract mathematical concept; it is a fundamental tool. It underpins algorithms in machine learning, informs decisions in game theory, governs packet routing in networks, and drives simulations. This module begins by revisiting the core principles of probability theory and introduces the crucial concept of a **random variable**, which allows us to formalize and quantify uncertain events—a necessity for building intelligent and efficient computational systems.

---

### 1. Core Probability Theory

Probability is a measure of the likelihood that a particular event will occur. Its foundation lies in defining a **sample space (S)**, which is the set of all possible outcomes of a random experiment.

- **Event (E):** Any subset of the sample space (e.g., getting an even number when rolling a die: E = {2, 4, 6}).
- **Probability of an Event (P(E)):** A number between 0 and 1 (inclusive) that represents the chance of event E occurring. `P(E) = (Number of favorable outcomes) / (Total number of possible outcomes)`.

Two fundamental rules govern how probabilities interact:

1. **Addition Rule:** For two _mutually exclusive_ events (events that cannot happen simultaneously, like getting a 1 OR a 2 on a die roll):
   `P(A OR B) = P(A ∪ B) = P(A) + P(B)`

2. **Multiplication Rule:** For two _independent_ events (where the occurrence of one does not affect the probability of the other, like flipping a coin and then rolling a die):
   `P(A AND B) = P(A ∩ B) = P(A) * P(B)`

**Example:** Consider a fair six-sided die.

- Sample Space, `S = {1, 2, 3, 4, 5, 6}`
- Probability of rolling a 3, `P(3) = 1/6`.
- Probability of rolling an even number, `P(Even) = P({2,4,6}) = 3/6 = 1/2`.
- Probability of rolling a 3 **AND** an even number on the same roll? These events are mutually exclusive—a single outcome cannot be both 3 and even. Therefore, `P(3 ∩ Even) = 0`.

---

### 2. Random Variables

A **Random Variable (RV)** is a function that assigns a real number to each outcome in the sample space of a random experiment. In simpler terms, it's a variable whose value is determined by chance. We denote RVs with capital letters (e.g., X, Y) and their possible values with lowercase letters (e.g., x, y).

This is a powerful abstraction. It lets us move from talking about events like "getting heads" to working with numerical values like "X=1", which is far easier to model and analyze mathematically.

There are two main types of random variables:

#### a) Discrete Random Variables

A random variable is **discrete** if it can take on only a finite or countably infinite number of distinct values.

- **Examples:**
- `X`: The number of heads in 10 coin tosses. (Possible values: 0, 1, 2, ..., 10)
- `Y`: The number of bugs found in a software module. (Possible values: 0, 1, 2, 3, ...)
- `Z`: The result of rolling a die. (Possible values: 1, 2, 3, 4, 5, 6)

- **Probability Mass Function (PMF):** The function that gives the probability that a discrete random variable is _exactly equal_ to some value. It's defined as `p(x) = P(X = x)`.

For a fair die roll, the PMF would be:
`p(x) = 1/6` for `x = 1, 2, 3, 4, 5, 6`, and `p(x) = 0` for all other values of `x`.

- **Cumulative Distribution Function (CDF):** The probability that the random variable takes a value _less than or equal to_ a specific value `x`. It's defined as `F(x) = P(X ≤ x)`.

For the die roll, `F(3) = P(X ≤ 3) = P(1) + P(2) + P(3) = 1/6 + 1/6 + 1/6 = 1/2`.

#### b) Continuous Random Variables

(A brief mention as a point of contrast, though the focus here is on discrete)
A random variable is **continuous** if it can take an uncountably infinite number of values (e.g., any value in an interval). Examples include measuring time, distance, or temperature. They are described by a **Probability Density Function (PDF)** rather than a PMF.

---

### Key Points & Summary

- **Probability** quantifies uncertainty, measuring the likelihood of events from 0 (impossible) to 1 (certain).
- A **Random Variable (X)** is a crucial bridge that maps outcomes of random processes to numerical values, making them amenable to mathematical analysis.
- A **Discrete Random Variable** has a finite or countable number of possible values.
- The **Probability Mass Function (PMF), p(x)**, defines the probability distribution of a discrete RV for each specific value `x` (`P(X=x)`).
- The **Cumulative Distribution Function (CDF), F(x)**, gives the probability that a random variable is less than or equal to `x` (`P(X≤x)`).
- Understanding these foundations is essential before studying specific probability distributions (like Binomial, Poisson, and Geometric distributions in subsequent topics), which are simply predefined PMFs that model common real-world scenarios in computer science.
