# Joint Probability Distribution for Two Discrete Random Variables

## Introduction

In many real-world scenarios involving computer science—such as network traffic analysis, machine learning algorithms, or image processing—we often need to consider the behavior of **more than one random variable simultaneously**. A joint probability distribution allows us to model the relationship between two or more random variables. This module focuses on two discrete random variables, providing the foundational tools to understand their combined behavior.

## Core Concepts

### 1. Joint Probability Mass Function (Joint PMF)

Let **X** and **Y** be two discrete random variables defined on the same sample space. Their joint probability mass function, denoted as $p_{X,Y}(x, y)$, gives the probability that **X** takes the value *x* and **Y** takes the value *y* simultaneously.

$$p_{X,Y}(x, y) = P(X = x, Y = y)$$

**Properties of Joint PMF:**
1. **Non-negativity:** $p_{X,Y}(x, y) \geq 0$ for all $x, y$.
2. **Summation to 1:** The sum of probabilities over all possible pairs must be 1.
   $$\sum_{x} \sum_{y} p_{X,Y}(x, y) = 1$$

### 2. Marginal Probability Mass Functions

The marginal PMF gives the probability distribution of a single variable, ignoring the other. It is found by summing the joint PMF over all possible values of the other variable.

*   **Marginal PMF of X:**
    $$p_X(x) = P(X = x) = \sum_{y} p_{X,Y}(x, y)$$
*   **Marginal PMF of Y:**
    $$p_Y(y) = P(Y = y) = \sum_{x} p_{X,Y}(x, y)$$

### 3. Conditional Probability Mass Function

The conditional PMF describes the probability distribution of one variable, given that the other variable takes on a specific value.

*   **Probability of X given Y = y:**
    $$p_{X|Y}(x|y) = P(X = x | Y = y) = \frac{p_{X,Y}(x, y)}{p_Y(y)}, \quad \text{provided } p_Y(y) > 0$$
*   **Probability of Y given X = x:**
    $$p_{Y|X}(y|x) = P(Y = y | X = x) = \frac{p_{X,Y}(x, y)}{p_X(x)}, \quad \text{provided } p_X(x) > 0$$

### 4. Independence of Random Variables

Two discrete random variables **X** and **Y** are **independent** if and only if the joint PMF is the product of their marginal PMFs for all $x, y$:

$$p_{X,Y}(x, y) = p_X(x) \cdot p_Y(y)$$

If this condition does not hold for even one pair $(x, y)$, the variables are **dependent**.

## Example: Network Packet Analysis

Consider a server where, in a given millisecond:
*   Let **X** be the number of incoming data packets (0, 1, or 2).
*   Let **Y** be the number of outgoing acknowledgment packets (0 or 1).

Suppose the joint PMF is given by the following table:

| $p_{X,Y}(x, y)$ | **Y=0** | **Y=1** | **Marginal $p_X(x)$** |
| :--- | :---: | :---: | :---: |
| **X=0** | 0.10 | 0.20 | **0.30** |
| **X=1** | 0.15 | 0.30 | **0.45** |
| **X=2** | 0.05 | 0.20 | **0.25** |
| **Marginal $p_Y(y)$** | **0.30** | **0.70** | **1.00** |

**1. Find the probability of receiving 1 packet and sending 1 ack.**
$$P(X=1, Y=1) = p_{X,Y}(1, 1) = 0.30$$

**2. Find the marginal probability of sending 0 ack packets.**
$$p_Y(0) = \sum_{x} p_{X,Y}(x, 0) = 0.10 + 0.15 + 0.05 = 0.30$$

**3. Find the conditional probability of receiving 2 packets given that no ack was sent.**
$$p_{X\|Y}(2\|0) = \frac{p_{X,Y}(2, 0)}{p_Y(0)} = \frac{0.05}{0.30} \approx 0.1667$$

**4. Check for Independence:**  
Is $p_{X,Y}(0, 0) = p_X(0) \cdot p_Y(0)$?  
$0.10 \stackrel{?}{=} (0.30)(0.30) = 0.09$  
Since $0.10 \neq 0.09$, **X and Y are not independent**. The number of incoming packets and outgoing acks are dependent, which makes intuitive sense.

## Key Points & Summary

*   **Purpose:** A joint probability distribution models the probabilistic relationship between two or more random variables.
*   **Joint PMF:** $p_{X,Y}(x, y)$ gives the probability of the event $(X=x$ and $Y=y)$.
*   **Marginal PMF:** Found by summing the joint PMF over the other variable ($p_X(x) = \sum_{y} p_{X,Y}(x, y)$). It describes individual variable behavior.
*   **Conditional PMF:** Found using the definition of conditional probability ($p_{X\|Y}(x\|y) = \frac{p_{X,Y}(x, y)}{p_Y(y)}$). It describes the behavior of one variable given knowledge of the other.
*   **Independence:** Two variables are independent if their joint PMF factorizes into the product of their marginals for all values. This is a critical concept for simplifying complex models.
*   **Applications:** This foundation is essential for understanding concepts like covariance, correlation, and, crucially, the **Markov Chains** covered in the next part of this module.