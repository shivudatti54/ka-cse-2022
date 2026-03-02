# Stochastic Matrices

## Introduction

In engineering, particularly in computer science, we often model systems that evolve over time with some degree of randomness. Think of a server's state (busy/idle), the next word in a speech recognition model, or the page a web surfer visits next. A **Stochastic Matrix**, also known as a **transition matrix** or **probability matrix**, is a fundamental mathematical tool used to describe the transitions of such probabilistic systems, formally known as **Markov Chains**. This module explores the definition, properties, and application of these crucial matrices.

## Core Concepts

### 1. Definition and Properties

A square matrix \( P = [p_{ij}] \) is called a **stochastic matrix** (or right stochastic matrix) if it satisfies two conditions:

1.  **Non-negative Entries:** Every entry \( p*{ij} \) is a probability, meaning it is non-negative.
    \[
    p*{ij} \geq 0 \quad \text{for all } i, j
    \]

2.  **Row Sum of 1:** The sum of the probabilities in each row must equal 1. This makes sense because from any given state \( i \), the system must transition to _some_ state in the next step.
    \[
    \sum*{j} p*{ij} = 1 \quad \text{for each row } i
    \]

Each entry \( p\_{ij} \) represents the probability of transitioning from state \( i \) to state \( j \) in one time step. It answers the question: "Given the system is in state \( i \) now, what is the probability it will be in state \( j \) next?"

### 2. Connection to State Vectors

The state of a system at any time step \( n \) can be represented by a **state vector** \( \mathbf{x}^{(n)} \). This is a column vector where the \( i \)-th element represents the probability that the system is in state \( i \) at step \( n \). Consequently, a state vector must also satisfy:

- All entries are non-negative (\( \geq 0 \)).
- The sum of all its entries is 1.

The power of the stochastic matrix is revealed when we use it to model the evolution of the system. The state vector at the next time step, \( \mathbf{x}^{(n+1)} \), is calculated by multiplying the current state vector by the transition matrix:
\[
\mathbf{x}^{(n+1)} = \mathbf{x}^{(n)} \cdot P
\]
To find the state after \( k \) steps, you simply multiply by the matrix \( P \) \( k \) times:
\[
\mathbf{x}^{(n+k)} = \mathbf{x}^{(n)} \cdot P^k
\]
Here, \( P^k \) is the \( k \)-step transition matrix, and its entries give the probabilities of moving from state \( i \) to state \( j \) in exactly \( k \) steps.

## Example: Website Navigation Model

Imagine a user browsing a website with only three pages: Home (H), Products (P), and Contact (C). We can model their next click using a Markov chain. Let's define a stochastic matrix \( P \) where the states are {H, P, C}.

**Assumed Transition Probabilities:**

- From **Home (H)**: 70% chance to go to Products, 20% to Contact, 10% to stay on Home.
- From **Products (P)**: 50% chance to go back Home, 30% to go to Contact, 20% to stay on Products.
- From **Contact (C)**: 80% chance to go back Home, 0% to go to Products, 20% to stay on Contact.

The resulting stochastic matrix is:
\[
P = \begin{bmatrix}
\text{From H} \\
\text{From P} \\
\text{From C}
\end{bmatrix}
\begin{bmatrix}
0.1 & 0.7 & 0.2 \\
0.5 & 0.2 & 0.3 \\
0.8 & 0.0 & 0.2 \\
\end{bmatrix}
\quad \begin{aligned}
&\leftarrow \text{To H} \\
&\leftarrow \text{To P} \\
&\leftarrow \text{To C}
\end{aligned}
\]

Notice that each row sums to 1: `(0.1+0.7+0.2=1)`, `(0.5+0.2+0.3=1)`, `(0.8+0.0+0.2=1)`.

**Scenario: Suppose a user starts on the Home page.**
The initial state vector is: \( \mathbf{x}^{(0)} = \begin{bmatrix} 1 & 0 & 0 \end{bmatrix} \)

What is the probability distribution after one click (one step)?
\[
\mathbf{x}^{(1)} = \mathbf{x}^{(0)} \cdot P = \begin{bmatrix} 1 & 0 & 0 \end{bmatrix} \cdot
\begin{bmatrix}
0.1 & 0.7 & 0.2 \\
0.5 & 0.2 & 0.3 \\
0.8 & 0.0 & 0.2 \\
\end{bmatrix}
= \begin{bmatrix} 0.1 & 0.7 & 0.2 \end{bmatrix}
\]
This result directly mirrors the first row of \( P \), confirming there's a 10% chance they are still on H, 70% on P, and 20% on C.

What about after two clicks (two steps)? We calculate \( \mathbf{x}^{(2)} = \mathbf{x}^{(0)} \cdot P^2 \). First, we compute \( P^2 \):
\[
P^2 = \begin{bmatrix}
0.1 & 0.7 & 0.2 \\
0.5 & 0.2 & 0.3 \\
0.8 & 0.0 & 0.2 \\
\end{bmatrix}^2 =
\begin{bmatrix}
0.1\cdot0.1 + 0.7\cdot0.5 + 0.2\cdot0.8 & ... & ... \\
... & ... & ... \\
... & ... & ...
\end{bmatrix}
\]
Calculating the first element \( p^{(2)}\_{11} \) (probability of starting at H and being at H after 2 clicks):
\[
= (0.1)(0.1) + (0.7)(0.5) + (0.2)(0.8) = 0.01 + 0.35 + 0.16 = 0.52
\]
This calculation considers all possible paths: H→H→H, H→P→H, and H→C→H. We would compute all other elements similarly to get the full \( P^2 \) matrix.

## Key Points & Summary

- **Purpose:** A stochastic matrix \( P \) models the one-step transition probabilities between the states of a discrete Markov chain.
- **Core Properties:** 1) All entries \( p*{ij} \geq 0 \). 2) Each row sums to 1 (\( \sum_j p*{ij} = 1 \)).
- **State Evolution:** The state vector \( \mathbf{x}^{(n)} \) evolves according to the rule \( \mathbf{x}^{(n+1)} = \mathbf{x}^{(n)} \cdot P \).
- **k-step Transitions:** The \( k \)-th power of the matrix, \( P^k \), gives the transition probabilities for \( k \) steps.
- **Applications:** Crucial for modeling random processes in computer science, including queueing theory (network traffic), Google's PageRank algorithm, reinforcement learning, speech processing, and network reliability analysis.
