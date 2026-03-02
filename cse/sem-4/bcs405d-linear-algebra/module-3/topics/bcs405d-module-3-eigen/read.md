# Eigenvalues and Eigenvectors

## Table of Contents

- [Eigenvalues and Eigenvectors](#eigenvalues-and-eigenvectors)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Eigenvalues and Eigenvectors Definition](#1-eigenvalues-and-eigenvectors-definition)
  - [2. Characteristic Polynomial and Eigenvalues](#2-characteristic-polynomial-and-eigenvalues)
  - [3. Eigenvectors and Eigenspaces](#3-eigenvectors-and-eigenspaces)
  - [4. Cayley-Hamilton Theorem](#4-cayley-hamilton-theorem)
  - [5. Diagonalization](#5-diagonalization)
  - [6. Similar Matrices](#6-similar-matrices)
  - [7. Quadratic Forms](#7-quadratic-forms)
- [Examples](#examples)
  - [Example 1: Finding Eigenvalues and Eigenvectors](#example-1-finding-eigenvalues-and-eigenvectors)
  - [Example 2: Using Cayley-Hamilton Theorem](#example-2-using-cayley-hamilton-theorem)
  - [Example 3: Diagonalizing a Matrix](#example-3-diagonalizing-a-matrix)
- [Exam Tips](#exam-tips)

## Introduction

Eigenvalues and eigenvectors constitute one of the most fundamental concepts in linear algebra with extensive applications in engineering, physics, computer science, and data analysis. These concepts provide powerful tools for understanding linear transformations, solving systems of differential equations, performing principal component analysis, and many other advanced applications. In the context of the university's Linear Algebra course (BCS405D), Module 3 focuses extensively on these concepts as they form the backbone of modern computational techniques used in machine learning, image processing, and structural engineering.

The term "eigen" originates from the German word meaning "own" or "characteristic" - eigenvalues are sometimes called characteristic values. When a linear transformation is applied to a vector, eigenvectors represent the directions that remain unchanged (though possibly scaled), while eigenvalues represent the factor by which the eigenvector is scaled. This characteristic property makes them invaluable for analyzing stability in control systems, vibrations in mechanical structures, and quantum mechanical systems.

This topic requires approximately 8 hours of dedicated study to master, covering the computation of eigenvalues and eigenvectors, the Cayley-Hamilton theorem, matrix diagonalization, and quadratic forms. Understanding these concepts is essential for solving real-world engineering problems and forms a significant portion of the university examination.

## Key Concepts

### 1. Eigenvalues and Eigenvectors Definition

Given a square matrix A of order n × n, a non-zero vector v is called an eigenvector of A if there exists a scalar λ such that:

**Av = λv**

The scalar λ is called the eigenvalue corresponding to the eigenvector v. The equation Av = λv can be rewritten as:

**Av - λv = 0**
**(A - λI)v = 0**

For a non-trivial solution (v ≠ 0), the coefficient matrix (A - λI) must be singular, meaning its determinant must be zero:

**|A - λI| = 0**

This determinant equation is called the **characteristic equation** of matrix A. The polynomial |A - λI| is the characteristic polynomial, and its roots are the eigenvalues.

### 2. Characteristic Polynomial and Eigenvalues

For an n × n matrix A, the characteristic polynomial is given by:

**p(λ) = |A - λI| = (-1)ⁿ(λⁿ + c₁λⁿ⁻¹ + ... + cₙ₋₁λ + cₙ)**

The eigenvalues λ₁, λ₂, ..., λₙ are the roots of p(λ) = 0. Some important properties include:

- The sum of eigenvalues (trace) equals the sum of diagonal elements: Σλᵢ = tr(A)
- The product of eigenvalues equals the determinant: Πλᵢ = |A|
- Eigenvalues of a triangular matrix are its diagonal entries
- Eigenvalues of A and Aᵀ are identical

### 3. Eigenvectors and Eigenspaces

For each eigenvalue λ, the set of all eigenvectors corresponding to λ, along with the zero vector, forms a subspace called the **eigenspace**. This eigenspace is the null space of (A - λI):

**Eλ = {v ∈ ℝⁿ : (A - λI)v = 0}**

The dimension of the eigenspace is the geometric multiplicity of λ, while the multiplicity of λ as a root of the characteristic polynomial is the algebraic multiplicity. For each eigenvalue, there is at least one eigenvector, and the geometric multiplicity is always less than or equal to the algebraic multiplicity.

### 4. Cayley-Hamilton Theorem

The Cayley-Hamilton theorem states that every square matrix satisfies its own characteristic equation. If p(λ) = λⁿ + c₁λⁿ⁻¹ + ... + cₙ₋₁λ + cₙ is the characteristic polynomial of A, then:

**p(A) = Aⁿ + c₁Aⁿ⁻¹ + ... + cₙ₋₁A + cₙI = 0**

This theorem is extremely useful for:

- Computing powers of matrices
- Finding inverses of matrices
- Simplifying matrix expressions
- Solving systems of linear differential equations

### 5. Diagonalization

A matrix A is said to be diagonalizable if there exists an invertible matrix P such that:

**P⁻¹AP = D**

where D is a diagonal matrix containing the eigenvalues of A. The columns of P are the corresponding eigenvectors. A matrix is diagonalizable if and only if it has n linearly independent eigenvectors (i.e., the sum of geometric multiplicities equals n).

**Procedure for diagonalization:**

1. Find all eigenvalues of A
2. Find linearly independent eigenvectors for each eigenvalue
3. Form matrix P with eigenvectors as columns
4. Form diagonal matrix D with eigenvalues on diagonal
5. Verify that P⁻¹AP = D

### 6. Similar Matrices

Two matrices A and B are similar if there exists an invertible matrix P such that B = P⁻¹AP. Similar matrices share important properties:

- Same determinant
- Same rank
- Same trace
- Same characteristic polynomial (hence same eigenvalues)
- Same rank

### 7. Quadratic Forms

A quadratic form in n variables is a homogeneous polynomial of degree 2:

**Q(x) = xᵀAx = ΣᵢΣⱼ aᵢⱼxᵢxⱼ**

where A is a symmetric matrix. Quadratic forms are classified as:

- **Positive definite**: Q(x) > 0 for all x ≠ 0
- **Positive semi-definite**: Q(x) ≥ 0 for all x
- **Negative definite**: Q(x) < 0 for all x ≠ 0
- **Negative semi-definite**: Q(x) ≤ 0 for all x
- **Indefinite**: Q(x) can be positive or negative

A symmetric matrix A is:

- Positive definite if all eigenvalues are positive
- Positive semi-definite if all eigenvalues are non-negative

## Examples

### Example 1: Finding Eigenvalues and Eigenvectors

**Problem:** Find the eigenvalues and eigenvectors of A = [[3, 1], [1, 3]]

**Solution:**

**Step 1: Find the characteristic polynomial**

|A - λI| = |3-λ, 1; 1, 3-λ| = (3-λ)² - 1 = λ² - 6λ + 8

**Step 2: Find eigenvalues**

λ² - 6λ + 8 = 0
(λ - 2)(λ - 4) = 0
λ₁ = 2, λ₂ = 4

**Step 3: Find eigenvector for λ₁ = 2**

(A - 2I)v = 0
[[1, 1], [1, 1]] [x, y]ᵀ = [0, 0]ᵀ
x + y = 0 ⇒ y = -x

Eigenvector: v₁ = [1, -1]ᵀ (any scalar multiple)

**Step 4: Find eigenvector for λ₂ = 4**

(A - 4I)v = 0
[[-1, 1], [1, -1]] [x, y]ᵀ = [0, 0]ᵀ
-x + y = 0 ⇒ y = x

Eigenvector: v₂ = [1, 1]ᵀ (any scalar multiple)

**Answer:** Eigenvalues: 2, 4; Eigenvectors: [1, -1]ᵀ and [1, 1]ᵀ respectively

### Example 2: Using Cayley-Hamilton Theorem

**Problem:** Using Cayley-Hamilton theorem, find A⁴ for A = [[2, 1], [1, 1]]

**Solution:**

**Step 1: Find characteristic polynomial**

|A - λI| = |2-λ, 1; 1, 1-λ| = (2-λ)(1-λ) - 1 = λ² - 3λ + 1

**Step 2: Apply Cayley-Hamilton**

A² - 3A + I = 0
A² = 3A - I

**Step 3: Compute higher powers**

A³ = A·A² = A(3A - I) = 3A² - A = 3(3A - I) - A = 8A - 3I

A⁴ = A·A³ = A(8A - 3I) = 8A² - 3A = 8(3A - I) - 3A = 24A - 8I - 3A = 21A - 8I

**Step 4: Substitute A**

A⁴ = 21[[2, 1], [1, 1]] - 8[[1, 0], [0, 1]]
= [[42, 21], [21, 21]] - [[8, 0], [0, 8]]
= [[34, 21], [21, 13]]

**Answer:** A⁴ = [[34, 21], [21, 13]]

### Example 3: Diagonalizing a Matrix

**Problem:** Diagonalize the matrix A = [[4, 2], [2, 1]] if possible.

**Solution:**

**Step 1: Find eigenvalues**

|A - λI| = |4-λ, 2; 2, 1-λ| = (4-λ)(1-λ) - 4 = λ² - 5λ + 4 - 4 = λ² - 5λ

λ(λ - 5) = 0 ⇒ λ₁ = 0, λ₂ = 5

**Step 2: Find eigenvectors**

For λ₁ = 0: (A - 0I)v = 0 ⇒ [[4, 2], [2, 1]]v = 0
4x + 2y = 0 ⇒ 2x + y = 0 ⇒ y = -2x
v₁ = [1, -2]ᵀ

For λ₂ = 5: (A - 5I)v = 0 ⇒ [[-1, 2], [2, -4]]v = 0
-x + 2y = 0 ⇒ x = 2y
v₂ = [2, 1]ᵀ

**Step 3: Form P and D**

P = [[1, 2], [-2, 1]], D = [[0, 0], [0, 5]]

**Step 4: Verify diagonalization**

P⁻¹ = (1/(1-(-4)))[[1, -2], [2, 1]] = [[1/5, -2/5], [2/5, 1/5]]

P⁻¹AP = [[1/5, -2/5], [2/5, 1/5]] [[4, 2], [2, 1]] [[1, 2], [-2, 1]]
= [[0, 0], [0, 5]] = D ✓

**Answer:** A is diagonalizable with P = [[1, 2], [-2, 1]] and D = [[0, 0], [0, 5]]

## Exam Tips

1. **Characteristic Equation**: Always start by computing |A - λI| = 0. For 2×2 matrices, use the shortcut: λ² - (trace)λ + (det) = 0

2. **Verification**: After finding eigenvalues and eigenvectors, verify Av = λv for at least one case to catch calculation errors

3. **Cayley-Hamilton Applications**: Remember that CH theorem can compute A⁻¹ when det(A) ≠ 0: A⁻¹ = -(1/cₙ)(Aⁿ⁻¹ + c₁Aⁿ⁻² + ... + cₙ₋₁I)

4. **Diagonalization Condition**: A matrix with n distinct eigenvalues is always diagonalizable - this is the quickest check in exams

5. **Quadratic Forms**: For classification, use the leading principal minors (Sylvester's criterion) or check eigenvalues of the symmetric matrix

6. **Similar Matrices**: Remember that similar matrices have identical eigenvalues, determinants, traces, and ranks - use this for verification

7. **Complex Eigenvalues**: When eigenvalues are complex conjugates (a ± ib), the matrix cannot be diagonalized over real numbers but can be over complex numbers
