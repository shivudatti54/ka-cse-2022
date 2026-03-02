# Introduction to Linear Transformations - Summary

## Key Definitions

- **Linear Transformation**: A function T: V → W between vector spaces V and W that satisfies T(u + v) = T(u) + T(v) and T(cv) = cT(v) for all u, v ∈ V and scalars c.

- **Domain**: The vector space V on which the transformation is defined.

- **Codomain**: The vector space W into which the transformation maps.

- **Image/Range**: The set {T(v) : v ∈ V} ⊆ W of all possible outputs.

- **Zero Transformation**: T(v) = 0 for all v ∈ V.

- **Identity Transformation**: I(v) = v for all v ∈ V.

## Important Formulas

- **Combined Linearity Condition**: T(cu + dv) = cT(u) + dT(v) for all u, v ∈ V and scalars c, d.

- **Linear Combination Preservation**: T(a₁v₁ + a₂v₂ + ... + aₙvₙ) = a₁T(v₁) + a₂T(v₂) + ... + aₙT(vₙ).

- **Determination by Basis**: If {v₁, ..., vₙ} is a basis of V, then knowing T(v₁), ..., T(vₙ) determines T completely.

## Key Points

1. A linear transformation must preserve both vector addition and scalar multiplication operations.

2. Every linear transformation maps the zero vector to the zero vector: T(0) = 0.

3. Linear transformations preserve linear combinations: the image of a linear combination equals the linear combination of the images.

4. A linear transformation is completely determined by its action on a basis of the domain.

5. Common linear transformations in ℝ² include scaling, rotation, reflection, projection, and shear.

6. Transformations that translate (shift the origin) or introduce constant terms are NOT linear—they are affine.

7. Linear transformations can exist between infinite-dimensional spaces (e.g., differentiation on polynomial spaces).

8. The set of all linear transformations from V to W is itself a vector space, denoted L(V, W).

9. Every linear transformation from ℝⁿ to ℝᵐ can be represented by an m×n matrix.

## Common Mistakes

1. **Forgetting the Origin**: Forgetting that T(0) = 0 is a necessary condition and failing to check this when verifying linearity.

2. **Confusing Linear with Affine**: Treating T(x) = Ax + b (where b ≠ 0) as linear; this is actually an affine transformation.

3. **Omitting One Property**: Verifying only additivity OR only homogeneity when checking linearity, rather than both.

4. **Incorrect Basis Reasoning**: Failing to recognize that knowing images of basis vectors completely determines a linear transformation.

5. **Ignoring Domain/Codomain**: Not specifying or incorrectly identifying the domain and codomain when describing transformations.
