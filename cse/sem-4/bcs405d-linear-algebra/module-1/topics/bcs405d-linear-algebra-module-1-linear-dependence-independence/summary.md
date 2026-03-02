# Linear Dependence and Independence - Summary

## Key Definitions and Concepts

- **Linear Combination**: An expression c₁v₁ + c₂v₂ + ... + cₙvₙ where cᵢ are scalars.
- **Linear Dependence**: A set {v₁, v₂, ..., vₙ} is linearly dependent if there exist scalars c₁, c₂, ..., cₙ, not all zero, such that c₁v₁ + c₂v₂ + ... + cₙvₙ = 0.
- **Linear Independence**: A set is linearly independent if the only solution to c₁v₁ + c₂v₂ + ... + cₙvₙ = 0 is c₁ = c₂ = ... = cₙ = 0 (trivial solution).
- **Basis**: A set that is both linearly independent and spans the vector space.

## Important Formulas and Theorems

- **Two-vector test**: {v₁, v₂} is dependent ⇔ v₁ = k·v₂ for some scalar k
- **Dimension rule**: In ℝⁿ, any set of more than n vectors is linearly dependent
- **Zero vector rule**: Any set containing the zero vector is linearly dependent
- **Matrix rank test**: Form matrix with vectors as columns/rows, reduce to echelon form. Number of pivots = number of independent vectors.

## Key Points

1. Linear dependence means at least one vector can be written as a linear combination of others; linear independence means each vector adds unique directional information.

2. The trivial solution (all coefficients zero) always satisfies the zero equation for any set of vectors.

3. Two vectors in ℝ² are dependent if they lie on the same line through the origin.

4. For n vectors in ℝⁿ, they are independent if and only if the determinant of the n×n matrix is non-zero.

5. The maximum number of linearly independent vectors in ℝⁿ is n (equals the dimension).

6. Row reduction to echelon form is the most reliable method for testing independence of multiple vectors.

7. If vectors are dependent, there exist infinitely many non-trivial dependence relationships.

## Common Mistakes to Avoid

1. **Forgetting "not all zero"**: Students often confuse dependence with the trivial equation - the definition requires non-zero coefficients.

2. **Assuming dependent means one is multiple**: This is only true for exactly two vectors. With three or more, dependencies can be more complex.

3. **Ignoring the zero vector**: Any set containing the zero vector is automatically dependent - don't spend time testing it.

4. **Wrong matrix orientation**: Ensure consistency - use columns for column vectors and perform row operations (or vice versa).

## Revision Tips

1. Practice at least 5 problems from each method: definition test, matrix method, and determinant test.

2. Memorize the key theorems and apply the dimension rule for quick elimination in MCQs.

3. For exam problems, always start by checking if any vector is the zero vector or if there are more vectors than the dimension.

4. When finding dependence relationships, set up the homogeneous system and use the null space approach.
