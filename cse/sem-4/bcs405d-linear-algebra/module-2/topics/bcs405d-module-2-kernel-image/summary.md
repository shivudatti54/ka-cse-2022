# Kernel and Image of a Linear Transformation - Summary

## Key Definitions and Concepts

- **Linear Transformation**: A mapping T: V → W preserving vector addition and scalar multiplication (T(u+v) = T(u)+T(v), T(cv) = cT(v))

- **Kernel (Null Space)**: Ker(T) = {v ∈ V : T(v) = 0} — all inputs mapped to zero output. Always a subspace of the domain.

- **Image (Range)**: Im(T) = {w ∈ W : w = T(v) for some v ∈ V} — all possible outputs. Always a subspace of the codomain.

- **Rank**: Dimension of the image, dim(Im(T))

- **Nullity**: Dimension of the kernel, dim(Ker(T))

## Important Formulas and Theorems

- **Rank-Nullity Theorem**: dim(Ker(T)) + dim(Im(T)) = dim(V)

- For matrix A (m×n): Rank(A) + Nullity(A) = n

- T is one-to-one ⇔ Ker(T) = {0} ⇔ Nullity(T) = 0

- T is onto ⇔ Im(T) = W ⇔ Rank(T) = dim(W)

- For T: ℝⁿ → ℝᵐ: Rank = n ⇒ one-to-one; Rank = m ⇒ onto

## Key Points

1. The kernel measures "information loss" — larger kernel means more vectors collapse to zero.

2. Kernel and image are always subspaces regardless of the transformation.

3. Rank cannot exceed the minimum of dimensions: Rank ≤ min(m, n) for T: ℝⁿ → ℝᵐ.

4. A one-to-one transformation preserves linear independence: if T is injective and vectors are linearly independent in V, their images are independent in W.

5. The column space of a matrix equals the image of the corresponding linear transformation.

6. Row operations do not change the null space but change the column space differently.

7. A linear transformation from ℝⁿ to ℝⁿ is invertible if and only if Ker(T) = {0} (or equivalently, Im(T) = ℝⁿ).

## Common Mistakes to Avoid

1. Confusing domain with codomain when determining if transformation is onto.

2. Forgetting that kernel always contains the zero vector.

3. Incorrectly stating that image equals codomain without verification.

4. Using the wrong dimension in Rank-Nullity Theorem (using codomain instead of domain).

5. Solving Ax = b instead of Ax = 0 when finding the kernel.

## Revision Tips

1. Practice solving homogeneous systems Ax = 0 to find kernels quickly.

2. Memorize the equivalence: one-to-one ↔ kernel = {0}.

3. Remember: rank tells you how many "independent directions" survive the transformation.

4. For exams, always verify answers using Rank-Nullity Theorem.

5. Draw the mapping diagram: domain → transformation → codomain, labeling kernel (subset of domain) and image (subset of codomain).
