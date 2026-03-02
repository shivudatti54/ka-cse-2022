# Vector Spaces - Summary

## Key Definitions and Concepts

- **Vector Space**: A set V with two operations (vector addition and scalar multiplication) satisfying ten axioms including closure, commutativity, associativity, existence of identity and inverses.

- **Subspace**: A subset W of V that is itself a vector space under the same operations. Conditions: W ≠ ∅ (contains 0), closed under addition, closed under scalar multiplication.

- **Linear Combination**: Vector v = c₁v₁ + c₂v₂ + ... + cₖvₖ where cᵢ are scalars.

- **Span**: Span{v₁, v₂, ..., vₖ} is the set of all linear combinations of the given vectors.

- **Linearly Independent**: Vectors v₁, v₂, ..., vₙ are linearly independent if c₁v₁ + c₂v₂ + ... + cₙvₙ = 0 implies all cᵢ = 0.

- **Basis**: A set of linearly independent vectors that span the entire vector space.

- **Dimension**: The number of vectors in any basis of the vector space (denoted dim(V)).

## Important Formulas and Theorems

- **Subspace Test**: W ⊆ V is a subspace if and only if: (i) 0 ∈ W, (ii) u, v ∈ W ⇒ u + v ∈ W, (iii) u ∈ W, c ∈ F ⇒ cu ∈ W

- **Dependence Test**: Vectors are linearly dependent if one can be expressed as a linear combination of others.

- **Dimension Relationship**: If V has dimension n, then any set of n linearly independent vectors is a basis; any set of more than n vectors is linearly dependent.

- **Span as Subspace**: For any set S ⊆ V, Span(S) is a subspace of V.

## Key Points

- ℝⁿ, Pₙ (polynomials of degree ≤ n), Mₘₙ(ℝ) (matrices), and function spaces are all examples of vector spaces.

- The zero vector space has dimension 0; it contains only the zero vector.

- Standard basis for ℝⁿ consists of unit vectors e₁, e₂, ..., eₙ.

- A subspace of dimension one is called a line; dimension two is a plane.

- The span of a single non-zero vector is a line through the origin.

- If vectors span V and are linearly independent, they form a basis of V.

- Dimension of Mₘₙ(ℝ) is mn; dimension of Pₙ is n+1.

## Common Mistakes to Avoid

- Forgetting to check if zero vector belongs to the set when verifying subspaces.

- Assuming any set of n vectors in ℝⁿ is a basis—they must be linearly independent.

- Confusing linear dependence with having proportional vectors only—dependence is more general.

- Forgetting that subspaces must contain the origin; sets like {(x,y) : x + y = 1} are NOT subspaces.

## Revision Tips

1. Practice verifying vector space axioms with at least 3-4 different examples.

2. Memorize the subspace test procedure: zero vector → closure under addition → closure under scalar multiplication.

3. Work through problems finding bases for subspaces defined by equations (solve the system, express in terms of free variables).

4. Remember: More vectors than dimension = automatically dependent; n vectors in ℝⁿ that span = check independence for basis.
