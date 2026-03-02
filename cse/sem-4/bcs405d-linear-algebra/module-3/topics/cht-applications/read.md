# Applications of Cayley-Hamilton Theorem

## Table of Contents

- [Applications of Cayley-Hamilton Theorem](#applications-of-cayley-hamilton-theorem)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Cayley-Hamilton Theorem Statement](#cayley-hamilton-theorem-statement)
  - [Characteristic Polynomial](#characteristic-polynomial)
  - [Application 1: Computing Powers of Matrices](#application-1-computing-powers-of-matrices)
  - [Application 2: Finding Inverse of a Matrix](#application-2-finding-inverse-of-a-matrix)
  - [Application 3: Minimal Polynomial](#application-3-minimal-polynomial)
  - [Application 4: Expressing Matrix as Linear Combination](#application-4-expressing-matrix-as-linear-combination)
- [Examples](#examples)
  - [Example 1: Computing A⁴ using Cayley-Hamilton Theorem](#example-1-computing-a-using-cayley-hamilton-theorem)
  - [Example 2: Finding Inverse using Cayley-Hamilton Theorem](#example-2-finding-inverse-using-cayley-hamilton-theorem)
  - [Example 3: Finding A³ in terms of I and A](#example-3-finding-a-in-terms-of-i-and-a)
- [Exam Tips](#exam-tips)

## Introduction

The Cayley-Hamilton Theorem is one of the most fundamental results in linear algebra, establishing a profound connection between a square matrix and its characteristic polynomial. Named after mathematicians Arthur Cayley and William Rowan Hamilton, this theorem states that every square matrix satisfies its own characteristic equation. This seemingly simple statement has far-reaching consequences in matrix theory and its applications to engineering problems.

For the university's Linear Algebra course, understanding the applications of the Cayley-Hamilton Theorem is crucial as it provides powerful computational techniques that simplify complex matrix operations. The theorem enables us to compute powers of matrices, find matrix inverses, solve systems of linear differential equations, and determine minimal polynomials—all essential skills for a computer science engineer. These applications are particularly valuable in areas like computer graphics, control systems, and data science where matrix computations are ubiquitous.

## Key Concepts

### Cayley-Hamilton Theorem Statement

If A is an n×n matrix and p(λ) = det(λI - A) = λⁿ + cₙ₋₁λⁿ⁻¹ + ... + c₁λ + c₀ is the characteristic polynomial of A, then:

**p(A) = Aⁿ + cₙ₋₁Aⁿ⁻¹ + ... + c₁A + c₀I = O** (zero matrix)

This means the matrix A, when substituted into its own characteristic polynomial, yields the zero matrix.

### Characteristic Polynomial

For an n×n matrix A, the characteristic polynomial is defined as:
p(λ) = det(λI - A)

For a 2×2 matrix A = [[a, b], [c, d]], the characteristic polynomial is:
p(λ) = λ² - (a+d)λ + (ad-bc)

For a 3×3 matrix A, we compute det(λI - A) to obtain a cubic polynomial.

### Application 1: Computing Powers of Matrices

Using Cayley-Hamilton theorem, we can express higher powers of A as linear combinations of lower powers. This is particularly useful for computing Aⁿ without performing repeated matrix multiplications.

If p(A) = 0, then A² = -(c₁A + c₀I) for 2×2 matrices, and we can recursively find higher powers.

### Application 2: Finding Inverse of a Matrix

From the Cayley-Hamilton theorem, if A is invertible (det(A) ≠ 0), then:
A⁻¹ = -(1/c₀)[Aⁿ⁻¹ + cₙ₋₁Aⁿ⁻² + ... + c₁I]

For a 2×2 matrix, if p(λ) = λ² - tr(A)λ + det(A) = 0, then:
A² - tr(A)A + det(A)I = 0
Multiplying by A⁻¹: A - tr(A)I + det(A)A⁻¹ = 0
Therefore: A⁻¹ = (1/det(A))[tr(A)I - A]

### Application 3: Minimal Polynomial

The minimal polynomial m(λ) of a matrix A is the monic polynomial of least degree such that m(A) = 0. The Cayley-Hamilton theorem tells us that the characteristic polynomial p(λ) annihilates A, so the minimal polynomial always divides the characteristic polynomial. Finding the minimal polynomial helps in understanding the structure of the matrix.

### Application 4: Expressing Matrix as Linear Combination

Any power of A can be expressed as a linear combination of I, A, A², ..., Aⁿ⁻¹. This is useful in various computational contexts.

## Examples

### Example 1: Computing A⁴ using Cayley-Hamilton Theorem

**Problem**: Given A = [[2, 1], [1, 2]], find A⁴.

**Solution**:

**Step 1**: Find the characteristic polynomial
|λI - A| = |λ-2, -1; -1, λ-2| = (λ-2)² - 1 = λ² - 4λ + 3

So p(λ) = λ² - 4λ + 3

**Step 2**: Apply Cayley-Hamilton Theorem
p(A) = A² - 4A + 3I = O
Therefore, A² = 4A - 3I

**Step 3**: Compute A³
A³ = A·A² = A(4A - 3I) = 4A² - 3A
Substituting A² = 4A - 3I:
A³ = 4(4A - 3I) - 3A = 16A - 12I - 3A = 13A - 12I

**Step 4**: Compute A⁴
A⁴ = A·A³ = A(13A - 12I) = 13A² - 12A
Substituting A² = 4A - 3I:
A⁴ = 13(4A - 3I) - 12A = 52A - 39I - 12A = 40A - 39I

**Step 5**: Express in terms of A and I
A⁴ = 40[[2,1],[1,2]] - 39[[1,0],[0,1]]
= [[80-39, 40], [40, 80-39]] = [[41, 40], [40, 41]]

### Example 2: Finding Inverse using Cayley-Hamilton Theorem

**Problem**: Find A⁻¹ for A = [[3, 1], [2, 2]]

**Solution**:

**Step 1**: Find characteristic polynomial
|λI - A| = |λ-3, -1; -2, λ-2| = (λ-3)(λ-2) - (-1)(-2) = λ² - 5λ + 4

So p(λ) = λ² - 5λ + 4, where c₀ = 4

**Step 2**: Apply Cayley-Hamilton Theorem
A² - 5A + 4I = O
A² - 5A = -4I

**Step 3**: Multiply by A⁻¹
A - 5I = -4A⁻¹
Therefore, A⁻¹ = (1/4)(5I - A)

**Step 4**: Compute the inverse
A⁻¹ = (1/4)([[5,0],[0,5]] - [[3,1],[2,2]])
= (1/4)[[2, -1], [-2, 3]]
= [[1/2, -1/4], [-1/2, 3/4]]

### Example 3: Finding A³ in terms of I and A

**Problem**: If A = [[1, 2], [0, 3]], find A³.

**Solution**:

**Step 1**: Characteristic polynomial
|λI - A| = |λ-1, -2; 0, λ-3| = (λ-1)(λ-3) = λ² - 4λ + 3

**Step 2**: Cayley-Hamilton
A² - 4A + 3I = 0
A² = 4A - 3I

**Step 3**: A³ = A·A² = A(4A - 3I) = 4A² - 3A
= 4(4A - 3I) - 3A = 16A - 12I - 3A = 13A - 12I

**Step 4**: Substitute A
A³ = 13[[1,2],[0,3]] - 12[[1,0],[0,1]]
= [[13-12, 26], [0, 39-12]] = [[1, 26], [0, 27]]

## Exam Tips

1. **Remember the characteristic polynomial formula**: For 2×2 matrix [[a,b],[c,d]], p(λ) = λ² - (a+d)λ + (ad-bc)

2. **Key identity for 2×2 inverse**: A⁻¹ = (1/det(A))[tr(A)I - A] — this is the fastest method for 2×2 matrices

3. **Always start by finding p(λ)**: The first step in any Cayley-Hamilton application is computing the characteristic polynomial

4. **Express in descending powers**: When using the theorem, rearrange to express higher powers in terms of lower ones

5. **Verify your answer**: Check that A⁻¹A = I when finding inverses, or compute A² directly to verify your power calculation

6. **For differential equations**: The Cayley-Hamilton theorem helps find solutions of the form e^(At) = α₀I + α₁A + α₂A² + ...

7. **Minimal polynomial always divides characteristic polynomial**: This relationship helps verify your minimal polynomial answers

8. **Practice 2×2 and 3×3 matrices thoroughly**: Most university exam questions focus on these sizes

9. **Don't forget the identity matrix**: When rearranging p(A) = 0, remember to include the I term for constant terms

10. **Time management**: The power method via Cayley-Hamilton is faster than direct multiplication for powers greater than 2
