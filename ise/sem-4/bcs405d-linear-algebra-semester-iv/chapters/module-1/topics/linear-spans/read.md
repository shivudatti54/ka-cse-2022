# Linear Spans

## Introduction

In Linear Algebra, we often work with sets of vectors. A fundamental question is: given a set of vectors, what are all the vectors we can possibly create by combining them? The concept of a **linear span** provides the elegant answer to this question. It is the cornerstone for understanding more complex ideas like linear independence, basis, and dimension. For  Engineering students, mastering this concept is crucial as it has direct applications in solving systems of equations, computer graphics, signal processing, and machine learning.

## Core Concepts

### 1. Linear Combination

Before we define a span, we must understand a **linear combination**.

Let $V$ be a vector space over a field $\mathbb{R}$ (real numbers). Let $S = \{\vec{v_1}, \vec{v_2}, ..., \vec{v_k}\}$ be a set of vectors in $V$. A vector $\vec{w}$ is called a **linear combination** of the vectors in $S$ if it can be expressed as:
$$\vec{w} = c_1\vec{v_1} + c_2\vec{v_2} + ... + c_k\vec{v_k}$$
where $c_1, c_2, ..., c_k$ are scalars (real numbers).

**In simple terms:** You multiply each vector by some scalar (which can be positive, negative, or zero) and then add all the results together.

### 2. Definition of Linear Span

The **linear span** of a set $S$ of vectors, denoted by $\text{span}(S)$ or $\langle S \rangle$, is the set of **all possible linear combinations** of the vectors in $S$.

$$\text{span}(S) = \{ c_1\vec{v_1} + c_2\vec{v_2} + ... + c_k\vec{v_k} \ | \ c_i \in \mathbb{R} \}$$

If $\text{span}(S) = V$, we say that $S$ **spans** the vector space $V$.

**Key Insight:** The span of a set $S$ is always a **subspace** of the vector space $V$. In fact, it is the **smallest subspace of $V$ that contains the set $S$**. This means any subspace that contains $S$ must also contain $\text{span}(S)$.

## Examples

### Example 1: Span in $\mathbb{R}^2$

Consider the set $S$ containing a single vector in $\mathbb{R}^2$: $S = \{ \begin{bmatrix} 2 \\ 1 \end{bmatrix} \}$.

What is $\text{span}(S)$?
It is all vectors of the form $c_1 \begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 2c_1 \\ c_1 \end{bmatrix}$, where $c_1$ is any real number.

Geometrically, this represents **all vectors that are scalar multiples** of $\begin{bmatrix} 2 \\ 1 \end{bmatrix}$. This is a straight line through the origin in the direction of that vector.

### Example 2: Spanning the Entire $\mathbb{R}^2$

Now, consider the standard basis vectors: $S = \{ \vec{e_1}, \vec{e_2} \} = \{ \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \end{bmatrix} \}$.

What is $\text{span}(S)$?
It is all vectors of the form $c_1\begin{bmatrix} 1 \\ 0 \end{bmatrix} + c_2\begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} c_1 \\ c_2 \end{bmatrix}$.

Since $c_1$ and $c_2$ can be _any_ real numbers, this combination can produce **every possible vector** in $\mathbb{R}^2$. Therefore, $\text{span}(S) = \mathbb{R}^2$. We say the set $S$ spans $\mathbb{R}^2$.

### Example 3: A Span that is a Plane in $\mathbb{R}^3$

Consider the set $S = \{ \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} \}$ in $\mathbb{R}^3$.

$\text{span}(S)$ is all vectors of the form $c_1\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} + c_2\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} = \begin{bmatrix} c_1 \\ c_2 \\ 0 \end{bmatrix}$.

This set includes all vectors whose z-component is zero. Geometrically, this is the entire **xy-plane** in three-dimensional space. It is a 2-dimensional subspace of $\mathbb{R}^3$.

## Key Points & Summary

- **Definition:** The **linear span** of a set of vectors $S$ is the collection of all possible linear combinations of those vectors.
- **Subspace:** The span of any set $S$ is always a **subspace** of the parent vector space.
- **"Smallest" Subspace:** It is the smallest subspace that contains the set $S$. If you have a set $S$ and you want to form a subspace from it, you take its span.
- **Spanning a Space:** If $\text{span}(S) = V$, then $S$ is called a **spanning set** for $V$. This means every vector in $V$ can be written as a linear combination of the vectors in $S$.
- **Geometric Interpretation:**
  - The span of a single non-zero vector is a **line** through the origin.
  - The span of two linearly independent vectors is a **plane** through the origin.
  - The span of three linearly independent vectors in $\mathbb{R}^3$ is the **entire space** $\mathbb{R}^3$.
- **Engineering Application:** In fields like control systems, the state space model of a system is said to be **controllable** if the control input can move the system state from any initial point to any other point in the state space. This controllability is directly determined by checking if a certain matrix (built from system matrices) spans $\mathbb{R}^n$.

Understanding linear spans is the first step towards grasping more advanced topics like basis, dimension, and rank, which are essential for solving real-world engineering problems.
