Of course. Here is a comprehensive educational module on Markov Chains for  Engineering students.

# Module 2: Markov Chains

## Introduction

In the previous section, we dealt with **Joint Probability Distributions**, which describe the simultaneous behavior of two or more random variables. Now, we move to a powerful application of probability theory: **Markov Chains**. A Markov Chain is a stochastic model that describes a sequence of possible events where the probability of each event depends **only** on the state attained in the previous event. This "memoryless" property, called the Markov Property, makes them incredibly useful for modeling systems in computer science, such as queueing theory, page ranking algorithms (like Google's PageRank), statistical modeling, and game theory.

## Core Concepts

### 1. The Markov Property

The fundamental idea behind a Markov chain is its lack of memory. Formally, the **Markov Property** states:

> The conditional probability of moving to the next state $X_{n+1}$ depends only on the current state $X_n$, and not on the sequence of events that preceded it.

Mathematically, this is expressed as:
$$P(X_{n+1} = j | X_n = i, X_{n-1} = i_{n-1}, ..., X_0 = i_0) = P(X_{n+1} = j | X_n = i)$$

### 2. State Space and Transition Probabilities

*   **State Space ($S$)**: The set of all possible states a system can be in. It can be finite (e.g., {Sunny, Rainy}) or infinite. We denote states as $i, j, k,$ etc.
*   **Transition Probability ($p_{ij}$)**: The probability of moving from state $i$ to state $j$ in one step.
    $$p_{ij} = P(X_{n+1} = j | X_n = i)$$
*   **Transition Probability Matrix ($P$)**: A square matrix that contains all the transition probabilities for a finite state space. The element in the $i^{th}$ row and $j^{th}$ column is $p_{ij}$.

**Properties of the Transition Matrix:**
1.  Every entry is a probability: $0 \leq p_{ij} \leq 1$
2.  The sum of probabilities in each row must be 1: $\sum_{j} p_{ij} = 1$ for all $i$.

### 3. n-Step Transitions and Chapman-Kolmogorov Equations

We are often interested in the probability of going from state $i$ to state $j$ in exactly $n$ steps, denoted as $p_{ij}^{(n)}$.

The **Chapman-Kolmogorov Equations** provide a way to compute these multi-step probabilities. They state that the probability of going from $i$ to $j$ in $m+n$ steps is the sum of the probabilities of going from $i$ to some intermediate state $k$ in $m$ steps, and then from $k$ to $j$ in $n$ steps, summed over all possible $k$.
$$p_{ij}^{(m+n)} = \sum_{k \in S} p_{ik}^{(m)} p_{kj}^{(n)}$$

A crucial result is that the $n$-step transition matrix is simply the one-step transition matrix $P$ raised to the $n^{th}$ power:
$$P^{(n)} = P^n$$

### 4. Classification of States

*   **Absorbing State:** A state $i$ is absorbing if $p_{ii} = 1$. Once entered, it is impossible to leave (e.g., a "Game Over" state).
*   **Accessible State:** State $j$ is accessible from state $i$ if $p_{ij}^{(n)} > 0$ for some $n \geq 0$.
*   **Irreducible Chain:** A Markov chain is irreducible if every state is accessible from every other state. There are no isolated subgroups.

## Example: Weather Model

Let's model the weather as a Markov chain with two states: **0: Sunny** and **1: Rainy**.

Suppose the transition probabilities are:
*   If today is Sunny ($0$), probability of tomorrow being Sunny is $0.8$, and Rainy is $0.2$.
*   If today is Rainy ($1$), probability of tomorrow being Sunny is $0.6$, and Rainy is $0.4$.

The **Transition Probability Matrix** $P$ is:
$$P = \begin{bmatrix}
p_{00} & p_{01} \\
p_{10} & p_{11}
\end{bmatrix}
= \begin{bmatrix}
0.8 & 0.2 \\
0.6 & 0.4
\end{bmatrix}$$

**Question:** If today is Friday and it is sunny, what is the probability that Sunday will be rainy?

This is a two-step transition. We need $p_{01}^{(2)}$ (Sunny Friday -> Rainy Sunday).

We calculate the two-step transition matrix:
$$P^{(2)} = P^2 = \begin{bmatrix}
0.8 & 0.2 \\
0.6 & 0.4
\end{bmatrix}
\begin{bmatrix}
0.8 & 0.2 \\
0.6 & 0.4
\end{bmatrix}
= \begin{bmatrix}
(0.8*0.8 + 0.2*0.6) & (0.8*0.2 + 0.2*0.4) \\
(0.6*0.8 + 0.4*0.6) & (0.6*0.2 + 0.4*0.4)
\end{bmatrix}
= \begin{bmatrix}
0.76 & 0.24 \\
0.72 & 0.28
\end{bmatrix}$$

The value $p_{01}^{(2)}$ is the element in row $0$, column $1$ of $P^2$, which is **0.24**. So, there is a 24% chance of rain on Sunday.

## Key Points & Summary

| Concept | Description | Importance |
| :--- | :--- | :--- |
| **Markov Property** | The future state depends only on the present state, not the past. | The foundational assumption that defines a Markov chain and simplifies modeling. |
| **State Space ($S$)** | The set of all possible conditions or values the system can hold. | Defines the scope of the problem being modeled. |
| **Transition Matrix ($P$)** | A matrix where each entry $p_{ij}$ is the probability of moving from state $i$ to $j$. | Encodes the entire dynamics of the Markov chain. Its properties (rows sum to 1) are critical. |
| **n-Step Transitions** | The probability $p_{ij}^{(n)}$ of moving from $i$ to $j$ in $n$ steps. | Found by raising the transition matrix $P$ to the power of $n$ ($P^n$). |
| **Chapman-Kolmogorov Eqns** | $p_{ij}^{(m+n)} = \sum_{k} p_{ik}^{(m)} p_{kj}^{(n)}$ | Provide the mathematical foundation for calculating multi-step transitions. |
| **Applications** | Used in **PageRank**, **queueing theory**, **speech recognition**, **predictive text**, and **game AI**. | A versatile tool for computer scientists to model real-world random processes. |