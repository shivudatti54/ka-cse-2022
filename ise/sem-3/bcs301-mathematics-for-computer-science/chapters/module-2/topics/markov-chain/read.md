# Module 2: Markov Chain

## Introduction

A Markov Chain, named after the Russian mathematician Andrey Markov, is a powerful mathematical model used to describe a sequence of possible events where the probability of each event depends **only** on the state attained in the previous event. This "memoryless" property, called the **Markov Property**, makes it an indispensable tool in computer science for modeling systems that evolve over time. Applications range widely, including webpage ranking (Google's PageRank algorithm), speech recognition, queueing theory, game theory, and predictive text.

## Core Concepts

### 1. The Markov Property

The fundamental assumption of a Markov chain is the **Markov Property** (or memorylessness). It states that the future state of the process depends only on the present state, not on the sequence of events that preceded it.

Mathematically, for a process with states $S_0, S_1, ..., S_n$, this is written as:
$$P(S_{n+1} = x | S_0, S_1, ..., S_n) = P(S_{n+1} = x | S_n)$$
Where $P$ is the probability, and $x$ is a possible state.

### 2. State Space

The set of all possible states a system can be in is called the **State Space**. It can be finite or infinite. For example, the state space for a weather model could be $\{\text{Sunny}, \text{Rainy}\}$.

### 3. Transition Probability

The probability of moving from one state to another is called the **Transition Probability**. We denote the probability of moving from state $i$ to state $j$ in one step as $P_{ij}$.
$$P_{ij} = P(S_{n+1} = j | S_n = i)$$

### 4. Transition Probability Matrix (TPM)

For a finite Markov chain with $N$ states, all transition probabilities can be conveniently represented in an $N \times N$ matrix called the **Transition Probability Matrix (TPM)**, denoted as $P$.

$$
P = \begin{bmatrix}
P_{11} & P_{12} & \cdots & P_{1N} \\
P_{21} & P_{22} & \cdots & P_{2N} \\
\vdots & \vdots & \ddots & \vdots \\
P_{N1} & P_{N2} & \cdots & P_{NN}
\end{bmatrix}
$$

**Key Properties of the TPM:**

- Each entry $P_{ij}$ is a probability, so $0 \leq P_{ij} \leq 1$.
- The sum of probabilities in each row must be 1. That is, $\sum_{j=1}^{N} P_{ij} = 1$ for every row $i$. This is because from any given state $i$, the process must transition to _some_ state in the next step.

## Example: Weather Prediction Model

Let's model the daily weather based on the previous day's weather. Our state space is $\{\text{Sunny (S)}, \text{Rainy (R)}\}$.

Suppose the transition probabilities are:

- If today is Sunny, probability of tomorrow being Sunny is 0.8, and Rainy is 0.2.
- If today is Rainy, probability of tomorrow being Sunny is 0.6, and Rainy is 0.4.

The Transition Probability Matrix is:

$$
P = \begin{bmatrix}
 & \text{To S} & \text{To R} \\
\text{From S} & 0.8 & 0.2 \\
\text{From R} & 0.6 & 0.4 \\
\end{bmatrix}
$$

**Question:** If it is sunny today (Day 0), what is the probability that it will be rainy the day after tomorrow (Day 2)?

**Solution:**
We need to find all possible paths over two days that start at `S` and end at `R`.

1.  Path 1: Sunny (Day0) -> Sunny (Day1) -> Rainy (Day2)
    Probability: $0.8 \times 0.2 = 0.16$
2.  Path 2: Sunny (Day0) -> Rainy (Day1) -> Rainy (Day2)
    Probability: $0.2 \times 0.4 = 0.08$

The total probability is the sum of the probabilities of all possible paths: $0.16 + 0.08 = 0.24$.

We can find this efficiently by looking at the $(S, R)$ entry of the matrix $P^2$ (the TPM raised to the power of 2, representing two steps).

$$
P^2 = P \times P = \begin{bmatrix}
0.8 & 0.2 \\
0.6 & 0.4 \\
\end{bmatrix}
\times
\begin{bmatrix}
0.8 & 0.2 \\
0.6 & 0.4 \\
\end{bmatrix}
= \begin{bmatrix}
(0.8\times0.8 + 0.2\times0.6) & (0.8\times0.2 + 0.2\times0.4) \\
(0.6\times0.8 + 0.4\times0.6) & (0.6\times0.2 + 0.4\times0.4) \\
\end{bmatrix}
= \begin{bmatrix}
0.76 & 0.24 \\
0.72 & 0.28 \\
\end{bmatrix}
$$

The entry in row 1 (Sunny), column 2 (Rainy) is $0.24$, confirming our calculation.

## Key Points & Summary

- **Markov Property:** The cornerstone of a Markov chain. The next state depends only on the current state, not on the history of states.
- **State Space ($S$):** The collection of all possible states of the system.
- **Transition Probability ($P_{ij}$):** The probability of moving from state $i$ to state $j$ in a single step.
- **Transition Probability Matrix ($P$):** A square matrix representing all possible transition probabilities. Each row sums to 1.
- **n-step Transitions:** The probability of moving from state $i$ to state $j$ in $n$ steps is given by the $(i, j)$ entry of the matrix $P^n$.
- **Wide Applicability:** Markov chains are a simple yet profoundly useful model for stochastic (random) processes in computer science, engineering, economics, and genetics.
