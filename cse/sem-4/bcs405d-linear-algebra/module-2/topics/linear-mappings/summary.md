# Linear Mappings - Summary

## Key Definitions and Concepts

- **Linear Transformation**: A function T: V → W between vector spaces is linear if T(u + v) = T(u) + T(v) and T(cu) = cT(u) for all u, v ∈ V and scalars c.
- **Kernel (Null Space)**: Ker(T) = {v ∈ V : T(v) = 0}, a subspace of V
- **Range (Image)**: Range(T) = {T(v) : v ∈ V}, a subspace of W
- **One-to-one**: T is injective if T(u) = T(v) implies u = v (equivalently, Ker(T) = {0})
- **Onto**: T is surjective if Range(T) = W

## Important Formulas and Theorems

- **Rank-Nullity Theorem**: dim(Ker(T)) + dim(Range(T)) = dim(V) for V finite-dimensional
- **Matrix Representation**: For standard bases, apply T to each basis vector and use coordinates as columns
- **Composition**: Matrix of S ∘ T equals product of matrices: [S][T]

## Key Points

- A necessary condition for linearity is T(0) = 0; if this fails, the transformation is not linear
- The kernel represents "information lost" during transformation; range represents the "output space"
- Zero transformation and identity transformation are always linear
- Standard linear transformations in R² include rotation, scaling, reflection, projection, and shear
- One-to-one transformations have trivial kernel; onto transformations have range equal to codomain

## Common Mistakes to Avoid

- Forgetting to verify both additivity and homogeneity when proving linearity
- Confusing kernel (domain) with range (codomain)
- Assuming a transformation is linear without checking T(0) = 0
- Miscounting dimensions when applying Rank-Nullity Theorem

## Revision Tips

1. Practice verifying linearity with at least 5 different transformations, including non-linear ones
2. Memorize the Rank-Nullity Theorem and practice computing kernel and range dimensions
3. Review matrix representation by working through examples with different bases
4. Create a table of common linear transformations in R² with their matrices
