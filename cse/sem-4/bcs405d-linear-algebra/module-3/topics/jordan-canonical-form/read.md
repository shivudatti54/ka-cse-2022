# Jordan Canonical Form

## Table of Contents

- [Jordan Canonical Form](#jordan-canonical-form)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Eigenvalues and Eigenvectors](#1-eigenvalues-and-eigenvectors)
  - [2. Algebraic and Geometric Multiplicity](#2-algebraic-and-geometric-multiplicity)
  - [3. Generalized Eigenvectors](#3-generalized-eigenvectors)
  - [4. Jordan Block](#4-jordan-block)
  - [5. Jordan Matrix](#5-jordan-matrix)
  - [6. Jordan Canonical Form Theorem](#6-jordan-canonical-form-theorem)
  - [7. Cayley-Hamilton Theorem](#7-cayley-hamilton-theorem)
  - [8. Minimal Polynomial](#8-minimal-polynomial)
  - [9. Computing Jordan Form](#9-computing-jordan-form)
  - [10. Similar Matrices](#10-similar-matrices)
- [Examples](#examples)
  - [Example 1: Finding Jordan Form of a 2×2 Matrix](#example-1-finding-jordan-form-of-a-22-matrix)
  - [Example 2: Jordan Form with Distinct Eigenvalues](#example-2-jordan-form-with-distinct-eigenvalues)
  - [Example 3: Finding Jordan Form Given Eigenvalues](#example-3-finding-jordan-form-given-eigenvalues)
- [Exam Tips](#exam-tips)

## Introduction

The Jordan Canonical Form (also known as Jordan Normal Form or Jordan Standard Form) is one of the most important concepts in linear algebra, particularly in the study of linear transformations and matrices. Named after the French mathematician Camille Jordan, this form provides a canonical representation of a square matrix that captures the essential algebraic structure of the linear transformation it represents.

In practical terms, the Jordan Canonical Form simplifies complex matrix computations by transforming a given matrix into a nearly diagonal form through a similarity transformation. This is particularly valuable when dealing with systems of linear differential equations, vibration analysis, and control theory applications in engineering. For computer science students, understanding Jordan Canonical Form is essential for topics like Markov chains, graph theory (adjacency matrices), and machine learning algorithms involving eigendecomposition.

The Jordan form reveals the geometric multiplicity versus algebraic multiplicity of eigenvalues, information that is crucial for understanding the complete structure of a linear transformation. While real matrices may require complex eigenvalues and conjugate Jordan blocks, the theory extends naturally to both real and complex vector spaces.

## Key Concepts

### 1. Eigenvalues and Eigenvectors

Given a square matrix A of order n, a scalar λ is called an eigenvalue if there exists a non-zero vector v such that Av = λv. The vector v is called an eigenvector corresponding to the eigenvalue λ. The set of all eigenvalues is called the spectrum of A.

### 2. Algebraic and Geometric Multiplicity

- **Algebraic Multiplicity (mₐ)**: The number of times an eigenvalue λ appears as a root of the characteristic polynomial. If (x-λ)^mₐ divides the characteristic polynomial, then mₐ is the algebraic multiplicity.

- **Geometric Multiplicity (mᵍ)**: The dimension of the eigenspace corresponding to λ, i.e., the number of linearly independent eigenvectors for λ. Always mᵍ ≤ mₐ.

### 3. Generalized Eigenvectors

A vector v is a generalized eigenvector of rank k corresponding to eigenvalue λ if (A - λI)^k v = 0 but (A - λI)^(k-1) v ≠ 0. The chain of generalized eigenvectors forms the building blocks of Jordan blocks.

### 4. Jordan Block

A Jordan block of size k corresponding to eigenvalue λ is a k×k matrix of the form:

```
J(λ, k) = | λ 1 0 ... 0 |
 | 0 λ 1 ... 0 |
 | . . . . |
 | 0 0 ... λ 1 |
 | 0 0 ... 0 λ |
```

The diagonal contains λ, and the superdiagonal contains 1s. Every Jordan block has exactly one eigenvector.

### 5. Jordan Matrix

A Jordan matrix is a block diagonal matrix where each block is a Jordan block:

```
J = | J(λ₁, k₁) 0 ... 0 |
 | 0 J(λ₂, k₂) ... 0 |
 | . . . . |
 | 0 0 ... J(λₘ, kₘ) |
```

### 6. Jordan Canonical Form Theorem

For every square matrix A, there exists an invertible matrix P such that P⁻¹AP = J, where J is the Jordan Canonical Form of A. The Jordan form is unique up to the order of Jordan blocks.

### 7. Cayley-Hamilton Theorem

Every square matrix satisfies its own characteristic polynomial. If p(λ) = det(λI - A) = λⁿ + aₙ₋₁λⁿ⁻¹ + ... + a₀, then p(A) = Aⁿ + aₙ₋₁Aⁿ⁻¹ + ... + a₀I = 0.

### 8. Minimal Polynomial

The minimal polynomial m(x) is the monic polynomial of least degree such that m(A) = 0. It divides the characteristic polynomial and has the same irreducible factors.

### 9. Computing Jordan Form

To find the Jordan Canonical Form:

1. Find eigenvalues from characteristic polynomial |λI - A| = 0
2. For each eigenvalue λ, find the null space of (A - λI)^k for increasing k
3. Determine the number and sizes of Jordan blocks for each eigenvalue
4. Construct the Jordan matrix

### 10. Similar Matrices

Two matrices A and B are similar if there exists an invertible matrix P such that B = P⁻¹AP. Similar matrices represent the same linear transformation in different bases and have identical eigenvalues, characteristic polynomials, and Jordan forms.

## Examples

### Example 1: Finding Jordan Form of a 2×2 Matrix

**Problem**: Find the Jordan Canonical Form of A = [[4, 1], [0, 4]]

**Solution**:

**Step 1**: Find the characteristic polynomial
|λI - A| = |[λ-4, -1], [0, λ-4]| = (λ-4)²

Eigenvalue: λ = 4 with algebraic multiplicity mₐ = 2

**Step 2**: Find eigenvectors
(A - 4I) = [[0, 1], [0, 0]]

Solving (A - 4I)v = 0:
[[0, 1], [0, 0]][x, y]ᵀ = [0, 0]ᵀ
This gives y = 0, so x is free

Eigenvectors: v₁ = [1, 0]ᵀ (only one eigenvector)
Geometric multiplicity mᵍ = 1

**Step 3**: Find generalized eigenvector
We need v₂ such that (A - 4I)v₂ = v₁

Let v₂ = [a, b]ᵀ
[[0, 1], [0, 0]][a, b]ᵀ = [1, 0]ᵀ
This gives: b = 1, and 0 = 0 (second equation is automatically satisfied)

So v₂ = [0, 1]ᵀ works (a can be 0)

**Step 4**: Form P and find Jordan form
P = [v₁, v₂] = [[1, 0], [0, 1]]

P⁻¹AP = [[4, 1], [0, 4]] = J(4, 2)

**Answer**: Jordan Canonical Form J = [[4, 1], [0, 4]] (this matrix is already in Jordan form!)

---

### Example 2: Jordan Form with Distinct Eigenvalues

**Problem**: Find the Jordan Canonical Form of A = [[2, 0, 0], [0, 3, 1], [0, 0, 3]]

**Solution**:

**Step 1**: Characteristic polynomial
|λI - A| = |λ-2, 0, 0; 0, λ-3, -1; 0, 0, λ-3|
= (λ-2)(λ-3)²

Eigenvalues: λ₁ = 2 (mₐ = 1), λ₂ = 3 (mₐ = 2)

**Step 2**: For λ = 2:
(A - 2I) = [[0, 0, 0], [0, 1, 1], [0, 0, 1]]
Eigenvector: v₁ = [1, 0, 0]ᵀ
This gives one Jordan block J(2, 1)

**Step 3**: For λ = 3:
(A - 3I) = [[-1, 0, 0], [0, 0, 1], [0, 0, 0]]
Solving (A - 3I)v = 0:
-v₁ = 0, v₃ = 0, so v₁, v₂ free
Eigenvectors: [0, 1, 0]ᵀ, [0, 0, 1]ᵀ
Geometric multiplicity = 2 = algebraic multiplicity

Since mᵍ = mₐ = 2, we get two 1×1 blocks for λ = 3

**Step 4**: Jordan Canonical Form
J = [[2, 0, 0], [0, 3, 0], [0, 0, 3]]

**Answer**: J is a diagonal matrix with eigenvalues on the diagonal

---

### Example 3: Finding Jordan Form Given Eigenvalues

**Problem**: A 4×4 matrix has eigenvalues 2 (algebraic multiplicity 2, geometric multiplicity 1) and 3 (algebraic multiplicity 2, geometric multiplicity 2). Find the possible Jordan Canonical Forms.

**Solution**:

**For λ = 2**: mₐ = 2, mᵍ = 1
Since mᵍ < mₐ, we must have one Jordan block of size 2:
J(2, 2) = [[2, 1], [0, 2]]

**For λ = 3**: mₐ = 2, mᵍ = 2
Since mᵍ = mₐ, we get two 1×1 blocks:
J(3, 1) = [3], J(3, 1) = [3]

**Possible Jordan Canonical Forms**:

Since Jordan blocks for different eigenvalues can be arranged in any order, we have:

```
J = | 2 1 0 0 |
 | 0 2 0 0 |
 | 0 0 3 0 |
 | 0 0 0 3 |
```

**Answer**: The Jordan form consists of one 2×2 block for λ = 2 and two 1×1 blocks for λ = 3.

## Exam Tips

1. **Remember the key relationship**: For each eigenvalue, the number of Jordan blocks equals the geometric multiplicity, and the sum of the sizes of Jordan blocks equals the algebraic multiplicity.

2. **Characteristic vs Minimal Polynomial**: The characteristic polynomial is det(λI - A), while the minimal polynomial has the same roots but powers equal to the size of the largest Jordan block for each eigenvalue.

3. **Diagonalizable**: A matrix is diagonalizable if and only if for every eigenvalue, geometric multiplicity equals algebraic multiplicity (i.e., all Jordan blocks are 1×1).

4. **P⁻¹AP = J**: Remember that the similarity transformation preserves eigenvalues, determinant, trace, rank, and characteristic/minimal polynomials.

5. **Computing Jordan Form steps**: Always find eigenvalues first, then find bases for ker(A-λI)^k for increasing k to determine Jordan chain lengths.

6. **Cayley-Hamilton Application**: Use it to simplify matrix computations, express higher powers of A as combinations of lower powers, and find A⁻¹ when det(A) ≠ 0.

7. **Practice similar matrices**: Two matrices are similar iff they have the same Jordan Canonical Form (up to permutation of blocks).

8. **Complex eigenvalues**: For real matrices with complex eigenvalues, Jordan blocks come in conjugate pairs if the form must be real.

9. **Powers of Jordan blocks**: (J(λ, k))^m has λ^m on the diagonal and binomial coefficients on the superdiagonals - useful for computing matrix powers.

10. **Minimal polynomial degree**: The degree of the minimal polynomial equals the size of the largest Jordan block for each distinct eigenvalue.
