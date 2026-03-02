# Gram-Schmidt Orthogonalization Process - Summary

## Key Definitions and Concepts

- **Inner Product**: ⟨**u**, **v**⟩ = u₁v₁ + u₂v₂ + ... + uₙvₙ (for vectors in ℝⁿ)
- **Norm**: ||**v**|| = √⟨**v**, **v**⟩ = √(v₁² + v₂² + ... + vₙ²)
- **Orthogonal Vectors**: **u** ⊥ **v** if and only if ⟨**u**, **v**⟩ = 0
- **Orthonormal Vectors**: Vectors that are mutually orthogonal and each has unit length (⟨**eᵢ**, **eⱼ**⟩ = δᵢⱼ)

## Important Formulas and Theorems

- **Projection Formula**: projᵤ(**v**) = (⟨**v**, **u**⟩/⟨**u**, **u**⟩)**u**
- **Gram-Schmidt Orthogonalization**:
  - **q₁** = **a₁**
  - **qₖ** = **aₖ** - Σⱼ⟨**aₖ**, **qⱼ**⟩/⟨**qⱼ**, **qⱼ**⟩**qⱼ** for k ≥ 2
- **Normalization**: **eₖ** = **qₖ**/||**qₖ**||
- **QR Decomposition**: A = QR, where Q has orthonormal columns

## Key Points

- The Gram-Schmidt process converts any set of n linearly independent vectors into an orthogonal set of n vectors.
- The resulting orthogonal/orthonormal vectors span the same subspace as the original vectors.
- Each **qₖ** is orthogonal to all previous **q₁**, **q₂**, ..., **qₖ₋₁**.
- QR decomposition via Gram-Schmidt has R as an upper triangular matrix.
- Modified Gram-Schmidt is numerically more stable than the classical approach.
- If vectors are linearly dependent, the process yields zero vectors (which cannot be normalized).

## Common Mistakes to Avoid

- Forgetting to normalize when an orthonormal basis is required.
- Computing the projection using the wrong formula or using normalized vectors in projection calculations without adjusting.
- Skipping verification that orthogonal vectors are indeed orthogonal (dot product = 0).
- Using dependent vectors in the input - Gram-Schmidt requires linear independence.

## Revision Tips

1. Practice at least 3-4 problems of varying difficulty to master the computation steps.
2. Always verify your orthogonal vectors by computing their dot products.
3. Remember the connection: Gram-Schmidt → Orthogonal vectors → Normalize → Q matrix in QR.
4. Keep the projection formula handy: it's the core of the entire process.
5. Understand that order of input vectors affects the output, but any orthogonal set spans the same space.
