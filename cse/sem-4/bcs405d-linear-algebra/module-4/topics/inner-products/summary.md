# Inner Products - Summary

## Key Definitions and Concepts

- **Inner Product**: A binary operation ⟨u, v⟩ on a vector space V satisfying: (i) conjugate symmetry, (ii) linearity in the first argument, and (iii) positive-definiteness.
- **Inner Product Space**: A vector space equipped with an inner product; real cases are Euclidean spaces, complex cases are unitary spaces.
- **Norm induced by Inner Product**: ||v|| = √⟨v, v⟩, providing length and distance notions.
- **Orthogonal Vectors**: u ⟂ v if and only if ⟨u, v⟩ = 0.
- **Orthogonal Set**: A set where every pair of distinct vectors is orthogonal; orthonormal if all vectors also have unit norm.
- **Orthogonal Complement W⊥**: All vectors orthogonal to every vector in subspace W.

## Important Formulas and Theorems

- **Cauchy-Schwarz Inequality**: |⟨u, v⟩| ≤ ||u|| ||v||, equality iff u and v are linearly dependent
- **Angle between vectors**: cos θ = ⟨u, v⟩/(||u|| ||v||) for nonzero u, v
- **Gram-Schmidt Process**: v₁ = x₁; vₖ = xₖ - Σᵢ₌₁ᵏ⁻¹ ⟨xₖ, vᵢ⟩/⟨vᵢ, vᵢ⟩vᵢ
- **Projection Formula**: projᵥ(u) = ⟨u, v⟩/⟨v, v⟩ × v
- **Best Approximation**: projᵂ(v) minimizes ||v - w|| over all w ∈ W
- **Direct Sum Decomposition**: V = W ⊕ W⊥, with (W⊥)⊥ = W

## Key Points

- The dot product on ℝⁿ is the standard example of an inner product: ⟨x, y⟩ = Σxᵢyᵢ
- An orthonormal basis simplifies computations: coordinates are simply inner products with basis vectors
- Gram-Schmidt eliminates the need to solve systems of equations when finding orthogonal bases
- The orthogonal complement of a subspace always forms a subspace
- Every finite-dimensional subspace has an orthonormal basis obtained by Gram-Schmidt followed by normalization
- Positive-definiteness ensures the norm is well-defined (non-negative and zero only for zero vector)

## Common Mistakes to Avoid

- Forgetting to check positive-definiteness when verifying if a function is an inner product
- Confusing orthogonal (⟨u, v⟩ = 0) with orthonormal (⟨u, v⟩ = 0 AND ||u|| = ||v|| = 1)
- Applying the angle formula when one or both vectors are zero vectors
- Using the wrong field (real vs. complex) when computing inner products—complex inner products require conjugation
- Forgetting to normalize when converting orthogonal basis to orthonormal basis

## Revision Tips

1. Practice computing inner products for different spaces: ℝⁿ vectors, matrices, and functions.
2. Work through at least three Gram-Schmidt examples until the process becomes automatic.
3. Memorize the Cauchy-Schwarz inequality form and remember when equality holds.
4. Visualize orthogonal projections as "dropping perpendiculars" to subspaces.
5. Solve previous years' university examination questions on this topic to understand the question patterns.
