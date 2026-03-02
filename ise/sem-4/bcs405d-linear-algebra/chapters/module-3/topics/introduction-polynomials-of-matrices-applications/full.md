# Linear Algebra

### Introduction

Linear algebra is a branch of mathematics that deals with the study of linear equations, vector spaces, and linear transformations. It is a fundamental subject that has numerous applications in various fields, including physics, engineering, computer science, and economics. In this module, we will explore some of the key concepts in linear algebra, including polynomials of matrices, the Cayley-Hamilton theorem, eigen spaces of a linear transformation, and characteristic and minimal polynomial.

### Polynomials of Matrices

A polynomial of a matrix is an expression of the form:

p(A) = a*n A^n + a*(n-1) A^(n-1) + ... + a_1 A + a_0 I

where A is a square matrix, a_i are scalars, and I is the identity matrix. The coefficients a_i are constants, and the powers of A are determined according to the rules of matrix multiplication.

To evaluate p(A), we need to multiply the matrix A by each power of A and then add up the resulting matrices, weighted by their corresponding coefficients.

### Examples

- Evaluate p(A) = A^2 + 2A + 3I for A = [[2, 1], [1, 2]]

  To evaluate p(A), we need to calculate A^2, 2A, and 3I, and then add them up:

  A^2 = [[2, 1], [1, 2]] _ [[2, 1], [1, 2]] = [[5, 4], [4, 5]]
  2A = 2 _ [[2, 1], [1, 2]] = [[4, 2], [2, 4]]
  3I = 3 \* [[1, 0], [0, 1]] = [[3, 0], [0, 3]]

  Therefore, p(A) = A^2 + 2A + 3I = [[5, 4], [4, 5]] + [[4, 2], [2, 4]] + [[3, 0], [0, 3]] = [[12, 6], [6, 12]]

- Evaluate p(A) = A^3 - 5A^2 + 6A - 3I for A = [[3, 2], [2, 3]]

  To evaluate p(A), we need to calculate A^3, 5A^2, 6A, and 3I, and then subtract and add them up:

  A^3 = [[3, 2], [2, 3]] _ [[3, 2], [2, 3]] = [[21, 18], [18, 21]]
  5A^2 = 5 _ [[3, 2], [2, 3]] _ [[3, 2], [2, 3]] = [[45, 40], [40, 45]]
  6A = 6 _ [[3, 2], [2, 3]] = [[18, 12], [12, 18]]
  3I = 3 \* [[1, 0], [0, 1]] = [[3, 0], [0, 3]]

  Therefore, p(A) = A^3 - 5A^2 + 6A - 3I = [[21, 18], [18, 21]] - [[45, 40], [40, 45]] + [[18, 12], [12, 18]] - [[3, 0], [0, 3]] = [[-9, -6], [-6, -9]]

### Applications of Cayley-Hamilton Theorem

The Cayley-Hamilton theorem states that every square matrix satisfies its own characteristic equation. This theorem has numerous applications in linear algebra, including:

- **Diagonalization**: The Cayley-Hamilton theorem allows us to diagonalize a matrix by using its characteristic polynomial.
- **Eigenvalues**: The Cayley-Hamilton theorem provides a way to find the eigenvalues of a matrix by solving its characteristic equation.
- **Determinant**: The Cayley-Hamilton theorem allows us to calculate the determinant of a matrix using its characteristic polynomial.

### Examples

- Find the eigenvalues of the matrix A = [[2, 1], [1, 2]] using the Cayley-Hamilton theorem.

First, we need to calculate the characteristic polynomial of A:

p(A) = det(A - λI) = det([[2 - λ, 1], [1, 2 - λ]]) = (2 - λ)^2 - 1 = λ^2 - 4λ + 3

The Cayley-Hamilton theorem states that A satisfies its own characteristic equation, so we can write:

A^2 - 4A + 3I = 0

We can now solve for the eigenvalues of A by factoring the characteristic polynomial:

(λ - 1)(λ - 3) = 0

Therefore, the eigenvalues of A are λ = 1 and λ = 3.

