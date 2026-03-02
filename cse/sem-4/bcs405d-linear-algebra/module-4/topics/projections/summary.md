# Projections - Summary

## Key Definitions and Concepts

- **Projection**: A linear transformation P such that P² = P, mapping vectors onto a subspace
- **Orthogonal Projection**: Projection where the error vector is orthogonal to the subspace
- **Projection onto Line**: proj_u(x) = (x·u/u·u)u
- **Projection Matrix**: P = A(A^T A)⁻¹A^T for projecting onto Col(A)
- **Least Squares**: Solution minimizing ||b - Ax||² via normal equations A^T Ax = A^T b

## Important Formulas and Theorems

- **Scalar Projection**: comp_u(x) = x·u/||u||
- **Vector Projection**: proj_u(x) = (x·u/u·u)u
- **Projection Matrix**: P = A(A^T A)⁻¹A^T
- **Normal Equations**: A^T A x = A^T b
- **Decomposition**: x = proj_W(x) + perp_W(x), where perp_W(x) ∈ W⊥

## Key Points

- Projection matrices are idempotent (P² = P) and symmetric (P^T = P) for orthogonal projections
- The dimension of the subspace equals rank(P) = trace(P)
- Orthogonal projection minimizes the distance between vector and subspace
- Least squares solution is the projection of b onto column space of A
- Error vector is always orthogonal to the subspace in orthogonal projections
- Gram-Schmidt uses projections to create orthogonal/orthonormal sets
- For unit vector u, proj_u(x) = (x·u)u

## Common Mistakes to Avoid

- Forgetting to check linear independence of columns before using projection matrix formula
- Confusing orthogonal projection with oblique projection in calculations
- Not verifying idempotent property P² = P when checking answers
- Using wrong formula for projection when vector u is not a unit vector

## Revision Tips

- Practice computing projections by hand for 2D and 3D cases
- Memorize the projection matrix formula and its properties
- Understand geometric interpretation: projection = "closest point" on subspace
- Solve at least 3-4 least squares problems using normal equations
- Verify projection matrix answers by checking P² = P
