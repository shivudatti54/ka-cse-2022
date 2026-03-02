# Subspaces - Summary

## Key Definitions and Concepts

- **Subspace**: A subset W of a vector space V that is itself a vector space under the same operations. Must contain zero vector, and be closed under addition and scalar multiplication.

- **Subspace Test**: A subset W is a subspace if and only if: (i) 0 ∈ W, (ii) u, v ∈ W implies u + v ∈ W, and (iii) u ∈ W and c ∈ F implies cu ∈ W.

- **Span**: The set of all linear combinations of a set of vectors. Always forms a subspace.

- **Direct Sum (W₁ ⊕ W₂)**: Sum of subspaces where W₁ ∩ W₂ = {0}, ensuring unique representation of vectors.

## Important Formulas and Theorems

- **Span as Subspace**: span{v₁, v₂, ..., vₖ} is always a subspace of V
- **Intersection Property**: W₁ ∩ W₂ is always a subspace (if W₁, W₂ are subspaces)
- **Dimension of Direct Sum**: dim(W₁ ⊕ W₂) = dim(W₁) + dim(W₂)
- **Subspace Criterion**: W is a subspace ⟺ cw₁ + dw₂ ∈ W for all w₁, w₂ ∈ W and all scalars c, d

## Key Points

- Every vector space has at least two subspaces: {0} (trivial) and V itself
- A line through origin in R² or R³ is a 1-dimensional subspace
- A plane through origin in R³ is a 2-dimensional subspace
- Union of subspaces is a subspace only when one contains the other
- The sum W₁ + W₂ always contains both W₁ and W₂ and is the smallest subspace containing both
- For subspaces defined by homogeneous linear equations, the solution set is always a subspace

## Common Mistakes to Avoid

- Forgetting to check the zero vector condition when determining if a set is a subspace
- Assuming the union of two subspaces is always a subspace (it isn't)
- Confusing the sum of subspaces (W₁ + W₂) with the union (W₁ ∪ W₂)
- Not verifying linear independence when claiming a set is a basis

## Revision Tips

- Practice identifying subspaces in R² and R³ by visualizing lines and planes through the origin
- Memorize the three conditions of the subspace test and apply them systematically
- Work through problems involving finding bases and dimensions of subspaces defined by equations
- Remember: geometric intuition helps - subspaces "pass through the origin" in Euclidean spaces
