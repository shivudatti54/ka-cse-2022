# Projections

## Table of Contents

- [Projections](#projections)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Projection onto a Line](#1-projection-onto-a-line)
  - [2. Projection Matrix onto a Subspace](#2-projection-matrix-onto-a-subspace)
  - [3. Properties of Projection Matrices](#3-properties-of-projection-matrices)
  - [4. Orthogonal Projection](#4-orthogonal-projection)
  - [5. Projection and Least Squares](#5-projection-and-least-squares)
  - [6. Gram-Schmidt and Projections](#6-gram-schmidt-and-projections)
- [Examples](#examples)
  - [Example 1: Projection onto a Line in R²](#example-1-projection-onto-a-line-in-r)
  - [Example 2: Projection Matrix onto a Plane](#example-2-projection-matrix-onto-a-plane)
  - [Example 3: Least Squares Using Projection](#example-3-least-squares-using-projection)
- [Exam Tips](#exam-tips)

## Introduction

Projections are fundamental concepts in linear algebra with extensive applications in computer graphics, machine learning, signal processing, and solving least squares problems. A projection is a linear transformation that maps a vector onto a subspace in such a way that the resulting vector lies in that subspace. When we project a vector onto a subspace, we find the "closest" point in that subspace to the original vector.

In the context of the university's linear algebra course, understanding projections is crucial because they form the foundation for many advanced topics including orthogonal decompositions, QR factorization, and least squares approximation. Projections help us decompose vectors into components that lie in specific subspaces, which is essential for solving systems of equations that may not have exact solutions. The study of projections also connects deeply to the concept of orthogonal complements and the Gram-Schmidt orthogonalization process.

## Key Concepts

### 1. Projection onto a Line

Given a non-zero vector **u** in Rⁿ, the projection of a vector **x** onto the direction of **u** is given by the formula:

$$\text{proj}_{\mathbf{u}}(\mathbf{x}) = \frac{\mathbf{x} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}} \mathbf{u} = \frac{\mathbf{x}^T \mathbf{u}}{\mathbf{u}^T \mathbf{u}} \mathbf{u}$$

The scalar coefficient (x·u)/(u·u) represents the component of **x** in the direction of **u**. This projection vector lies on the line spanned by **u**.

### 2. Projection Matrix onto a Subspace

For projecting onto the column space of a matrix A (with linearly independent columns), the projection matrix is given by:

$$P = A(A^T A)^{-1}A^T$$

This matrix P has several important properties: P² = P (idempotent), P = P^T (symmetric), and rank(P) = rank(A). The projection matrix transforms any vector in Rⁿ into its projection onto the column space of A.

### 3. Properties of Projection Matrices

- **Idempotent**: P² = P (applying projection twice gives same result)
- **Symmetric**: P^T = P (for orthogonal projections)
- **Trace**: trace(P) = rank(P) = dimension of the subspace
- **Eigenvalues**: Only 0 or 1

### 4. Orthogonal Projection

A projection is called orthogonal when the error vector (x - proj_W(x)) is orthogonal to every vector in the subspace W. For orthogonal projections onto a subspace W, we have the decomposition:

$$\mathbf{x} = \text{proj}_W(\mathbf{x}) + \text{perp}_W(\mathbf{x})$$

where proj_W(x) ∈ W and perp_W(x) ∈ W⊥ (orthogonal complement).

### 5. Projection and Least Squares

The least squares solution to Ax = b is given by solving the normal equations:

$$A^T A \mathbf{x} = A^T \mathbf{b}$$

The vector b̂ = proj\_{Col(A)}(b) = PA = A(A^T A)^{-1}A^T b is the projection of b onto the column space of A. The least squares solution minimizes the squared error ||b - Ax||².

### 6. Gram-Schmidt and Projections

The Gram-Schmidt orthogonalization process uses projections to produce orthogonal vectors. Given linearly independent vectors, we project each subsequent vector onto the subspace spanned by previously processed vectors and subtract to obtain orthogonal components.

## Examples

### Example 1: Projection onto a Line in R²

**Problem:** Project the vector x = (3, 4) onto the line spanned by u = (1, 1).

**Solution:**

**Step 1:** Compute u·u = 1² + 1² = 2

**Step 2:** Compute x·u = 3(1) + 4(1) = 7

**Step 3:** Apply the projection formula:
$$\text{proj}_{\mathbf{u}}(\mathbf{x}) = \frac{7}{2}(1, 1) = \left(\frac{7}{2}, \frac{7}{2}\right) = (3.5, 3.5)$$

**Verification:** The error vector (3-3.5, 4-3.5) = (-0.5, 0.5) is orthogonal to u since (-0.5)(1) + (0.5)(1) = 0.

### Example 2: Projection Matrix onto a Plane

**Problem:** Find the projection matrix onto the xy-plane in R³.

**Solution:**

The xy-plane is spanned by e₁ = (1, 0, 0) and e₂ = (0, 1, 0).

**Step 1:** Form matrix A = [e₁ e₂] = [[1, 0], [0, 1], [0, 0]]

**Step 2:** Compute A^T A = [[1, 0], [0, 1]] = I₂ (2×2 identity)

**Step 3:** Compute (A^T A)⁻¹ = I₂

**Step 4:** Compute projection matrix:
P = A(A^T A)⁻¹ A^T = AA^T = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]

This matrix maps any vector (x, y, z) to (x, y, 0), confirming projection onto xy-plane.

### Example 3: Least Squares Using Projection

**Problem:** Find the least squares solution for the system:
x₁ + x₂ = 3
2x₁ + 3x₂ = 7
x₁ + 2x₂ = 4

**Solution:**

**Step 1:** Write in matrix form Ax = b:
A = [[1, 1], [2, 3], [1, 2]], b = [3, 7, 4]^T

**Step 2:** Compute A^T A:
A^T A = [[1²+2²+1², 1+3+2], [1+3+2, 1²+3²+2²]] = [[6, 6], [6, 14]]

**Step 3:** Compute A^T b:
A^T b = [1(3)+2(7)+1(4), 1(3)+3(7)+2(4)] = [21, 34]

**Step 4:** Solve normal equations:
6x₁ + 6x₂ = 21 → x₁ + x₂ = 3.5
6x₁ + 14x₂ = 34 → 3x₁ + 7x₂ = 17

Subtracting: (3x₁+7x₂) - 3(x₁+x₂) = 17 - 10.5 → 4x₂ = 6.5 → x₂ = 1.625
Then x₁ = 3.5 - 1.625 = 1.875

**Least squares solution:** x₁ = 1.875, x₂ = 1.625

## Exam Tips

1. **Remember the projection formula**: For projecting onto span{u}, use proj_u(x) = (x·u/u·u)u. This is frequently tested in university exams.

2. **Projection matrix properties**: Know that P² = P and P = P^T for orthogonal projections. These properties help verify your answers quickly.

3. **Least squares connection**: Understand that the least squares solution involves projecting b onto Col(A) and solving normal equations A^T Ax = A^T b.

4. **Dimension of projection**: The trace of projection matrix equals the dimension of the subspace, which is useful for verification.

5. **Orthogonal complement relationship**: Remember that x - proj_W(x) is always orthogonal to W. This is key for proving orthogonal projections.

6. **Gram-Schmidt application**: The Gram-Schmidt process uses projections to orthogonalize vectors: v*k = u_k - Σ*{j=1}^{k-1} proj\_{v_j}(u_k).

7. **Common mistake**: Don't forget to check if columns of A are linearly independent before applying the projection formula P = A(A^T A)⁻¹A^T.
