Of course. Here is a comprehensive educational note on Probability Vectors, tailored for  Engineering students.

# Mathematics for Computer Science

## Module 2: Joint Probability Distribution & Markov Chain

### Topic: Probability Vectors

---

### 1. Introduction

A probability vector is a fundamental building block in stochastic processes, which are crucial for modeling systems in computer science like queueing networks, randomized algorithms, and machine learning (e.g., PageRank algorithm). It provides a concise mathematical way to represent the state of a system where the outcome is probabilistic. Simply put, a probability vector is a vector that describes the distribution of probabilities across all possible states of a system.

### 2. Core Concepts

#### 2.1 Definition

A **probability vector** is a row vector $\vec{v} = [v_1, v_2, v_3, ..., v_n]$ whose components satisfy two conditions:

1.  **Non-negativity:** Every element $v_i$ is non-negative.
    $$v_i \geq 0 \quad \text{for all } i$$
2.  **Sum to One:** The sum of all elements in the vector equals 1.
    $$\sum_{i=1}^{n} v_i = v_1 + v_2 + ... + v_n = 1$$

#### 2.2 Interpretation

Each element $v_i$ in the vector represents the probability that the system is in state $i$. For example, if we have a system with 3 possible states (e.g., a machine that is `Idle`, `Busy`, or `Broken`), a probability vector $\vec{v} = [0.2, 0.7, 0.1]$ means:

- There is a 20% chance the machine is `Idle`.
- There is a 70% chance the machine is `Busy`.
- There is a 10% chance the machine is `Broken`.

#### 2.3 Connection to Markov Chains

This is where probability vectors become powerful. In a Markov chain, which models a system that moves from state to state with given probabilities, we represent the system's **state at a given time step $n$** with a probability vector, often denoted as $\vec{v}^{(n)}$.

The real utility is in prediction. The state of the system at the next time step ($n+1$) is calculated by multiplying the current state vector by the **transition probability matrix** $P$.

$$\vec{v}^{(n+1)} = \vec{v}^{(n)} \cdot P$$

This operation distributes the current probabilities according to the rules defined in matrix $P$, yielding a new probability vector for the next state.

### 3. Example

Let's model a simple weather system. Suppose the weather is either **Sunny (S)** or **Rainy (R)**. The transition probabilities are given by the matrix $P$:

$$
P = \begin{bmatrix}
P(S \rightarrow S) & P(S \rightarrow R) \\
P(R \rightarrow S) & P(R \rightarrow R)
\end{bmatrix}
= \begin{bmatrix}
0.8 & 0.2 \\
0.4 & 0.6
\end{bmatrix}
$$

- Interpretation: If it's sunny today, there's an 80% chance it will be sunny tomorrow and a 20% chance it will be rainy. If it's rainy today, there's a 40% chance it will be sunny tomorrow and a 60% chance it will remain rainy.

**Scenario:** Suppose we know with certainty that today is sunny. Our initial state vector is:
$$\vec{v}^{(0)} = [P(S), P(R)] = [1, 0]$$

**Question:** What is the forecast for tomorrow ($\vec{v}^{(1)}$)?

**Solution:**
$$\vec{v}^{(1)} = \vec{v}^{(0)} \cdot P = [1, 0] \cdot \begin{bmatrix} 0.8 & 0.2 \\ 0.4 & 0.6 \end{bmatrix}$$

To multiply, we calculate the dot product of $\vec{v}^{(0)}$ with each _column_ of $P$:

- Probability of Sunny tomorrow: $(1 \times 0.8) + (0 \times 0.4) = 0.8$
- Probability of Rainy tomorrow: $(1 \times 0.2) + (0 \times 0.6) = 0.2$

Therefore, the new state vector is:
$$\vec{v}^{(1)} = [0.8, 0.2]$$

This is a valid probability vector (non-negative elements summing to 1). We can now use this to find the weather for the day after tomorrow by computing $\vec{v}^{(2)} = \vec{v}^{(1)} \cdot P$.

---

### 4. Key Points & Summary

| Key Point       | Description                                                                                                                            |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| **Definition**  | A row vector where all entries are $\geq 0$ and sum to $1$.                                                                            |
| **Purpose**     | To represent the probability distribution over a finite set of states in a system.                                                     |
| **Notation**    | Often denoted as $\vec{v}$ or $\vec{\pi}$. $\vec{v}^{(n)}$ represents the state at time $n$.                                           |
| **Operation**   | The core operation is the vector-matrix multiplication: $\vec{v}^{(n+1)} = \vec{v}^{(n)} \cdot P$, where $P$ is the transition matrix. |
| **Application** | Essential for analyzing **Markov Chains**, which are used in network theory, speech recognition, statistics, and game theory.          |
| **Validation**  | Always check that your result is indeed a probability vector (non-negative elements summing to 1).                                     |
