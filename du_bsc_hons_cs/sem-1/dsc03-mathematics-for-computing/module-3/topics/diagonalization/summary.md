# Diagonalization - Summary

## Key Definitions and Concepts

- **Diagonalizable Matrix**: A square matrix A is diagonalizable if there exists an invertible matrix P such that P⁻¹AP = D, where D is a diagonal matrix.

- **Eigenvalue (λ)**: A scalar λ such that Av = λv for some non-zero vector v (eigenvector).

- **Eigenvector (v)**: A non-zero vector that satisfies Av = λv.

- **Algebraic Multiplicity (AM)**: Number of times an eigenvalue appears as a root of the characteristic polynomial.

- **Geometric Multiplicity (GM)**: Dimension of the eigenspace (number of linearly independent eigenvectors for an eigenvalue).

- **Characteristic Equation**: |A - λI| = 0, where I is the identity matrix.

## Important Formulas and Theorems

- **Diagonalization Condition**: A is diagonalizable ⟺ A has n linearly independent eigenvectors ⟺ GM = AM for all eigenvalues.

- **Diagonalization Formula**: P⁻¹AP = D, where columns of P are eigenvectors, diagonal entries of D are corresponding eigenvalues.

- **Symmetric Matrix Theorem**: Every real symmetric matrix is diagonalizable via an orthogonal matrix Q (QᵀAQ = D).

- **Distinct Eigenvalues**: If A has n distinct eigenvalues, then A is automatically diagonalizable.

- **Power of Matrix**: If A = PDP⁻¹, then Aᵏ = PDᵏP⁻¹, where Dᵏ simply raises each diagonal entry to power k.

## Key Points

- A matrix is diagonalizable if and only if it possesses n linearly independent eigenvectors.

- Distinct eigenvalues guarantee diagonalizability; repeated eigenvalues require checking multiplicities.

- For symmetric matrices, always consider orthogonal diagonalization using Q instead of P.

- The matrix P must be invertible (non-singular), which requires linearly independent columns.

- Diagonal matrices are trivially diagonalizable with P = I (identity matrix).

- The order of eigenvectors in P must match the order of eigenvalues in D.

- Geometric multiplicity is always less than or equal to algebraic multiplicity.

- Diagonalization simplifies matrix operations, especially computing powers of matrices.

## Common Mistakes to Avoid

- **Forgetting to Check Linear Independence**: Not verifying that eigenvectors are linearly independent before forming P.

- **Order Mismatch**: Placing eigenvalues in D in a different order than corresponding eigenvectors in P.

- **Incorrect Inverse Computation**: Making arithmetic errors when computing P⁻¹, especially for 2×2 matrices.

- **Assuming Repeated Eigenvalues Mean Non-Diagonalizable**: A matrix with repeated eigenvalues can still be diagonalizable if GM = AM.

- **Ignoring Zero Eigenvalues**: Treating zero eigenvalues differently; they must be included in the diagonal matrix D.

## Revision Tips

1. **Practice 3-4 Complete Problems**: Solve full diagonalization problems from previous year question papers within time limits.

2. **Master the Basics**: Ensure complete understanding of eigenvalues and eigenvectors before attempting diagonalization.

3. **Memorize the Step Sequence**: Characteristic polynomial → Eigenvalues → Eigenvectors → Form P and D → Verify.

4. **Focus on Special Cases**: Review symmetric matrix diagonalization and orthogonal matrices separately.

5. **Use Quick Verification**: Always check P⁻¹AP = D to catch errors immediately.