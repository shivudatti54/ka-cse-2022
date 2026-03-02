# Quadratic Forms and Its Classifications

## Introduction

Quadratic forms are fundamental mathematical objects in linear algebra that appear extensively in optimization, physics, engineering, and statistics. A quadratic form is a homogeneous polynomial of degree 2 in variables x₁, x₂, ..., xₙ. In simpler terms, it represents a function that takes a vector and produces a scalar through a symmetric matrix. The study of quadratic forms and their classification is essential for understanding concepts like definiteness of matrices, which plays a crucial role in determining the nature of critical points in optimization problems.

In the context of the university's Linear Algebra course, quadratic forms are particularly important because they connect the abstract concepts of eigenvalues and eigenvectors with practical applications in stability analysis, principal component analysis (PCA), and quadratic programming. The classification of quadratic forms helps us determine whether a given form is positive definite, negative definite, positive semi-definite, negative semi-definite, or indefinite. This classification is entirely determined by the eigenvalues of the symmetric matrix representing the quadratic form.

This module will provide a comprehensive understanding of quadratic forms, their representation using matrices, and the systematic methods for classifying them. We will also explore how to transform quadratic forms into canonical forms through orthogonal transformations, which simplifies their analysis significantly.

## Key Concepts

### 1. Definition of Quadratic Forms

A **quadratic form** in n variables x₁, x₂, ..., xₙ is a homogeneous polynomial of degree 2 given by:

Q(x₁, x₂, ..., xₙ) = Σᵢ Σⱼ aᵢⱼ xᵢ xⱼ

where aᵢⱼ are real coefficients and aᵢⱼ = aⱼᵢ (the matrix is symmetric).

For example:

- In 2 variables: Q(x, y) = ax² + 2bxy + cy²
- In 3 variables: Q(x, y, z) = ax² + by² + cz² + 2dxy + 2eyz + 2fzx

### 2. Matrix Representation

Every quadratic form can be represented as:

Q(x) = xᵀAx

where x = [x₁, x₂, ..., xₙ]ᵀ is a column vector and A is a symmetric n×n matrix called the **matrix of the quadratic form**.

For a 2-variable quadratic form Q(x, y) = ax² + 2bxy + cy², the matrix representation is:

Q(x, y) = [x y] [a b] [x]
[b c] [y]

The symmetric matrix A = [[a, b], [b, c]] captures all coefficients of the quadratic form.

### 3. Classification of Quadratic Forms

The classification of a quadratic form Q(x) = xᵀAx is determined by the **definiteness** of the symmetric matrix A:

**Positive Definite:** Q(x) > 0 for all non-zero vectors x. The matrix A has all positive eigenvalues. For example, Q(x, y) = x² + y².

**Negative Definite:** Q(x) < 0 for all non-zero vectors x. The matrix A has all negative eigenvalues. For example, Q(x, y) = -x² - y².

**Positive Semi-Definite:** Q(x) ≥ 0 for all x. The matrix A has all non-negative eigenvalues. For example, Q(x, y) = (x + y)².

**Negative Semi-Definite:** Q(x) ≤ 0 for all x. The matrix A has all non-positive eigenvalues. For example, Q(x, y) = -(x + y)².

**Indefinite:** Q(x) takes both positive and negative values. The matrix A has both positive and negative eigenvalues. For example, Q(x, y) = x² - y².

### 4. Sylvester's Law of Inertia

Sylvester's Law of Inertia states that for any real symmetric matrix A, there exists an invertible matrix P such that PᵀAP is a diagonal matrix with diagonal entries consisting of:

- p entries of +1 (positive eigenvalues)
- n entries of -1 (negative eigenvalues)
- z entries of 0 (zero eigenvalues)

The triplet (p, n, z) is called the **signature** of the quadratic form, where p + n + z = n (the number of variables).

### 5. Principal Minors Test

For determining definiteness, we can use **principal minors**:

**For Positive Definiteness:** All leading principal minors of A must be positive.
For a 2×2 matrix A = [[a, b], [b, c]], we need:

- a > 0
- ac - b² > 0

For a 3×3 matrix, we need all three leading principal minors positive.

**For Negative Definiteness:** The leading principal minors must alternate in sign, starting with negative.
For a 2×2 matrix:

- a < 0
- ac - b² > 0

### 6. Canonical Form

A quadratic form can be transformed into a **canonical form** (also called diagonal form) through an orthogonal transformation. If A has eigenvalues λ₁, λ₂, ..., λₙ with corresponding orthonormal eigenvectors, then:

Q(x) = yᵀDy where D = diag(λ₁, λ₂, ..., λₙ) and x = Py where P is the orthogonal matrix of eigenvectors.

