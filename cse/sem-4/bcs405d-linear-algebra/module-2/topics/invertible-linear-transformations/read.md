# Invertible Linear Transformations

## Table of Contents

- [Invertible Linear Transformations](#invertible-linear-transformations)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of Invertible Linear Transformations](#definition-of-invertible-linear-transformations)
  - [Conditions for Invertibility](#conditions-for-invertibility)
  - [Relationship with Matrix Representation](#relationship-with-matrix-representation)
  - [Inverse Matrix and Inverse Transformation](#inverse-matrix-and-inverse-transformation)
  - [Properties of Invertible Linear Transformations](#properties-of-invertible-linear-transformations)
  - [Rank-Nullity Theorem Connection](#rank-nullity-theorem-connection)
  - [Finding Inverse of a Linear Transformation](#finding-inverse-of-a-linear-transformation)
- [Examples](#examples)
  - [Example 1: Inverse of a 2D Rotation](#example-1-inverse-of-a-2d-rotation)
  - [Example 2: Inverse of a Scaling Transformation](#example-2-inverse-of-a-scaling-transformation)
  - [Example 3: Checking Invertibility](#example-3-checking-invertibility)
- [Exam Tips](#exam-tips)

## Introduction

In linear algebra, linear transformations serve as fundamental mappings between vector spaces. Among these transformations, **invertible linear transformations** occupy a special place as they represent bijective mappings that can be "undone." An invertible linear transformation preserves the structure of vector spaces in such a way that we can recover the original input from any output. This concept is crucial in many applications, including computer graphics, cryptography, solving systems of linear equations, and quantum computing.

The study of invertible linear transformations connects deeply with matrix theory, as the invertibility of a linear transformation is equivalent to the invertibility of its matrix representation. Understanding when and how a linear transformation can be inverted is essential for solving practical engineering problems, particularly in fields like signal processing and control systems.

## Key Concepts

### Definition of Invertible Linear Transformations

A linear transformation T: V → W between two vector spaces is called **invertible** if there exists a function S: W → V such that:

- S(T(v)) = v for all v ∈ V (T followed by S gives identity on V)
- T(S(w)) = w for all w ∈ W (S followed by T gives identity on W)

The transformation S is called the **inverse** of T and is denoted as T⁻¹.

### Conditions for Invertibility

A linear transformation T: V → W is invertible if and only if it is **bijective** (both one-to-one and onto). This means:

1. **One-to-One (Injective)**: If T(u) = T(v), then u = v for all u, v ∈ V
2. **Onto (Surjective)**: For every w ∈ W, there exists some v ∈ V such that T(v) = w

### Relationship with Matrix Representation

If T: ℝⁿ → ℝᵐ is a linear transformation represented by an m×n matrix A, then:

- T is invertible (as a function) if and only if A is an invertible matrix
- For T to be invertible, we must have m = n (square matrix)
- A is invertible if and only if det(A) ≠ 0
- The rank of A must be n (full rank)

### Inverse Matrix and Inverse Transformation

If T(x) = Ax is an invertible linear transformation from ℝⁿ to ℝⁿ, then T⁻¹(y) = A⁻¹y, where A⁻¹ is the inverse matrix satisfying AA⁻¹ = I and A⁻¹A = I.

### Properties of Invertible Linear Transformations

1. The inverse of a linear transformation is itself linear
2. If T is invertible, then (T⁻¹)⁻¹ = T
3. If S and T are invertible, then (ST)⁻¹ = T⁻¹S⁻¹
4. If T is invertible, then ker(T) = {0} (null space contains only zero vector)
5. If T is invertible, then rank(T) = dim(V) = dim(W)

### Rank-Nullity Theorem Connection

The Rank-Nullity Theorem states: dim(V) = rank(T) + nullity(T)

For an invertible transformation T: V → W:

- nullity(T) = 0 (since ker(T) = {0})
- rank(T) = dim(V)
- Therefore, dim(V) = dim(W)

### Finding Inverse of a Linear Transformation

**Method 1: Using Standard Matrices**

1. Find the standard matrix A of T
2. Compute A⁻¹ if it exists
3. The inverse transformation is T⁻¹(x) = A⁻¹x

**Method 2: Using Definition**
Find T⁻¹ by solving T(v) = w for v in terms of w

## Examples

### Example 1: Inverse of a 2D Rotation

Consider the linear transformation T: ℝ² → ℝ² that rotates vectors by 90° counterclockwise.

**Solution:**
The standard matrix for this transformation is:
A = [0 -1]
[1 0]

To find T⁻¹, we need A⁻¹. For a rotation by θ, the inverse is rotation by -θ (or 270°).

det(A) = (0)(0) - (-1)(1) = 1 ≠ 0, so A is invertible.

A⁻¹ = [0 1]
[-1 0]

This represents rotation by -90° (or 270° counterclockwise).

Therefore, T⁻¹(x₁, x₂) = (x₂, -x₁)

**Verification:** T(T⁻¹(x₁, x₂)) = T(x₂, -x₁) = (-(-x₁), x₂) = (x₁, x₂) ✓

### Example 2: Inverse of a Scaling Transformation

Let T: ℝ³ → ℝ³ be defined by T(x, y, z) = (2x, 3y, 4z). Find T⁻¹.

**Solution:**
The standard matrix is A = diag(2, 3, 4), which is diagonal.

Since det(A) = 2 × 3 × 4 = 24 ≠ 0, A is invertible.

A⁻¹ = diag(1/2, 1/3, 1/4)

Therefore, T⁻¹(x, y, z) = (x/2, y/3, z/4)

**Verification:** T(T⁻¹(x, y, z)) = T(x/2, y/3, z/4) = (2(x/2), 3(y/3), 4(z/4)) = (x, y, z) ✓

### Example 3: Checking Invertibility

Determine whether T: ℝ³ → ℝ³ defined by T(x, y, z) = (x + y, y + z, x + z) is invertible. If so, find T⁻¹.

**Solution:**
Step 1: Find the standard matrix A.

T(1, 0, 0) = (1, 0, 1) → first column
T(0, 1, 0) = (1, 1, 0) → second column
T(0, 0, 1) = (0, 1, 1) → third column

A = [1 1 0]
[0 1 1]
[1 0 1]

Step 2: Find det(A).

det(A) = 1 × (1×1 - 1×0) - 1 × (0×1 - 1×1) + 0 × (0×0 - 1×1)
= 1 × 1 - 1 × (-1) + 0
= 1 + 1 = 2 ≠ 0

Since det(A) ≠ 0, T is invertible.

Step 3: Find A⁻¹ using the adjugate method or row reduction.

Using the formula A⁻¹ = (1/det(A)) × adj(A)

adj(A) = [1 -1 -1]
[1 1 -1]
[-1 1 1]

A⁻¹ = (1/2) × adj(A) = [1/2 -1/2 -1/2]
[1/2 1/2 -1/2]
[-1/2 1/2 1/2]

Therefore, T⁻¹(x, y, z) = (1/2)(x - y - z, x + y - z, -x + y + z)

## Exam Tips

1. **Remember the key equivalence**: A linear transformation T is invertible if and only if its matrix representation A is invertible (det(A) ≠ 0).

2. **One-to-one implies invertible on ℝⁿ**: For T: ℝⁿ → ℝⁿ, if T is one-to-one, then it is automatically onto (and hence invertible) because of dimension equality.

3. **Always check determinant first**: When asked to find the inverse of a linear transformation, first compute the determinant of its standard matrix. If det = 0, the transformation is not invertible.

4. **Null space characterization**: For an invertible transformation, the kernel (null space) contains only the zero vector. This is a quick test: if ker(T) ≠ {0}, then T is not invertible.

5. **Property of inverses**: Remember that (ST)⁻¹ = T⁻¹S⁻¹ (order reversed). This is a common exam question.

6. **Dimension requirement**: An invertible linear transformation must map between vector spaces of equal dimension. If dim(V) ≠ dim(W), T cannot be invertible.

7. **Verify your inverse**: Always check by computing T(T⁻¹(v)) = v or T⁻¹(T(v)) = v to ensure correctness.

8. **Connection to rank**: An invertible transformation has full rank equal to the dimension of the domain (and codomain).
