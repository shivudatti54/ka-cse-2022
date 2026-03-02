# Linear Algebra

## Module: Eigenvalues and EigenVectors

### Introduction

- Linear algebra is a branch of mathematics that studies vectors and linear transformations.
- Eigenvalues and eigenvalues are fundamental concepts in linear algebra.

### Polynomials of Matrices

- A polynomial of a matrix P is a mathematical expression of the form:
  P(x) = a*n P^n + a*{n-1} P^(n-1) + ... + a_1 P + a_0 I
- where P is an n x n matrix, a_i are coefficients, I is the identity matrix, and x is a variable.

### Applications of Cayley-Hamilton Theorem

- The Cayley-Hamilton theorem states that every square matrix satisfies its own characteristic equation.
- Formula: P(x) = x^n + a\_{n-1}x^(n-1) + ... + a_1x + a_0 I = 0
- Theorem states: P^n = a\_{n-1}P^(n-1) + ... + a_1P + a_0 I

### Eigen Spaces of a Linear Transformation

- The eigen space of a linear transformation T is the set of all vectors that remain unchanged under the transformation.
- Formula: Eigenv(λ) = {v | Tv = λv}
- The dimension of the eigenspace is equal to the multiplicity of the eigenvalue.

### Characteristic and Minimal Polynomial

- The characteristic polynomial of a matrix P is the polynomial of P defined in Theorem 1.
- The minimal polynomial of a matrix P is the smallest polynomial of P such that P^n = 0.
- Formula: Characteristic polynomial = det(xI - P)
- Formula: Minimal polynomial = gcd{Det(xI - P^k) | k = 1,2,...}

## Important Formulas and Definitions:

- Eigenvalue: λ
- Eigenvector: v
- Characteristic polynomial: det(xI - P)
- Minimal polynomial: gcd{Det(xI - P^k) | k = 1,2,...}
- Cayley-Hamilton Theorem: P(x) = x^n + a\_{n-1}x^(n-1) + ... + a_1x + a_0 I = 0
