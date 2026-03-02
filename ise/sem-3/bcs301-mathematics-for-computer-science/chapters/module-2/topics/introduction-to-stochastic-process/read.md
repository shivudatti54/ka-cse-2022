# Introduction to Stochastic Processes

**Subject:** Mathematics for Computer Science
**Module:** Module 2: Joint Probability Distribution & Markov Chain
**Topic:** Introduction to Stochastic Process

## 1. Introduction

In the deterministic world of traditional algorithms, the output is entirely predictable from the input. However, many real-world systems that computer scientists model are inherently **random**. Network traffic, queue wait times, stock prices, and genetic algorithms all involve an element of unpredictability.

A **Stochastic Process** is the mathematical tool we use to describe and analyze systems that evolve randomly over time. It provides a framework for modeling sequences of random events where the future state depends, at least partially, on chance. This foundational concept is crucial for understanding Markov Chains, which are a specific and highly useful type of stochastic process.

## 2. Core Concepts Explained

### What is a Stochastic Process?

Formally, a stochastic process is defined as a collection of random variables, $\{X(t), t \in T\}$, defined on a common probability space.

- **$T$ (Index Set):** This represents "time." It can be discrete (e.g., $T = \{0, 1, 2, 3, ...\}$) or continuous (e.g., $T = [0, \infty)$).
  - **Discrete-Time Process:** The state of the system is observed at specific, countable intervals. $X_n$ denotes the state at step $n$.
  - **Continuous-Time Process:** The state of the system is observed continuously over an interval of time. $X(t)$ denotes the state at time $t$.

- **$X(t)$ (State Space):** The value of the random variable at time $t$ is called the **state**. The set of all possible states is the state space ($S$), which can also be discrete (finite or countable) or continuous.
  - **Discrete-State Process (Chain):** The system has a countable number of possible states (e.g., number of packets in a router buffer, number of users logged in).
  - **Continuous-State Process:** The state can take any value in an interval (e.g., the exact temperature of a CPU).

For this module, we focus primarily on **Discrete-Time, Discrete-State Stochastic Processes**, as this is the category to which Markov Chains belong.

### Key Characteristic: Dependencies

The most important aspect of any stochastic process is how the future state depends on the past states. This dependency structure defines the type of process.

- **Independent Process:** The simplest case, where $X_{n+1}$ is independent of all previous states $X_n, X_{n-1}, ...$. This is often too simplistic for real-world models.
- **Markov Process:** This is a crucial class where the future state depends _only_ on the _present_ state, not on the entire history. This "memoryless" property is formally stated as:
  $P(X_{n+1} = j | X_n = i, X_{n-1} = i_{n-1}, ..., X_0 = i_0) = P(X_{n+1} = j | X_n = i)$
- **Other Processes:** More complex processes might have dependencies on several previous states or even the entire history.

## 3. Example: A Simple Random Walk (Discrete-Time)

This is a classic example of a stochastic process.

- **Description:** A particle moves along a number line. At each discrete time step, it takes a step either to the right or to the left.
- **Index Set ($T$):** Discrete. $n = 0, 1, 2, 3, ...$ (each step number).
- **State Space ($S$):** Discrete. All integers, $\{..., -2, -1, 0, 1, 2, ...\}$ (the particle's position).
- **Random Variables:** Let $X_n$ be the position of the particle after $n$ steps.
- **Probability Structure:** Assume the probability of moving right is $p$ and left is $q = 1-p$. Each step is independent of the others.

**How it works:**

1.  Start at $X_0 = 0$.
2.  At step 1 ($n=1$): Toss a coin.
    - Heads (probability $p$): $X_1 = 0 + 1 = 1$
    - Tails (probability $q$): $X_1 = 0 - 1 = -1$
3.  At step 2 ($n=2$): Toss again. The new position depends on the _current_ position.
    - If $X_1=1$, then $X_2$ could be $2$ (with prob. $p$) or $0$ (with prob. $q$).
    - If $X_1=-1$, then $X_2$ could be $0$ (with prob. $p$) or $-2$ (with prob. $q$).

This process is random (stochastic) and its path, the sequence $\{X_0, X_1, X_2, ...\}$, is a **stochastic process**. Crucially, this specific random walk is also a **Markov process**—the next position $X_{n+1}$ depends only on the current position $X_n$, not on how it got there.

## 4. Key Points & Summary

| **Aspect**            | **Description**                                                                                                                                                          |
| :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Definition**        | A family of random variables $\{X(t), t \in T\}$ representing the evolution of a random system over time.                                                                |
| **Index Set ($T$)**   | Represents time. Can be **discrete** (e.g., steps) or **continuous** (e.g., real-time).                                                                                  |
| **State Space ($S$)** | The set of all possible values the process can take. Can be **discrete** (countable) or **continuous**.                                                                  |
| **Dependency**        | The core of the model. Defines how the future state relates to the past. The **Markov property** (memorylessness) is a key type of dependency.                           |
| **Relevance for CS**  | Essential for modeling queues, network reliability, packet traffic, randomized algorithms, machine learning (e.g., MDPs, Hidden Markov Models), and financial computing. |

**Summary:** A stochastic process is the mathematical framework for modeling any system that behaves randomly over time. It is characterized by its _time domain_ (discrete/continuous), its _state space_ (discrete/continuous), and most importantly, the _probabilistic dependencies between its states_. Understanding this general concept is the first and most critical step toward mastering specific models like the **Markov Chain**, which we will study next.
