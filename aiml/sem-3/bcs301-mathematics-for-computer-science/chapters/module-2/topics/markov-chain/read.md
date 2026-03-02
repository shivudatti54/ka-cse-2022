# Module 2: Markov Chain

## 1. Introduction

In the study of mathematics for computer science, we often encounter systems whose future state depends only on their current state, not on the sequence of events that preceded it. This "memoryless" property is the foundational concept behind **Markov Chains**. Named after the Russian mathematician Andrey Markov, these mathematical models are indispensable for analyzing and predicting the behavior of complex stochastic (random) systems. They have profound applications in computer science, including Google's PageRank algorithm, queuing theory for network traffic analysis, speech recognition, data compression, and predictive text modeling.

## 2. Core Concepts

A Markov Chain models a system that moves through a finite set of **states**. The system undergoes changes from one state to another at each time step, and these changes are called **transitions**.

### Formal Definition

A **Markov Chain** is a stochastic process $\{X_n\}$, $n = 0, 1, 2, ...$ that satisfies the **Markov Property**:

$$
P(X_{n+1} = j \ | \ X_n = i, X_{n-1} = i_{n-1}, ..., X_0 = i_0) = P(X_{n+1} = j \ | \ X_n = i)
$$

This equation states that the probability of transitioning to the next state $j$ depends **only** on the current state $i$, and is completely independent of all the previous states ($i_{n-1}, ..., i_0$). The process has no memory of the path it took to get to state $i$.

### Transition Probability Matrix (TPM)

The probabilities of moving from one state to another are called **transition probabilities**, denoted as:

$$
p_{ij} = P(X_{n+1} = j \ | \ X_n = i)
$$

These probabilities are typically organized into a **Transition Probability Matrix (TPM)**, denoted by $P$.

$$
P = \begin{bmatrix}
p_{11} & p_{12} & \cdots & p_{1N} \\
p_{21} & p_{22} & \cdots & p_{2N} \\
\vdots & \vdots & \ddots & \vdots \\
p_{N1} & p_{N2} & \cdots & p_{NN}
\end{bmatrix}
$$

**Properties of the TPM:**
1.  Every entry $p_{ij}$ is a probability, so $0 \leq p_{ij} \leq 1$.
2.  The sum of probabilities in any given row must be 1: $\sum_{j=1}^{N} p_{ij} = 1$ for all $i$.

This matrix provides a complete description of the Markov Chain's dynamics.

### State Classification

*   **Absorbing State:** A state $i$ is absorbing if $p_{ii} = 1$. Once entered, it is impossible to leave (e.g., a "game over" state).
*   **Transient State:** A state that, after being entered, there is a non-zero probability of never returning to it.
*   **Recurrent State:** A state that, once left, will eventually be revisited.

## 3. Example: The Weather Model

Let's model a simple system where the weather can be either **Sunny (S)** or **Rainy (R)**. We assume the weather tomorrow depends only on the weather today.

We define the transition probabilities:
*   If today is Sunny (S):
    *   Probability tomorrow is Sunny: $p_{SS} = 0.8$
    *   Probability tomorrow is Rainy: $p_{SR} = 0.2$
*   If today is Rainy (R):
    *   Probability tomorrow is Sunny: $p_{RS} = 0.6$
    *   Probability tomorrow is Rainy: $p_{RR} = 0.4$

The **Transition Probability Matrix** $P$ for this Markov Chain is:

$$
P = \begin{bmatrix}
& \text{to } S & \text{to } R \\
\text{from } S & 0.8 & 0.2 \\
\text{from } R & 0.6 & 0.4 \\
\end{bmatrix}
$$

Now, let's find the probability that it will be sunny **two days from now** if it is rainy today ($X_0 = R$).

We want $P(X_2 = S \ | \ X_0 = R)$.

The possible paths over two days are:
1.  Rainy → Sunny → Sunny
2.  Rainy → Rainy → Sunny

Using the TPM:
*   Path 1 probability: $p_{RS} \cdot p_{SS} = (0.6)(0.8) = 0.48$
*   Path 2 probability: $p_{RR} \cdot p_{RS} = (0.4)(0.6) = 0.24$

The total probability is the sum of the probabilities of all possible paths: $0.48 + 0.24 = 0.72$.

This result can be found more efficiently by computing the $(i, j)$-th entry of the matrix $P^2$, which gives all two-step transition probabilities. Here, the entry in row 2 (Rainy), column 1 (Sunny) of $P^2$ would indeed be $0.72$.

## 4. Key Points & Summary

*   **Memoryless Property:** The core of a Markov Chain is that the future state depends only on the present state, not on the past.
*   **Transition Probability Matrix (TPM):** A square matrix $P$ where the entry $p_{ij}$ is the probability of moving from state $i$ to state $j$. Each row must sum to 1.
*   **State Classification:** States can be absorbing, transient, or recurrent, describing their long-term behavior within the system.
*   **n-Step Transitions:** The probability of moving from state $i$ to state $j$ in $n$ steps is given by the $(i, j)$-th entry of the matrix $P^n$.
*   **Wide Applicability:** From algorithm analysis and network modeling to AI/ML and game theory, Markov Chains provide a powerful framework for predicting the behavior of random systems in computer science.