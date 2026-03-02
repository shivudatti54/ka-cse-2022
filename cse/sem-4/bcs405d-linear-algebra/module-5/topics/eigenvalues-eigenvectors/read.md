# Eigenvalues and Eigenvectors

## Table of Contents

- [Eigenvalues and Eigenvectors](#eigenvalues-and-eigenvectors)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of Eigenvalues and Eigenvectors](#definition-of-eigenvalues-and-eigenvectors)
  - [Characteristic Equation](#characteristic-equation)
  - [Finding Eigenvalues and Eigenvectors](#finding-eigenvalues-and-eigenvectors)
  - [Properties of Eigenvalues](#properties-of-eigenvalues)
  - [Algebraic and Geometric Multiplicity](#algebraic-and-geometric-multiplicity)
  - [Diagonalization](#diagonalization)
  - [Cayley-Hamilton Theorem](#cayley-hamilton-theorem)
- [Examples](#examples)
  - [Example 1: Finding Eigenvalues and Eigenvectors of a 2×2 Matrix](#example-1-finding-eigenvalues-and-eigenvectors-of-a-22-matrix)
  - [Example 2: Verifying Eigenvalue-Eigenvector Relationship](#example-2-verifying-eigenvalue-eigenvector-relationship)
  - [Example 3: Diagonalization](#example-3-diagonalization)
- [Exam Tips](#exam-tips)

## Introduction

Eigenvalues and Eigenvectors are fundamental concepts in Linear Algebra with extensive applications in engineering, physics, computer science, and data analysis. In simple terms, when we apply a linear transformation to a vector, an eigenvector is a special vector that does not change its direction—only its magnitude may change. The factor by which the eigenvector's length changes is called the eigenvalue. These concepts form the backbone of many advanced topics including diagonalization, quadratic forms, and principal component analysis. Understanding eigenvalues and eigenvectors is crucial for solving systems of differential equations, stability analysis in control systems, and quantum mechanics. This topic carries significant weight in the university examinations, and a thorough understanding can help students score high marks.

## Key Concepts

### Definition of Eigenvalues and Eigenvectors

Let A be an n×n square matrix. A non-zero vector v is called an eigenvector of A if there exists a scalar λ such that:

**Av = λv**

The scalar λ is called the eigenvalue corresponding to the eigenvector v.

### Characteristic Equation

The eigenvalues of matrix A are the roots of the characteristic equation:

**det(A - λI) = 0**

where I is the n×n identity matrix and det denotes the determinant.

### Finding Eigenvalues and Eigenvectors

**Step 1:** Form the matrix (A - λI)

**Step 2:** Compute the determinant and set it equal to zero: det(A - λI) = 0

**Step 3:** Solve the resulting polynomial equation in λ to find eigenvalues

**Step 4:** For each eigenvalue λ, solve (A - λI)v = 0 to find the corresponding eigenvectors

### Properties of Eigenvalues

1. The sum of eigenvalues equals the trace of the matrix (sum of diagonal elements)
2. The product of eigenvalues equals the determinant of the matrix
3. If λ is an eigenvalue of A, then λ^k is an eigenvalue of A^k
4. If A is invertible, then 1/λ is an eigenvalue of A⁻¹
5. Eigenvalues of a symmetric matrix are all real
6. Eigenvalues of an orthogonal matrix have absolute value 1

### Algebraic and Geometric Multiplicity

The algebraic multiplicity of an eigenvalue is the number of times it appears as a root of the characteristic equation. The geometric multiplicity is the dimension of the eigenspace (number of linearly independent eigenvectors corresponding to that eigenvalue). Geometric multiplicity is always less than or equal to algebraic multiplicity.

### Diagonalization

A matrix A is diagonalizable if there exists a matrix P such that P⁻¹AP = D, where D is a diagonal matrix. The columns of P are the eigenvectors of A, and the diagonal elements of D are the corresponding eigenvalues. A sufficient condition for diagonalization is that A has n linearly independent eigenvectors.

### Cayley-Hamilton Theorem

Every square matrix satisfies its own characteristic equation. If the characteristic polynomial is p(λ) = det(A - λI) = (-1)ⁿλⁿ + cₙ₋₁λⁿ⁻¹ + ... + c₀, then p(A) = 0.

## Examples

### Example 1: Finding Eigenvalues and Eigenvectors of a 2×2 Matrix

**Problem:** Find the eigenvalues and eigenvectors of A = [[4, 2], [1, 3]]

**Solution:**

**Step 1:** Form characteristic equation
det(A - λI) = det([[4-λ, 2], [1, 3-λ]]) = 0

**Step 2:** Compute determinant
(4-λ)(3-λ) - 2(1) = 0
12 - 4λ - 3λ + λ² - 2 = 0
λ² - 7λ + 10 = 0

**Step 3:** Solve for λ
(λ - 5)(λ - 2) = 0
λ₁ = 5, λ₂ = 2

**Step 4:** Find eigenvectors

For λ₁ = 5:
(A - 5I)v = 0
[[-1, 2], [1, -2]] [x, y]ᵀ = [0, 0]
-x + 2y = 0 ⇒ x = 2y
Eigenvector: v₁ = [2, 1]ᵀ

For λ₂ = 2:
(A - 2I)v = 0
[[2, 2], [1, 1]] [x, y]ᵀ = [0, 0]
2x + 2y = 0 ⇒ x = -y
Eigenvector: v₂ = [-1, 1]ᵀ

### Example 2: Verifying Eigenvalue-Eigenvector Relationship

**Problem:** Verify that v = [1, 2]ᵀ is an eigenvector of A = [[3, 1], [2, 4]] and find the corresponding eigenvalue.

**Solution:**

Compute Av:
Av = [[3, 1], [2, 4]] [1, 2]ᵀ = [3(1) + 1(2), 2(1) + 4(2)]ᵀ = [5, 10]ᵀ

Notice that [5, 10]ᵀ = 5 × [1, 2]ᵀ

Therefore, λ = 5 and v = [1, 2]ᵀ is indeed an eigenvector corresponding to eigenvalue λ = 5.

### Example 3: Diagonalization

**Problem:** Diagonalize the matrix A = [[6, -2], [-2, 3]]

**Solution:**

First, find eigenvalues:
det(A - λI) = det([[6-λ, -2], [-2, 3-λ]]) = 0
(6-λ)(3-λ) - 4 = 0
λ² - 9λ + 14 = 0
(λ - 7)(λ - 2) = 0
λ₁ = 7, λ₂ = 2

Find eigenvectors:
For λ = 7: v₁ = [1, -1]ᵀ
For λ = 2: v₂ = [2, 1]ᵀ

Form P = [[1, 2], [-1, 1]] and D = [[7, 0], [0, 2]]

Verify: P⁻¹AP = D
P⁻¹ = (1/3)[[1, -2], [1, 1]]
P⁻¹AP = [[7, 0], [0, 2]] = D ✓

## Exam Tips

1. **Always start with the characteristic equation** det(A - λI) = 0 when finding eigenvalues—this is the standard approach and earns full method marks.

2. **Remember the properties**: Sum of eigenvalues = Trace, Product = Determinant. Use these for quick verification of your answers.

3. **For 3×3 matrices**, expand the determinant carefully using cofactor expansion or SARRUS method to avoid algebraic errors.

4. **When finding eigenvectors**, set up the augmented matrix and use Gaussian elimination—show all intermediate steps in university exams.

5. **Check your answers**: Verify that Av = λv for each eigenvalue-eigenvector pair. This is a quick way to catch calculation errors.

6. **Diagonalization requires n linearly independent eigenvectors**—if the matrix has repeated eigenvalues, check if geometric multiplicity equals algebraic multiplicity.

7. **For symmetric matrices**, eigenvalues are always real and eigenvectors corresponding to distinct eigenvalues are orthogonal—use this property to verify results.

8. **Time management**: In exam, if stuck on a complex determinant, use the characteristic polynomial formula for 2×2 and 3×3 matrices directly.

9. **Cayley-Hamilton theorem applications**: Can be used to find A⁻¹ and powers of matrices—remember this shortcut for inverse calculations.

10. **Word problems**: Some university questions apply eigenvalues to stability analysis or vibration problems—understand the physical interpretation of eigenvalues.
