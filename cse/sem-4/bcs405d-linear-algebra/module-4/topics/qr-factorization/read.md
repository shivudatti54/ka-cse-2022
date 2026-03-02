# QR Factorization

## Table of Contents

- [QR Factorization](#qr-factorization)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of QR Factorization](#definition-of-qr-factorization)
  - [Relationship Between Q and R](#relationship-between-q-and-r)
  - [Gram-Schmidt Orthogonalization Process](#gram-schmidt-orthogonalization-process)
  - [Modified Gram-Schmidt (MGS)](#modified-gram-schmidt-mgs)
  - [Householder Reflections](#householder-reflections)
  - [Givens Rotations](#givens-rotations)
- [Examples](#examples)
  - [Example 1: QR Factorization Using Gram-Schmidt](#example-1-qr-factorization-using-gram-schmidt)
  - [Example 2: QR Factorization of 3×3 Matrix](#example-2-qr-factorization-of-33-matrix)
  - [Example 3: Solving Least Squares Using QR](#example-3-solving-least-squares-using-qr)
- [Exam Tips](#exam-tips)

## Introduction

QR Factorization (also known as QR Decomposition) is a fundamental matrix decomposition technique in linear algebra that expresses any matrix with linearly independent columns as the product of an orthogonal matrix Q and an upper triangular matrix R. This decomposition is particularly significant in numerical linear algebra, eigenvalue computations, and solving least squares problems. The factorization provides a stable and efficient way to perform various matrix operations, making it essential for students applications in signal processing, data science, and engineering computations.

The importance of QR factorization stems from its numerical stability and wide range of applications. Unlike other decompositions, the QR factorization using Gram-Schmidt orthogonalization (modified version) or Householder reflections maintains excellent numerical properties, avoiding the accumulation of rounding errors. In the university's linear algebra curriculum, this topic connects theoretical concepts with practical computational methods, preparing students for advanced courses in numerical methods and engineering computations.

## Key Concepts

### Definition of QR Factorization

For an m×n matrix A with linearly independent columns (m ≥ n), the QR factorization is defined as:
A = QR

Where:

- Q is an m×m orthogonal matrix (Q^T Q = I) whose first n columns form an orthonormal basis for the column space of A
- R is an m×n upper triangular matrix (all elements below the main diagonal are zero)

### Relationship Between Q and R

The matrix Q has the property that Q^T = Q^(-1), meaning Q^T Q = I. The columns of Q are called orthonormal vectors. The matrix R is upper triangular, meaning r\_{ij} = 0 for all i > j. Importantly, since A has linearly independent columns, R is guaranteed to be non-singular (all diagonal elements are non-zero).

### Gram-Schmidt Orthogonalization Process

The classical Gram-Schmidt process converts a set of linearly independent vectors into an orthogonal (or orthonormal) set. For QR factorization, we apply this to the columns of matrix A:

Given A = [a₁ a₂ ... aₙ], we compute:

- u₁ = a₁, then q₁ = u₁/||u₁||
- u₂ = a₂ - (q₁^T a₂)q₁, then q₂ = u₂/||u₂||
- u₃ = a₃ - (q₁^T a₃)q₁ - (q₂^T a₃)q₂, then q₃ = u₃/||u₃||
- Continue for all columns

The resulting Q matrix has columns q₁, q₂, ..., qₙ, and R contains the coefficients: rᵢⱼ = qᵢ^T aⱼ for i ≤ j.

### Modified Gram-Schmidt (MGS)

The Modified Gram-Schmidt algorithm produces identical results to classical Gram-Schmidt but with better numerical stability. The key difference is that MGS orthogonalizes vectors one at a time against all previously computed orthogonal vectors, rather than processing all vectors simultaneously.

### Householder Reflections

Householder QR factorization uses orthogonal transformations (Householder matrices) to introduce zeros below pivots. A Householder matrix has the form:
H = I - 2uu^T

Where u is a unit vector. This method is more numerically stable than Gram-Schmidt and is preferred in practice for computing QR factorization.

### Givens Rotations

Givens rotations are another method for QR factorization, particularly useful for introducing zeros in specific positions. A Givens rotation matrix G(i,j,θ) rotates vectors in the plane of coordinates i and j by angle θ.

## Examples

### Example 1: QR Factorization Using Gram-Schmidt

Find the QR factorization of A = [[1, 1], [1, 2], [1, 1]]

**Solution:**

Given A = [a₁ a₂] where a₁ = [1,1,1]^T and a₂ = [1,2,1]^T

**Step 1: Compute for first column**
u₁ = a₁ = [1,1,1]^T
||u₁|| = √(1² + 1² + 1²) = √3
q₁ = u₁/||u₁|| = [1/√3, 1/√3, 1/√3]^T

**Step 2: Compute for second column**
r₁₁ = q₁^T a₁ = [1/√3, 1/√3, 1/√3] · [1,1,1] = 3/√3 = √3
r₁₂ = q₁^T a₂ = [1/√3, 1/√3, 1/√3] · [1,2,1] = (1+2+1)/√3 = 4/√3

u₂ = a₂ - r₁₂q₁ = [1,2,1]^T - (4/√3)[1/√3,1/√3,1/√3]^T
u₂ = [1-4/3, 2-4/3, 1-4/3]^T = [-1/3, 2/3, -1/3]^T

||u₂|| = √((-1/3)² + (2/3)² + (-1/3)²) = √(1/9 + 4/9 + 1/9) = √(6/9) = √6/3

q₂ = u₂/||u₂|| = [-1/3, 2/3, -1/3] × (3/√6) = [-1/√6, 2/√6, -1/√6]^T

**Step 3: Form Q and R matrices**
Q = [q₁ q₂] = [[1/√3, -1/√6], [1/√3, 2/√6], [1/√3, -1/√6]]

R = [[√3, 4/√3], [0, √6/3], [0, 0]] = [[√3, 4/√3], [0, √6/3]]

**Verification:** QR = [[1, 1], [1, 2], [1, 1]] = A ✓

### Example 2: QR Factorization of 3×3 Matrix

Find QR factorization of A = [[1, 2], [2, 1]]

**Solution:**

a₁ = [1,2]^T, a₂ = [2,1]^T

**Step 1:**
u₁ = a₁ = [1,2]^T
||u₁|| = √(1+4) = √5
q₁ = [1/√5, 2/√5]^T

**Step 2:**
r₁₁ = q₁^T a₁ = [1/√5, 2/√5] · [1,2] = (1+4)/√5 = 5/√5 = √5
r₁₂ = q₁^T a₂ = [1/√5, 2/√5] · [2,1] = (2+2)/√5 = 4/√5

u₂ = a₂ - r₁₂q₁ = [2,1]^T - (4/√5)[1/√5, 2/√5]^T = [2-4/5, 1-8/5]^T = [6/5, -3/5]^T

||u₂|| = √((6/5)² + (-3/5)²) = √(36/25 + 9/25) = √(45/25) = √45/5 = 3√5/5

q₂ = u₂/||u₂|| = [6/5, -3/5] × (5/(3√5)) = [6/(3√5), -3/(3√5)] = [2/√5, -1/√5]

**Result:**
Q = [[1/√5, 2/√5], [2/√5, -1/√5]]
R = [[√5, 4/√5], [0, 3√5/5]]

### Example 3: Solving Least Squares Using QR

Use QR factorization to solve the least squares problem Ax = b for:
A = [[1, 1], [1, 2], [1, 1]], b = [1, 0, 1]^T

**Solution:**

From Example 1, we have QR factorization of A.

To solve Ax = b in least squares sense:

- Multiply both sides by Q^T: Q^TQRx = Q^Tb
- Since Q^TQ = I: Rx = Q^Tb

Compute Q^Tb:
Q^T = [[1/√3, 1/√3, 1/√3], [-1/√6, 2/√6, -1/√6]]

Q^Tb = [[1/√3, 1/√3, 1/√3], [-1/√6, 2/√6, -1/√6]] × [1, 0, 1]^T
= [[1/√3 + 0 + 1/√3], [-1/√6 + 0 + (-1/√6)]]
= [[2/√3], [-2/√6]]

Now solve Rx = Q^Tb:
[[√3, 4/√3], [0, √6/3]] × [x₁, x₂]^T = [2/√3, -2/√6]^T

From second row: (√6/3)x₂ = -2/√6
x₂ = (-2/√6) × (3/√6) = -6/6 = -1

From first row: √3 x₁ + (4/√3)(-1) = 2/√3
√3 x₁ - 4/√3 = 2/√3
√3 x₁ = 6/√3 = 2√3
x₁ = 2

Solution: x = [2, -1]^T

## Exam Tips

1. **Remember the dimensions**: For A (m×n) with m ≥ n, Q is (m×m) orthogonal and R is (m×n) upper triangular.

2. **Key property of Q**: Always verify Q^T Q = I or columns of Q are unit vectors that are mutually orthogonal.

3. **R is always upper triangular**: All elements below the main diagonal in R must be zero; this is a defining characteristic.

4. **For exam problems**: When performing Gram-Schmidt, compute the projections carefully using the inner product formula.

5. **Alternative representation**: Remember that for computational purposes, only the first n columns of Q are needed since R's last m-n rows are zero.

6. **Stability comparison**: Modified Gram-Schmidt is numerically more stable than classical Gram-Schmidt—know when to apply each.

7. **Applications**: QR factorization is used for solving least squares, computing eigenvalues via QR algorithm, and finding orthonormal bases.

8. **Verification always works**: Always verify your answer by computing QR and checking it equals A.
