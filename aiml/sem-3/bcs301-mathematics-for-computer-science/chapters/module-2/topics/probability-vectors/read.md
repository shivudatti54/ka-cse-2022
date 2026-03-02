Of course. Here is a comprehensive educational module on Probability Vectors, tailored for  Engineering students.

***

### **Module 2: Probability Vectors**

#### **1. Introduction**

In the study of Markov Chains and joint probability distributions, we often deal with systems that can be in one of several distinct states. A **probability vector** is a fundamental mathematical tool that provides a snapshot of the system's state at a given time. It is a compact way to represent a probability distribution over a finite set of outcomes. Understanding probability vectors is crucial for analyzing stochastic processes, which have applications in computer science areas like queueing theory, machine learning algorithms (e.g., PageRank), and network reliability analysis.

#### **2. Core Concepts**

**Definition:**
A probability vector is a **row vector** whose components are **non-negative real numbers** and whose entries **sum to 1**.

If we have a system with `n` possible states, a probability vector `v` is defined as:
$$ v = \begin{bmatrix} v_1 & v_2 & v_3 & \ldots & v_n \end{bmatrix} $$
It must satisfy the following two conditions:
1.  **Non-negativity:** $v_i \geq 0$ for all $i$ ($1 \leq i \leq n$).
2.  **Sum to One:** $v_1 + v_2 + v_3 + \ldots + v_n = 1$.

Each component $v_i$ represents the probability that the system is in state `i`.

**Interpretation:**
The vector `v` gives a complete description of the system's state at a specific moment. For example:
*   $v_1 = 0.25$ means there is a 25% chance the system is in State 1.
*   $v_2 = 0.60$ means there is a 60% chance it is in State 2.
*   And so on for all `n` states.

**Connection to Markov Chains:**
Probability vectors are the building blocks of Markov Chains.
*   **Initial State Vector:** This is a probability vector that defines the starting conditions of the system. For instance, if a computer server can be either `[IDLE, BUSY]`, an initial vector of `v⁽⁰⁾ = [0.9, 0.1]` means it has a 90% chance of starting idle and a 10% chance of starting busy.
*   **State Vector at step `n`:** The state of the system after `n` transitions is also described by a probability vector, often denoted as `v⁽ⁿ⁾`.

#### **3. Example**

Let's consider a simple weather model for Bangalore. Assume the weather can only be in one of two states on any given day: **Sunny (S)** or **Rainy (R)**.

**a) Valid Probability Vectors:**
*   `v = [0.8, 0.2]` → This means P(Sunny) = 0.8 and P(Rainy) = 0.2.
    *   Check: $0.8 \geq 0$, $0.2 \geq 0$, and $0.8 + 0.2 = 1$. **Valid.**
*   `v = [1, 0]` → This represents a day that is certainly sunny. P(Sunny)=1, P(Rainy)=0.
    *   Check: $1 + 0 = 1$. **Valid.**
*   `v = [0.25, 0.75]` → This means P(Sunny) = 0.25 and P(Rainy) = 0.75.
    *   Check: $0.25 + 0.75 = 1$. **Valid.**

**b) Invalid Probability Vectors:**
*   `v = [0.6, 0.5]` → The sum is $0.6 + 0.5 = 1.1 \neq 1$. **Invalid.**
*   `v = [0.9, -0.1]` → Contains a negative probability, which is impossible. **Invalid.**

Now, imagine on a particular day (Day 0), the weather forecast says there's a 100% chance of rain. Our initial state probability vector is:
$$ v^{(0)} = \begin{bmatrix} P(S) & P(R) \end{bmatrix} = \begin{bmatrix} 0 & 1 \end{bmatrix} $$

This vector `v⁽⁰⁾` is our starting point for predicting the weather on subsequent days using a Markov Chain.

#### **4. Key Points & Summary**

| Property | Description |
| :--- | :--- |
| **Format** | A row vector: $v = [v_1, v_2, ..., v_n]$ |
| **Constraint 1** | All entries must be **non-negative** ($v_i \geq 0$). |
| **Constraint 2** | All entries must sum to **exactly 1** ($\sum v_i = 1$). |
| **Interpretation** | Each entry $v_i$ is the probability of the system being in state `i`. |
| **Application** | Used to represent the **initial state** and any **future state** in a Markov Chain. |

**Summary:**
A probability vector is a formal, mathematically precise way to represent a discrete probability distribution. It is defined by two strict rules: non-negativity and the sum of components equaling one. For  students in Computer Science, mastering this concept is essential for working with stochastic models, which are used to simulate and analyze real-world systems that involve randomness, such as data networks, algorithmic processes, and hardware systems. It is the fundamental "state description" used to evolve a Markov Chain through time using transition matrices.