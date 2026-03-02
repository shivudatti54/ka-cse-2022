# Introduction to Eigenvalues and Eigenvectors

## Table of Contents

- [Introduction to Eigenvalues and Eigenvectors](#introduction-to-eigenvalues-and-eigenvectors)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of Eigenvalues and Eigenvectors](#definition-of-eigenvalues-and-eigenvectors)
  - [Algebraic and Geometric Multiplicity](#algebraic-and-geometric-multiplicity)
  - [The Eigenspace](#the-eigenspace)
- [Examples](#examples)
  - [Example 1: Computing Eigenvalues and Eigenvectors](#example-1-computing-eigenvalues-and-eigenvectors)
  - [Example 2: Matrix with Repeated Eigenvalue](#example-2-matrix-with-repeated-eigenvalue)
  - [Example 3: Matrix with Complex Eigenvalues](#example-3-matrix-with-complex-eigenvalues)
- [Exam Tips](#exam-tips)

## Introduction

Eigenvalues and eigenvectors constitute one of the most fundamental concepts in linear algebra, with far-reaching applications across physics, engineering, computer science, and economics. The term "eigen" originates from the German word meaning "own" or "characteristic," reflecting the idea that these special vectors retain their direction under a linear transformation while only being scaled by a factor known as the eigenvalue.

The study of eigenvalues and eigenvectors provides profound insights into the behavior of linear transformations. When we apply a linear transformation to a vector, the result is typically a vector pointing in a completely different direction. However, there exist special vectors—eigenvectors—for which the transformation produces only a scalar multiple of the original vector. This remarkable property makes eigenvalues and eigenvectors indispensable tools for understanding the intrinsic structure of matrices and linear operators.

This introduction establishes the foundational definitions and conceptual framework necessary for exploring the rich theory of eigenvalues and eigenvectors. We shall examine the characteristic equation, explore methods for computing eigenvalues and eigenvectors, and develop an understanding of their geometric significance. The concepts introduced here will serve as building blocks for more advanced topics such as diagonalization, Jordan canonical form, and spectral decomposition.

## Key Concepts

### Definition of Eigenvalues and Eigenvectors

Let **A** be an n × n square matrix. A scalar λ is called an **eigenvalue** of A if there exists a non-zero vector **v** in ℝⁿ such that:

**Av = λv**

The non-zero vector **v** is then called an **eigenvector** corresponding to the eigenvalue λ. The equation Av = λv can be rearranged as:

**(A - λI)v = 0**

where I is the n × n identity matrix. For a non-zero eigenvector v to exist, the matrix (A - λI) must be singular, meaning its determinant must equal zero. This leads to the **characteristic equation**:

**det(A - λI) = 0**

The polynomial det(A - λI) is called the **characteristic polynomial** of A. The roots of this polynomial are precisely the eigenvalues of A.

### Algebraic and Geometric Multiplicity

Each eigenvalue λ has an **algebraic multiplicity**, which is the number of times it appears as a root of the characteristic polynomial. The **geometric multiplicity** of an eigenvalue is the dimension of its eigenspace, which is the set of all eigenvectors corresponding to that eigenvalue (including the zero vector). It is always true that:

**1 ≤ geometric multiplicity ≤ algebraic multiplicity**

When the geometric multiplicity equals the algebraic multiplicity for all eigenvalues, the matrix is said to be **diagonalizable**.

### The Eigenspace

For a given eigenvalue λ, the eigenspace Eλ is defined as:

**Eλ = {v ∈ ℝⁿ : Av = λv} = null(A - λI)**

The eigenspace is a subspace of ℝⁿ, and its dimension equals the geometric multiplicity of λ. Finding eigenvectors involves solving the homogeneous system (A - λI)v = 0 for each eigenvalue λ.

## Examples

### Example 1: Computing Eigenvalues and Eigenvectors

Let A = [[2, 1], [1, 2]] be a 2×2 matrix.

**Step 1: Find the characteristic polynomial**

det(A - λI) = det([[2-λ, 1], [1, 2-λ]]) = (2-λ)² - 1 = λ² - 4λ + 3

**Step 2: Solve the characteristic equation**

λ² - 4λ + 3 = 0
(λ - 1)(λ - 3) = 0
λ₁ = 1, λ₂ = 3

**Step 3: Find eigenvectors**

For λ₁ = 1:
(A - I)v = [[1, 1], [1, 1]]v = 0
The system gives x + y = 0, so v₁ = [1, -1]ᵀ

For λ₂ = 3:
(A - 3I)v = [[-1, 1], [1, -1]]v = 0
The system gives -x + y = 0, so v₂ = [1, 1]ᵀ

### Example 2: Matrix with Repeated Eigenvalue

Let A = [[4, 0], [0, 4]] = 4I.

The characteristic polynomial is (4-λ)² = 0, so λ = 4 is an eigenvalue with algebraic multiplicity 2.

All non-zero vectors are eigenvectors since Av = 4v for any v. The eigenspace has dimension 2, meaning the geometric multiplicity equals 2.

### Example 3: Matrix with Complex Eigenvalues

Let A = [[0, -1], [1, 0]] (rotation by 90°).

Characteristic polynomial: λ² + 1 = 0
Eigenvalues: λ = i, λ = -i (complex conjugates)

This matrix has no real eigenvalues, which makes geometric sense—a 90° rotation sends every real vector to a perpendicular direction, so no non-zero vector can satisfy Av = λv with λ real.

## Exam Tips

1. **Master the characteristic equation**: Remember that eigenvalues are roots of det(A - λI) = 0. Always start by computing this determinant.

2. **Verify eigenvectors correctly**: After finding an eigenvalue λ, substitute back into (A - λI)v = 0 to find the corresponding eigenvectors.

3. **Check the sum of eigenvalues**: The trace of a matrix (sum of diagonal elements) equals the sum of eigenvalues. This provides a useful verification.

4. **Check the product of eigenvalues**: The determinant of a matrix equals the product of its eigenvalues. Always verify your computed eigenvalues satisfy this property.

5. **Understand geometric vs. algebraic multiplicity**: This distinction is crucial for determining diagonalizability and appears frequently in examination questions.

6. **Handle zero eigenvalues carefully**: λ = 0 is a valid eigenvalue when the matrix is singular (det(A) = 0). The eigenvector in this case satisfies Av = 0.

7. **Practice with different matrix types**: Be comfortable finding eigenvalues of diagonal, triangular, and symmetric matrices, as each has special properties that simplify computations.
