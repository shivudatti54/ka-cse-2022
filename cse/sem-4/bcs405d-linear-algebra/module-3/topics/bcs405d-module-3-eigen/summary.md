# Eigenvalues and Eigenvectors - Summary

## Key Definitions and Concepts

- **Eigenvalue and Eigenvector**: For matrix A, a scalar λ is an eigenvalue if there exists a non-zero vector v such that Av = λv. Vector v is the corresponding eigenvector.

- **Characteristic Equation**: |A - λI| = 0, where I is the identity matrix. Roots of this equation are eigenvalues.

- **Eigenspace**: The set of all eigenvectors for an eigenvalue λ, plus the zero vector: Eλ = {v : (A - λI)v = 0}

- **Diagonalization**: Matrix A is diagonalizable if A = PDP⁻¹, where D is diagonal and P contains eigenvectors as columns.

- **Quadratic Form**: Q(x) = xᵀAx, where A is symmetric. Classification based on sign of Q(x) for x ≠ 0.

## Important Formulas and Theorems

- **Trace-Determinant Relation**: Sum of eigenvalues = trace(A); Product of eigenvalues = det(A)
- **Cayley-Hamilton**: Every matrix satisfies its own characteristic equation: p(A) = 0
- **Sylvester's Criterion**: For positive definite matrix, all leading principal minors must be positive

## Key Points

- Eigenvalues of triangular matrix equal its diagonal entries
- Matrix with n distinct eigenvalues is always diagonalizable
- Similar matrices have identical eigenvalues, determinant, trace, and rank
- Symmetric matrices always have real eigenvalues and orthogonal eigenvectors
- Cayley-Hamilton theorem provides alternative method for computing A⁻¹ and Aⁿ

## Common Mistakes to Avoid

- Forgetting to subtract λI from diagonal entries when forming characteristic equation
- Not checking linear independence of eigenvectors when claiming diagonalizability
- Using the wrong matrix in quadratic form - must use symmetric matrix
- Confusing algebraic multiplicity (root multiplicity) with geometric multiplicity (eigenspace dimension)

## Revision Tips

1. Practice 2×2 and 3×3 matrices thoroughly - most exam questions are from these sizes
2. Memorize the characteristic equation shortcut for 2×2: λ² - tr(A)λ + det(A) = 0
3. For diagonalization, always verify P⁻¹AP = D as final step
4. Focus on Cayley-Hamilton applications - this is frequently asked in university exams
5. Understand geometric interpretation: eigenvectors remain in same direction after transformation, eigenvalues indicate stretching/compression factor
