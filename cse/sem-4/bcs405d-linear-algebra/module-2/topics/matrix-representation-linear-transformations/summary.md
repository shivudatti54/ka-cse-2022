# Matrix Representation of Linear Transformations - Summary

## Key Definitions and Concepts

- **Linear Transformation**: A function T: V → W between vector spaces satisfying T(u + v) = T(u) + T(v) and T(cu) = cT(u) for all vectors u, v and scalars c.

- **Matrix Representation**: For linear transformation T: V → W with ordered bases B*V (dimension n) and B_W (dimension m), the m × n matrix A = [T]*{B*W}^{B_V} satisfies [T(v)]*{B*W} = A[v]*{B_V} for all v in V.

- **Standard Matrix**: Matrix representation when using standard bases; columns are images of standard basis vectors.

## Important Formulas and Theorems

- **Matrix of T**: If B*V = {v₁, ..., vₙ} and B_W = {w₁, ..., wₘ}, then A = [[T(v₁)]*{B*W} | [T(v₂)]*{B*W} | ... | [T(vₙ)]*{B_W}]

- **Composition**: [T∘S] = [T][S] (matrix product, order matters)

- **Change of Basis**: [T]\_{new} = Q^{-1}AP, where P is change-of-basis matrix in domain and Q in codomain

- **Rotation by θ**: [[cos θ, -sin θ], [sin θ, cos θ]]

- **Reflection across x-axis**: [[1, 0], [0, -1]]

- **Scaling by k**: kI = [[k, 0], [0, k]]

## Key Points

1. Every linear transformation between finite-dimensional spaces has a unique matrix representation once bases are chosen.

2. The dimension of the domain equals the number of columns; dimension of codomain equals the number of rows.

3. Standard basis problems are most common in examinations.

4. Matrix multiplication corresponds to composition of transformations.

5. The same transformation has different matrices in different bases.

6. Special geometric transformations have standard matrix forms that should be memorized.

7. To find the matrix: apply T to each basis vector of domain, express results in codomain basis, use as columns.

## Common Mistakes to Avoid

1. **Forgetting to express in correct basis**: Always express transformed vectors in terms of the codomain basis, not just using the raw vectors.

2. **Reversing order in composition**: T∘S corresponds to matrix AB (apply S first, then T), not BA.

3. **Incorrect dimension**: Matrix will be m × n where n = dim(V) and m = dim(W).

4. **Assuming standard bases**: When bases are non-standard, you must use coordinate vectors properly.

## Revision Tips

1. Practice finding matrices for T: ℝ² → ℝ² transformations until automatic.

2. Memorize standard matrices for rotation, reflection, scaling, projection, and shear.

3. Work through at least 3-4 problems involving composition of transformations.

4. Understand the geometric interpretation of common transformations.

5. Review change of basis concept and practice one example with non-standard bases.
