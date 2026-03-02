# Joint Probability Distribution for Two Discrete Random Variables

## Introduction

In many real-world scenarios, especially in computer science, we are interested in the behavior of _multiple random variables simultaneously_. For instance, you might want to analyze the relationship between the number of CPU cycles (`X`) and the amount of memory used (`Y`) by a process. A **joint probability distribution** provides the complete picture of the probability for these two discrete random variables occurring together. It is the foundation for understanding concepts like dependence, independence, and correlation, which are crucial for fields like machine learning, performance analysis, and network modeling.

## Core Concepts

### 1. Joint Probability Mass Function (Joint PMF)

The central tool for describing two discrete random variables is the Joint PMF. For any two discrete random variables `X` and `Y`, defined on the same sample space, their joint probability mass function is given by:

$$p_{X,Y}(x, y) = P(X = x, Y = y)$$

This function gives the probability that `X` takes the specific value `x` _and_ `Y` takes the specific value `y` at the same time.

**Properties of Joint PMF:**

- **Non-negativity:** $p_{X,Y}(x, y) \geq 0$ for all $x$, $y$.
- **Sum to 1:** $\sum_{x}\sum_{y}p_{X,Y}(x, y) = 1$

### 2. Marginal Probability Mass Functions

Often, we are interested in the probability distribution of just one of the variables, ignoring the other. This is called the **marginal distribution**. We can obtain the marginal PMFs from the joint PMF by summing over all possible values of the other variable.

- **Marginal PMF of X:** $p_X(x) = P(X = x) = \sum_{y}p_{X,Y}(x, y)$
- **Marginal PMF of Y:** $p_Y(y) = P(Y = y) = \sum_{x}p_{X,Y}(x, y)$

Think of it as adding up the probabilities along a row or column in a joint probability table.

### 3. Independence of Random Variables

Two discrete random variables `X` and `Y` are said to be **independent** if and only if the joint PMF factorizes into the product of their marginal PMFs for _all_ $x$ and $y$:

$$p_{X,Y}(x, y) = p_X(x) \cdot p_Y(y)$$

This means that knowing the value of `X` gives us no information about the value of `Y`, and vice versa. If this condition is not met, the variables are **dependent**.

## Example: Website Load Times

Let's define two discrete random variables for a web server:

- Let `X` be the number of images on a webpage (1, 2, or 3).
- Let `Y` be the page load time, categorized as `0` for Fast (<2s) or `1` for Slow (≥2s).

Suppose the observed joint probability distribution is given by the following table:

| $p_{X,Y}(x, y)$       | **Y = 0 (Fast)** | **Y = 1 (Slow)** | **Marginal $p_X(x)$** |
| :-------------------- | :--------------: | :--------------: | :-------------------: |
| **X = 1**             |       0.30       |       0.10       |       **0.40**        |
| **X = 2**             |       0.20       |       0.20       |       **0.40**        |
| **X = 3**             |       0.05       |       0.15       |       **0.20**        |
| **Marginal $p_Y(y)$** |     **0.55**     |     **0.45**     |       **1.00**        |

**1. Calculating a Joint Probability:**
The probability that a page has 2 images and loads slowly is found directly from the table: $P(X=2, Y=1) = 0.20$.

**2. Calculating a Marginal Probability:**
The probability that a page has 3 images ($X=3$), regardless of its load time, is the sum of the probabilities in that row:
$P(X=3) = p_X(3) = P(X=3, Y=0) + P(X=3, Y=1) = 0.05 + 0.15 = 0.20$.

**3. Checking for Independence:**
Are `X` and `Y` independent? Let's check for one cell. If they were independent, $P(X=1, Y=0)$ should equal $P(X=1) \cdot P(Y=0)$.

- $P(X=1) \cdot P(Y=0) = (0.40) \cdot (0.55) = 0.22$
- But the table shows $P(X=1, Y=0) = 0.30$

Since $0.30 \neq 0.22$, the variables are **not independent**. The load time depends on the number of images.

## Key Points & Summary

- **Purpose:** A joint probability distribution describes the probabilistic behavior of two random variables, `X` and `Y`, together.
- **Joint PMF:** The function $p_{X,Y}(x, y) = P(X=x, Y=y)$ is the cornerstone of this analysis.
- **Marginal PMF:** Found by summing the joint PMF over the other variable (e.g., $p_X(x) = \sum_{y}p_{X,Y}(x, y)$). It gives the individual distribution of one variable.
- **Independence:** Two variables are independent only if their joint PMF is the product of their marginal PMFs for all possible values. This is a crucial concept for simplifying complex models.
- **Application:** This is a fundamental building block for more advanced topics like **covariance**, **correlation**, and **Markov Chains**, where the state of the next event depends on the joint probability of previous states.
