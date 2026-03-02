# Singular and Non-Singular Linear Transformations - Summary

## Key Definitions and Concepts

- **Linear Transformation:** A mapping T: V → W between vector spaces satisfying T(u+v) = T(u) + T(v) and T(αv) = αT(v) for all u,v ∈ V and scalars α.

- **Singular (Degenerate) Transformation:** A linear transformation that is not one-to-one; distinct vectors map to the same output. Equivalently, ker(T) contains non-zero vectors.

- **Non-Singular (Invertible) Transformation:** A linear transformation that is one-to-one; distinct vectors map to distinct outputs. Equivalently, ker(T) = {0}.

- **Kernel (Null Space):** ker(T) = {v ∈ V : T(v) = 0}. For non-singular T, ker(T) = {0}.

- **Range (Image):** Range(T) = {T(v) : v ∈ V}. For non-singular T, dim(Range) = dim(Domain).

## Important Formulas and Theorems

- **Rank-Nullity Theorem:** Rank(T) + Nullity(T) = dim(V), where V is the domain.

- **Non-singularity Criteria (for T: ℝⁿ → ℝⁿ):**
  - T is non-singular ⇔ det(A) ≠ 0 (A is the matrix representation)
  - T is non-singular ⇔ Rank(A) = n
  - T is non-singular ⇔ A is invertible
  - T is non-singular ⇔ T is one-to-one ⇔ T is onto (when dim(domain) = dim(codomain))

- **Inverse Transformation:** If T is non-singular, T⁻¹ exists and (T⁻¹)⁻¹ = T.

## Key Points

- Singular transformations "collapse" dimensions; non-singular transformations preserve dimensional structure.

- For a transformation between equal-dimensional spaces, one-to-one and onto are equivalent conditions for non-singularity.

- The zero transformation (T(v) = 0 for all v) is always singular.

- Identity transformation I(v) = v is always non-singular.

- Determinant test: det(A) = 0 indicates singularity; det(A) ≠ 0 indicates non-singularity.

- Rank equals the number of linearly independent columns (or rows) of the matrix representation.

- Nullity equals the dimension of the solution space to T(v) = 0.

## Common Mistakes to Avoid

1. **Confusing domain and codomain dimensions:** A transformation from ℝ³ to ℝ² can be non-singular (one-to-one) even though it cannot be onto.

2. **Forgetting the Rank-Nullity theorem:** Always verify that Rank + Nullity equals the domain dimension.

3. **Incorrect determinant calculation:** For 3×3 matrices, carefully compute using cofactor expansion or other methods.

4. **Assuming invertibility in different spaces:** A transformation from ℝⁿ to ℝᵐ (where n ≠ m) cannot have a two-sided inverse.

## Revision Tips

1. Practice identifying singular/non-singular transformations by finding the kernel – if only the zero vector maps to zero, the transformation is non-singular.

2. Memorize the equivalence: for n×n matrices, non-singular ↔ det ≠ 0 ↔ full rank ↔ invertible.

3. Solve at least 5 problems from previous university question papers on this topic.

4. Create a quick reference table comparing properties of singular vs. non-singular transformations.

5. Remember that projection onto a subspace is always singular (unless projecting onto the entire space).
