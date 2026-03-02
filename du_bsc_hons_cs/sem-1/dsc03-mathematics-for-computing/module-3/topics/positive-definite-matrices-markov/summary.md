# Positive Definite Matrices & Markov Chains

## Introduction

This topic combines two fundamental concepts in linear algebra essential for computer science applications: **Positive Definite Matrices** and **Markov Chains**. These concepts are part of the Delhi University NEP 2024 UGCF syllabus for BSc (Hons) Computer Science, specifically under the Mathematics for Computing course. They form the mathematical foundation for various algorithms and real-world applications.

---

## Key Concepts

### Positive Definite Matrices

- **Definition**: A symmetric matrix $A$ is **positive definite** if $x^TAx > 0$ for all non-zero vectors $x$ in $\mathbb{R}^n$
- **Properties**:
  - All eigenvalues are positive
  - All leading principal minors are positive (Sylvester's criterion)
  - Has a unique Cholesky decomposition: $A = LL^T$ where $L$ is lower triangular with positive diagonal entries
  - Determinant is positive
  - Inverses are also positive definite

- **Types**:
  - **Positive Semi-definite**: $x^TAx \geq 0$ for all $x$ (eigenvalues ≥ 0)
  - **Negative Definite**: $x^TAx < 0$ for all non-zero $x$

- **Applications in Computing**:
  - Optimization algorithms (convex functions)
  - Machine learning (kernel methods, Gaussian processes)
  - Numerical linear algebra
  - Quadratic programming

### Markov Chains/Matrices

- **Definition**: A **Markov matrix** (stochastic matrix) is a square matrix where:
  - Each entry is non-negative
  - Each row sums to 1

- **Properties**:
  - Largest eigenvalue = 1 (Perron-Frobenius theorem)
  - Corresponding eigenvector contains non-negative entries
  - Used to represent transition probabilities in Markov chains

- **Markov Chain Concepts**:
  - **State space**: Set of all possible states
  - **Transition matrix**: Probability of moving from state $i$ to state $j$
  - **Stationary distribution**: Vector $\pi$ such that $\pi^T P = \pi^T$
  - **Ergodic/Irreducible**: Can reach any state from any state
  - **Regular**: Some power of transition matrix has all positive entries

- **Connection to Positive Definiteness**:
  - For reversible Markov chains, the matrix $D^{1/2}PD^{-1/2}$ is symmetric
  - The generator matrix of a Markov process is negative semi-definite
  - Covariance matrices in probabilistic models are positive definite

---

## Conclusion

Understanding positive definite matrices and Markov chains is crucial for computer science students. These concepts underpin optimization algorithms, machine learning models, and probabilistic computing. Mastery of these topics enables efficient solving of linear systems, probability computations, and algorithm analysis—skills essential for both academic success and practical applications in computing.