# Rank-Nullity Theorem - Summary

## Key Definitions and Concepts

- **Linear Transformation T: V → W**: A mapping between vector spaces satisfying additivity and homogeneity properties.

- **Kernel (Null Space) Ker(T)**: The set {v ∈ V : T(v) = 0}, a subspace of V. Its dimension is called **nullity**.

- **Image (Column Space) Im(T)**: The set {T(v) ∈ W : v ∈ V}, a subspace of W. Its dimension is called **rank**.

- **Rank of a matrix**: The number of linearly independent columns (or rows), equal to the dimension of the column space and row space.

- **Nullity of a matrix**: The dimension of the solution space to Ax = 0, equal to the number of free variables.

## Important Formulas and Theorems

- **Rank-Nullity Theorem**: For T: V → W with V finite-dimensional: **dim(V) = rank(T) + nullity(T)**

- **Matrix form**: For an m×n matrix A: **n = rank(A) + nullity(A)**

- **Fundamental Theorem dimensions**:
  - Col(A): dimension = rank(A) in ℝ^m
  - Null(A): dimension = n - rank(A) in ℝ^n
  - Row(A): dimension = rank(A) in ℝ^n
  - Null(A^T): dimension = m - rank(A) in ℝ^m

- **Injectivity condition**: T is one-to-one ⇔ nullity(T) = 0 ⇔ Ker(T) = {0}

- **Surjectivity condition**: T is onto ⇔ rank(T) = dim(W)

## Key Points

- The Rank-Nullity Theorem states that the dimension of the domain equals the sum of the rank and nullity of the transformation.

- Rank measures how much of the output space is "covered," while nullity measures how much information is "lost" (collapses to zero).

- For a homogeneous system Ax = 0 with n variables and rank r, the solution space has dimension n - r (nullity).

- A linear transformation is an isomorphism if and only if it is both one-to-one and onto, requiring full rank equal to the domain dimension.

- The rank of a matrix equals the number of pivots in its row echelon form, and also equals rank(A^T).

- For consistent systems Ax = b, the number of free variables equals nullity(A).

## Common Mistakes to Avoid

- Confusing the domain dimension with codomain dimension in the formula—always remember dim(V) = rank + nullity, where V is the domain.

- Forgetting that rank(A) = rank(A^T); the row space and column space always have the same dimension.

- Incorrectly determining pivot positions; always complete row reduction to RREF for accurate rank calculation.

- Applying the theorem to infinite-dimensional spaces without proper justification—the theorem requires finite-dimensional vector spaces.

## Revision Tips

1. Practice finding RREF of various matrices and counting pivots to quickly determine rank.

2. Remember: nullity = number of variables - rank for homogeneous systems; use this to immediately find solution space dimension.

3. For exam problems, identify matrix dimensions first, find rank via row operations, then apply Rank-Nullity to find the unknown quantity.

4. Visualize the transformation: rank shows "output dimensionality" while nullity shows "collapsed dimensions."
