# Matrices and Determinants - Summary

## Key Definitions and Concepts

- **Matrix**: A rectangular array of elements arranged in rows and columns; denoted as A = [aᵢⱼ]ₘₓₙ
- **Square Matrix**: Matrix with equal rows and columns (n × n)
- **Identity Matrix (I)**: Square matrix with 1s on diagonal and 0s elsewhere
- **Determinant**: Scalar value computed from square matrix elements; det(A) or |A|
- **Singular Matrix**: Matrix with determinant = 0 (non-invertible)
- **Non-singular Matrix**: Matrix with determinant ≠ 0 (invertible)
- **Adjugate (adj(A))**: Transpose of cofactor matrix
- **Rank**: Maximum number of linearly independent rows or columns

## Important Formulas and Theorems

- **2×2 Determinant**: det([[a, b], [c, d]]) = ad - bc
- **Inverse of 2×2 Matrix**: A^(-1) = (1/det(A)) × [[d, -b], [-c, a]]
- **General Inverse**: A^(-1) = adj(A) / det(A) when det(A) ≠ 0
- **Product of Determinants**: det(AB) = det(A) × det(B)
- **Transpose Determinant**: det(A^T) = det(A)
- **Scalar Multiple**: det(kA) = k^n × det(A) for n×n matrix
- **Cofactor**: Cᵢⱼ = (-1)^(i+j) × Mᵢⱼ (Mᵢⱼ is minor)

## Key Points

- Matrix addition requires same order; multiplication requires column of A equals row of B
- Matrix multiplication is associative but not commutative
- det(A) = 0 indicates singular matrix with no inverse
- Rank ≤ min(m, n) for m×n matrix; rank equals largest non-zero minor
- System Ax = b has solution iff rank(A) = rank([A|b])
- Elementary row operations preserve determinant value (except row swapping which changes sign)
- Identity matrix acts as multiplicative identity: AI = IA = A

## Common Mistakes to Forget

1. Assuming matrix multiplication is commutative (AB ≠ BA generally)
2. Forgetting to check determinant before finding inverse
3. Confusing the sign pattern in cofactor expansion
4. Adding matrices of different orders
5. Multiplying matrices with incompatible dimensions (columns of A ≠ rows of B)

## Revision Tips

1. Practice 2×2 determinant and inverse formulas until automatic
2. Remember the cofactor sign pattern: (+ - + / - + - / + - +)
3. Use row reduction to find rank quickly
4. For 3×3 determinants, use cofactor expansion or Sarrus rule
5. Always verify inverse by multiplying A × A^(-1) = I
