## Table of Contents

- [**Markov Chains**](#markov-chains)
  - [**1. Introduction: What is a Markov Chain?**](#1-introduction-what-is-a-markov-chain)
  - [**2. Core Concepts Explained**](#2-core-concepts-explained)
  - [**3. Example: A Simple Weather Model**](#3-example-a-simple-weather-model)
  - [**4. Steady-State (Stationary) Distribution**](#4-steady-state-stationary-distribution)
  - [**5. Key Points & Summary**](#5-key-points--summary)

## **Markov Chains**

### **1. Introduction: What is a Markov Chain?**

Imagine predicting the future state of a system where the next step depends _only_ on the current step, not on the entire history of how it got there. This powerful concept is the essence of a **Markov Chain**. Named after the Russian mathematician Andrey Markov, these mathematical models are indispensable in computer science for modeling a vast array of systems, including:

- **Algorithm analysis** (e.g., predicting cache hits/misses)
- **Speech recognition** and **natural language processing** (predicting the next word in a sentence)
- **Queueing theory** (modeling network traffic, server loads)
- **PageRank algorithm** (the original foundation of Google's search, modeling web surfing behavior)
- **Game design** (for AI and procedural content generation)

A Markov Chain is a stochastic (random) process that undergoes transitions from one state to another on a state space, with the probability of each transition depending solely on the current state and not on the sequence of events that preceded it. This is called the **Markov Property** or **memorylessness**.

---

### **2. Core Concepts Explained**

#### **a. The State Space and Transitions**

- **State (s_i):** A state represents a possible condition of the system. For example, in a weather model, states could be `Sunny`, `Cloudy`, and `Rainy`.
- **State Space (S):** The set of all possible states, `S = {s1, s2, ..., sn}`.

#### **b. Transition Probabilities and the Matrix**

The core of a Markov Chain is defined by how it moves between states.

- **Transition Probability (p_ij):** The probability of moving from state `i` to state `j` in exactly one step. It is denoted as:
  `p_ij = P(X_{n+1} = j | X_n = i)`

- **Transition Probability Matrix (P):** A square matrix where each entry `(i, j)` is the probability `p_ij`. The key properties of this matrix are:

1.  Every probability `p_ij` must be between `0` and `1` (`0 ≤ p_ij ≤ 1`).
2.  The sum of probabilities in any given row must equal **1**. This is because from any state `i`, the system must transition to _some_ state in the next step.
    $$
    P = \begin{bmatrix}
    p_{11} & p_{12} & \cdots & p_{1n} \\
    p_{21} & p_{22} & \cdots & p_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    p_{n1} & p_{n2} & \cdots & p_{nn}
    \end{bmatrix}
    $$

#### **c. State Classification**

States in a Markov Chain can be categorized, which helps in understanding long-term behavior:

- **Absorbing State:** A state `i` is absorbing if `p_ii = 1`. Once entered, it is impossible to leave (e.g., a "Game Over" state).
- **Recurrent State:** A state that the process will eventually return to with probability 1.
- **Transient State:** A state that there is a non-zero probability the process will _never_ return to.

---

### **3. Example: A Simple Weather Model**

Let's model the weather with states: `S = {Sunny, Rainy}`.

Assume the transition probabilities are:

- If it is **Sunny** today:
- Probability it's **Sunny** tomorrow: `0.8`
- Probability it's **Rainy** tomorrow: `0.2`
- If it is **Rainy** today:
- Probability it's **Sunny** tomorrow: `0.6`
- Probability it's **Rainy** tomorrow: `0.4`

**The Transition Probability Matrix `P` is:**

$$
P = \begin{bmatrix}
 & \text{Sunny} & \text{Rainy} \\
\text{Sunny} & 0.8 & 0.2 \\
\text{Rainy} & 0.6 & 0.4 \\
\end{bmatrix}
$$

**Question:** If it is Rainy today (Day 0), what is the probability it will be Sunny _the day after tomorrow_ (Day 2)?

We represent the initial state as a vector: `v^(0) = [0, 1]` (where index 0 is Sunny, index 1 is Rainy).

The state probabilities after `n` steps are found by multiplying the initial state vector by the transition matrix `P` raised to the power `n`.

**For Day 1:** `v^(1) = v^(0) * P = [0, 1] * P = [0.6, 0.4]`
(There's a 60% chance it will be Sunny on Day 1)

**For Day 2:** `v^(2) = v^(0) * P^2`
We can calculate `P^2`:

$$
P^2 = \begin{bmatrix}
0.8 & 0.2 \\
0.6 & 0.4 \\
\end{bmatrix} \cdot
\begin{bmatrix}
0.8 & 0.2 \\
0.6 & 0.4 \\
\end{bmatrix} =
\begin{bmatrix}
(0.8*0.8 + 0.2*0.6) & (0.8*0.2 + 0.2*0.4) \\
(0.6*0.8 + 0.4*0.6) & (0.6*0.2 + 0.4*0.4) \\
\end{bmatrix} =
\begin{bmatrix}
0.76 & 0.24 \\
0.72 & 0.28 \\
\end{bmatrix}
$$

Now, `v^(2) = [0, 1] * P^2 = [0.72, 0.28]`

**Answer:** There is a **72%** probability that it will be Sunny on Day 2.

---

### **4. Steady-State (Stationary) Distribution**

A fundamental question is: what happens to the system in the long run? Does it settle into a stable distribution of probabilities?

A probability vector `π` is called a **steady-state distribution** if:
`π = π * P`

This means applying the transition matrix no longer changes the distribution; the system has reached a kind of equilibrium. For our weather model, we solve:
`[π_sunny, π_rainy] = [π_sunny, π_rainy] * P`
with the constraint that `π_sunny + π_rainy = 1`.

Solving this yields `π_sunny = 0.75` and `π_rainy = 0.25`. This means, regardless of today's weather, in the long run, 75% of the days will be sunny and 25% will be rainy.

---

### **5. Key Points & Summary**

| **Concept**               | **Description**                                                              | **Importance**                                                        |
| :------------------------ | :--------------------------------------------------------------------------- | :-------------------------------------------------------------------- |
| **Markov Property**       | The future state depends only on the present state, not on the past.         | Provides model simplicity and computational tractability.             |
| **State Space (S)**       | The set of all possible conditions of the system.                            | Defines what you are modeling.                                        |
| **Transition Matrix (P)** | A matrix where `P[i][j]` is the probability of moving from state `i` to `j`. | **Core** of the model. Encapsulates all dynamics. Rows must sum to 1. |
| **n-Step Probability**    | Probability calculated using `P^n`.                                          | Predicts state after `n` transitions.                                 |
| **Steady-State (π)**      | A distribution vector such that `π = π * P`.                                 | Describes the long-term, equilibrium behavior of the system.          |

**Summary:** A Markov Chain is a memoryless random process defined by its states and a transition probability matrix. It is a powerful tool for modeling systems where the next state is probabilistically determined by the current state. Understanding how to represent them via matrices, calculate multi-step behaviors, and find their steady-state distributions is crucial for applications across computer science and engineering.
