# Singular Value Decomposition (SVD) - Summary

## Key Definitions and Concepts

- **SVD**: Any m×n matrix A can be decomposed as A = UΣV^T where U (m×m) and V (n×n) are orthogonal matrices, and Σ (m×n) is diagonal with non-negative entries.

- **Singular Values**: Diagonal entries σ₁ ≥ σ₂ ≥ ... ≥ σᵣ > 0 of matrix Σ, representing the "stretching" factors in the transformation.

- **Left Singular Vectors**: Columns of U, eigenvectors of AA^T.

- **Right Singular Vectors**: Columns of V, eigenvectors of A^T A.

- **Compact SVD**: A = UᵣΣᵣVᵣ^T using only r non-zero singular values for rank-r matrices.

## Important Formulas and Theorems

- **SVD Definition**: A = UΣV^T
- **Singular Values**: σᵢ = √λᵢ(A^T A) = √λᵢ(AA^T)
- **Rank from SVD**: rank(A) = number of non-zero singular values
- **Orthogonality**: U^T U = Iₘ, V^T V = Iₙ
- **Eckart-Young Theorem**: Best k-rank approximation uses top k singular values
- **Energy Preservation**: Σᵢσᵢ² = Σᵢⱼaᵢⱼ²

## Key Points

- SVD works for any rectangular matrix, unlike eigenvalue decomposition which requires square matrices.
- Singular values are always non-negative real numbers.
- The columns of U and V form orthonormal bases for the column space and row space respectively.
- A zero singular value indicates linear dependence in the corresponding directions.
- Larger singular values capture more "energy" or information in the matrix.
- SVD provides optimal low-rank approximations in the Frobenius norm sense.
- The geometric interpretation is: rotation (V^T) → scaling (Σ) → rotation (U).

## Common Mistakes to Avoid

- Confusing singular values with eigenvalues - they are related but not the same.
- Forgetting that singular values are always non-negative.
- Not arranging singular values in descending order in the Σ matrix.
- Assuming SVD is unique - it's unique only when all singular values are distinct and non-zero.
- Confusing U and V matrices - U corresponds to row space transformations, V to column space.

## Revision Tips

1. Practice computing A^T A and finding its eigenvalues - this is the first step in any SVD problem.
2. Remember that V's columns are eigenvectors of A^T A, and U's columns are computed as uᵢ = (1/σᵢ)Avᵢ.
3. For quick verification, check that U and V are orthogonal matrices.
4. Focus on understanding the geometric meaning: any linear transformation can be viewed as rotation-scaling-rotation.
5. Remember: rank equals the count of non-zero singular values - this is frequently tested.
