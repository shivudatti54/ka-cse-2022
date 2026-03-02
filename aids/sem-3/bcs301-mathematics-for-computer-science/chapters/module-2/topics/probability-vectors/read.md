Of course. Here is a comprehensive educational note on Probability Vectors for  Engineering students.

# Module 2: Probability Vectors

## Introduction

In Mathematics for Computer Science, particularly in the study of stochastic processes like Markov Chains, we often deal with systems that can be in one of several states. A **probability vector** is a fundamental tool used to describe the likelihood of a system being in each of its possible states at a given point in time. It provides a complete and concise probabilistic description of the system, serving as the starting point for predicting its future behavior.

## Core Concepts

### 1. Definition

A probability vector is a **row vector** whose entries are non-negative real numbers and **sum to 1**.

Formally, a vector **v** = [v₁, v₂, v₃, ..., vₙ] is a probability vector if and only if:
1.  **vᵢ ≥ 0** for all *i* (each probability is non-negative).
2.  **v₁ + v₂ + ... + vₙ = 1** (the sum of all probabilities is 1).

### 2. Interpretation

Each entry *vᵢ* in the vector represents the probability of the system being in state *i*. For example, if a system has three possible states (e.g., "Working", "Idle", "Failed"), its state can be described by a probability vector **v** = [p, q, r], where:
*   `p` is the probability the system is "Working".
*   `q` is the probability the system is "Idle".
*   `r` is the probability the system is "Failed".
And, crucially, **p + q + r = 1**.

### 3. Connection to Markov Chains

Probability vectors are the building blocks of **Discrete-Time Markov Chains (DTMC)**. In a DTMC:
*   The **state probability vector** at step *k* is denoted as **π⁽ᵏ⁾**. This vector describes the probability distribution over all states at time *k*.
*   The evolution of the system is governed by the **transition probability matrix P**. The state vector at the next step (*k+1*) is calculated from the current state vector (*k*) using the matrix multiplication:
    **π⁽ᵏ⁺¹⁾ = π⁽ᵏ⁾ P**

This equation is the heart of a Markov Chain, and it shows how the probability vector gets transformed at each time step.

### 4. The Initial State Vector

The process begins with an **initial probability vector**, often denoted as **π⁽⁰⁾**. This vector defines the starting state of the system. It could represent a known state (e.g., the system always starts in state 1) or an initial distribution of probabilities.

## Examples

### Example 1: Valid Probability Vectors

Which of the following are valid probability vectors?
a) [0.2, 0.5, 0.3]
b) [0.7, 0.4, -0.1]
c) [0.25, 0.25, 0.25, 0.25]
d) [1, 0, 0]

**Solution:**
*   **a)** Valid. All entries are non-negative (≥0) and 0.2 + 0.5 + 0.3 = 1.
*   **b)** Invalid. The third entry is negative.
*   **c)** Valid. All entries are non-negative and sum to 1. This is a **uniform distribution**.
*   **d)** Valid. This is a **certainty vector**. The system is definitely in state 1 (probability = 1).

### Example 2: Application in a Simple Markov Chain

Imagine a machine that can be in two states: **Running (R)** or **Under Maintenance (M)**. Its behavior is governed by the transition probability matrix **P**:

| From/To | R     | M     |
| :------ | :---- | :---- |
| **R**   | 0.7   | 0.3   |
| **M**   | 0.8   | 0.2   |

This means, for example, if it's Running today, there's a 70% chance it will be Running tomorrow and a 30% chance it will be Under Maintenance.

**Scenario:** The machine starts on Monday completely repaired and running. Therefore, the initial state vector **π⁽⁰⁾** is:
**π⁽⁰⁾** = [ P(R) , P(M) ] = [1, 0]

**Question:** What is the probability vector for Tuesday (**π⁽¹⁾**)?

**Calculation:**
**π⁽¹⁾ = π⁽⁰⁾ P** = [1, 0] * **P** = [1, 0] * `[ [0.7, 0.3], [0.8, 0.2] ]`
                = [ (1×0.7 + 0×0.8) , (1×0.3 + 0×0.2) ]
                = [0.7, 0.3]

**Interpretation:** On Tuesday, the probability the machine is Running is **0.7**, and the probability it is Under Maintenance is **0.3**. Notice the sum is 1, confirming it's a valid probability vector.

## Key Points & Summary

*   **Definition:** A probability vector is a row vector with non-negative entries that sum to 1.
*   **Purpose:** It describes the probability distribution of a system across its possible states at a specific time.
*   **Initial Vector:** The **π⁽⁰⁾** vector defines the starting condition of a stochastic process.
*   **Markov Chains:** The core operation is **π⁽ⁿ⁺¹⁾ = π⁽ⁿ⁾ P**, where **P** is the transition matrix. This rule defines the system's evolution over time.
*   **Validation:** To check if a vector is a probability vector, ensure all elements are ≥ 0 and their sum is exactly 1.

Probability vectors provide the language to quantify uncertainty in state-based systems, making them indispensable for modeling queues, networks, algorithms, and various other applications in computer science and engineering.