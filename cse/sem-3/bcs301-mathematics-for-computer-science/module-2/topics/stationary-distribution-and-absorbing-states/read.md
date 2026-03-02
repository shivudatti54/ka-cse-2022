# Stationary Distribution of Regular Markov Chains and Absorbing States

## Table of Contents

- [Stationary Distribution of Regular Markov Chains and Absorbing States](#stationary-distribution-of-regular-markov-chains-and-absorbing-states)
- [1. Introduction](#1-introduction)
- [2. Stationary (Steady-State) Distribution](#2-stationary-steady-state-distribution)
  - [2.1 Definition](#21-definition)
  - [2.2 How to Find the Stationary Distribution](#22-how-to-find-the-stationary-distribution)
  - [2.3 Relationship to Regular Stochastic Matrices](#23-relationship-to-regular-stochastic-matrices)
- [3. Absorbing States and Absorbing Markov Chains](#3-absorbing-states-and-absorbing-markov-chains)
  - [3.1 Definition of an Absorbing State](#31-definition-of-an-absorbing-state)
  - [3.2 Definition of an Absorbing Markov Chain](#32-definition-of-an-absorbing-markov-chain)
  - [3.3 Canonical Form of an Absorbing Chain](#33-canonical-form-of-an-absorbing-chain)
  - [3.4 The Fundamental Matrix](#34-the-fundamental-matrix)
  - [3.5 Key Results from the Fundamental Matrix](#35-key-results-from-the-fundamental-matrix)
- [4. Worked Examples](#4-worked-examples)
  - [Example 1: Finding the Stationary Distribution of a Regular Markov Chain](#example-1-finding-the-stationary-distribution-of-a-regular-markov-chain)
  - [Example 2: Finding the Stationary Distribution of a 3-State Chain](#example-2-finding-the-stationary-distribution-of-a-3-state-chain)
  - [Example 3: Absorbing Markov Chain -- Fundamental Matrix](#example-3-absorbing-markov-chain----fundamental-matrix)
- [5. Comparison: Regular Chains vs. Absorbing Chains](#5-comparison-regular-chains-vs-absorbing-chains)
- [6. Applications in Computer Science](#6-applications-in-computer-science)
- [7. Key Formulas Summary](#7-key-formulas-summary)
- [8. Important Points for Exams](#8-important-points-for-exams)

## 1. Introduction

In the study of Markov Chains, one of the most important questions is: **What happens in the long run?** Does the system settle into a predictable pattern, or does it get trapped in certain states? This topic answers both questions by introducing two fundamental concepts: the **Stationary (Steady-State) Distribution** of regular Markov chains, and **Absorbing States** and their associated chains.

## 2. Stationary (Steady-State) Distribution

### 2.1 Definition

A probability vector `pi = [pi_1, pi_2, ..., pi_n]` is called a **stationary distribution** (or steady-state distribution, or equilibrium distribution) of a Markov chain with transition matrix `P` if it satisfies two conditions:

1. **Invariance condition:** `pi * P = pi`
2. **Probability condition:** `pi_1 + pi_2 + ... + pi_n = 1`, where each `pi_i >= 0`

**Interpretation:** If the Markov chain starts with the distribution `pi`, then after one transition (or any number of transitions), the distribution remains exactly `pi`. The system is in equilibrium -- it has "settled down."

### 2.2 How to Find the Stationary Distribution

To find `pi` for a given transition matrix `P`, follow these steps:

**Step 1:** Write out the equation `pi * P = pi` as a system of linear equations.

For a 2-state system with `pi = [pi_1, pi_2]` and transition matrix:

```
P = | p_11 p_12 |
 | p_21 p_22 |
```

The equation `pi * P = pi` expands to:

- `pi_1 * p_11 + pi_2 * p_21 = pi_1`
- `pi_1 * p_12 + pi_2 * p_22 = pi_2`

**Step 2:** Rearrange each equation by bringing all terms to one side. This gives the homogeneous system `pi * (P - I) = 0`.

**Step 3:** Since the equations from Step 2 are linearly dependent (they are not all independent), replace one of them with the normalizing constraint:

- `pi_1 + pi_2 + ... + pi_n = 1`

**Step 4:** Solve the resulting system of equations.

### 2.3 Relationship to Regular Stochastic Matrices

Recall that a stochastic matrix `P` is **regular** if some power `P^k` (for some integer `k >= 1`) has all strictly positive entries.

**Fundamental Theorem for Regular Markov Chains:**

If `P` is a regular stochastic matrix, then:

1. `P` has a **unique** stationary distribution `pi`.
2. Every entry of `pi` is strictly positive (`pi_i > 0` for all `i`).
3. The powers `P^k` converge to a matrix `W` where every row equals `pi`:

```
P^k --> W = | pi_1 pi_2 ... pi_n |
| pi_1 pi_2 ... pi_n |
| ... ... ... ... |
| pi_1 pi_2 ... pi_n |
```

4. Regardless of the initial state distribution `v^(0)`, the distribution after `k` steps converges to `pi`:
   `v^(0) * P^k --> pi` as `k --> infinity`

**Key insight:** Regularity guarantees convergence to a unique steady state. Without regularity, the chain may oscillate, have multiple stationary distributions, or never converge.

---

## 3. Absorbing States and Absorbing Markov Chains

### 3.1 Definition of an Absorbing State

A state `i` in a Markov chain is called an **absorbing state** if the probability of remaining in that state is 1:

```
p_ii = 1
```

This means that once the chain enters state `i`, it can never leave. All other transition probabilities from state `i` are zero: `p_ij = 0` for all `j != i`.

**In the transition matrix:** An absorbing state corresponds to a row that has `1` on the diagonal and `0` everywhere else.

### 3.2 Definition of an Absorbing Markov Chain

A Markov chain is called an **absorbing Markov chain** if:

1. It has **at least one absorbing state**, and
2. From every non-absorbing (transient) state, it is **possible to reach** some absorbing state (in one or more steps).

### 3.3 Canonical Form of an Absorbing Chain

For an absorbing Markov chain with `r` absorbing states and `t` transient states (`t = n - r`), the transition matrix can be rearranged into **canonical form**:

```
P = | I O |
 | R Q |
```

Where:

- `I` is an `r x r` identity matrix (absorbing states to absorbing states)
- `O` is an `r x t` zero matrix (absorbing states to transient states -- impossible transitions)
- `R` is a `t x r` matrix (transient states to absorbing states)
- `Q` is a `t x t` matrix (transient states to transient states)

### 3.4 The Fundamental Matrix

The **fundamental matrix** `N` of an absorbing Markov chain is defined as:

```
N = (I - Q)^(-1) = I + Q + Q^2 + Q^3 + ...
```

Where `I` is the `t x t` identity matrix and `Q` is the submatrix from the canonical form.

**Interpretation of N:**

- The entry `N_ij` gives the **expected number of times** the chain visits transient state `j` before being absorbed, given that it starts in transient state `i`.

### 3.5 Key Results from the Fundamental Matrix

1. **Expected number of steps before absorption:** The sum of the entries in row `i` of `N` gives the expected total number of steps before the chain is absorbed, starting from transient state `i`. Formally: `t_i = sum of N_ij over all j`.

2. **Absorption probabilities:** The matrix `B = N * R` gives the probabilities of being absorbed into each absorbing state. Entry `B_ij` is the probability of eventually being absorbed into absorbing state `j`, starting from transient state `i`.

---

## 4. Worked Examples

### Example 1: Finding the Stationary Distribution of a Regular Markov Chain

**Problem:** A system has two states A and B with the transition matrix:

```
 A B
A | 0.7 0.3 |
B | 0.4 0.6 |
```

Find the stationary distribution.

**Solution:**

**Step 1:** Let `pi = [pi_A, pi_B]`. Write `pi * P = pi`:

```
pi_A * 0.7 + pi_B * 0.4 = pi_A ... (i)
pi_A * 0.3 + pi_B * 0.6 = pi_B ... (ii)
```

**Step 2:** Simplify equation (i):

```
0.7 * pi_A + 0.4 * pi_B = pi_A
0.4 * pi_B = pi_A - 0.7 * pi_A
0.4 * pi_B = 0.3 * pi_A
```

So: `pi_A / pi_B = 0.4 / 0.3 = 4/3`

(Equation (ii) gives the same relation: `0.3 * pi_A = 0.4 * pi_B`, confirming consistency.)

**Step 3:** Use the normalizing condition:

```
pi_A + pi_B = 1
```

Substitute `pi_A = (4/3) * pi_B`:

```
(4/3) * pi_B + pi_B = 1
(7/3) * pi_B = 1
pi_B = 3/7
pi_A = 4/7
```

**Answer:** The stationary distribution is `pi = [4/7, 3/7]` or approximately `[0.571, 0.429]`.

**Verification:** Check `pi * P = pi`:

```
[4/7, 3/7] * [[0.7, 0.3], [0.4, 0.6]]
= [4/7 * 0.7 + 3/7 * 0.4, 4/7 * 0.3 + 3/7 * 0.6]
= [2.8/7 + 1.2/7, 1.2/7 + 1.8/7]
= [4/7, 3/7] (Verified)
```

**Interpretation:** In the long run, the system spends 4/7 of its time in state A and 3/7 of its time in state B.

---

### Example 2: Finding the Stationary Distribution of a 3-State Chain

**Problem:** Consider a Markov chain with three states {1, 2, 3} and transition matrix:

```
 1 2 3
1 | 0.5 0.25 0.25 |
2 | 0.5 0.0 0.5 |
3 | 0.25 0.25 0.5 |
```

Find the stationary distribution.

**Solution:**

**Step 1:** Let `pi = [pi_1, pi_2, pi_3]`. Write `pi * P = pi`:

```
0.5*pi_1 + 0.5*pi_2 + 0.25*pi_3 = pi_1 ... (i)
0.25*pi_1 + 0.0*pi_2 + 0.25*pi_3 = pi_2 ... (ii)
0.25*pi_1 + 0.5*pi_2 + 0.5*pi_3 = pi_3 ... (iii)
```

**Step 2:** Simplify:

From (i): `-0.5*pi_1 + 0.5*pi_2 + 0.25*pi_3 = 0` --> `-2*pi_1 + 2*pi_2 + pi_3 = 0` ... (i')

From (ii): `0.25*pi_1 - pi_2 + 0.25*pi_3 = 0` --> `pi_1 - 4*pi_2 + pi_3 = 0` ... (ii')

From (iii): `0.25*pi_1 + 0.5*pi_2 - 0.5*pi_3 = 0` --> `pi_1 + 2*pi_2 - 2*pi_3 = 0` ... (iii')

**Step 3:** From (ii'): `pi_1 = 4*pi_2 - pi_3`

Substitute into (iii'): `(4*pi_2 - pi_3) + 2*pi_2 - 2*pi_3 = 0` --> `6*pi_2 - 3*pi_3 = 0` --> `pi_3 = 2*pi_2`

So: `pi_1 = 4*pi_2 - 2*pi_2 = 2*pi_2`

**Step 4:** Use normalization: `pi_1 + pi_2 + pi_3 = 1`

```
2*pi_2 + pi_2 + 2*pi_2 = 1
5*pi_2 = 1
pi_2 = 1/5
```

Therefore: `pi_1 = 2/5`, `pi_2 = 1/5`, `pi_3 = 2/5`

**Answer:** The stationary distribution is `pi = [2/5, 1/5, 2/5]` or `[0.4, 0.2, 0.4]`.

---

### Example 3: Absorbing Markov Chain -- Fundamental Matrix

**Problem:** Consider a Markov chain with states {1, 2, 3} where state 3 is absorbing:

```
 1 2 3
1 | 0.5 0.25 0.25 |
2 | 0.0 0.5 0.5 |
3 | 0.0 0.0 1.0 |
```

(a) Write the canonical form.
(b) Find the fundamental matrix N.
(c) Find the expected number of steps to absorption from each transient state.

**Solution:**

State 3 is absorbing (row 3 has `p_33 = 1`). States 1 and 2 are transient.

**(a) Canonical Form:**

Rearranging with absorbing state first (state 3), then transient states (1, 2):

```
P = | I O | = | 1.0 0.0 0.0 |
 | R Q | | 0.25 0.5 0.25 |
 | 0.5 0.0 0.5 |
```

So:

```
Q = | 0.5 0.25 | R = | 0.25 |
 | 0.0 0.5 | | 0.5 |
```

**(b) Fundamental Matrix:**

```
I - Q = | 1-0.5 -0.25 | = | 0.5 -0.25 |
 | -0.0 1-0.5 | | 0.0 0.5 |
```

Find the inverse of `(I - Q)`:

```
det(I - Q) = 0.5 * 0.5 - (-0.25)(0.0) = 0.25
```

```
N = (I - Q)^(-1) = (1/0.25) * | 0.5 0.25 | = | 2.0 1.0 |
 | 0.0 0.5 | | 0.0 2.0 |
```

**(c) Expected steps to absorption:**

Sum the rows of N:

- Starting from state 1: `2.0 + 1.0 = 3.0` steps
- Starting from state 2: `0.0 + 2.0 = 2.0` steps

**Absorption probabilities:** Since there is only one absorbing state (state 3), `B = N * R`:

```
B = | 2.0 1.0 | * | 0.25 | = | 2.0*0.25 + 1.0*0.5 | = | 1.0 |
 | 0.0 2.0 | | 0.5 | | 0.0*0.25 + 2.0*0.5 | | 1.0 |
```

Both transient states are absorbed into state 3 with probability 1, which confirms this is indeed an absorbing chain.

---

## 5. Comparison: Regular Chains vs. Absorbing Chains

| Property                    | Regular Markov Chain                             | Absorbing Markov Chain                        |
| --------------------------- | ------------------------------------------------ | --------------------------------------------- |
| **Absorbing states**        | None                                             | At least one                                  |
| **Long-run behavior**       | Converges to unique stationary distribution `pi` | Eventually gets trapped in absorbing state(s) |
| **Stationary distribution** | Unique, all entries positive                     | Not unique; concentrated on absorbing states  |
| **Key analysis tool**       | Solving `pi*P = pi`                              | Fundamental matrix `N = (I - Q)^(-1)`         |
| **All states visited?**     | Yes, with positive probability                   | Transient states visited finitely many times  |

---

## 6. Applications in Computer Science

1. **Google PageRank:** The PageRank algorithm models web browsing as a regular Markov chain. The stationary distribution gives the importance (rank) of each web page.

2. **Random Walks on Graphs:** Analyzing connectivity, cover time, and mixing time of random walks uses stationary distributions.

3. **Gambler's Ruin Problem:** A classic absorbing Markov chain problem where the absorbing states represent going broke or reaching a target wealth.

4. **Reliability Engineering:** Modeling system states (operational, degraded, failed) where "failed" is an absorbing state. The fundamental matrix provides expected time to failure.

5. **Natural Language Processing:** Hidden Markov Models use stationary distributions for speech recognition and text generation.

6. **Network Protocols:** Modeling packet transmission where successful delivery is an absorbing state, and the fundamental matrix gives expected retransmission counts.

---

## 7. Key Formulas Summary

| Formula             | Description                                 |
| ------------------- | ------------------------------------------- |
| `pi * P = pi`       | Stationary distribution condition           |
| `sum(pi_i) = 1`     | Normalization condition                     |
| `p_ii = 1`          | Absorbing state condition                   |
| `N = (I - Q)^(-1)`  | Fundamental matrix of absorbing chain       |
| `t_i = sum_j(N_ij)` | Expected steps to absorption from state `i` |
| `B = N * R`         | Absorption probability matrix               |

---

## 8. Important Points for Exams

1. Always verify that a matrix is stochastic (rows sum to 1) before proceeding.
2. When solving `pi * P = pi`, remember that the equations are dependent -- you must replace one with the normalization condition `sum(pi_i) = 1`.
3. For absorbing chains, clearly identify absorbing and transient states before writing the canonical form.
4. The fundamental matrix `N` always exists for a valid absorbing Markov chain because `(I - Q)` is always invertible when `Q` comes from transient states.
5. Always verify your stationary distribution by checking `pi * P = pi` and `sum(pi_i) = 1`.
