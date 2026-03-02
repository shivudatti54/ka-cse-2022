# Higher Transition Probabilities in Markov Chains

## Table of Contents

- [Higher Transition Probabilities in Markov Chains](#higher-transition-probabilities-in-markov-chains)
- [Introduction](#introduction)
- [Core Concepts](#core-concepts)
  - [The `n`-Step Transition Probability](#the-n-step-transition-probability)
  - [The Chapman-Kolmogorov Equations](#the-chapman-kolmogorov-equations)
  - [The `n`-Step Transition Matrix](#the-n-step-transition-matrix)
- [Example](#example)
- [Key Points & Summary](#key-points--summary)

## Introduction

In the previous sections, you learned about Markov chains and how a one-step transition probability, denoted as $P_{ij}$, represents the probability of moving from state $i$ to state $j$ in a single step. But what if we need to predict the state of the system not one step, but `n` steps into the future? This is where the concept of **Higher Transition Probabilities** comes in. An `n`-step transition probability, denoted as $P_{ij}^{(n)}$, is the probability that a process in state $i$ will be in state $j`after exactly`n` additional transitions.

## Core Concepts

### The `n`-Step Transition Probability

The `n`-step transition probability is defined as:
$$P_{ij}^{(n)} = P\{X_{n+m} = j | X_m = i\}$$

This represents the probability of being in state `j` at time `n+m`, given that the process was in state `i` at time `m`. For a **homogeneous** Markov chain (where transition probabilities do not change over time), these probabilities depend only on the number of steps `n`, not on the starting time `m`.

### The Chapman-Kolmogorov Equations

The fundamental tool for computing `n`-step probabilities is the set of **Chapman-Kolmogorov Equations**. These equations provide a method to compute $P_{ij}^{(n)}$ by breaking the `n`-step path from `i` to `j` into two parts: a first step (or `r` steps) to an intermediate state `k`, and the remaining steps from `k` to `j`.

The equation is:
$$P_{ij}^{(n)} = \sum_{k} P_{ik}^{(r)} \cdot P_{kj}^{(n-r)} \quad \text{for all } 0 < r < n$$

The most common and useful form sets `r=1` and `n=m+n`:
$$P_{ij}^{(m+n)} = \sum_{k} P_{ik}^{(m)} \cdot P_{kj}^{(n)}$$

This means the probability of going from `i` to `j` in `m+n` steps is the sum over all possible intermediate states `k` of the probability of going from `i` to `k` in `m` steps multiplied by the probability of going from `k` to `j` in `n` steps.

### The `n`-Step Transition Matrix

Just as the one-step transition probabilities can be arranged into a **Transition Probability Matrix** `P`, the `n`-step probabilities can be arranged into an `n`-step transition matrix $P^{(n)}$. The most important result is:

$$P^{(n)} = P^n$$

That is, the `n`-step transition matrix is simply the **`n`-th power** of the one-step transition matrix `P`. This provides a straightforward computational method.

## Example

Let's consider a simple two-state Markov chain representing the weather (Sunny vs Rainy).

The one-step transition matrix is:

$$
P = \begin{bmatrix}
P_{SS} & P_{SR} \\
P_{RS} & P_{RR}
\end{bmatrix} = \begin{bmatrix}
0.8 & 0.2 \\
0.3 & 0.7
\end{bmatrix}
$$

Let's find the probability that it will be sunny in two days, given that it is sunny today, i.e., $P_{SS}^{(2)}$.

**Method 1: Using the Chapman-Kolmogorov Equation**
We sum over all possible intermediate states `k` (which are Sunny and Rainy).
$$P_{SS}^{(2)} = P_{SS} \cdot P_{SS} + P_{SR} \cdot P_{RS} = (0.8)(0.8) + (0.2)(0.3) = 0.64 + 0.06 = 0.70$$
$$P_{SR}^{(2)} = P_{SS} \cdot P_{SR} + P_{SR} \cdot P_{RR} = (0.8)(0.2) + (0.2)(0.7) = 0.16 + 0.14 = 0.30$$
$$P_{RS}^{(2)} = P_{RS} \cdot P_{SS} + P_{RR} \cdot P_{RS} = (0.3)(0.8) + (0.7)(0.3) = 0.24 + 0.21 = 0.45$$
$$P_{RR}^{(2)} = P_{RS} \cdot P_{SR} + P_{RR} \cdot P_{RR} = (0.3)(0.2) + (0.7)(0.7) = 0.06 + 0.49 = 0.55$$

**Method 2: Using Matrix Multiplication ($P^2$)**

$$
P^{(2)} = P^2 = \begin{bmatrix}
0.8 & 0.2 \\
0.3 & 0.7
\end{bmatrix} \cdot \begin{bmatrix}
0.8 & 0.2 \\
0.3 & 0.7
\end{bmatrix} = \begin{bmatrix}
(0.8\cdot0.8 + 0.2\cdot0.3) & (0.8\cdot0.2 + 0.2\cdot0.7) \\
(0.3\cdot0.8 + 0.7\cdot0.3) & (0.3\cdot0.2 + 0.7\cdot0.7)
\end{bmatrix} = \begin{bmatrix}
0.70 & 0.30 \\
0.45 & 0.55
\end{bmatrix}
$$

Both methods confirm that $P_{SS}^{(2)} = 0.70$. We can find probabilities for any number of steps by computing higher powers, e.g., $P^{(5)} = P^5$.

## Key Points & Summary

- **Purpose:** Higher transition probabilities ($P_{ij}^{(n)}$) allow us to make predictions about the long-term behavior of a Markov chain.
- **Chapman-Kolmogorov Equations:** The fundamental recursive equations that relate transition probabilities of different step lengths. They work by conditioning on an intermediate state.
- **Matrix Power Method:** The most efficient way to compute all `n`-step probabilities simultaneously is by raising the one-step transition matrix `P` to the `n`-th power ($P^{(n)} = P^n$). This is highly suitable for computational implementation.
- **Interpretation:** The $(i, j)$-th entry of the matrix $P^n$ gives the probability $P_{ij}^{(n)}$.
- **Application:** This concept is crucial for understanding the long-term (steady-state) behavior of systems, which will be covered in the next topic. It has direct applications in performance analysis of computer networks, queueing systems, randomized algorithms, and Google's PageRank algorithm.
