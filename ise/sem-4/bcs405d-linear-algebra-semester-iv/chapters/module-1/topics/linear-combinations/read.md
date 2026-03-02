# Linear Combinations (Linear Algebra - Module 1: Vector Spaces)

## Introduction

In the study of Linear Algebra, we often deal with vectors. A fundamental question we ask is: **Given a set of vectors, can we use them to construct or "reach" other vectors?** The concept of a **linear combination** provides the precise mathematical tool to answer this question. It is the primary mechanism for building new vectors from a given set and forms the cornerstone for more advanced ideas like spanning sets, linear independence, and basis, which you will encounter throughout this module on Vector Spaces.

## Core Concepts

### 1. Formal Definition

Let $V$ be a vector space over a field $\mathbb{F}$ (for our purposes, $\mathbb{F}$ is typically the set of real numbers $\mathbb{R}$). Let $\vec{v_1}, \vec{v_2}, ..., \vec{v_k}$ be a set of vectors in $V$.

A vector $\vec{w}$ in $V$ is called a **linear combination** of the vectors $\vec{v_1}, \vec{v_2}, ..., \vec{v_k}$ if there exist scalars $c_1, c_2, ..., c_k$ in $\mathbb{F}$ such that:

$$\vec{w} = c_1\vec{v_1} + c_2\vec{v_2} + ... + c_k\vec{v_k}$$

The scalars $c_1, c_2, ..., c_k$ are called the **coefficients** of the linear combination.

### 2. The Process: How to Form a Linear Combination

Forming a linear combination involves two operations inherent to the definition of a vector space:

1. **Scalar Multiplication:** Multiply each vector $\vec{v_i}$ by its corresponding coefficient $c_i$.
2. **Vector Addition:** Add the resulting scaled vectors together.

### 3. The Span

The set of **all possible linear combinations** of a given set of vectors $\{\vec{v_1}, \vec{v_2}, ..., \vec{v_k}\}$ is called the **span** of that set. It is denoted as $\text{Span}\{\vec{v_1}, \vec{v_2}, ..., \vec{v_k}\}$.

- If $\text{Span}\{\vec{v_1}, \vec{v_2}, ..., \vec{v_k}\}$ encompasses the entire vector space $V$, we say the set **spans** $V$.
- Asking "Is $\vec{w}$ a linear combination of $\{\vec{v_1}, \vec{v_2}, ..., \vec{v_k}\}$?" is equivalent to asking "Is $\vec{w}$ in $\text{Span}\{\vec{v_1}, \vec{v_2}, ..., \vec{v_k}\}$?"

## Examples

Let's illustrate this with vectors in $\mathbb{R}^2$.

**Example 1: A Simple Linear Combination**

Consider the vectors $\vec{v_1} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ and $\vec{v_2} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$.

Is $\vec{w} = \begin{bmatrix} 5 \\ -3 \end{bmatrix}$ a linear combination of $\vec{v_1}$ and $\vec{v_2}$?

We need to find scalars $c_1$ and $c_2$ such that:
$c_1\begin{bmatrix} 1 \\ 0 \end{bmatrix} + c_2\begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 5 \\ -3 \end{bmatrix}$

This leads to the system of equations:
$c_1 + 0c_2 = 5$
$0c_1 + c_2 = -3$

The solution is trivial: $c_1 = 5$, $c_2 = -3$. Therefore, $\vec{w}$ is indeed a linear combination. In fact, these two vectors span all of $\mathbb{R}^2$.

**Example 2: A Less Obvious Case**

Consider the vectors $\vec{u_1} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$ and $\vec{u_2} = \begin{bmatrix} 3 \\ 1 \end{bmatrix}$.

Is $\vec{b} = \begin{bmatrix} 1 \\ 5 \end{bmatrix}$ a linear combination of $\vec{u_1}$ and $\vec{u_2}$?

We set up the equation:
$c_1\begin{bmatrix} 1 \\ 2 \end{bmatrix} + c_2\begin{bmatrix} 3 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 5 \end{bmatrix}$

This gives the system:
$c_1 + 3c_2 = 1$
$2c_1 + c_2 = 5$

Solving this system (e.g., by elimination), we find $c_1 = \frac{14}{5}$ and $c_2 = -\frac{3}{5}$. Since a solution exists, $\vec{b}$ is a linear combination of $\vec{u_1}$ and $\vec{u_2}$.

**Example 3: A Non-Example**

Using the same vectors $\vec{u_1}$ and $\vec{u_2}$ from above, is $\vec{c} = \begin{bmatrix} 2 \\ 2 \end{bmatrix}$ a linear combination?

We set up the system:
$c_1 + 3c_2 = 2$
$2c_1 + c_2 = 2$

Attempting to solve, we find this system is **inconsistent** (e.g., multiplying the first equation by 2 and subtracting from the second leads to a contradiction like $0=2$). There are no scalars $c_1$, $c_2$ that satisfy both equations. Therefore, $\vec{c}$ is **not** a linear combination of $\vec{u_1}$ and $\vec{u_2}$. Geometrically, this means $\vec{c}$ does not lie in the plane spanned by $\vec{u_1}$ and $\vec{u_2}$.

## Key Points / Summary

- **Definition:** A linear combination is a sum of scalar multiples of vectors.
- **Fundamental Question:** A central problem in linear algebra is determining whether a given vector can be expressed as a linear combination of a given set of vectors.
- **Solving for Combinations:** This question leads to a system of linear equations. If the system is consistent, the vector is a linear combination; if inconsistent, it is not.
- **The Span:** The set of all linear combinations of a set of vectors is called their span. It represents all the vectors that can be "reached" using those building blocks.
- **Foundation Concept:** Understanding linear combinations is absolutely essential for grasping subsequent topics like linear independence, basis, and dimension. It is the foundational operation within a vector space.
