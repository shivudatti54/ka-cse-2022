# Characteristic Polynomial and Cayley-Hamilton Theorem

## Introduction

In linear algebra, the characteristic polynomial of a square matrix is a polynomial that encodes information about the matrix's eigenvalues. The Cayley-Hamilton theorem is a fundamental result that states that every square matrix satisfies its own characteristic polynomial. This theorem has far-reaching implications in various fields, including computer science, physics, and engineering.

The characteristic polynomial and Cayley-Hamilton theorem are essential tools in computing, particularly in areas like computer graphics, machine learning, and data analysis. They help us understand the properties of matrices and their behavior under various transformations.

## Key Concepts

### Characteristic Polynomial

Given a square matrix A of size n x n, the characteristic polynomial of A is defined as:

pA(x) = det(xI - A)

where I is the identity matrix of size n x n, and det denotes the determinant.

The characteristic polynomial is a monic polynomial of degree n, and its roots are the eigenvalues of A.

### Cayley-Hamilton Theorem

The Cayley-Hamilton theorem states that every square matrix A satisfies its own characteristic polynomial:

pA(A) = 0

This means that if we substitute A for x in the characteristic polynomial, we get the zero matrix.

### Proof of Cayley-Hamilton Theorem

The proof of the Cayley-Hamilton theorem involves showing that the matrix A satisfies its own characteristic polynomial. This can be done using various methods, including induction, algebraic manipulations, or geometric interpretations.

## Examples

### Example 1: Find the characteristic polynomial of a matrix

Suppose we have a 2 x 2 matrix A:

A = [[2, 1], [1, 3]]

To find the characteristic polynomial, we compute:

pA(x) = det(xI - A)
= det([[x-2, -1], [-1, x-3]])
= (x-2)(x-3) - (-1)(-1)
= x^2 - 5x + 5

The characteristic polynomial is pA(x) = x^2 - 5x + 5.

### Example 2: Verify the Cayley-Hamilton theorem for a matrix

Using the same matrix A as above, we can verify the Cayley-Hamilton theorem:

pA(A) = A^2 - 5A + 5I
= [[2, 1], [1, 3]]^2 - 5[[2, 1], [1, 3]] + 5[[1, 0], [0, 1]]
= [[4, 5], [5, 10]] - [[10, 5], [5, 15]] + [[5, 0], [0, 5]]
= [[0, 0], [0, 0]]

As expected, pA(A) = 0, verifying the Cayley-Hamilton theorem.

## Exam Tips

1. To find the characteristic polynomial, use the formula pA(x) = det(xI - A).
2. The characteristic polynomial is a monic polynomial of degree n, where n is the size of the matrix.
3. The roots of the characteristic polynomial are the eigenvalues of the matrix.
4. The Cayley-Hamilton theorem states that every square matrix satisfies its own characteristic polynomial.
5. To verify the Cayley-Hamilton theorem, substitute the matrix A for x in the characteristic polynomial and show that the result is the zero matrix.
6. The Cayley-Hamilton theorem has important implications in various fields, including computer science, physics, and engineering.
7. Be able to apply the Cayley-Hamilton theorem to solve problems involving matrices and their properties.