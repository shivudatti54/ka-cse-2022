# Stochastic Matrices

## Table of Contents

- [Stochastic Matrices](#stochastic-matrices)
- [Introduction](#introduction)
- [Core Concepts](#core-concepts)
  - [1. Definition and Properties](#1-definition-and-properties)
  - [2. State Vectors](#2-state-vectors)
  - [3. The Power of a Stochastic Matrix](#3-the-power-of-a-stochastic-matrix)
- [Example: The Weather Model](#example-the-weather-model)
- [Key Points & Summary](#key-points--summary)

## Introduction

In the study of **Mathematics for Computer Science**, particularly within probability theory and modeling sequential processes, Stochastic Matrices emerge as a fundamental tool. They form the backbone of **Markov Chains**, which are powerful mathematical systems used to model random processes that evolve over time. Understanding stochastic matrices is crucial for applications ranging from algorithm analysis (e.g., PageRank) and queueing theory to game AI and speech recognition.

---

## Core Concepts

### 1. Definition and Properties

A **stochastic matrix** (also called a probability matrix, transition matrix, or Markov matrix) is a square matrix used to describe the transitions of a Markov chain.

A square matrix **P = [pᵢⱼ]** of size `n x n` is called a **stochastic matrix** if it satisfies two key properties:

1. **Non-negativity:** Every entry is a probability, hence non-negative.
   `0 ≤ pᵢⱼ ≤ 1` for all `i, j`.

2. **Row Normalization:** The sum of the probabilities in each row must be 1. This ensures that from any state `i`, the next step must go to _some_ state.
   `∑ⱼ pᵢⱼ = 1` for every row `i`.

In essence, the entry `pᵢⱼ` represents the probability of transitioning from state `i` to state `j` in one step.

### 2. State Vectors

A **state vector** (or probability vector) **x** is a column vector that represents a probability distribution over all possible states. Its entries are non-negative and sum to 1.

If **xₖ** is the state vector at time `k`, then the state vector at the next time step, `k+1`, is calculated by multiplying by the stochastic matrix:
**xₖ₊₁** = **P** \* **xₖ**

This simple equation is the engine of a Markov chain, allowing us to project the state of the system forward in time.

### 3. The Power of a Stochastic Matrix

To find the probability of moving from state `i` to state `j` in exactly `m` steps, we use the `m`-step transition matrix, which is simply the matrix **P** raised to the power `m` (**Pᵐ**).

The entry `(Pᵐ)ᵢⱼ` gives the probability of being in state `j` after `m` steps, starting from state `i`.

---

## Example: The Weather Model

Let's model a simple weather system where a day is either **Sunny (S)** or **Rainy (R)**. The probabilities for the next day's weather are:

- If today is Sunny (S), probability of tomorrow being Sunny is 0.8 and Rainy is 0.2.
- If today is Rainy (R), probability of tomorrow being Sunny is 0.6 and Rainy is 0.4.

We can define our states in order: `[Sunny, Rainy]`.

The stochastic (transition) matrix **P** is:

| From \ To | **S** | **R** |
| :-------- | :---: | :---: |
| **S**     |  0.8  |  0.2  |
| **R**     |  0.6  |  0.4  |

Or, written as a matrix:
**P** = `[ [0.8, 0.2], `
` [0.6, 0.4] ]`

**Row 1 (S):** `0.8 + 0.2 = 1`
**Row 2 (R):** `0.6 + 0.4 = 1`
It satisfies the properties of a stochastic matrix.

**Question:** If it is sunny today (100% probability), what is the probability distribution for the day after tomorrow?

**Step 1:** Represent today's state as a vector: **x₀** = `[1, 0]ᵀ` (100% sunny, 0% rainy).

**Step 2:** Find the state vector for tomorrow (**x₁**) and the day after (**x₂**).
**x₁** = **P** _ **x₀** = `[ [0.8, 0.2], ` _ `[1, 0]ᵀ` = `[(0.8*1 + 0.2*0), (0.6*1 + 0.4*0)]ᵀ` = `[0.8, 0.6]ᵀ`
`[0.6, 0.4] ]`
So, tomorrow: P(Sunny)=0.8, P(Rainy)=0.2.

**Step 3:** Find the state for the day after tomorrow.
**x₂** = **P** _ **x₁** = **P²** _ **x₀**
Let's calculate **P²**:
**P²** = **P** * **P** = `[ [0.8*0.8 + 0.2*0.6, 0.8*0.2 + 0.2*0.4], `=`[ [0.64 + 0.12, 0.16 + 0.08], `
 ` [0.6*0.8 + 0.4*0.6, 0.6*0.2 + 0.4\*0.4] ]` ` [0.48 + 0.24, 0.12 + 0.16] ]` =`[ [0.76, 0.24], `
 ` [0.72, 0.28] ]`

Now, **x₂** = **P²** _ **x₀** = `[ [0.76, 0.24], ` _ `[1, 0]ᵀ` = `[0.76, 0.72]ᵀ`? Wait, no!
`[0.72, 0.28] ]`
Correct calculation: The first _column_ of **P²** gives the probabilities of ending in state _S_ after 2 steps, starting from each state. Since we start from S, we need the top-left entry.
**P(2 steps from S to S)** = `(P²)₁₁` = **0.76**
**P(2 steps from S to R)** = `(P²)₁₂` = **0.24**

Therefore, the probability that it is sunny the day after tomorrow is **0.76**, and rainy is **0.24**.

---

## Key Points & Summary

- **Definition:** A stochastic matrix is a square matrix of probabilities where each row sums to 1.
- **Purpose:** It defines the one-step transition probabilities between states in a Markov chain.
- **State Evolution:** The future state vector **xₖ₊₁** is found by multiplying the current state vector **xₖ** by the stochastic matrix: **xₖ₊₁ = P ⋅ xₖ**.
- **Multi-step Transitions:** The `m`-step transition probabilities are contained in the matrix **Pᵐ**.
- **Applications:** Crucial for modeling any system with probabilistic state transitions, including randomized algorithms, network traffic, finance, and machine learning (Hidden Markov Models).
- **Next Step:** This concept leads directly to analyzing the long-term behavior of a system, such as finding the **steady-state distribution** of a Markov chain.
