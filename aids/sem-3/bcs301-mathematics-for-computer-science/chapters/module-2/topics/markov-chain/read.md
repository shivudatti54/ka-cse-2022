# Module 2: Markov Chain

## Introduction

In the study of stochastic processes—systems that evolve randomly over time—the **Markov Chain** is a fundamental and powerful model. Named after the Russian mathematician Andrey Markov, it provides a way to predict the future state of a system based *only* on its present state, not on the full history of its past states. This "memoryless" property, known as the **Markov Property**, makes these chains computationally tractable and incredibly useful for modeling real-world systems in computer science, such as queueing networks, web page ranking (Google's PageRank), speech recognition, and game theory.

## Core Concepts

### 1. The Markov Property

A stochastic process $\{X_n, n = 0, 1, 2, ...\}$ has the Markov Property if the conditional probability of its future state, given its present and all past states, depends *only* on the present state. Mathematically:

$$
P(X_{n+1} = j \ | \ X_n = i, X_{n-1} = i_{n-1}, ..., X_0 = i_0) = P(X_{n+1} = j \ | \ X_n = i)
$$

This means the past history of the process is irrelevant; only the current state $i$ influences the probability of moving to the next state $j$.

### 2. State Space

The set of all possible values or conditions that the random variables $X_n$ can take is called the **state space** ($S$). It can be:
*   **Finite:** e.g., $S = \{\text{Sunny}, \text{Rainy}\}$ for weather models.
*   **Infinite:** e.g., $S = \{0, 1, 2, ...\}$ for queue lengths.

### 3. Transition Probabilities

The probability of moving from state $i$ to state $j$ in one time step is called the **one-step transition probability**:

$$
P_{ij} = P(X_{n+1} = j \ | \ X_n = i)
$$

These probabilities are the core building blocks of a Markov chain.

### 4. Transition Probability Matrix (TPM)

For a finite state space with $N$ states ($S = \{1, 2, ..., N\}$), all one-step transition probabilities can be neatly organized into an $N \times N$ matrix called the **Transition Probability Matrix** ($P$).

$$
P = \begin{bmatrix}
P_{11} & P_{12} & \cdots & P_{1N} \\
P_{21} & P_{22} & \cdots & P_{2N} \\
\vdots & \vdots & \ddots & \vdots \\
P_{N1} & P_{N2} & \cdots & P_{NN}
\end{bmatrix}
$$

**Key Properties of the TPM:**
1.  Every entry $P_{ij}$ is a probability, so $0 \leq P_{ij} \leq 1$.
2.  The sum of probabilities in any row must be 1: $\sum_{j=1}^{N} P_{ij} = 1$ for all $i$. Each row represents the probability distribution of the next state, given the current state.

### 5. n-Step Transitions and Chapman-Kolmogorov Equations

The probability of going from state $i$ to state $j$ in $n$ steps is denoted by $P_{ij}^{(n)}$. The **Chapman-Kolmogorov equations** provide a method to compute these multi-step probabilities using the one-step TPM. Crucially, the $n$-step transition matrix is simply the one-step TPM raised to the $n^{\text{th}}$ power:

$$
P^{(n)} = P^n
$$

This is a key result that makes predicting the system's state multiple steps into the future a straightforward matrix multiplication operation.

## Example: The Weather Model

Consider a simple model where the weather is either **Sunny (S)** or **Rainy (R)**. Assume it has the Markov property with the following transition rules:
*   If it is sunny today, the probability it will be sunny tomorrow is 0.8.
*   If it is sunny today, the probability it will rain tomorrow is 0.2.
*   If it is rainy today, the probability it will be sunny tomorrow is 0.6.
*   If it is rainy today, the probability it will rain tomorrow is 0.4.

**1. State Space:** $S = \{\text{Sunny}, \text{Rainy}\}$

**2. Transition Probability Matrix ($P$):**
We can assign states: 1 = Sunny, 2 = Rainy.

$$
P = \begin{bmatrix}
P_{11} & P_{12} \\
P_{21} & P_{22}
\end{bmatrix} = \begin{bmatrix}
0.8 & 0.2 \\
0.6 & 0.4
\end{bmatrix}
$$

**3. Predicting the Weather in Two Days:**
What is the probability that it will be sunny two days from now if it is rainy today? We need $P_{21}^{(2)}$.

$$
P^{(2)} = P^2 = \begin{bmatrix}
0.8 & 0.2 \\
0.6 & 0.4
\end{bmatrix} \begin{bmatrix}
0.8 & 0.2 \\
0.6 & 0.4
\end{bmatrix} = \begin{bmatrix}
(0.8)(0.8)+(0.2)(0.6) & (0.8)(0.2)+(0.2)(0.4) \\
(0.6)(0.8)+(0.4)(0.6) & (0.6)(0.2)+(0.4)(0.4)
\end{bmatrix} = \begin{bmatrix}
0.76 & 0.24 \\
0.72 & 0.28
\end{bmatrix}
$$

The element in the second row, first column ($P_{21}^{(2)} = 0.72$) is our answer. There is a 72% chance it will be sunny two days from now if it is raining today.

## Key Points & Summary

*   **Memoryless Property:** A Markov Chain's future state depends only on its present state, not its past history.
*   **State Space:** The set of all possible conditions the system can be in.
*   **Transition Probability Matrix (TPM):** A square matrix ($P$) where each entry $P_{ij}$ is the probability of moving from state $i$ to state $j$ in one step. The rows of this matrix must sum to 1.
*   **n-Step Predictions:** The probability of moving from state $i$ to state $j$ in $n$ steps is found by raising the TPM to the $n^{\text{th}}$ power ($P^n$) and reading the $(i,j)$-th element.
*   **Computer Science Applications:** Markov Chains are pivotal in algorithms like PageRank, which models a "random surfer" moving between web pages, and in modeling queues, network traffic, and genetic sequences in bioinformatics. Their simplicity and power make them an indispensable tool for engineers.