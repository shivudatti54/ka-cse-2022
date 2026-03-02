# Eigen-Spaces of a Linear Transformation

## Introduction

Eigen-spaces form one of the most fundamental concepts in linear algebra, particularly in the study of linear transformations. When we apply a linear transformation to a vector space, most vectors get "rotated" or "stretched" in some complex manner. However, there exist certain special vectors called eigenvectors that, when transformed, only get scaled by a scalar factor without changing their direction. The collection of all eigenvectors corresponding to a particular eigenvalue, together with the zero vector, forms a subspace known as the eigenspace.

The study of eigen-spaces is crucial in many engineering and scientific applications. In computer graphics, eigenvalues and eigenvectors are used for principal component analysis and image compression. In quantum mechanics, they represent observable quantities and their possible values. In vibration analysis and structural engineering, they help determine natural frequencies of systems. For computer science students, understanding eigen-spaces is essential for algorithms in machine learning, computer vision, and data science.

This module explores the theory of eigen-spaces in depth, covering eigenvalues, eigenvectors, the characteristic equation, eigenspace decomposition, and the conditions for diagonalization of matrices.

## Key Concepts

### 1. Eigenvalues and Eigenvectors

Let T: V → V be a linear transformation on a vector space V over a field F. A non-zero vector v ∈ V is called an eigenvector of T if there exists a scalar λ ∈ F such that:

**T(v) = λv**

The scalar λ is called the eigenvalue corresponding to the eigenvector v.

For a square matrix A of order n, a non-zero vector x ∈ ℝⁿ (or ℂⁿ) is an eigenvector if:

**Ax = λx**

for some scalar λ. The eigenvalue λ can be real or complex.

### 2. Characteristic Polynomial and Characteristic Equation

For an n × n matrix A, the characteristic polynomial is defined as:

**p(λ) = det(A - λI) = det(λI - A)**

where I is the n × n identity matrix.

The characteristic equation is:

**det(A - λI) = 0**

The roots of this equation are the eigenvalues of matrix A. For an n × n matrix, there are exactly n roots (counting multiplicities) in the complex number field.

**Example:** For matrix A = [[2, 1], [1, 2]]:

- A - λI = [[2-λ, 1], [1, 2-λ]]
- det(A - λI) = (2-λ)² - 1 = λ² - 4λ + 3
- Characteristic equation: λ² - 4λ + 3 = 0
- Eigenvalues: λ = 1, λ = 3

### 3. Eigenspaces

For a linear transformation T with eigenvalue λ, the eigenspace corresponding to λ is defined as:

**Eλ = {v ∈ V : T(v) = λv} = {v ∈ V : (T - λI)(v) = 0}**

For a matrix A, the eigenspace corresponding to eigenvalue λ is:

**Eλ = {x ∈ ℝⁿ : (A - λI)x = 0} = Null(A - λI)**

The eigenspace is the null space (kernel) of the matrix (A - λI). It is a subspace of the vector space V.

**Properties of Eigenspaces:**

- Eλ always contains the zero vector
- If v is an eigenvector with eigenvalue λ, then any scalar multiple of v is also an eigenvector with the same eigenvalue
- Eigenspaces corresponding to distinct eigenvalues are linearly independent
- The dimension of Eλ is the geometric multiplicity of λ

### 4. Algebraic and Geometric Multiplicity

Let λ be an eigenvalue of matrix A with multiplicity m in the characteristic polynomial (algebraic multiplicity).

- **Algebraic Multiplicity (AM):** The number of times λ appears as a root of the characteristic polynomial
- **Geometric Multiplicity (GM):** The dimension of the eigenspace Eλ, i.e., the number of linearly independent eigenvectors corresponding to λ

**Important Relationship:** For every eigenvalue, **1 ≤ GM ≤ AM**

### 5. Diagonalization

A matrix A of order n is said to be diagonalizable if there exists an invertible matrix P and a diagonal matrix D such that:

**A = PDP⁻¹**

or equivalently, **D = P⁻¹AP**

**Diagonalization Condition:** A matrix A is diagonalizable if and only if:

1. A has n linearly independent eigenvectors
2. The sum of the dimensions of all eigenspaces equals n
3. For each eigenvalue, geometric multiplicity equals algebraic multiplicity

If A is diagonalizable and λ₁, λ₂, ..., λₖ are distinct eigenvalues with eigenvectors v₁, v₂, ..., vₙ, then:

**P = [v₁ v₂ ... vₙ]** (columns are eigenvectors)
**D = diag(λ₁, λ₂, ..., λₙ)** (diagonal entries are corresponding eigenvalues)

### 6. Cayley-Hamilton Theorem

