# Linear Algebra: Eigenvalues and EigenVectors

=====================================================

## Introduction

---

Linear Algebra is a branch of mathematics that deals with the study of linear equations, vector spaces, and linear transformations. Eigenvalues and EigenVectors are fundamental concepts in Linear Algebra that help us understand the behavior of linear transformations.

### Key Concepts

- **Eigenvalues**: Scalars that represent how much a linear transformation changes a vector.
- **EigenVectors**: Vectors that, when transformed by a linear transformation, result in a scaled version of themselves.

## Polynomials of Matrices

---

Polynomials of Matrices are expressions that involve powers and products of matrices. We can use polynomials to study the properties of matrices and their eigenvalues.

### Definition

A polynomial of a matrix A is an expression of the form:

f(A) = a*n A^n + a*(n-1) A^(n-1) + ... + a_1 A + a_0 I

where a_i are constants, I is the identity matrix, and n is a positive integer.

### Example

f(A) = 3A^2 + 2A - 1

## Applications of Cayley-Hamilton Theorem

---

The Cayley-Hamilton Theorem states that every square matrix satisfies its own characteristic equation.

### Definition

The characteristic equation of a matrix A is:

|A - λI| = 0

where λ is an eigenvalue of A, and I is the identity matrix.

### Theorem

The Cayley-Hamilton Theorem states that:

f(A) = 0

for any polynomial f(x) that is the characteristic equation of A.

### Example

Suppose A is a 2x2 matrix with characteristic equation:

x^2 - 3x + 2 = 0

Then, by the Cayley-Hamilton Theorem, we have:

A^2 - 3A + 2I = 0

## Eigen Spaces of a Linear Transformation

---

An eigen space of a linear transformation T is the set of all vectors that are mapped to zero by T.

### Definition

The eigen space of T corresponding to an eigenvalue λ is:

E_λ = {v | T(v) = λv}

### Example

Suppose T is a linear transformation on R^2 with matrix A, and λ = 2 is an eigenvalue of T. Then, the eigen space E_2 is:

E_2 = {v | Av = 2v}

## Characteristic and Minimal Polynomials

---

The characteristic polynomial and minimal polynomial of a matrix A are polynomials that describe the eigenvalues and eigenvalues of A, respectively.

### Definition

The characteristic polynomial of A is:

p_A(x) = |A - xI|

The minimal polynomial of A is:

q_A(x) = min{f(x) | f(x) divides p_A(x)}

### Example

Suppose A is a 3x3 matrix with characteristic polynomial:

x^3 - 6x^2 + 11x - 6

Then, the minimal polynomial of A must divide this polynomial and have degree at most 3.

### Study Tips

- Understand the definitions of eigenvalues, eigen vectors, polynomials of matrices, Cayley-Hamilton theorem, eigen spaces, characteristic polynomials, and minimal polynomials.
- Learn to calculate the characteristic and minimal polynomials of a matrix.
- Practice finding the eigenvalues and eigen vectors of a matrix.
- Learn to apply the Cayley-Hamilton theorem to solve problems.

### Practice Problems

1.  Find the characteristic and minimal polynomials of the matrix:

A = [[2, 1], [1, 2]]

2.  Find the eigenvalues and eigen vectors of the matrix:

A = [[1, 0], [0, 1]]

3.  Find the eigen space of the linear transformation T with matrix A, where T(v) = Av.

4.  Apply the Cayley-Hamilton theorem to solve a linear system.

5.  Find the minimal polynomial of the matrix:

A = [[0, 1], [1, 0]]

Note: These practice problems are meant to be a starting point for your studying. Make sure to practice them thoroughly and understand the concepts behind them.
