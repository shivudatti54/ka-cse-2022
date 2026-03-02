# Polynomials of Matrices

## Table of Contents

- [Polynomials of Matrices](#polynomials-of-matrices)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Characteristic Polynomial](#characteristic-polynomial)
  - [Cayley-Hamilton Theorem](#cayley-hamilton-theorem)
  - [Minimal Polynomial](#minimal-polynomial)
  - [Polynomial of a Matrix](#polynomial-of-a-matrix)
  - [Applications of Matrix Polynomials](#applications-of-matrix-polynomials)
- [Examples](#examples)
  - [Example 1: Finding Characteristic Polynomial](#example-1-finding-characteristic-polynomial)
  - [Example 2: Verifying Cayley-Hamilton Theorem](#example-2-verifying-cayley-hamilton-theorem)
  - [Example 3: Computing A⁵ Using Cayley-Hamilton Theorem](#example-3-computing-a-using-cayley-hamilton-theorem)
- [Exam Tips](#exam-tips)

## Introduction

Polynomials of matrices form a fundamental concept in linear algebra with significant applications in engineering systems, control theory, and vibration analysis. When we substitute a square matrix into a polynomial, we obtain another matrix through matrix multiplication and scalar operations. This concept becomes particularly powerful when combined with the Cayley-Hamilton Theorem, which states that every square matrix satisfies its own characteristic equation. This theorem provides an elegant method for computing matrix powers, finding inverses, and evaluating matrix functions without performing extensive computations.

The study of matrix polynomials is essential for CSE students as it connects abstract algebraic concepts to practical engineering applications. In vibration analysis of mechanical systems, polynomial matrices help model dynamic behavior. In electrical circuits, they assist in analyzing network stability. The ability to express high powers of matrices as linear combinations of lower powers (due to the Cayley-Hamilton Theorem) simplifies complex calculations significantly.

## Key Concepts

### Characteristic Polynomial

For an n×n matrix A, the characteristic polynomial is defined as p(λ) = det(A - λI), where I is the identity matrix of order n. This polynomial is of degree n and its roots are the eigenvalues of the matrix. The characteristic polynomial can be expressed as:

p(λ) = λⁿ + cₙ₋₁λⁿ⁻¹ + ... + c₁λ + c₀

where the coefficients are determined by the trace and determinants of principal minors of A.

### Cayley-Hamilton Theorem

The Cayley-Hamilton Theorem states that every square matrix A satisfies its own characteristic equation. If p(λ) = det(A - λI) = 0 is the characteristic equation, then:

p(A) = Aⁿ + cₙ₋₁Aⁿ⁻¹ + ... + c₁A + c₀I = O

This remarkable theorem allows us to express higher powers of A as linear combinations of I, A, A², ..., Aⁿ⁻¹, which is crucial for simplifying matrix computations.

### Minimal Polynomial

The minimal polynomial m(λ) of a matrix A is the monic polynomial of least degree such that m(A) = O. It divides every polynomial that annihilates A and has the same set of distinct roots as the characteristic polynomial (though possibly with lower multiplicities). The minimal polynomial can be found by determining the smallest power of each invariant factor.

### Polynomial of a Matrix

Given a polynomial f(x) = aₘxᵐ + aₘ₋₁xᵐ⁻¹ + ... + a₁x + a₀, the matrix polynomial f(A) is defined as:

f(A) = aₘAᵐ + aₘ₋₁Aᵐ⁻¹ + ... + a₁A + a₀I

Matrix polynomials follow most algebraic properties of scalar polynomials, including addition, subtraction, and multiplication, with matrix multiplication replacing scalar multiplication.

### Applications of Matrix Polynomials

The primary application is computing high powers of matrices. For example, to compute A¹⁰⁰, instead of multiplying A by itself 100 times, we can use the Cayley-Hamilton Theorem to express A¹⁰⁰ as a linear combination of I, A, A², ..., Aⁿ⁻¹. Similarly, the inverse of a matrix can be expressed in terms of powers of A when A is invertible.

## Examples

### Example 1: Finding Characteristic Polynomial

**Problem:** Find the characteristic polynomial of A = [[2, 1], [1, 2]]

**Solution:**
Step 1: Form the matrix (A - λI)
A - λI = [[2-λ, 1], [1, 2-λ]]

Step 2: Compute determinant
det(A - λI) = (2-λ)(2-λ) - 1(1)
= (2-λ)² - 1
= 4 - 4λ + λ² - 1
= λ² - 4λ + 3

Step 3: Write characteristic polynomial
p(λ) = λ² - 4λ + 3

The eigenvalues are λ = 1 and λ = 3.

### Example 2: Verifying Cayley-Hamilton Theorem

**Problem:** Verify Cayley-Hamilton Theorem for A = [[2, 1], [1, 2]]

**Solution:**
From Example 1, we have p(λ) = λ² - 4λ + 3

According to Cayley-Hamilton Theorem:
p(A) = A² - 4A + 3I = O

Compute A²:
A² = [[2, 1], [1, 2]] × [[2, 1], [1, 2]]
= [[4+1, 2+2], [2+2, 1+4]]
= [[5, 4], [4, 5]]

Now compute p(A):
A² - 4A + 3I = [[5, 4], [4, 5]] - 4×[[2, 1], [1, 2]] + 3×[[1, 0], [0, 1]]
= [[5, 4], [4, 5]] - [[8, 4], [4, 8]] + [[3, 0], [0, 3]]
= [[5-8+3, 4-4+0], [4-4+0, 5-8+3]]
= [[0, 0], [0, 0]]

Thus, p(A) = O, verifying the Cayley-Hamilton Theorem.

### Example 3: Computing A⁵ Using Cayley-Hamilton Theorem

**Problem:** Using Cayley-Hamilton Theorem, find A⁵ for A = [[2, 1], [1, 2]]

**Solution:**
From Examples 1 and 2, we have:
p(A) = A² - 4A + 3I = O
Therefore: A² = 4A - 3I

This allows us to reduce higher powers:

A³ = A·A² = A(4A - 3I) = 4A² - 3A
= 4(4A - 3I) - 3A = 16A - 12I - 3A = 13A - 12I

A⁴ = A·A³ = A(13A - 12I) = 13A² - 12A
= 13(4A - 3I) - 12A = 52A - 39I - 12A = 40A - 39I

A⁵ = A·A⁴ = A(40A - 39I) = 40A² - 39A
= 40(4A - 3I) - 39A = 160A - 120I - 39A = 121A - 120I

Now substitute A = [[2, 1], [1, 2]]:
121A - 120I = 121×[[2, 1], [1, 2]] - 120×[[1, 0], [0, 1]]
= [[242, 121], [121, 242]] - [[120, 0], [0, 120]]
= [[122, 121], [121, 122]]

Therefore, A⁵ = [[122, 121], [121, 122]]

## Exam Tips

1. **Remember the Cayley-Hamilton Theorem statement clearly**: Every square matrix satisfies its own characteristic equation p(A) = O.

2. **Characteristic polynomial calculation**: Always set up (A - λI) correctly and compute the determinant carefully, watching signs.

3. **Express powers systematically**: When computing Aᵏ for large k, recursively reduce using the relation Aⁿ = -cₙ₋₁Aⁿ⁻¹ - ... - c₀I obtained from p(A) = O.

4. **Finding inverse**: If A is invertible and p(λ) = λⁿ + cₙ₋₁λⁿ⁻¹ + ... + c₁λ + c₀, then c₀ ≠ 0 and A⁻¹ = -(1/c₀)(Aⁿ⁻¹ + cₙ₋₁Aⁿ⁻² + ... + c₁I).

5. **Minimal polynomial relationship**: The minimal polynomial divides the characteristic polynomial and has the same distinct roots.

6. **Practice reduction technique**: Always express the highest power in terms of lower powers using the characteristic equation before computing.

7. **Verification problems**: In exam questions asking to verify Cayley-Hamilton Theorem, compute A² first, then substitute into p(A) = O.

8. **Matrix multiplication accuracy**: When computing examples, double-check matrix multiplication as arithmetic errors are common.
