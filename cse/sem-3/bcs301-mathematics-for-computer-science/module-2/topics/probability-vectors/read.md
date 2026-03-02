# Probability Vectors

## Table of Contents

- [Probability Vectors](#probability-vectors)
- [1. Introduction](#1-introduction)
- [2. Core Concepts](#2-core-concepts)
  - [Definition](#definition)
  - [Interpretation](#interpretation)
  - [Connection to Markov Chains](#connection-to-markov-chains)
- [3. Example](#3-example)
- [4. Key Points & Summary](#4-key-points--summary)

## 1. Introduction

In the realm of Mathematics for Computer Science, particularly in stochastic processes like Markov Chains, we need a tool to represent the state of a system at a given point in time. A **Probability Vector** is this fundamental tool. It is a compact mathematical object that encapsulates the likelihood of a system being in each of its possible states. Understanding probability vectors is crucial for analyzing algorithms, network queues, machine learning models, and any system that involves probabilistic transitions.

## 2. Core Concepts

### Definition

A probability vector (or stochastic vector) is a **row vector** whose components are **non-negative real numbers** that sum to **exactly 1**.

Mathematically, a vector $\vec{v} = [v_1, v_2, v_3, ..., v_n]$ is a probability vector if it satisfies two conditions:

1. $0 \leq v_i \leq 1$ for all $i$ (each component is a probability).
2. $v_1 + v_2 + v_3 + ... + v_n = 1$ (the total probability is 1).

### Interpretation

Each component $v_i$ of the vector represents the probability that the system is in state $i$ at a specific time. For example:

- If we have a system with 3 possible states (e.g., `Working`, `Idle`, `Failed`), a probability vector $\vec{v} = [0.7, 0.2, 0.1]$ means:
- P(System is `Working`) = 0.7
- P(System is `Idle`) = 0.2
- P(System is `Failed`) = 0.1

### Connection to Markov Chains

This is where probability vectors become powerful. In a Markov Chain, the state of the system changes over time according to a transition probability matrix ($P$).

If $\vec{v}^{(k)}$ is the **state probability vector** at time step $k$, then the state vector at the next time step, $\vec{v}^{(k+1)}$, is calculated by:
$$\vec{v}^{(k+1)} = \vec{v}^{(k)} \cdot P$$

We multiply the current state vector (a row vector) by the transition matrix (a square matrix) from the **right** to get the new state vector. This operation effectively sums the probabilities of all paths that could lead to each new state.

## 3. Example

Let's model a simple website server. It can be in one of two states:

- $S_1$: Operational
- $S_2$: Crashed

The transition probability matrix $P$ is given below. This matrix reads as: "The probability of going from state $i$ to state $j$".

$$
P = \begin{bmatrix}
0.9 & 0.1 \\ # From Operational to Operational = 0.9, to Crashed = 0.1
0.5 & 0.5 \\ # From Crashed to Operational = 0.5, to Crashed = 0.5
\end{bmatrix}
$$

**Scenario: Suppose the server starts operational. What is the state vector after one time step?**

The initial state is known with certainty: it is operational.
So, the initial state vector is: $\vec{v}^{(0)} = [1, 0]$

To find the state after one step ($k=1$):
$$\vec{v}^{(1)} = \vec{v}^{(0)} \cdot P = [1, 0] \cdot \begin{bmatrix} 0.9 & 0.1 \\ 0.5 & 0.5 \end{bmatrix}$$

Let's compute this:

- Probability of being in $S_1$ (Operational) at $k=1$:
  $= (1 \times 0.9) + (0 \times 0.5) = 0.9$
- Probability of being in $S_2$ (Crashed) at $k=1$:
  $= (1 \times 0.1) + (0 \times 0.5) = 0.1$

Therefore, the new state vector is:
$$\vec{v}^{(1)} = [0.9, 0.1]$$

This is a valid probability vector (0.9 + 0.1 = 1). We can now use $\vec{v}^{(1)}$ to compute $\vec{v}^{(2)} = \vec{v}^{(1)} \cdot P$, and so on, to see how the system evolves over time.

## 4. Key Points & Summary

- **Purpose:** A probability vector represents the probability distribution of a system across its possible states at a given time.
- **Form:** It is always a **row vector** $\vec{v} = [v_1, v_2, ..., v_n]$.
- **Two Rules:**

1.  Each element $v_i$ must satisfy $0 \leq v_i \leq 1$.
2.  The sum of all elements must be 1 ($\sum v_i = 1$).

- **Application:** It is the primary tool for calculating the evolution of state probabilities in a **Markov Chain** through repeated multiplication with the transition matrix: $\vec{v}^{(k+1)} = \vec{v}^{(k)} \cdot P$.
- **Initial State:** Often, the initial vector $\vec{v}^{(0)}$ is a pure state (e.g., $[1, 0, 0, ..., 0]$), meaning the system starts in a known, definite state.
