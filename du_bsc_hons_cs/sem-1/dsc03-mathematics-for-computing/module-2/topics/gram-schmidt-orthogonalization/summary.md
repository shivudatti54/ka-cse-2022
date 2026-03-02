# Gram-Schmidt Orthogonalization - Summary

## Key Definitions and Concepts

- **Inner Product**: A binary operation ⟨u, v⟩ on a vector space satisfying linearity, symmetry, and positive definiteness
- **Orthogonal Vectors**: Vectors u and v are orthogonal if ⟨u, v⟩ = 0
- **Orthonormal Vectors**: Vectors that are orthogonal AND have unit norm (length = 1)
- **Vector Projection**: projᵤ(v) = (⟨v, u⟩/⟨u, u⟩) × u gives the component of v along u
- **Gram-Schmidt Process**: Transforms linearly independent vectors into an orthogonal (or orthonormal) set

## Important Formulas and Theorems

- **Projection Formula**: projᵤ(v) = (⟨v, u⟩/⟨u, u⟩) × u
- **Gram-Schmidt Orthogonalization**: u₁ = v₁; uₖ = vₖ - Σⱼ⟨vₖ, uⱼ⟩/⟨uⱼ, uⱼ⟩uⱼ for k = 2 to n
- **Normalization**: eₖ = uₖ/||uₖ|| = uₖ/√⟨uₖ, uₖ⟩
- **QR Decomposition**: A = QR where Q has orthonormal columns and R is upper triangular

## Key Points

- The Gram-Schmidt process produces an orthogonal set from linearly independent vectors
- Each new orthogonal vector is obtained by subtracting projections of the original vector onto all previous orthogonal vectors
- The resulting orthogonal vectors span the same subspace as the original vectors
- Normalization converts orthogonal vectors to orthonormal vectors (unit length)
- The process is order-dependent; input order affects the output orthogonal set
- Modified Gram-Schmidt is numerically more stable for floating-point computations
- QR decomposition via Gram-Schmidt is fundamental in least squares solving and eigenvalue computations

## Common Mistakes to Forget

- Forgetting to subtract projections onto ALL previously computed orthogonal vectors
- Confusing orthogonal (zero dot product) with orthonormal (zero dot product + unit norm)
- Not verifying orthogonality of the result through dot product checks
- Attempting to orthogonalize linearly dependent vectors (results in zero vectors)
- Using wrong formula for projection (missing division by ⟨u, u⟩)

## Revision Tips

1. Practice at least 3-4 problems with different vector spaces to master the computational steps
2. Always verify your final answer by checking orthogonality: ⟨uᵢ, uⱼ⟩ = 0 for i ≠ j
3. Memorize the projection formula as it's the foundation of the entire process
4. Understand the geometric interpretation: each new vector removes components in directions of previous vectors
5. Connect to QR decomposition as this shows practical applications in computing contexts
6. Review the modified Gram-Schmidt variant for numerical stability considerations