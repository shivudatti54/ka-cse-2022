# Inner Product Spaces - Summary

## Key Definitions and Concepts

- **Inner Product:** A function ⟨·, ·⟩: V × V → F satisfying conjugate symmetry, linearity in the first argument, and positive-definiteness.

- **Norm (Length):** ‖v‖ = √⟨v, v⟩, measuring the "size" of a vector.

- **Orthogonal Vectors:** u ⊥ v iff ⟨u, v⟩ = 0

- **Orthonormal Set:** Vectors that are mutually orthogonal with unit norm: ⟨vᵢ, vⱼ⟩ = δᵢⱼ

- **Orthogonal Complement:** W⊥ = {v ∈ V : ⟨v, w⟩ = 0 ∀w ∈ W}

## Important Formulas and Theorems

- **Standard Inner Product (ℝⁿ):** ⟨u, v⟩ = u₁v₁ + u₂v₂ + ... + uₙvₙ

- **Cauchy-Schwarz Inequality:** |⟨u, v⟩| ≤ ‖u‖·‖v‖

- **Triangle Inequality:** ‖u + v‖ ≤ ‖u‖ + ‖v‖

- **Gram-Schmidt Process:** vₖ = wₖ - Σᵢ₌₁ᵏ⁻¹ (⟨wₖ, vᵢ⟩/⟨vᵢ, vᵢ⟩)vᵢ

- **Projection Formula:** proj_v(w) = (⟨w, v⟩/⟨v, v⟩)v

## Key Points

- Inner products generalize dot products to abstract vector spaces, enabling geometric concepts.

- For finite-dimensional spaces, every subspace W has W⊥ such that W ⊕ W⊥ = V.

- The Gram-Schmidt process produces an orthogonal basis without changing the span.

- An orthonormal basis simplifies computations: any vector v = Σ⟨v, uᵢ⟩uᵢ.

- Complex inner products require conjugation in the second argument.

- The orthogonal projection onto a subspace gives the closest approximation in that subspace.

- A set of n mutually orthogonal nonzero vectors in ℝⁿ must be a basis.

## Common Mistakes to Forget

- Forgetting the conjugate in complex inner products: ⟨u, v⟩ ≠ uᵀv for complex vectors.

- Not normalizing after Gram-Schmidt when an orthonormal basis is required.

- Confusing orthogonal (perpendicular) with orthogonal complement (all vectors perpendicular to a subspace).

- Using the wrong formula for projection—remember it's always onto the direction being projected onto.

## Revision Tips

1. Practice verifying inner products with different functions to master the axiom checks.

2. Memorize the Gram-Schmidt algorithm step-by-step and practice with at least 3 different examples.

3. Remember: orthogonal sets of nonzero vectors are always linearly independent.

4. For complex spaces, keep track of which argument gets the conjugate—always the second one.

5. Sketch the orthogonal decomposition v = proj_W(v) + (v - proj_W(v)) to visualize the Best Approximation Theorem.
