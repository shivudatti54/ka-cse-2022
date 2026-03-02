# Eigen-Spaces of a Linear Transformation - Summary

## Key Definitions and Concepts

- **Eigenvector:** A non-zero vector v such that T(v) = λv for some scalar λ
- **Eigenvalue:** The scalar λ corresponding to an eigenvector
- **Eigenspace (Eλ):** The set {v : (A - λI)v = 0} = Null(A - λI), a subspace containing all eigenvectors for λ plus the zero vector
- **Characteristic Polynomial:** p(λ) = det(A - λI)
- **Characteristic Equation:** det(A - λI) = 0

## Important Formulas and Theorems

- **Eigenvalue equation:** Ax = λx or (A - λI)x = 0
- **Characteristic polynomial:** p(λ) = det(A - λI) = (-1)ⁿ(λⁿ - trace(A)λⁿ⁻¹ + ... + det(A))
- **Cayley-Hamilton:** p(A) = O (every matrix satisfies its own characteristic equation)
- **Diagonalization:** A = PDP⁻¹ where D is diagonal with eigenvalues, P contains eigenvectors as columns
- **Diagonalizability condition:** A has n linearly independent eigenvectors (or GM = AM for all eigenvalues)

## Key Points

- Eigenvalues are roots of the characteristic polynomial; there are n roots (counting multiplicity) in ℂ
- Eigenspaces are subspaces (always contain zero vector; closed under addition and scalar multiplication)
- Distinct eigenvalues yield linearly independent eigenvectors
- Algebraic multiplicity (AM): root multiplicity in characteristic polynomial
- Geometric multiplicity (GM): dimension of eigenspace; always 1 ≤ GM ≤ AM
- Matrix is diagonalizable iff sum of geometric multiplicities = n (or GM = AM for each λ)
- Similar matrices share eigenvalues, characteristic polynomial, and geometric multiplicities
- Complex eigenvalues occur in conjugate pairs for real matrices

## Common Mistakes to Avoid

1. Forgetting to include the zero vector in eigenspace definitions (the set naturally includes it)
2. Confusing algebraic multiplicity with geometric multiplicity (they are not always equal)
3. Assuming all matrices are diagonalizable (only those with n independent eigenvectors are)
4. Computing characteristic polynomial as det(A) - λ instead of det(A - λI)
5. Not checking if eigenvectors are linearly independent before diagonalizing

## Revision Tips

1. Practice finding eigenvalues by solving characteristic equations for various 2×2 and 3×3 matrices
2. Always verify that eigenvectors from different eigenspaces are linearly independent
3. Remember: If AM = GM = 1 for all eigenvalues, the matrix is definitely diagonalizable
4. For the exam, focus on computing eigenspaces by solving (A - λI)x = 0 using row reduction
5. Use Cayley-Hamilton to find A⁻¹: If p(A) = 0, then A⁻¹ can be expressed as a polynomial in A
