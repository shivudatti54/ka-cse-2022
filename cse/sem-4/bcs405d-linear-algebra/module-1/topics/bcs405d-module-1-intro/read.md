# Introduction to Linear Algebra

## Table of Contents

- [Introduction to Linear Algebra](#introduction-to-linear-algebra)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Matrices](#1-matrices)
  - [2. Vectors](#2-vectors)
  - [3. Systems of Linear Equations](#3-systems-of-linear-equations)
  - [4. Determinants](#4-determinants)
  - [5. Rank of a Matrix](#5-rank-of-a-matrix)
  - [6. Vector Spaces](#6-vector-spaces)
- [Examples](#examples)
  - [Example 1: Matrix Multiplication](#example-1-matrix-multiplication)
  - [Example 2: Solving System Using Gaussian Elimination](#example-2-solving-system-using-gaussian-elimination)
  - [Example 3: Finding Determinant](#example-3-finding-determinant)
- [Exam Tips](#exam-tips)

## Introduction

Linear Algebra is a fundamental branch of mathematics that deals with vectors, vector spaces, linear transformations, and systems of linear equations. It serves as the backbone for numerous engineering and scientific applications, from computer graphics and machine learning to structural engineering and quantum computing. For Computer Science and Engineering students at university, Linear Algebra provides the mathematical foundation essential for understanding algorithms, data structures, and computational techniques used in modern software development.

The subject originated from the study of linear equations and their solutions, evolving into a comprehensive mathematical framework that generalizes to n-dimensional spaces. Unlike calculus, which deals with continuous change, Linear Algebra focuses on linear relationships and transformations, making it particularly suitable for digital computation where discrete operations dominate. The beauty of Linear Algebra lies in its elegant balance between theoretical depth and practical applicability—every concept learned has direct engineering applications that students will encounter throughout their careers.

This module introduces the core concepts of Linear Algebra, beginning with matrices and their operations, progressing through vectors and vector spaces, and culminating in the solution techniques for systems of linear equations. Mastery of these foundational topics is crucial as they form the basis for more advanced topics like eigenvalues, eigenvectors, and matrix decompositions covered in subsequent modules.

## Key Concepts

### 1. Matrices

A matrix is a rectangular array of numbers, symbols, or expressions arranged in rows and columns. The size or dimension of a matrix is defined by the number of rows (m) and columns (n), written as m × n. Matrices serve as the primary tool for representing and solving linear systems in Linear Algebra.

**Types of Matrices:**

- **Row Matrix:** A matrix with single row (1 × n)
- **Column Matrix:** A matrix with single column (m × 1)
- **Square Matrix:** Number of rows equals number of columns (m = n)
- **Diagonal Matrix:** A square matrix where all non-diagonal elements are zero
- **Identity Matrix (I):** A diagonal matrix with all diagonal elements equal to 1
- **Zero Matrix (O):** All elements are zero
- **Symmetric Matrix:** A = A^T (matrix equals its transpose)
- **Skew-Symmetric Matrix:** A^T = -A

**Matrix Operations:**

- **Addition:** Two matrices of same dimension can be added element-wise
- **Scalar Multiplication:** Each element multiplied by a scalar value
- **Matrix Multiplication:** The (i,j) element of product AB is computed by taking dot product of i-th row of A with j-th column of B

### 2. Vectors

A vector is a mathematical object that has both magnitude and direction. In Linear Algebra, vectors are often represented as ordered n-tuples or column matrices. Vectors form the building blocks of vector spaces and are essential for understanding linear transformations.

**Vector Operations:**

- **Addition:** Component-wise addition
- **Scalar Multiplication:** Each component multiplied by scalar
- **Dot Product (Scalar Product):** a·b = Σaᵢbᵢ
- **Cross Product (in 3D):** Produces a vector perpendicular to both input vectors
- **Magnitude:** ||v|| = √(v₁² + v₂² + ... + vₙ²)

### 3. Systems of Linear Equations

A linear equation in n variables has the form a₁x₁ + a₂x₂ + ... + aₙxₙ = b, where aᵢ are coefficients, xᵢ are variables, and b is the constant term. A system of linear equations consists of multiple such equations that must be satisfied simultaneously.

**Methods of Solving:**

- **Gaussian Elimination:** Forward elimination to row echelon form, then back substitution
- **Gauss-Jordan Elimination:** Reduces to reduced row echelon form (RREF)
- **Matrix Inverse Method:** For systems Ax = b, solution is x = A⁻¹b (when A is invertible)
- **Cramer's Rule:** Uses determinants for small systems

### 4. Determinants

The determinant is a scalar value derived from a square matrix that encodes important properties of the linear transformation described by the matrix. For a 2×2 matrix [[a,b],[c,d]], the determinant is ad - bc.

**Properties of Determinants:**

- det(AB) = det(A) × det(B)
- det(A⁻¹) = 1/det(A)
- det(A^T) = det(A)
- If two rows/columns are identical, det(A) = 0
- Swapping rows changes sign of determinant

### 5. Rank of a Matrix

The rank of a matrix is the maximum number of linearly independent rows or columns. It provides crucial information about the solvability of linear systems:

- If rank(A) = rank([A|b]) = n (number of variables), unique solution exists
- If rank(A) = rank([A|b]) < n, infinitely many solutions
- If rank(A) < rank([A|b]), no solution (inconsistent system)

### 6. Vector Spaces

A vector space is a collection of vectors that can be added together and multiplied by scalars to produce another vector within the same space. The space must satisfy eight axioms including closure under addition and scalar multiplication, commutativity, associativity, existence of additive identity and inverses.

## Examples

### Example 1: Matrix Multiplication

Given A = [[1, 2], [3, 4]] and B = [[5, 6], [7, 8]], find AB.

**Solution:**

AB = [[1×5 + 2×7, 1×6 + 2×8], [3×5 + 4×7, 3×6 + 4×8]]
= [[5 + 14, 6 + 16], [15 + 28, 18 + 32]]
= [[19, 22], [43, 50]]

### Example 2: Solving System Using Gaussian Elimination

Solve the system:
x + y + z = 6
2x + y - z = 1
3x + 2y + z = 8

**Solution:**

Write augmented matrix:
[1 1 1 | 6]
[2 1 -1 | 1]
[3 2 1 | 8]

R₂ → R₂ - 2R₁: [1 1 1 | 6]
[0 -1 -3 |-11]
[3 2 1 | 8]

R₃ → R₃ - 3R₁: [1 1 1 | 6]
[0 -1 -3 |-11]
[0 -1 -2 |-10]

R₃ → R₃ - R₂: [1 1 1 | 6]
[0 -1 -3 |-11]
[0 0 1 | 1]

From R₃: z = 1
From R₂: -y - 3(1) = -11 → -y = -8 → y = 8
From R₁: x + 8 + 1 = 6 → x = -3

Solution: x = -3, y = 8, z = 1

### Example 3: Finding Determinant

Find det(A) where A = [[4, 3], [2, 5]]

**Solution:**
det(A) = (4)(5) - (3)(2) = 20 - 6 = 14

## Exam Tips

1. **Remember matrix multiplication is NOT commutative:** AB ≠ BA in general. This is a common trick in exam questions.

2. **For inverse of 2×2 matrix:** Swap diagonal elements, negate off-diagonals, divide by determinant: [[a,b],[c,d]]⁻¹ = (1/det) × [[d,-b],[-c,a]]

3. **Rank shortcuts:** If you see a row of all zeros or two identical rows, rank is reduced. Also remember rank ≤ min(m,n) for m×n matrix.

4. **Determinant shortcuts:** For triangular matrices, determinant is product of diagonal elements. For identity, determinant = 1.

5. **System consistency check:** Always verify rank(A) = rank([A|b]) before solving. This saves time on inconsistent systems.

6. **Matrix operations dimension check:** For addition, dimensions must match. For multiplication, columns of A must equal rows of B (if A is m×n and B is n×p, result is m×p).

7. **Special matrices to recognize:** Identity matrix acts as multiplicative identity (AI = IA = A). Zero matrix is additive identity.
