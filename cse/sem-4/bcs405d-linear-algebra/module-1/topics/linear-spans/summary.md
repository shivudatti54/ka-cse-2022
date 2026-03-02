# Linear Spans - Summary

## Key Definitions and Concepts

- **Linear Combination:** An expression c₁v₁ + c₂v₂ + ... + cₖvₖ where cᵢ are scalars and vᵢ are vectors.

- **Linear Span:** The set Span(S) = {c₁v₁ + c₂v₂ + ... + cₖvₖ : cᵢ ∈ F} of all linear combinations of vectors in S.

- **Spanning Set:** A set S in V is a spanning set if Span(S) = V, meaning every vector in V can be expressed as a linear combination of vectors in S.

- **Standard Basis for ℝⁿ:** The set {e₁, e₂, ..., eₙ} where e₁ = (1, 0, ..., 0), etc., spans ℝⁿ.

## Important Formulas and Theorems

- Span of single vector in ℝ³: Span{(a, b, c)} = {(ta, tb, tc) : t ∈ ℝ} (a line through origin)
- Span of two independent vectors in ℝ³: A plane through the origin
- Span of three linearly independent vectors in ℝ³: The entire ℝ³ space
- If vectors are linearly independent in ℝⁿ and there are n of them, they span ℝⁿ

## Key Points

- Span always contains the zero vector (choose all scalars as 0)
- Span(S) is always a subspace of V, regardless of S
- The span of any set is the smallest subspace containing that set
- In ℝ², any two non-collinear vectors span the entire plane
- In ℝ³, three linearly independent vectors span the entire space
- Fewer than n vectors in ℝⁿ cannot span ℝⁿ
- Removing vectors that are linear combinations of others does not change the span

## Common Mistakes to Avoid

1. Forgetting that span is always through the origin—it never offsets from zero
2. Confusing linear dependence with spanning: dependent vectors may still span (if at least one is non-zero)
3. Assuming any two vectors in ℝ³ span ℝ³—they must be linearly independent
4. Neglecting to check if a solution exists when determining if a vector lies in a span

## Revision Tips

1. Practice writing vectors as linear combinations with unknown scalars
2. Solve 5-6 problems on checking if a vector belongs to a span
3. Visualize spans in ℝ² and ℝ³ to build geometric intuition
4. Remember that span questions reduce to solving linear systems—practice Gaussian elimination
5. Review the connection between spanning sets and linear independence (basis concept)
