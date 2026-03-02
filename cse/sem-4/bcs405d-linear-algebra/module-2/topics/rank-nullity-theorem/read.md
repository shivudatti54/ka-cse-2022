# Rank-Nullity Theorem

## Table of Contents

- [Rank-Nullity Theorem](#rank-nullity-theorem)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Linear Transformations and Vector Spaces](#linear-transformations-and-vector-spaces)
  - [Image (Range) of a Linear Transformation](#image-range-of-a-linear-transformation)
  - [Kernel (Null Space) of a Linear Transformation](#kernel-null-space-of-a-linear-transformation)
  - [The Rank-Nullity Theorem Statement](#the-rank-nullity-theorem-statement)
  - [Fundamental Subspaces of a Matrix](#fundamental-subspaces-of-a-matrix)
  - [One-to-One and Onto Transformations](#one-to-one-and-onto-transformations)
- [Examples](#examples)
  - [Example 1: Verifying Rank-Nullity for a 2×3 Matrix](#example-1-verifying-rank-nullity-for-a-23-matrix)
  - [Example 2: Determining Rank and Nullity from RREF](#example-2-determining-rank-and-nullity-from-rref)
  - [Example 3: Application to Linear Systems](#example-3-application-to-linear-systems)
- [Exam Tips](#exam-tips)

## Introduction

The Rank-Nullity Theorem is one of the most fundamental results in linear algebra, establishing a profound relationship between the dimensions of the four fundamental subspaces associated with a linear transformation. This theorem, attributed to the French mathematician Henri Poincaré and later formalized by linear algebraists, provides an essential bridge between the algebraic properties of matrices and their geometric interpretations. The theorem states that for any linear transformation T: V → W, the dimension of the domain V equals the sum of the rank (dimension of the image) and the nullity (dimension of the kernel) of T.

Understanding this theorem is crucial for several reasons. First, it provides a complete picture of how a linear transformation acts on its domain—it tells us how much of the output space is "covered" by the transformation (rank) and how much information is "lost" in the process (nullity). Second, the theorem serves as a powerful tool for solving systems of linear equations, determining whether solutions exist, and if so, characterizing their structure. Third, it forms the foundation for more advanced topics in linear algebra, including eigenvector analysis, diagonalization, and applications in engineering disciplines such as control systems and signal processing. For university students, this theorem appears frequently in examinations and forms the basis for understanding computational methods used in engineering analysis.

## Key Concepts

### Linear Transformations and Vector Spaces

A linear transformation T: V → W between two vector spaces V and W (over the same field, typically ℝ or ℂ) satisfies two properties for all vectors u, v in V and scalars c:

1. T(u + v) = T(u) + T(v) - additivity
2. T(cu) = cT(u) - homogeneity

The domain V is where the transformation begins, and the codomain W is where the output resides. Both V and W must be finite-dimensional for the Rank-Nullity Theorem to apply directly.

### Image (Range) of a Linear Transformation

The image (also called the range or column space) of a linear transformation T: V → W is defined as:

**Im(T) = {T(v) ∈ W : v ∈ V}**

The image is a subspace of W. Its dimension is called the **rank** of T, denoted as rank(T). The rank measures how "large" the output space is covered by the transformation. For a matrix A representing the transformation, the rank equals the dimension of the column space of A (the number of linearly independent columns).

### Kernel (Null Space) of a Linear Transformation

The kernel (also called the null space) of a linear transformation T: V → W is defined as:

**Ker(T) = {v ∈ V : T(v) = 0}**

The kernel is a subspace of V. Its dimension is called the **nullity** of T, denoted as nullity(T). The nullity measures how "much" of the input space maps to the zero vector—in other words, how much information is lost during the transformation. For a matrix A, the null space consists of all solutions to the homogeneous system Ax = 0.

### The Rank-Nullity Theorem Statement

For a linear transformation T: V → W where V is finite-dimensional:

**dim(V) = rank(T) + nullity(T)**

In matrix notation, for an m×n matrix A:

**n = rank(A) + nullity(A)**

where rank(A) = dim(Col(A)) and nullity(A) = dim(Null(A)).

This theorem tells us that the dimension of the domain is completely accounted for—some dimensions map to non-zero outputs (contributing to rank), while others collapse to zero (contributing to nullity).

### Fundamental Subspaces of a Matrix

For an m×n matrix A, the theorem relates four fundamental subspaces:

1. **Column Space (Col(A))**: Subspace of ℝ^m spanned by columns of A; dimension = rank(A)
2. **Null Space (Null(A))**: Subspace of ℝ^n containing solutions to Ax = 0; dimension = nullity(A)
3. **Row Space (Row(A))**: Subspace of ℝ^n spanned by rows of A; dimension = rank(A)
4. **Left Null Space (Null(A^T))**: Subspace of ℝ^m containing solutions to A^T y = 0; dimension = m - rank(A)

The Rank-Nullity Theorem specifically relates the column space and null space since they live in complementary dimensions of the domain and codomain.

### One-to-One and Onto Transformations

The Rank-Nullity Theorem provides simple criteria for determining if a linear transformation is one-to-one or onto:

- **T is one-to-one (injective)** if and only if nullity(T) = 0, which means Ker(T) = {0}
- **T is onto (surjective)** if and only if rank(T) = dim(W)
- **T is an isomorphism** if and only if it is both one-to-one and onto, which requires dim(V) = dim(W) = rank(T)

For a transformation from V to V (square matrix case), being one-to-one is equivalent to being onto.

## Examples

### Example 1: Verifying Rank-Nullity for a 2×3 Matrix

Consider the matrix A = [[1, 2, 3], [2, 4, 6]]. This is a 2×3 matrix with rank 1 (since second row is twice the first).

**Step 1: Find the null space**
We need to solve Ax = 0:
[1 2 3][x₁] [0]
[2 4 6][x₂] = [0]

The equations are:
x₁ + 2x₂ + 3x₃ = 0
2x₁ + 4x₂ + 6x₃ = 0 (redundant, twice the first)

Let x₂ = s, x₃ = t. Then x₁ = -2s - 3t.

Null space vectors: [-2s-3t, s, t] = s[-2,1,0] + t[-3,0,1]

Two linearly independent vectors, so nullity = 2.

**Step 2: Apply Rank-Nullity**
n = 3, rank = 1, nullity = 2
3 = 1 + 2 ✓

The theorem holds: dimension of domain (3) equals rank (1) plus nullity (2).

### Example 2: Determining Rank and Nullity from RREF

For matrix B = [[1, 2, 0, 3], [2, 4, 0, 7], [3, 6, 0, 10]], find rank and nullity.

**Step 1: Row reduce to echelon form**
RREF gives: [[1, 2, 0, 3], [0, 0, 0, 1], [0, 0, 0, 0]]

**Step 2: Identify pivot columns**
Pivot columns: 1st and 4th columns
Rank = number of pivots = 2

**Step 3: Find nullity using Rank-Nullity**
n = 4 (number of columns)
nullity = n - rank = 4 - 2 = 2

**Step 4: Verify by finding null space**
From RREF:
x₁ + 2x₂ + 3x₄ = 0
x₄ = 0

Let x₂ = s, x₃ = t, x₄ = 0
Then x₁ = -2s

Solution: [-2s, s, t, 0] = s[-2,1,0,0] + t[0,0,1,0]
Two free variables confirm nullity = 2.

### Example 3: Application to Linear Systems

Consider the system Ax = b where A = [[1, 1, 1], [1, 2, 2], [1, 3, 4]] and b = [3, 5, 8]^T.

**Step 1: Determine rank of A**
Row reduce A to RREF:
[[1, 1, 1], [1, 2, 2], [1, 3, 4]] → [[1, 0, -1], [0, 1, 2], [0, 0, 0]]
Rank = 2

**Step 2: Find augmented matrix rank**
Augmented matrix [A|b] = [[1,1,1,3], [1,2,2,5], [1,3,4,8]]
Row reduce: [[1,0,-1,1], [0,1,2,2], [0,0,0,0]]
Rank of augmented matrix = 2

**Step 3: Apply consistency condition**
Since rank(A) = rank([A|b]) = 2, the system is consistent.

**Step 4: Determine solution structure**
Number of variables n = 3
Number of constraints (rank) = 2
Degrees of freedom = n - rank = 1 (one free variable)

Solution has 1 parameter, confirming Rank-Nullity: nullity = 3 - 2 = 1.

## Exam Tips

1. **Remember the exact formula**: For linear transformation T: V → W with V finite-dimensional, always write dim(V) = rank(T) + nullity(T). For matrix A (m×n), remember n = rank(A) + nullity(A).

2. **Identify rank correctly**: Rank equals the number of pivots in row echelon form, number of non-zero rows in RREF, or the number of linearly independent columns (or rows).

3. **Null space dimension from homogeneous solutions**: If solving Ax = 0 has n variables and rank r, then nullity = n - r. The number of free variables equals nullity.

4. **One-to-one test**: A linear transformation T is one-to-one if and only if nullity(T) = 0, which occurs when rank(T) = dim(V) for transformations V → W.

5. **Onto test for square matrices**: For T: V → V (square matrix), T is onto if and only if it is one-to-one (both equivalent to full rank).

6. **Consistent system condition**: Ax = b has solutions if and only if rank(A) = rank([A|b]). Rank-Nullity helps find the number of free variables in the solution.

7. **Fundamental theorem connections**: Remember that rank(A) = rank(A^T), and for an m×n matrix: nullity(A) = n - rank(A), nullity(A^T) = m - rank(A).

8. **Column space vs row space**: Column space dimension always equals row space dimension (both equal rank), but they live in different spaces (ℝ^m and ℝ^n respectively).

9. **Geometric interpretation**: Rank tells us the dimension of the "output space" used, while nullity tells us how many dimensions "collapse" to zero.

10. **Work systematically**: When solving problems, first identify the matrix dimensions, then find rank using RREF or row operations, then apply Rank-Nullity to find the complementary quantity.
