# Diagonalization and Orthogonal Diagonalization - Summary

## Key Definitions and Concepts

- **Diagonalizable Matrix**: A matrix A is diagonalizable if A = PDP⁻¹ for some invertible P and diagonal D, where columns of P are eigenvectors of A.

- **Eigenvalue/Eigenvector**: For non-zero vector v, Av = λv where λ is eigenvalue and v is corresponding eigenvector.

- **Orthogonal Diagonalization**: A = QDQᵀ where Q is orthogonal (Q⁻¹ = Qᵀ) and D is diagonal.

- **Similar Matrices**: A and B are similar if B = PAP⁻¹ for some invertible P; they represent the same linear transformation in different bases.

- **Spectral Theorem**: Every symmetric matrix has real eigenvalues and can be orthogonally diagonalized.

## Important Formulas and Theorems

- **Characteristic Equation**: det(A - λI) = 0
- **Diagonalization Condition**: A has n linearly independent eigenvectors ⇔ A is diagonalizable
- **Distinct Eigenvalues**: n distinct eigenvalues guarantee diagonalizability
- **Symmetric Matrix Properties**: Real eigenvalues; eigenvectors from distinct eigenvalues are orthogonal
- **Orthogonal Matrix**: QᵀQ = I; columns form orthonormal set

## Key Points

- Diagonalization simplifies matrix powers: Aᵏ = PDᵏP⁻¹
- Geometric multiplicity (eigenspace dimension) ≤ algebraic multiplicity (root multiplicity)
- If geometric multiplicity equals algebraic multiplicity for all eigenvalues, matrix is diagonalizable
- Symmetric matrices always admit orthogonal diagonalization with orthonormal eigenvectors
- Quadratic forms xᵀAx can be diagonalized via orthogonal transformation to principal axes
- The Spectral Theorem guarantees existence of complete orthonormal eigenbasis for symmetric matrices
- Orthogonal transformations preserve lengths and angles: ||Qx|| = ||x||

## Common Mistakes to Avoid

1. Forgetting to check if eigenvectors are linearly independent when claiming diagonalizability
2. Not matching eigenvalue order between D and corresponding eigenvector columns in P
3. Assuming all diagonalizable matrices are orthogonally diagonalizable (only symmetric matrices have this property)
4. Confusing algebraic multiplicity (from characteristic equation) with geometric multiplicity (eigenspace dimension)
5. Using non-orthogonal matrices when orthogonal diagonalization is required for symmetric matrices

## Revision Tips

1. Practice 3-4 diagonalization problems covering different eigenvalue scenarios (distinct, repeated, complex)
2. Always verify PDP⁻¹ = A after diagonalizing to check correctness
3. For symmetric matrices, remember to orthonormalize eigenvectors using Gram-Schmidt when needed
4. Memorize that symmetric → orthogonal diagonalization is guaranteed (Spectral Theorem)
5. Understand that diagonalization is essentially a change of basis to the eigenbasis
