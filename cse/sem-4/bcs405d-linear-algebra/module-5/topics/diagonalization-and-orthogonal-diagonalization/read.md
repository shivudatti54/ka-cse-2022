# Diagonalization and Orthogonal Diagonalization

## Introduction

Diagonalization represents one of the most powerful techniques in linear algebra, allowing us to simplify complex matrix operations by transforming a matrix into a diagonal form. This process has profound implications in various engineering applications, including vibration analysis, quantum mechanics, image processing, and principal component analysis. When a matrix can be diagonalized, computations that would otherwise be computationally expensive become significantly simpler, making this concept essential for every engineering student.

Orthogonal diagonalization takes this concept further by requiring that the transformation matrix be orthogonal, which preserves lengths and angles. This is particularly important for symmetric matrices, which always admit orthogonal diagonalization according to the Spectral Theorem. The ability to orthogonally diagonalize a symmetric matrix has far-reaching applications in statistics (PCA), physics (normal modes), and engineering (optimization problems). In this module, we will explore the conditions for diagonalization, the procedures involved, and the special properties of symmetric matrices that enable orthogonal diagonalization.

## Key Concepts

### 1. Eigenvalues and Eigenvectors Review

For an n×n matrix A, a non-zero vector v is called an eigenvector if Av = λv for some scalar λ, which is the corresponding eigenvalue. The characteristic equation det(A - λI) = 0 determines the eigenvalues, and for each eigenvalue, we find eigenvectors from the null space of (A - λI).

### 2. Diagonalization Definition

A matrix A is said to be diagonalizable if there exists an invertible matrix P and a diagonal matrix D such that A = PDP⁻¹. The matrix P's columns are linearly independent eigenvectors of A, and D's diagonal entries are the corresponding eigenvalues. The diagonal matrix D is similar to A, meaning they represent the same linear transformation in different bases.

### 3. Conditions for Diagonalization

A matrix A is diagonalizable if and only if it has n linearly independent eigenvectors. This is equivalent to saying that for each eigenvalue, the geometric multiplicity (dimension of eigenspace) equals its algebraic multiplicity (multiplicity as root of characteristic polynomial). For practical purposes, if A has n distinct eigenvalues, then A is definitely diagonalizable. However, repeated eigenvalues may or may not allow diagonalization depending on whether we can find enough linearly independent eigenvectors.

### 4. Procedure for Diagonalization

To diagonalize a matrix A:

