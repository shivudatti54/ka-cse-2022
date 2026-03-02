# Row Space and Column Space of a Matrix - Summary

## Key Definitions and Concepts

- **Row Space R(A)**: The subspace of ℝⁿ spanned by all row vectors of matrix A; contains all linear combinations of rows.

- **Column Space C(A)**: The subspace of ℝᵐ spanned by all column vectors of matrix A; represents all possible outputs Ax where x ∈ ℝⁿ.

- **Rank r = rank(A)**: The dimension of both R(A) and C(A); equals the number of pivots in RREF.

## Important Formulas and Theorems

- **Rank inequality**: 0 ≤ rank(A) ≤ min(m, n) for an m×n matrix

- **Full rank**: rank(A) = min(m, n); square matrix has full rank if invertible

- **Rank-Nullity**: dim(null(A)) = n - rank(A) for m×n matrix

- **Transpose property**: rank(A) = rank(Aᵀ)

- **Fundamental theorem**: row rank = column rank (always true)

## Key Points

- Elementary row operations preserve rank but change the column space
- Non-zero rows in RREF form a basis for R(A)
- Pivot columns in RREF correspond to basis vectors for C(A) in the original matrix
- A system Ax = b has solutions if and only if b ∈ C(A)
- The rank indicates the number of linearly independent rows and columns
- Zero matrix has rank 0; identity matrix Iₙ has rank n

## Common Mistakes to Avoid

- Confusing the ambient spaces: R(A) ⊂ ℝⁿ while C(A) ⊂ ℝᵐ
- Taking echelon form columns as column space basis instead of original matrix columns
- Forgetting that row operations change the column space (though not its dimension)
- Incorrectly counting pivots when rows have leading zeros

## Revision Tips

1. Practice reducing matrices to RREF and identifying pivot positions
2. Remember: "Pivots in echelon form → basis for row space; pivot columns in original → basis for column space"
3. Always verify that row rank equals column rank in your calculations
4. Use rank to quickly check matrix invertibility: rank = n for n×n matrix means invertible
