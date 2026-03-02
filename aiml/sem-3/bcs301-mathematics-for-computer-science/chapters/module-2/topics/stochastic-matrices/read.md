# Stochastic Matrices

## Introduction

In the study of **Markov Chains**, a fundamental tool for modeling systems that undergo transitions from one state to another in a probabilistic manner is the **Stochastic Matrix**. Also known as a **probability matrix** or **transition matrix**, it is a square matrix that describes the transitions of a Markov chain. Understanding stochastic matrices is crucial for analyzing systems in various computer science domains, including information theory, queueing networks, randomized algorithms, and machine learning (e.g., PageRank algorithm).

---

## Core Concepts

### 1. Definition and Properties

A square matrix **P = [pᵢⱼ]** of size `n x n` is called a **stochastic matrix** (or **right stochastic matrix**) if it satisfies the following two conditions:

1.  **Non-negativity:** Every element must be a probability, i.e., non-negative.
    $$p_{ij} \geq 0 \quad \text{for all } i, j$$

2.  **Row Sum of 1:** The sum of the elements in each row must equal 1.
    $$\sum_{j=1}^{n} p_{ij} = 1 \quad \text{for each } i$$

This means each row of the matrix **P** is a probability distribution. The element `pᵢⱼ` represents the probability of moving from state `i` to state `j` in one step.

**Note:** A **left stochastic matrix** is defined similarly but requires that the *columns* sum to 1. In the context of Markov chains, the right stochastic matrix is the standard definition.

### 2. Connection to State Vectors

The state of a Markov chain at a given step `n` is represented by a **state probability vector**, a row vector **x⁽ⁿ⁾** = [x₁, x₂, ..., xₙ] where each element `xᵢ` is the probability of the system being in state `i` at step `n`. The sum of the elements in **x⁽ⁿ⁾** must be 1.

The power of a stochastic matrix is revealed when we use it to compute future states. The state vector at step `n+1` is calculated from the state vector at step `n` by:
$$ \mathbf{x}^{(n+1)} = \mathbf{x}^{(n)} \mathbf{P} $$

To find the state after `k` steps, we simply multiply the initial state vector **x⁽⁰⁾** by the matrix **P** raised to the `k`-th power:
$$ \mathbf{x}^{(k)} = \mathbf{x}^{(0)} \mathbf{P}^{k} $$
This makes **Pᵏ** itself a stochastic matrix, whose elements represent the **k-step transition probabilities**.

### 3. Regular Markov Chains and Steady-State

A key question in Markov chains is: what happens in the long run? For a special type of stochastic matrix called a **regular** matrix, the system converges to a unique **steady-state distribution vector**, regardless of the starting state.

A stochastic matrix **P** is regular if some power **Pᵏ** contains only **strictly positive** entries (no zeros).

The steady-state vector **π** is a probability vector that remains unchanged by the application of the transition matrix:
$$ \mathbf{\pi} = \mathbf{\pi} \mathbf{P} $$
This equation defines **π** as the **left eigenvector** of **P** corresponding to the eigenvalue 1. We can solve for **π** using this matrix equation along with the condition that the sum of its probabilities is 1 (`π₁ + π₂ + ... + πₙ = 1`).

---

## Example: The Weather Model

Consider a simple model where the weather is either **Sunny (S)** or **Rainy (R)**. The probabilities for the next day's weather are:
*   If today is Sunny: probability of tomorrow being Sunny is 0.8, Rainy is 0.2.
*   If today is Rainy: probability of tomorrow being Sunny is 0.6, Rainy is 0.4.

This defines a Markov chain. We can represent its transition probabilities with a stochastic matrix **P**, where state 1 is Sunny and state 2 is Rainy.

**Stochastic Matrix P:**
$$
\mathbf{P} = \begin{bmatrix}
0.8 & 0.2 \\
0.6 & 0.4 \\
\end{bmatrix}
$$
*   Row 1 (Sunny): `p₁₁ = 0.8`, `p₁₂ = 0.2` → Sum = 1.0
*   Row 2 (Rainy): `p₂₁ = 0.6`, `p₂₂ = 0.4` → Sum = 1.0

**Question:** If it is sunny today (initial state vector **x⁽⁰⁾** = [1, 0]), what is the probability it will be sunny two days from now?

**Solution:**
$$ \mathbf{x}^{(2)} = \mathbf{x}^{(0)} \mathbf{P}^{2} $$
First, compute **P²**:
$$
\mathbf{P}^{2} = \begin{bmatrix}
0.8 & 0.2 \\
0.6 & 0.4 \\
\end{bmatrix}
\begin{bmatrix}
0.8 & 0.2 \\
0.6 & 0.4 \\
\end{bmatrix}
= \begin{bmatrix}
(0.8)(0.8)+(0.2)(0.6) & (0.8)(0.2)+(0.2)(0.4) \\
(0.6)(0.8)+(0.4)(0.6) & (0.6)(0.2)+(0.4)(0.4) \\
\end{bmatrix}
= \begin{bmatrix}
0.76 & 0.24 \\
0.72 & 0.28 \\
\end{bmatrix}
$$
Now, find the state vector:
$$ \mathbf{x}^{(2)} = [1, 0] \begin{bmatrix} 0.76 & 0.24 \\ 0.72 & 0.28 \\ \end{bmatrix} = [(1)(0.76) + (0)(0.72), (1)(0.24) + (0)(0.28)] = [0.76, 0.24] $$
The probability that it is sunny in two days is **0.76**.

**Steady-State:** This matrix is regular. Solving **πP = π** and `π₁ + π₂ = 1`:
$$
\begin{align*}
\pi_1 &= 0.8\pi_1 + 0.6\pi_2 \\
\pi_2 &= 0.2\pi_1 + 0.4\pi_2 \\
\pi_1 + \pi_2 &= 1
\end{align*}
$$
From the first equation: `π₁ = 0.8π₁ + 0.6(1-π₁)` → `π₁ = 0.8π₁ + 0.6 - 0.6π₁` → `π₁ = 0.2π₁ + 0.6` → `0.8π₁ = 0.6` → `π₁ = 0.75`. Thus, `π₂ = 0.25`.

The long-term forecast is **75% sunny** and **25% rainy**.

---

## Key Points & Summary

*   **Definition:** A stochastic matrix **P** is a square matrix with non-negative entries where each row sums to 1.
*   **Purpose:** It encodes the one-step transition probabilities between states in a Markov chain.
*   **State Evolution:** The state vector after `k` steps is found by **x⁽ᵏ⁾ = x⁽⁰⁾Pᵏ**.
*   **Regular Matrix:** If some power **Pᵏ** has all positive entries, the matrix is regular.
*   **Steady-State:** A regular Markov chain converges to a unique steady-state vector **π**, found by solving **π = πP** with the normalization condition.
*   **Computer Science Applications:** These concepts are vital for modeling random processes in areas like network traffic analysis, randomized algorithms, and reinforcement learning.