# Linear Transformation - Summary

## Key Definitions and Concepts

- **Linear Transformation**: A function T: V → W between vector spaces satisfying T(u+v) = T(u)+T(v) and T(cu) = cT(v) for all vectors u,v and scalars c.

- **Kernel (Null Space)**: Ker(T) = {v ∈ V | T(v) = 0}, a subspace of V containing all vectors mapping to zero.

- **Range (Image)**: Range(T) = {w ∈ W | w = T(v) for some v ∈ V}, a subspace of W containing all output vectors.

- **Rank**: Dimension of the range of T.

- **Nullity**: Dimension of the kernel of T.

- **One-to-One (Injective)**: T is one-to-one iff Ker(T) = {0}.

- **Onto (Surjective)**: T is onto iff Range(T) = W.

- **Eigenvector**: Non-zero vector v satisfying T(v) = λv for some eigenvalue λ.

## Important Formulas and Theorems

- **Matrix Representation**: For T: ℝⁿ → ℝᵐ, T(x) = Ax where A is m×n matrix with columns as T(e₁), T(e₂), ..., T(eₙ).

- **Rank-Nullity Theorem**: dim(Ker(T)) + dim(Range(T)) = dim(V)

- **Composition**: [S∘T] = [S][T] (matrix multiplication)

- **Invertibility**: T is invertible iff one-to-one and onto; matrix A is invertible iff det(A) ≠ 0

- **Characteristic Equation**: det(A - λI) = 0 for eigenvalues

## Key Points

- Linear transformations preserve vector addition and scalar multiplication.

- The zero vector always maps to the zero vector under any linear transformation.

- A one-to-one linear transformation has kernel = {0}; nullity = 0.

- Onto transformations satisfy dim(Range) = dim(W).

- Rotation matrices in ℝ² have the form [[cos θ, -sin θ], [sin θ, cos θ]].

- Projection transformations are onto but not one-to-one.

- Eigenvalues of a rotation matrix in ℝ² are e^(iθ) and e^(-iθ) for non-zero angles.

## Common Mistakes to Avoid

- Forgetting to verify linearity before applying transformation properties.

- Confusing the order of matrix multiplication in composition (S∘T corresponds to [S][T]).

- Incorrectly computing kernel by forgetting to include the zero vector.

- Assuming a transformation is invertible without checking both one-to-one and onto conditions.

- Mixing up rank and nullity dimensions in the Rank-Nullity formula.

## Revision Tips

- Practice finding matrix representations by applying T to each standard basis vector.

- Solve at least 3-4 problems involving kernel and range computation.

- Memorize the Rank-Nullity Theorem and practice applying it in various contexts.

- Review characteristic polynomial problems to strengthen eigenvalue skills.

- Draw diagrams for transformations in ℝ² to visualize kernel and range relationships.