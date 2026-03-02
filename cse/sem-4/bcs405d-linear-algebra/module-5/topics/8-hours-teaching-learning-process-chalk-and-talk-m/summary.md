# Eigenvalues and Eigenvectors - Summary

## Key Definitions and Concepts

- **Eigenvector**: A non-zero vector v such that Av = λv for some scalar λ
- **Eigenvalue**: The scalar λ corresponding to an eigenvector where the direction remains unchanged
- **Characteristic Equation**: det(A - λI) = 0, whose roots are the eigenvalues
- **Eigenspace**: The set of all eigenvectors corresponding to a given eigenvalue plus the zero vector

## Important Formulas and Theorems

- **Av = λv**: Fundamental eigenvalue-eigenvector definition
- **det(A - λI) = 0**: Characteristic equation
- **Sum of eigenvalues = trace(A)**: Sum of diagonal elements
- **Product of eigenvalues = det(A)**: Determinant of the matrix
- **Cayley-Hamilton**: Every matrix satisfies its own characteristic equation
- **Diagonalization**: A = PDP⁻¹ where D is diagonal with eigenvalues

## Key Points

- Eigenvectors corresponding to distinct eigenvalues are always linearly independent
- A matrix with n distinct eigenvalues is always diagonalizable
- For symmetric matrices, eigenvalues are real and eigenvectors are orthogonal
- Geometric multiplicity ≤ Algebraic multiplicity for each eigenvalue
- If A is invertible, eigenvalues of A⁻¹ are 1/λ (where λ ≠ 0)
- The eigenvalue of a projection matrix is either 0 or 1

## Common Mistakes to Avoid

- Forgetting to subtract λI from A before computing the determinant
- Failing to include the zero vector in eigenspace discussions
- Not checking linear independence when diagonalizing
- Calculation errors in determinant expansion, especially for 3×3 matrices
- Assuming all matrices are diagonalizable (not all are)

## Revision Tips

- Practice finding eigenvalues and eigenvectors for at least 5 different matrices
- Memorize the key properties and use them for answer verification
- Understand the geometric interpretation: eigenvectors don't change direction
- Review past university questions on diagonalization and Cayley-Hamilton theorem
- Create a quick reference sheet with all formulas for last-minute revision
