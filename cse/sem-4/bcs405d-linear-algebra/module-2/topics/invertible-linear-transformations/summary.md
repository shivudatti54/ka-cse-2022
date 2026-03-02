# Invertible Linear Transformations - Summary

## Key Definitions and Concepts

- **Invertible Linear Transformation**: A linear transformation T: V → W is invertible if there exists S: W → V such that ST = I_V and TS = I_W. The inverse is denoted T⁻¹.

- **Bijective**: A transformation is invertible if and only if it is both one-to-one (injective) and onto (surjective).

- **One-to-One**: T(u) = T(v) implies u = v; equivalently, ker(T) = {0}.

- **Onto**: For every w ∈ W, there exists v ∈ V such that T(v) = w.

## Important Formulas and Theorems

- **Matrix Invertibility Condition**: T(x) = Ax is invertible ⇔ A is invertible ⇔ det(A) ≠ 0 ⇔ rank(A) = n (for n×n matrix)

- **Inverse Transformation**: If T(x) = Ax, then T⁻¹(y) = A⁻¹y

- **Composition of Inverses**: (ST)⁻¹ = T⁻¹S⁻¹

- **Rank-Nullity**: dim(V) = rank(T) + nullity(T); for invertible T: nullity = 0, rank = dim(V)

## Key Points

1. An invertible linear transformation must map between vector spaces of equal dimension.

2. The determinant test (det(A) ≠ 0) is the quickest way to check invertibility for matrix representations.

3. The inverse of a linear transformation is always linear.

4. Kernel of an invertible transformation contains only the zero vector.

5. For T: ℝⁿ → ℝⁿ, being one-to-one is equivalent to being onto (and hence invertible).

6. The inverse transformation "undoes" what the original transformation does.

7. If T is invertible, then (T⁻¹)⁻¹ = T.

## Common Mistakes to Assume

- Forgetting that invertibility requires square matrices (m = n for matrix representation)

- Confusing the order when inverting products: (ST)⁻¹ ≠ S⁻¹T⁻¹

- Assuming a transformation is invertible without checking det(A) ≠ 0

- Confusing one-to-one with onto—they are both required for invertibility

## Revision Tips

1. Practice finding inverses by computing A⁻¹ from the standard matrix of T.

2. Memorize the equivalence: T invertible ⇔ det(A) ≠ 0 ⇔ rank(A) = n ⇔ ker(T) = {0}.

3. Always verify your inverse by composing with the original transformation.

4. Remember that for ℝⁿ → ℝⁿ transformations, one-to-one implies onto (and vice versa).
