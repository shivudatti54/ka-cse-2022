# Jordan Canonical Form - Summary

## Key Definitions and Concepts

- **Jordan Canonical Form**: A block diagonal matrix where each block is a Jordan block, representing the simplest form of a square matrix under similarity transformation.

- **Jordan Block**: A square matrix with constant λ on the diagonal, 1s on the superdiagonal, and 0s elsewhere; represents a single eigenvalue with one associated eigenvector.

- **Algebraic Multiplicity (mₐ)**: Number of times an eigenvalue appears as a root of the characteristic polynomial.

- **Geometric Multiplicity (mᵍ)**: Dimension of the eigenspace, equal to the number of linearly independent eigenvectors for an eigenvalue.

- **Generalized Eigenvector**: Vector v where (A-λI)^k v = 0 for some k, but (A-λI)^(k-1) v ≠ 0.

- **Similar Matrices**: Matrices A and B where B = P⁻¹AP for some invertible matrix P; they represent the same linear transformation.

## Important Formulas and Theorems

- **Characteristic Polynomial**: p(λ) = det(λI - A) = ∏(λ - λᵢ)^(mₐᵢ)
- **Cayley-Hamilton Theorem**: p(A) = 0 (every matrix satisfies its characteristic polynomial)
- **Number of Jordan Blocks**: Equals geometric multiplicity for each eigenvalue
- **Block Size Sum**: For each eigenvalue, sum of Jordan block sizes equals algebraic multiplicity
- **Diagonalizable Condition**: mᵍ = mₐ for all eigenvalues

## Key Points

- The Jordan Canonical Form is unique up to the ordering of Jordan blocks.
- A matrix is diagonalizable iff all Jordan blocks are 1×1.
- Similarity preserves eigenvalues, characteristic polynomial, minimal polynomial, rank, and trace.
- The minimal polynomial's exponent for each eigenvalue equals the largest Jordan block size.
- Powers of Jordan blocks can be computed using binomial expansion.
- Complex eigenvalues in real matrices appear in conjugate pairs in the Jordan form.
- The transition matrix P has generalized eigenvectors as its columns.

## Common Mistakes to Avoid

1. Confusing algebraic multiplicity (root multiplicity) with geometric multiplicity (eigenspace dimension).
2. Assuming all matrices are diagonalizable—non-diagonalizable matrices require Jordan blocks.
3. Forgetting that the number of Jordan blocks equals geometric multiplicity, not algebraic.
4. Computing characteristic polynomial incorrectly—always subtract A from λI.
5. Trying to diagonalize when geometric multiplicity < algebraic multiplicity.

## Revision Tips

1. Practice finding Jordan forms of 2×2 and 3×3 matrices with varying eigenvalue structures.
2. Memorize the relationship: for each eigenvalue, mᵍ ≤ mₐ, and the difference determines Jordan block sizes.
3. Remember that diagonalizable ⇔ minimal polynomial has no repeated roots.
4. Review Cayley-Hamilton theorem applications for quick matrix power computations.
5. Focus on understanding generalized eigenvector chains—they are the key to constructing the transition matrix P.
