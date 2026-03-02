# Eigenvalues and Eigenvectors - Summary

## Key Definitions

- **Eigenvalue (λ)**: A scalar λ for which there exists a non-zero vector v such that Av = λv
- **Eigenvector (v)**: A non-zero vector that satisfies Av = λv for some eigenvalue λ
- **Eigenspace (Eλ)**: The set {v : Av = λv} = null(A - λI), a subspace containing all eigenvectors for λ
- **Characteristic polynomial**: p(λ) = det(A - λI)
- **Characteristic equation**: det(A - λI) = 0
- **Algebraic multiplicity**: Number of times an eigenvalue appears as a root
- **Geometric multiplicity**: Dimension of the eigenspace Eλ

## Important Formulas

- **Eigenvalue equation**: Av = λv or (A - λI)v = 0
- **Characteristic equation**: det(A - λI) = 0
- **Trace property**: tr(A) = Σ λᵢ (sum of eigenvalues)
- **Determinant property**: det(A) = Π λᵢ (product of eigenvalues)
- **Geometric-inequality**: 1 ≤ geometric multiplicity ≤ algebraic multiplicity

## Key Points

1. Eigenvectors must be non-zero by definition; the zero vector is never considered an eigenvector.

2. Each eigenvalue has infinitely many corresponding eigenvectors (any non-zero scalar multiple of an eigenvector is also an eigenvector).

3. The characteristic polynomial of an n×n matrix has degree n, so there are exactly n eigenvalues counting multiplicities.

4. A matrix is singular if and only if zero is one of its eigenvalues.

5. The eigenvalues of a triangular matrix (including diagonal matrices) are simply its diagonal entries.

6. Complex eigenvalues of real matrices always occur in conjugate pairs.

7. A matrix is diagonalizable if and only if the geometric multiplicity equals the algebraic multiplicity for each eigenvalue.

8. The sum and product of eigenvalues provide quick verification tools through trace and determinant.

## Common Mistakes

1. Forgetting to include the identity matrix when forming (A - λI); writing A - λ instead of A - λI.

2. Assuming eigenvectors are unique—they are determined only up to scalar multiples.

3. Confusing algebraic multiplicity (root multiplicity) with geometric multiplicity (eigenspace dimension).

4. Not checking that computed eigenvectors satisfy Av = λv before submitting answers.

5. Overlooking that eigenvalues can be complex numbers, particularly when working with rotation matrices.