1. Find all eigenvalues of A by solving the characteristic equation
2. For each eigenvalue, find a basis for the corresponding eigenspace
3. Arrange all eigenvectors as columns of matrix P (order matters—eigenvalues in D match column order in P)
4. Form diagonal matrix D with eigenvalues on the diagonal (matching P's column order)
5. Verify that A = PDP⁻¹

### 5. Similar Matrices

Two matrices A and B are similar if there exists an invertible matrix P such that B = PAP⁻¹. Similar matrices represent the same linear transformation but in different coordinate systems. Similarity preserves eigenvalues, determinant, rank, trace, and characteristic polynomial. Diagonalization is essentially finding a basis in which the transformation matrix is diagonal.

### 6. Orthogonal Diagonalization

A matrix A is orthogonally diagonalizable if there exists an orthogonal matrix Q (where Q⁻¹ = Qᵀ) and a diagonal matrix D such that A = QDQᵀ. The key difference from regular diagonalization is that we require an orthogonal transformation matrix, which preserves the Euclidean norm. This means the change of basis is a pure rotation or reflection without scaling.

### 7. Symmetric Matrices and Orthogonal Diagonalization

A symmetric matrix (A = Aᵀ) has remarkable properties:

- All eigenvalues are real numbers
- Eigenvectors corresponding to distinct eigenvalues are orthogonal
- For each eigenvalue, we can find an orthonormal basis for its eigenspace
- Every symmetric matrix is orthogonally diagonalizable (Spectral Theorem)

### 8. The Spectral Theorem

The Spectral Theorem states that for any symmetric matrix A, there exists an orthogonal matrix Q such that A = QDQᵀ, where D is a diagonal matrix containing the real eigenvalues of A. This theorem guarantees that symmetric matrices can always be orthogonally diagonalized, and the columns of Q are orthonormal eigenvectors of A.

### 9. Quadratic Forms and Diagonalization

A quadratic form in n variables is expressed as Q(x) = xᵀAx, where A is a symmetric matrix. By orthogonally diagonalizing A using QDQᵀ, we can rewrite the quadratic form as Q(x) = yᵀDy, where y = Qᵀx. This transformation to principal axes eliminates cross-product terms and simplifies optimization problems involving quadratic forms.

## Examples

### Example 1: Diagonalizing a 2×2 Matrix

**Problem:** Diagonalize the matrix A = [[4, 2], [1, 3]]

**Solution:**

**Step 1: Find eigenvalues**

- Characteristic equation: det(A - λI) = 0
- det([[4-λ, 2], [1, 3-λ]]) = (4-λ)(3-λ) - 2(1) = λ² - 7λ + 10 = 0
- (λ - 5)(λ - 2) = 0, so λ₁ = 5, λ₂ = 2

**Step 2: Find eigenvectors**

- For λ₁ = 5: Solve (A - 5I)v = 0 → [[-1, 2], [1, -2]]v = 0
- v₁ = [2, 1] (or any non-zero multiple)
- For λ₂ = 2: Solve (A - 2I)v = 0 → [[2, 2], [1, 1]]v = 0
- v₂ = [1, -1] (or any non-zero multiple)

**Step 3: Form P and D**

- P = [[2, 1], [1, -1]]
- D = [[5, 0], [0, 2]]

**Step 4: Verify**

- P⁻¹ = (1/(2·(-1) - 1·1)) [[-1, -1], [-1, 2]] = [[1/3, 1/3], [1/3, -2/3]]
- PDP⁻¹ = [[2, 1], [1, -1]] × [[5, 0], [0, 2]] × [[1/3, 1/3], [1/3, -2/3]] = A ✓

### Example 2: Orthogonal Diagonalization of a Symmetric Matrix

**Problem:** Orthogonally diagonalize A = [[2, 1], [1, 2]]

**Solution:**

**Step 1: Find eigenvalues**

- Characteristic equation: det([[2-λ, 1], [1, 2-λ]]) = (2-λ)² - 1 = λ² - 4λ + 3 = 0
- λ₁ = 3, λ₂ = 1

**Step 2: Find eigenvectors and orthonormalize**

- For λ₁ = 3: (A - 3I)v = 0 → [[-1, 1], [1, -1]]v = 0 → v₁ = [1, 1]
- Normalize: u₁ = [1/√2, 1/√2]
- For λ₂ = 1: (A - I)v = 0 → [[1, 1], [1, 1]]v = 0 → v₂ = [1, -1]
- Normalize: u₂ = [1/√2, -1/√2]
- Note: u₁ and u₂ are already orthogonal

**Step 3: Form orthogonal matrix Q**

- Q = [[1/√2, 1/√2], [1/√2, -1/√2]] (columns are orthonormal eigenvectors)

**Step 4: Form diagonal matrix D**

- D = QᵀAQ = [[3, 0], [0, 1]]

**Answer:** A = QDQᵀ where Q is orthogonal and D = [[3, 0], [0, 1]]

### Example 3: When Diagonalization Fails

**Problem:** Show that A = [[1, 1], [0, 1]] is not diagonalizable.

**Solution:**

**Step 1: Find eigenvalues**

- Characteristic equation: det([[1-λ, 1], [0, 1-λ]]) = (1-λ)² = 0
- λ = 1 (algebraic multiplicity = 2)

**Step 2: Find eigenvectors**

- Solve (A - I)v = 0 → [[0, 1], [0, 0]]v = 0
- This gives 0·x + 1·y = 0 → y = 0
- Eigenspace = span{[1, 0]}, which has dimension 1

**Step 3: Analyze**

- Geometric multiplicity = 1 < Algebraic multiplicity = 2
- We cannot find 2 linearly independent eigenvectors

**Conclusion:** A is not diagonalizable because we cannot form an invertible matrix P with 2 linearly independent eigenvectors.

## Exam Tips

1. **Remember the key test**: A matrix is diagonalizable if and only if it has n linearly independent eigenvectors (for an n×n matrix).

2. **Distinct eigenvalues guarantee diagonalization**: If all n eigenvalues are distinct, the matrix is definitely diagonalizable—this is a sufficient but not necessary condition.

3. **For symmetric matrices, always apply Spectral Theorem**: Remember that symmetric matrices are always orthogonally diagonalizable with real eigenvalues.

4. **Orthogonal matrices preserve norms**: QᵀQ = I, which means column vectors are orthonormal and lengths are preserved during transformation.

5. **Practice finding eigenvectors**: Most diagonalization problems require correct eigenvector computation—master the Gauss-Jordan method for solving (A - λI)v = 0.

6. **Quadratic forms use symmetric matrices**: When diagonalizing quadratic forms xᵀAx, ensure A is symmetric first (if not, replace with (A + Aᵀ)/2).

7. **Order matters in P and D**: The diagonal entries of D must correspond to the column positions of eigenvectors in P.

8. **Verify your diagonalization**: Always multiply PDP⁻¹ to confirm it equals A—this catches ordering and computation errors.