- Find the determinant of the matrix A = [[2, 1], [1, 2]] using the Cayley-Hamilton theorem.

First, we need to calculate the characteristic polynomial of A:

p(A) = det(A - λI) = det([[2 - λ, 1], [1, 2 - λ]]) = (2 - λ)^2 - 1 = λ^2 - 4λ + 3

The Cayley-Hamilton theorem states that A satisfies its own characteristic equation, so we can write:

A^2 - 4A + 3I = 0

We can now calculate the determinant of A by using the characteristic polynomial:

det(A) = (-1)^n p(0) = (-1)^2 3 = 3

### Eigen Spaces of a Linear Transformation

An eigen space of a linear transformation is a subspace of the vector space that is spanned by the eigenvectors of the linear transformation. The eigen values of a linear transformation are scalars that satisfy the equation:

Ax = λx

where x is an eigenvector of the linear transformation.

### Examples

- Find the eigen vectors of the linear transformation T: R^2 → R^2 defined by the matrix A = [[2, 1], [1, 2]].

First, we need to find the eigenvalues of A:

p(A) = det(A - λI) = det([[2 - λ, 1], [1, 2 - λ]]) = (2 - λ)^2 - 1 = λ^2 - 4λ + 3

The Cayley-Hamilton theorem states that A satisfies its own characteristic equation, so we can write:

A^2 - 4A + 3I = 0

We can now solve for the eigenvalues of A by factoring the characteristic polynomial:

(λ - 1)(λ - 3) = 0

Therefore, the eigenvalues of A are λ = 1 and λ = 3.

Next, we need to find the corresponding eigen vectors:

Ax = λx

For λ = 1:

[[2, 1], [1, 2]] \* [x1, x2] = [x1, x2]

Let x1 = s and x2 = t. Then:

2s + t = x1
s + 2t = x2

We can now solve for s and t:

s = 1
t = 0

Therefore, one eigenvector of A is [1, 0].

For λ = 3:

[[2, 1], [1, 2]] \* [x1, x2] = [3x1, 3x2]

Let x1 = s and x2 = t. Then:

2s + t = 3s
s + 2t = 3t

We can now solve for s and t:

s = 0
t = 0

Therefore, another eigenvector of A is [0, 0].

- Find the eigen spaces of the linear transformation T: R^2 → R^2 defined by the matrix A = [[2, 1], [1, 2]].

We have already found the eigenvalues and eigenvectors of A:

Eigenvalues: λ = 1, λ = 3
Eigenvectors: [1, 0], [0, 0]

The eigen space corresponding to λ = 1 is spanned by the eigenvector [1, 0], so it is a one dimensional subspace of R^2.

The eigen space corresponding to λ = 3 is spanned by the eigenvector [0, 0], but since this eigenvector is the zero vector, the eigen space corresponds to λ = 3 is the trivial subspace {0}.

### Characteristic and Minimal Polynomials

The characteristic polynomial of a matrix A is a polynomial of the form:

p(A) = det(A - λI)

The minimal polynomial of a matrix A is a polynomial of the form:

m(A) = det(A - λI)

such that m(A) is the smallest degree polynomial that annihilates A.

### Examples

- Find the characteristic and minimal polynomials of the matrix A = [[2, 1], [1, 2]].

First, we need to calculate the characteristic polynomial of A:

p(A) = det(A - λI) = det([[2 - λ, 1], [1, 2 - λ]]) = (2 - λ)^2 - 1 = λ^2 - 4λ + 3

The characteristic polynomial is p(A) = λ^2 - 4λ + 3.

Next, we need to find the minimal polynomial of A. To do this, we need to find the smallest degree polynomial that annihilates A. We can start by dividing the characteristic polynomial by the smallest degree polynomial:

(λ^2 - 4λ + 3) = (λ - 1)(λ - 3)

The quotient is λ - 1, so the minimal polynomial of A is m(A) = (λ - 1).

### Further Reading

- "Linear Algebra and Its Applications" by Gilbert Strang
- "A First Course in Linear Algebra" by David C. Lay
- "Linear Algebra" by Jim Hefferon
- "Introduction to Linear Algebra" by Mark Sherman
