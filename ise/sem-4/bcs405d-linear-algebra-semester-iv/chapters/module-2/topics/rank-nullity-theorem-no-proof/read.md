# Linear Algebra: The Rank-Nullity Theorem

## Introduction

The Rank-Nullity Theorem is a fundamental result in linear algebra that provides a powerful and elegant relationship between the dimensions of the two most important subspaces associated with a linear transformation: its range and its null space. It acts as a bridge, connecting the properties of a transformation from its domain to its codomain. For engineering students, this theorem is crucial as it has applications in solving systems of linear equations, understanding the solvability of circuits, analyzing control systems, and in data science for concepts like dimensionality reduction.

## Core Concepts

To understand the Rank-Nullity Theorem, we must first be clear about three key ideas:

1.  **Linear Transformation (`T`)**: A function `T: V → W` between two vector spaces that preserves vector addition and scalar multiplication. For our purposes, we often consider `T: Rⁿ → Rᵐ`, defined by `T(x) = A x`, where `A` is an `m×n` matrix.

2.  **Null Space (Kernel)**: The set of all vectors in the domain `V` that map to the zero vector in `W`.
    `Null(T) = { v in V | T(v) = 0 }`
    - Its dimension is called the **nullity** of `T`, denoted as `nullity(T)`.

3.  **Range (Image)**: The set of all vectors in the codomain `W` that are images of some vector in `V`.
    `Range(T) = { T(v) in W | v in V }`
    - Its dimension is called the **rank** of `T`, denoted as `rank(T)`.

### The Theorem Statement

Let `T: V → W` be a linear transformation, where `V` is a finite-dimensional vector space. The Rank-Nullity Theorem states:

**`dim(V) = rank(T) + nullity(T)`**

In simpler terms, the dimension of the domain vector space is equal to the dimension of the transformation's output (range) plus the dimension of the set of inputs that get squashed to zero (null space).

If the transformation is represented by an `m × n` matrix `A`, the theorem becomes:
**`n = rank(A) + nullity(A)`**
where `n` is the number of columns in `A`.

## Examples

**Example 1: A Transformation from R³ to R²**
Consider the linear transformation `T: R³ → R²` defined by the matrix:
`A = [[1, 2, 0], [2, 4, 1]]`

- **Step 1: Find `rank(T)` (Dimension of Range)**
  The range of `T` is the column space of `A`. Let's find the rank by reducing `A` to row-echelon form.
  `A = [[1, 2, 0], [2, 4, 1]] ~ [[1, 2, 0], [0, 0, 1]]` (R2 -> R2 - 2\*R1)
  The pivot columns are 1 and 3. So, `rank(A) = 2`.

- **Step 2: Find `nullity(T)` (Dimension of Null Space)**
  Solve `A x = 0` for the null space.
  From the reduced matrix: `x₁ + 2x₂ = 0` and `x₃ = 0`. Let `x₂ = t` (a free variable), then `x₁ = -2t`.
  The solution is `x = t * [-2, 1, 0]ᵀ`. This is a one-dimensional space spanned by a single vector.
  So, `nullity(A) = 1`.

- **Step 3: Verify the Theorem**
  `dim(V) = dim(R³) = 3`
  `rank(T) + nullity(T) = 2 + 1 = 3`
  The theorem holds: `3 = 2 + 1`.

**Example 2: A One-to-One Transformation**
Consider a transformation `T: R² → R³` with `rank(T) = 2`. What is its nullity?
According to the theorem:
`dim(V) = rank(T) + nullity(T)`
`2 = 2 + nullity(T)`
Therefore, `nullity(T) = 0`.

A nullity of zero means the null space contains only the zero vector. This is the definition of a **one-to-one (injective)** transformation. The theorem shows that if a transformation maps into a _larger_ space (e.g., R² → R³) and has full rank (rank equals the dimension of the domain), it must be one-to-one.

## Key Points & Summary

- **Fundamental Relationship:** The Rank-Nullity Theorem provides a critical link between the dimensions of the range and null space of a linear transformation.
- **Conservation of Dimension:** The dimension `n` of the domain is "conserved" or "partitioned" into the rank and the nullity. Some input dimensions (`rank`) are used to create the output, while others (`nullity`) are "lost" or compressed to zero.
- **Applications:**
  - **Solving `Ax = b`:** If `rank(A)` is known, the theorem immediately tells us the number of free variables (`nullity(A)`) in the solution to the homogeneous system `Ax = 0`.
  - **Checking Properties:** A transformation is **one-to-one (injective)** if and only if `nullity(T) = 0`. It is **onto (surjective)** if and only if `rank(T) = dim(W)`.
  - **Data Science:** In Principal Component Analysis (PCA), the concepts of rank and nullity help in understanding the intrinsic dimensionality of a dataset.
- **The Bottom Line:** For any `m × n` matrix `A`, the number of pivot columns (`rank`) plus the number of free columns (`nullity`) always equals `n`, the total number of columns.
