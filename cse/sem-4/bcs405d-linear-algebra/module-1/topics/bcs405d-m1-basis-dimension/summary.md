# Basis and Dimension - Summary

## Key Definitions and Concepts

- **Linearly Independent:** A set of vectors {v₁, v₂, ..., vₖ} is linearly independent if c₁v₁ + c₂v₂ + ... + cₖvₖ = 0 implies c₁ = c₂ = ... = cₖ = 0
- **Spanning Set:** A set spans vector space V if every vector in V can be expressed as a linear combination of the set
- **Basis:** A set that is both linearly independent and spans V; every vector in V has a unique representation as a linear combination of basis vectors
- **Dimension:** The number of vectors in any basis for V, denoted dim(V)

## Important Formulas and Theorems

- All bases of a finite-dimensional vector space have the same number of elements (dimension)
- If dim(V) = n: n linearly independent vectors ⇒ basis; n vectors spanning V ⇒ basis
- dim(ℝⁿ) = n, dim(Pₙ) = n + 1, dim(Mₘₓₙ) = mn
- Basis Extension Theorem: Any linearly independent set can be extended to a basis
- For homogeneous systems Ax = 0, parametric form of solutions gives a basis for null space
- Rank(A) = dim(Col(A)) = dim(Row(A))

## Key Points

- A basis provides both a minimal spanning set and a maximal linearly independent set
- The standard basis for ℝⁿ is {e₁, e₂, ..., eₙ} where eᵢ has 1 in position i and 0 elsewhere
- For n vectors in ℝⁿ, they form a basis if and only if the determinant of the matrix is non-zero
- Subspaces have dimensions less than or equal to the containing space
- If dim(W) = dim(V) and W ⊆ V, then W = V
- The zero vector space has dimension 0 with empty basis

## Common Mistakes to Avoid

1. Checking only one condition (independence OR span) when verifying a basis
2. Confusing the number of vectors with the dimension (dimension is the count, not the vector entries)
3. Forgetting that different bases for the same space have the same number of vectors
4. Not recognizing that column dependence in a matrix relates to linear dependence of column vectors

## Revision Tips

1. Practice identifying bases by checking both conditions systematically
2. Remember the dimension formulas for common vector spaces
3. For solution spaces, always write in parametric vector form to extract basis vectors
4. Use row reduction to find bases for column spaces and check linear independence
5. Review the relationship between rank, nullity, and dimensions using the Rank-Nullity Theorem
