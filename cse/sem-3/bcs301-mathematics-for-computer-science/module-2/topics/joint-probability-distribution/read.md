# Joint Probability Distribution for Two Discrete Random Variables

## Table of Contents

- [Joint Probability Distribution for Two Discrete Random Variables](#joint-probability-distribution-for-two-discrete-random-variables)
- [1. Introduction](#1-introduction)
- [2. Core Concepts](#2-core-concepts)
  - [2.1 Joint Probability Mass Function (JPMF)](#21-joint-probability-mass-function-jpmf)
  - [2.2 Marginal Probability Mass Functions](#22-marginal-probability-mass-functions)
  - [2.3 Conditional Probability Mass Function](#23-conditional-probability-mass-function)
  - [2.4 Independence of Random Variables](#24-independence-of-random-variables)
- [3. Example](#3-example)
- [4. Key Points & Summary](#4-key-points--summary)

## 1. Introduction

In many real-world engineering and computer science scenarios, we are not just interested in a single random outcome but in the relationship between _multiple_ random outcomes. For instance, you might want to model the relationship between the number of CPU cycles (X) and memory usage (Y) of a process, or the correlation between packet loss (X) and network latency (Y). A **Joint Probability Distribution** provides the complete probabilistic model for two or more random variables considered simultaneously. This module focuses on the discrete case, where the random variables can only take on a countable set of values.

## 2. Core Concepts

### 2.1 Joint Probability Mass Function (JPMF)

For two discrete random variables **X** and **Y**, defined on the same sample space, their joint probability mass function, denoted as $p_{X,Y}(x, y)$, gives the probability that **X** takes the value _x_ and **Y** takes the value _y_ simultaneously.

$$p_{X,Y}(x, y) = P(X = x, Y = y)$$

**Properties of JPMF:**

1. **Non-negativity:** $p_{X,Y}(x, y) \geq 0$ for all $x$, $y$.
2. **Sum to 1:** The sum of all possible joint probabilities must be 1.
   $$\sum_{x} \sum_{y} p_{X,Y}(x, y) = 1$$

### 2.2 Marginal Probability Mass Functions

Often, we need the probability distribution of one variable, ignoring the other. This is found by **summing** the joint probabilities over all possible values of the other variable. These are called the **marginal probability mass functions**.

- The marginal PMF of **X** is: $p_X(x) = P(X = x) = \sum_{y} p_{X,Y}(x, y)$
- The marginal PMF of **Y** is: $p_Y(y) = P(Y = y) = \sum_{x} p_{X,Y}(x, y)$

Think of it as "projecting" the 2D joint distribution onto a single axis to find the individual behavior of each variable.

### 2.3 Conditional Probability Mass Function

The conditional PMF gives the probability distribution of one variable, given that the other variable has taken a specific value. It is defined as:

$$p_{X|Y}(x | y) = P(X = x | Y = y) = \frac{P(X = x, Y = y)}{P(Y = y)} = \frac{p_{X,Y}(x, y)}{p_Y(y)}$$

provided $p_Y(y) > 0$. Similarly, $p_{Y|X}(y | x) = \frac{p_{X,Y}(x, y)}{p_X(x)}$.

### 2.4 Independence of Random Variables

Two discrete random variables **X** and **Y** are said to be **independent** if and only if knowing the value of one provides no information about the value of the other. This translates to:

$$p_{X,Y}(x, y) = p_X(x) \cdot p_Y(y) \quad \text{for all } x, y$$

If this condition holds, the joint probability is simply the product of the marginal probabilities.

## 3. Example

Let's define two random variables for a simple system:

- **X**: The number of times a server is accessed in one minute. (Possible values: 0, 1, 2)
- **Y**: The server's response status. (0 = OK, 1 = Slow, 2 = Error)

Their joint probability distribution is given by the following table:

|              | Y=0 | Y=1  | Y=2 | $p_X(x)$ (Marginal) |
| :----------- | :-: | :--: | :-: | :-----------------: |
| **X=0**      | 0.1 | 0.05 | 0.0 |        0.15         |
| **X=1**      | 0.2 | 0.1  | 0.1 |        0.40         |
| **X=2**      | 0.2 | 0.15 | 0.1 |        0.45         |
| **$p_Y(y)$** | 0.5 | 0.3  | 0.2 |       **1.0**       |

**Using this table, we can calculate:**

1. **Marginal Probabilities:**

- $P(X=2) = p_X(2) = 0.2 + 0.15 + 0.1 = 0.45$ (Sum of the row for X=2)
- $P(Y=1) = p_Y(1) = 0.05 + 0.1 + 0.15 = 0.3$ (Sum of the column for Y=1)

2. **Conditional Probability:**

- What is the probability the server is slow (Y=1) _given_ it was accessed twice (X=2)?
  $$P(Y=1 | X=2) = \frac{p_{X,Y}(2, 1)}{p_X(2)} = \frac{0.15}{0.45} = \frac{1}{3}$$

3. **Check for Independence:**

- Are X and Y independent? Check one cell: $p_{X,Y}(0,0) = 0.1$
- $p_X(0) \cdot p_Y(0) = (0.15) \cdot (0.5) = 0.075$
- Since $0.1 \neq 0.075$, the variables are **not independent**. The server load (X) affects its response status (Y).

## 4. Key Points & Summary

- **Purpose:** A joint probability distribution models the behavior of two or more random variables together.
- **JPMF:** $p_{X,Y}(x, y) = P(X=x, Y=y)$ is the fundamental building block.
- **Marginal PMF:** Found by summing the JPMF over the other variable ($p_X(x) = \sum_y p_{X,Y}(x, y)$). It describes individual variable behavior.
- **Conditional PMF:** Found using $P(X=x | Y=y) = \frac{p_{X,Y}(x, y)}{p_Y(y)}$. It describes the behavior of one variable when another is fixed.
- **Independence:** Two variables are independent if their joint PMF equals the product of their marginal PMFs for all values. This is a crucial simplifying assumption in many models.
- **Application:** This concept is foundational for moving into more complex topics like **Markov Chains**, where the next state depends probabilistically on the current state, directly utilizing the concept of conditional probability.
