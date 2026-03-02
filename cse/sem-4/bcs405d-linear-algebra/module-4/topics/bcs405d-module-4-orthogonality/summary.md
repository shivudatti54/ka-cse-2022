# Length and Orthogonality - Summary

## Key Definitions and Concepts

- **Dot Product**: **u** · **v** = u₁v₁ + u₂v₂ + ... + uₙvₙ for vectors in ℝⁿ
- **Norm (Length)**: ‖**v**‖ = √(**v** · **v**) = √(v₁² + v₂² + ... + vₙ²)
- **Unit Vector**: A vector with ‖**v**‖ = 1; normalized form: **v**/‖**v**‖
- **Distance**: d(**u**, **v**) = ‖**u** - **v**‖
- **Orthogonal Vectors**: **u** ⊥ **v** if **u** · **v** = 0
- **Orthogonal Set**: Set where all pairs of distinct vectors have zero dot product
- **Orthonormal Set**: Orthogonal set where all vectors have unit length
- **Orthogonal Complement**: W⊥ = {**v** ∈ ℝⁿ : **v** · **w** = 0 for all **w** ∈ W}

## Important Formulas and Theorems

- **Cauchy-Schwarz**: |**u** · **v**| ≤ ‖**u**‖‖**v**‖
- **Triangle Inequality**: ‖**u** + **v**‖ ≤ ‖**u**‖ + ‖**v**‖
- **Angle Formula**: cos θ = (**u** · **v**)/(‖**u**‖‖**v**‖)
- **Pythagorean Theorem**: If **u** ⊥ **v**, then ‖**u** + **v**‖² = ‖**u**‖² + ‖**v**‖²
- **Gram-Schmidt**: **vₖ** = **xₖ** - Σᵢ₌₁ᵏ⁻¹ proj\_{**vᵢ**}(**xₖ**)

## Key Points

- The dot product is commutative, distributive, and satisfies positivity properties
- Orthogonal non-zero vectors are always linearly independent
- An orthogonal set of non-zero vectors can be converted to orthonormal by normalization
- dim(W) + dim(W⊥) = n for any subspace W of ℝⁿ
- The Gram-Schmidt process produces an orthogonal set from linearly independent vectors
- Cauchy-Schwarz equality holds only when vectors are linearly dependent
- The zero vector is orthogonal to every vector in the space

## Common Mistakes to Avoid

- Confusing orthogonal (zero dot product) with perpendicular in higher dimensions
- Forgetting to normalize vectors when asked for an orthonormal basis
- Applying Pythagorean theorem without verifying orthogonality first
- Using the wrong formula for projection in Gram-Schmidt process

## Revision Tips

- Practice computing dot products and norms with various 2D and 3D vectors
- Memorize the Cauchy-Schwarz and triangle inequality statements
- Work through at least two Gram-Schmidt examples to master the process
- Remember: orthogonal vectors simplify many calculations—look for opportunities to use them
