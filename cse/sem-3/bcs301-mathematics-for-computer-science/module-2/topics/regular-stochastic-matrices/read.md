## Table of Contents

- [Module 2: Regular Stochastic Matrices](#module-2-regular-stochastic-matrices)
- [1. Introduction](#1-introduction)
- [2. Core Concepts](#2-core-concepts)
  - [What is a Stochastic Matrix?](#what-is-a-stochastic-matrix)
  - [Defining a Regular Stochastic Matrix](#defining-a-regular-stochastic-matrix)
- [3. Key Properties & The Steady-State Vector](#3-key-properties--the-steady-state-vector)
- [4. Example](#4-example)
- [5. Key Points & Summary](#5-key-points--summary)

---

# Module 2: Regular Stochastic Matrices

## 1. Introduction

In the study of Markov Chains, we model systems that transition from one state to another with certain probabilities. The engine behind this model is the **Transition Probability Matrix (TPM)**, `P`. A special and highly important class of these matrices is known as **Regular Stochastic Matrices**. Understanding their properties is crucial because they guarantee the Markov Chain will settle into a stable, long-term behavior, regardless of its starting state. This has profound applications in computer science, from Google's PageRank algorithm to predicting network traffic and analyzing randomized algorithms.

## 2. Core Concepts

### What is a Stochastic Matrix?

First, a quick recap. A square matrix `P` is called a **Stochastic Matrix** (or probability matrix) if:

1. Every entry `p_ij` is a probability, i.e., `0 ≤ p_ij ≤ 1`.
2. The sum of the entries in each row is 1. That is, `Σ_j p_ij = 1` for every row `i`.

This means each row represents a probability distribution over the possible next states.

### Defining a Regular Stochastic Matrix

A stochastic matrix `P` is said to be **regular** if some power of the matrix `P^k` (for some integer `k ≥ 1`) has **all entries strictly greater than zero**.

**In simpler terms:** If you can multiply the matrix by itself enough times (`k` times) and eventually get a new matrix where every single entry is positive (not zero), then the original matrix `P` is regular.

**Why is this important?** This property of "every entry being positive" means that it is possible to get from _any_ state `i` to _any_ state `j` in exactly `k` steps. The system is interconnected enough that no state is isolated or periodic in a way that prevents eventual access.

## 3. Key Properties & The Steady-State Vector

The most significant consequence of a Markov Chain having a regular transition matrix is the existence of a unique **steady-state vector** (or equilibrium vector).

Let `P` be a regular stochastic matrix. Then:

- There exists a unique probability vector `π` such that `πP = π`.
- This vector `π` is called the steady-state probability vector.
- Regardless of the initial state vector `v^(0)`, the state vectors `v^(k)` will converge to `π` as the number of steps `k` becomes large.
  `v^(0) * P^k → π` as `k → ∞`

**How to find `π`?**
The steady-state vector `π` is found by solving the system of linear equations:
`πP = π` and `π_1 + π_2 + ... + π_n = 1`
This can be rewritten as `π(P - I) = 0`, where `I` is the identity matrix. We solve this homogeneous system subject to the sum of probabilities being 1.

## 4. Example

Consider a simple weather model with two states: Sunny (S) and Rainy (R). Let the transition probability matrix be:

`P = [[0.7, 0.3],`
`[0.4, 0.6]]`

- **Is this matrix stochastic?** Yes, each row sums to 1.
- **Is it regular?** Let's check `P^1`. It already has all entries > 0. Therefore, it is regular.

Now, let's find the steady-state vector `π = [π_s, π_r]`.

Set up the equation `πP = π`:
`[π_s, π_r] * [[0.7, 0.3], [0.4, 0.6]] = [π_s, π_r]`

This gives us the system:

1. `0.7π_s + 0.4π_r = π_s`
2. `0.3π_s + 0.6π_r = π_r`
3. `π_s + π_r = 1`

Simplify equation 1:
`0.7π_s + 0.4π_r - π_s = 0 => -0.3π_s + 0.4π_r = 0`

Simplify equation 2:
`0.3π_s + 0.6π_r - π_r = 0 => 0.3π_s - 0.4π_r = 0`

Notice both simplified equations `-0.3π_s + 0.4π_r = 0` and `0.3π_s - 0.4π_r = 0` are equivalent. So we use one of them with the total probability equation:
`0.3π_s = 0.4π_r` and `π_s + π_r = 1`

Solving, we get `π_s = 4/7 ≈ 0.571` and `π_r = 3/7 ≈ 0.429`.

**Interpretation:** In the long run, regardless of today's weather, about 57.1% of the days will be sunny and 42.9% will be rainy.

## 5. Key Points & Summary

- **Definition:** A stochastic matrix `P` is **regular** if some power `P^k` has all entries > 0.
- **Implication:** Regularity means every state is eventually accessible from every other state.
- **Steady-State:** Regular matrices guarantee a **unique steady-state vector** `π` where `πP = π`.
- **Convergence:** For any initial state, the system will converge to this steady-state vector `π` over time.
- **Application:** This concept is fundamental for analyzing the long-term behavior of systems in areas like queueing theory, network analysis, information retrieval, and machine learning.

**Check for Regularity:** If you can find a path of some length from every state to every other state (i.e., the Markov chain is **irreducible** and **aperiodic**), then its transition matrix is regular. The "all positive entries" condition of `P^k` is a definitive test.
