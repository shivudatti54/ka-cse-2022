Of course. Here is comprehensive educational content on Markov Chains for  Engineering students, tailored for the "Mathematics for Computer Science" subject.

# Module 2: Markov Chains

## 1. Introduction

In many real-world systems, the next state depends only on the current state, not on the entire history of how the system got there. This "memoryless" property is the cornerstone of **Markov Chains**, named after the Russian mathematician Andrey Markov. They are powerful stochastic (random) models used extensively in computer science for applications like queueing theory (network traffic analysis), page ranking algorithms (Google's PageRank), statistical mechanics, speech recognition, and game theory. Understanding Markov chains provides a fundamental tool for modeling and analyzing systems that evolve randomly over time.

## 2. Core Concepts

### Definition and Properties

A **Markov Chain** is a stochastic process that undergoes transitions from one state to another on a state space. It must satisfy the **Markov Property** (Memoryless Property):

> The conditional probability of any future state \( X*{n+1} \), given the past states \( X_0, X_1, ..., X*{n-1} \) and the present state \( X_n \), depends only on the present state and not on the past states.

Mathematically, this is expressed as:
$$P(X_{n+1} = x_{n+1} | X_0 = x_0, X_1 = x_1, ..., X_n = x_n) = P(X_{n+1} = x_{n+1} | X_n = x_n)$$

### Transition Probability Matrix

The probabilities of moving from one state to another are called **transition probabilities**. If we have a finite number of states, say \( k \) states, we can arrange these probabilities into a matrix called the **Transition Probability Matrix (TPM)**, denoted by **P**.

$$
P = \begin{bmatrix} p_{11} & p_{12} & \cdots & p_{1k} \\
p_{21} & p_{22} & \cdots & p_{2k} \\
\vdots & \vdots & \ddots & \vdots \\
p_{k1} & p_{k2} & \cdots & p_{kk} \end{bmatrix}
$$

Where \( p*{ij} = P(X*{n+1} = j | X_n = i) \), the probability of moving from state \( i \) to state \( j \) in one step.

**Key properties of the TPM:**

1.  Every entry \( p*{ij} \) is a probability, so \( 0 \leq p*{ij} \leq 1 \).
2.  The sum of probabilities in any given row must be 1: \( \sum*{j=1}^{k} p*{ij} = 1 \) for all \( i \).

### State Classification

- **Accessible State:** State \( j \) is accessible from state \( i \) (\( i \rightarrow j \)) if it is possible to go from \( i \) to \( j \) in a finite number of steps (\( p\_{ij}^{(n)} > 0 \) for some \( n \geq 0 \)).
- **Communicating States:** States \( i \) and \( j \) **communicate** (\( i \leftrightarrow j \)) if \( i \rightarrow j \) and \( j \rightarrow i \). A set of states where all pairs communicate is called a **communicating class**.
- **Irreducible Chain:** A Markov chain is **irreducible** if it has only one communicating class; i.e., every state is reachable from every other state.
- **Absorbing State:** A state \( i \) is **absorbing** if once the system enters that state, it can never leave (\( p\_{ii} = 1 \)).

### Steady-State (Stationary) Distribution

A fundamental question is: what is the long-term behavior of the chain? After many transitions, do the state probabilities stabilize?

The **steady-state probability vector** \( \boldsymbol{\pi} \) is a row vector \( [\pi_1, \pi_2, ..., \pi_k] \) such that:
$$ \boldsymbol{\pi} = \boldsymbol{\pi} P $$
and
$$ \sum\_{i=1}^{k} \pi_i = 1 $$

The element \( \pi_i \) represents the long-run proportion of time the process is in state \( i \). Not all chains have a unique steady-state distribution (e.g., chains with absorbing states or periodic chains).

## 3. Example: The Weather Model

Consider a simple model for weather prediction where the weather is either **Sunny (S)** or **Rainy (R)**. Assume it has the Markov property with the following transition probabilities:

- If it is sunny today, tomorrow it will be sunny with probability 0.8 and rainy with probability 0.2.
- If it is rainy today, tomorrow it will be sunny with probability 0.6 and rainy with probability 0.4.

**1. State Space:** {Sunny, Rainy} or {S, R}
**2. Transition Probability Matrix (P):**
The matrix is defined with states ordered as [S, R].

$$
P = \begin{bmatrix}
0.8 & 0.2 \\  # From Sunny (row 1)
0.6 & 0.4    # From Rainy (row 2)
\end{bmatrix}
$$

**3. Finding the Steady-State Distribution:**
We want to find \( \boldsymbol{\pi} = [\pi_S, \pi_R] \) such that \( \boldsymbol{\pi} P = \boldsymbol{\pi} \).

This gives us the system of equations:

1.  \( \pi_S = 0.8\pi_S + 0.6\pi_R \)
2.  \( \pi_R = 0.2\pi_S + 0.4\pi_R \)
3.  \( \pi_S + \pi_R = 1 \)

From equation (1): \( \pi_S - 0.8\pi_S = 0.6\pi_R \) => \( 0.2\pi_S = 0.6\pi_R \) => \( \pi_S = 3\pi_R \)
Substitute into (3): \( 3\pi_R + \pi_R = 1 \) => \( 4\pi_R = 1 \) => \( \pi_R = 0.25 \)
Then \( \pi_S = 3 \times 0.25 = 0.75 \)

So, \( \boldsymbol{\pi} = [0.75, 0.25] \). This means in the long run, 75% of the days are sunny and 25% are rainy.

## 4. Key Points & Summary

- **Markov Property:** The future state depends only on the present state, not on the sequence of events that preceded it.
- **Transition Probability Matrix (TPM):** A square matrix **P** where each entry \( p\_{ij} \) is the probability of moving from state \( i \) to state \( j \). Each row sums to 1.
- **State Classification:** States can be classified based on communication and recurrence properties (e.g., communicating classes, irreducible chains, absorbing states).
- **Steady-State Distribution (**\( \boldsymbol{\pi} \) **):** The long-term probability vector found by solving \( \boldsymbol{\pi} = \boldsymbol{\pi}P \) with \( \sum \pi_i = 1 \). It represents the proportion of time the system spends in each state over a long period.
- **Applications:** Crucial for modeling random processes in computer networks (packet routing), search algorithms (PageRank), queueing theory, and many other areas of engineering and science.
