# QR Factorization - Summary

## Key Definitions and Concepts

- **QR Factorization**: Decomposition of matrix A (m×n with linearly independent columns) as A = QR, where Q is orthogonal (Q^T Q = I) and R is upper triangular
- **Orthogonal Matrix**: A square matrix Q where Q^T = Q^(-1), meaning columns are orthonormal vectors
- **Upper Triangular Matrix**: Matrix R where all elements below the main diagonal are zero (rᵢⱼ = 0 for i > j)

## Important Formulas and Theorems

- **Gram-Schmidt**: Given a₁, a₂, ..., aₙ (linearly independent), compute u₁ = a₁, u₂ = a₂ - (q₁ᵀa₂)q₁, etc., then normalize to get q vectors
- **QR relationship**: rᵢⱼ = qᵢᵀaⱼ for i ≤ j, and rᵢⱼ = 0 for i > j
- **Least squares via QR**: For Ax ≈ b, solve Rx = Q^T b after computing QR = A
- **Householder transformation**: H = I - 2uu^T where u is normalized vector

## Key Points

- QR factorization exists for any matrix with linearly independent columns (m ≥ n)
- The columns of Q form an orthonormal basis for the column space of A
- R is always non-singular when A has linearly independent columns (positive diagonal elements)
- Modified Gram-Schmidt is numerically more stable than classical Gram-Schmidt
- QR factorization via Householder reflections is preferred in numerical computation
- For square matrices (n×n), Q is also n×n and R is n×n upper triangular

## Common Mistakes to Avoid

- Confusing dimensions: Remember Q is m×m, R is m×n for A(m×n)
- Forgetting to normalize vectors in Gram-Schmidt process
- Computing R incorrectly—only compute rᵢⱼ = qᵢᵀaⱼ for i ≤ j
- Not verifying that Q^T Q = I in the final answer

## Revision Tips

- Practice 3-4 problems computing QR factorization using Gram-Schmidt
- Always verify QR = A after computation
- Memorize the relationship between R's diagonal elements and norms of u-vectors
- Understand why QR factorization is preferred over direct methods for least squares
- Review the connection between QR factorization and finding orthonormal bases