The Cayley-Hamilton theorem states that every square matrix satisfies its own characteristic equation. If p(λ) = det(A - λI) = (-1)ⁿλⁿ + cₙ₋₁λⁿ⁻¹ + ... + c₁λ + c₀ is the characteristic polynomial of A, then:

**p(A) = (-1)ⁿAⁿ + cₙ₋₁Aⁿ⁻¹ + ... + c₁A + c₀I = O**

This theorem is useful for computing inverse matrices and matrix powers.

## Examples

### Example 1: Finding Eigenvalues and Eigenspaces

**Problem:** Find the eigenvalues and corresponding eigenspaces for matrix A = [[3, -1], [1, 1]]

**Solution:**

**Step 1: Find the characteristic polynomial**

```
A - λI = [[3-λ, -1], [1, 1-λ]]
det(A - λI) = (3-λ)(1-λ) - (-1)(1)
 = (3-λ)(1-λ) + 1
 = 3 - 3λ - λ + λ² + 1
 = λ² - 4λ + 4
 = (λ - 2)²
```

**Step 2: Solve characteristic equation**

```
(λ - 2)² = 0
λ = 2 (with algebraic multiplicity 2)
```

**Step 3: Find eigenspace for λ = 2**

```
(A - 2I)x = 0
[[3-2, -1], [1, 1-2]] = [[1, -1], [1, -1]]

Row reduce: [1 -1; 0 0]
x₁ - x₂ = 0
x₁ = x₂

E₂ = {t[1, 1] : t ∈ ℝ}
```

The eigenspace has dimension 1 (geometric multiplicity = 1), while algebraic multiplicity = 2.

### Example 2: Checking Diagonalizability

**Problem:** Determine if matrix B = [[1, 1], [0, 1]] is diagonalizable.

**Solution:**

**Step 1: Find eigenvalues**

```
B - λI = [[1-λ, 1], [0, 1-λ]]
det(B - λI) = (1-λ)²
Characteristic equation: (1-λ)² = 0
λ = 1 (with algebraic multiplicity 2)
```

**Step 2: Find eigenspace for λ = 1**

```
(B - I)x = 0
[[0, 1], [0, 0]] = [0, 0]

From x₂ = 0, we get x = [x₁, 0] = x₁[1, 0]
E₁ = span{[1, 0]}
```

**Step 3: Check diagonalizability**

- Algebraic multiplicity: 2
- Geometric multiplicity: 1

Since GM ≠ AM, the matrix is **not diagonalizable**.

### Example 3: Diagonalizing a Matrix

**Problem:** Diagonalize matrix C = [[4, 2], [2, 4]] if possible.

**Solution:**

**Step 1: Find eigenvalues**

```
C - λI = [[4-λ, 2], [2, 4-λ]]
det(C - λI) = (4-λ)² - 4 = λ² - 8λ + 12 = (λ-2)(λ-6)
λ₁ = 2, λ₂ = 6
```

**Step 2: Find eigenvectors**

For λ₁ = 2:

```
(C - 2I)x = 0
[[2, 2], [2, 2]] → [1, 1; 0, 0]
x₁ + x₂ = 0 → v₁ = [1, -1]
```

For λ₂ = 6:

```
(C - 6I)x = 0
[[-2, 2], [2, -2]] → [1, -1; 0, 0]
x₁ - x₂ = 0 → v₂ = [1, 1]
```

**Step 3: Form P and D**

```
P = [[1, 1], [-1, 1]]
D = [[2, 0], [0, 6]]

Verify: P⁻¹CP = D
```

## Exam Tips

1. **Characteristic polynomial:** Remember det(A - λI) = 0 gives eigenvalues; practice expanding determinants for 2×2 and 3×3 matrices.

2. **Eigenspace as null space:** The eigenspace Eλ is Null(A - λI); to find it, solve the homogeneous system (A - λI)x = 0.

3. **Multiplicity relationship:** Always remember GM ≤ AM for each eigenvalue; if GM = AM for all eigenvalues, the matrix is diagonalizable.

4. **Diagonalization criterion:** For diagonalization, the matrix must have n linearly independent eigenvectors (or all eigenvalues must have GM = AM).

5. **Complex eigenvalues:** For real matrices with complex eigenvalues, eigenspaces still exist in ℂⁿ; be prepared to work with complex numbers.

6. **Cayley-Hamilton application:** Use p(A) = 0 to compute A⁻¹ or higher powers of A efficiently.

7. **Minimal polynomial:** The minimal polynomial divides the characteristic polynomial and has the same roots (though possibly lower multiplicities).

8. **Similar matrices:** Similar matrices A and B (B = P⁻¹AP) have the same eigenvalues, same characteristic polynomial, and same geometric multiplicities.