The canonical form becomes: Q(y₁, y₂, ..., yₙ) = λ₁y₁² + λ₂y₂² + ... + λₙyₙ²

## Examples

### Example 1: Classify the Quadratic Form

Classify the quadratic form Q(x, y) = 3x² + 10xy + 3y².

**Solution:**

Step 1: Write the matrix representation
A = [[3, 5], [5, 3]]

Step 2: Find eigenvalues
|A - λI| = 0
|[3-λ, 5], [5, 3-λ]| = 0
(3-λ)² - 25 = 0
λ² - 6λ + 9 - 25 = 0
λ² - 6λ - 16 = 0
(λ-8)(λ+2) = 0
λ₁ = 8, λ₂ = -2

Step 3: Classification
Since eigenvalues are 8 (positive) and -2 (negative), the quadratic form is **Indefinite**.

Verification using principal minors:

- Leading principal minor: a = 3 > 0
- Determinant: 3(3) - 5² = 9 - 25 = -16 < 0

This confirms the form is indefinite.

### Example 2: Determine Positive Definiteness

Determine if A = [[2, 1, 1], [1, 2, 1], [1, 1, 2]] is positive definite.

**Solution:**

Step 1: Calculate leading principal minors

First order: Δ₁ = 2 > 0

Second order: Δ₂ = |2 1; 1 2| = 2(2) - 1(1) = 4 - 1 = 3 > 0

Third order: Δ₃ = det(A) = 2(2×2 - 1×1) - 1(1×2 - 1×1) + 1(1×1 - 2×1)
= 2(4-1) - 1(2-1) + 1(1-2)
= 2(3) - 1(1) + 1(-1)
= 6 - 1 - 1 = 4 > 0

Step 2: Conclusion
All leading principal minors are positive. Therefore, A is **positive definite**.

This means the quadratic form Q(x, y, z) = 2x² + 2y² + 2z² + 2xy + 2yz + 2zx is positive definite.

### Example 3: Find Canonical Form

Find the canonical form of Q(x, y, z) = 2x² + 2y² + 2z² + 2xy + 2yz + 2zx through orthogonal transformation.

**Solution:**

Step 1: Write matrix form
A = [[2, 1, 1], [1, 2, 1], [1, 1, 2]]

Step 2: Find eigenvalues
|A - λI| = 0
(2-λ)[(2-λ)² - 1] - 1[1(2-λ) - 1] + 1[1 - 1(2-λ)] = 0
Simplifying: (1-λ)²(λ-4) = 0
Eigenvalues: λ₁ = λ₂ = 1, λ₃ = 4

Step 3: Find eigenvectors and orthogonal matrix P

For λ = 4: Solve (A - 4I)x = 0
[[-2, 1, 1], [1, -2, 1], [1, 1, -2]]x = 0
Eigenvector: v₁ = [1, 1, 1]

For λ = 1: Solve (A - I)x = 0
[[1, 1, 1], [1, 1, 1], [1, 1, 1]]x = 0
Eigenvectors: v₂ = [1, -1, 0], v₃ = [1, 1, -2]

Step 4: Orthogonalize and normalize
After orthogonalization, P = [[1/√3, 1/√2, 1/√6], [1/√3, -1/√2, 1/√6], [1/√3, 0, -2/√6]]

Step 5: Canonical form
The canonical form is: Q = y₁² + y₂² + 4y₃²

This is the diagonal form obtained through orthogonal transformation.

## Exam Tips

1. **Remember the matrix representation:** Always convert the given quadratic form to xᵀAx form first. For terms like 2bxy, remember the coefficient 2b goes into the off-diagonal positions as b and b.

2. **Eigenvalue method is most reliable:** For classification, finding eigenvalues is the most straightforward method. All positive → positive definite, all negative → negative definite, mixed signs → indefinite.

3. **Principal minors work only for leading minors:** Don't confuse leading principal minors with all principal minors. The principal minors test applies only to leading principal minors (top-left k×k submatrices).

4. **Sylvester's law gives signature:** The number of positive, negative, and zero eigenvalues (in the diagonal form) gives the signature (p, n, z) of the quadratic form.

5. **Canonical form uses orthogonal transformation:** The orthogonal transformation preserves the value of the quadratic form because orthogonal matrices preserve length: xᵀAx = yᵀ(PᵀAP)y.

6. **Check special cases carefully:** For 2×2 matrices, if a > 0 and ac - b² > 0, it's positive definite. For negative definite, a < 0 and ac - b² > 0.

7. **Semi-definite requires careful attention:** For semi-definite cases, principal minors test is not sufficient. You need to check eigenvalues or all principal minors (not just leading ones).

8. **Applications matter:** Understand that positive definite quadratic forms correspond to minima in optimization, indefinite forms to saddle points. This helps in understanding the practical significance.
