# Orthogonal Sets and Bases - Summary

## Key Definitions and Concepts

- **Orthogonal Vectors**: Two vectors **u** and **v** are orthogonal if **u** · **v** = 0
- **Orthogonal Set**: A set of non-zero vectors where every pair of distinct vectors has zero dot product
- **Orthonormal Set**: An orthogonal set where each vector has unit length (norm = 1), satisfying **u**ᵢ · **u**ⱼ = δᵢⱼ
- **Orthogonal Basis**: A basis consisting of orthogonal vectors for a subspace
- **Orthonormal Basis**: An orthogonal basis with unit-length vectors
- **Orthogonal Complement (W⊥)**: The set of all vectors orthogonal to every vector in subspace W

## Important Formulas and Theorems

- **Coordinate relative to orthogonal basis**: cᵢ = (**x** · **v**ᵢ)/(**v**ᵢ · **v**ᵢ)
- **Coordinate relative to orthonormal basis**: cᵢ = **x** · **u**ᵢ
- **Gram-Schmidt Process**: **v**₁ = **x**₁; **v**ⱼ = **x**ⱼ - Σᵢ₌₁^(j-1) [(**x**ⱼ · **v**ᵢ)/(**v**ᵢ · **v**ᵢ)] **v**ᵢ
- **Normalization**: **u**ᵢ = **v**ᵢ/||**v**ᵢ|| for orthonormal basis
- **Dimension Theorem**: dim(W) + dim(W⊥) = n for subspaces of ℝⁿ
- **Double Orthogonal Complement**: (W⊥)⊥ = W

## Key Points

- Orthogonal sets of non-zero vectors are always linearly independent
- An orthogonal set of n non-zero vectors in ℝⁿ forms an orthogonal basis for ℝⁿ
- The standard basis {**e**₁, **e**₂, ..., **e**ₙ} is an orthonormal basis
- Gram-Schmidt process converts any linearly independent set into an orthogonal set
- QR decomposition uses Gram-Schmidt: A = QR where Q has orthonormal columns
- Orthogonal matrices have orthonormal columns (or rows) and satisfy Q⁻¹ = Qᵀ
- Fourier basis is a classic example of orthonormal basis used in signal processing

## Common Mistakes to Avoid

- Forgetting to normalize when transitioning from orthogonal to orthonormal basis
- Using the wrong formula for coordinates (confusing orthogonal vs orthonormal cases)
- Not checking linear independence before applying Gram-Schmidt
- Computing dot products incorrectly, especially with negative signs

## Revision Tips

- Practice at least 3 Gram-Schmidt problems to master the iterative formula
- Remember that orthonormal simplifies all coordinate computations
- Connect concepts to QR decomposition for complete understanding
- Review least squares applications where orthogonal bases are essential
