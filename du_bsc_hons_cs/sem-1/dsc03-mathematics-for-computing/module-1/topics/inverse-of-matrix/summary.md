# Inverse of a Matrix - Summary

## Key Definitions and Concepts
- **Matrix Inverse**: A square matrix A is invertible if there exists A⁻¹ such that AA⁻¹ = A⁻¹A = I
- **Non-singular Matrix**: A matrix with non-zero determinant (det(A) ≠ 0); invertible
- **Singular Matrix**: A matrix with zero determinant; not invertible
- **Adjugate Matrix**: The transpose of the cofactor matrix; adj(A) = Cᵀ
- **Gauss-Jordan Method**: Transform [A|I] → [I|A⁻¹] using elementary row operations

## Important Formulas and Theorems
- **2×2 Inverse**: For A = [a b; c d], A⁻¹ = (1/det(A))[d -b; -c a] where det(A) = ad - bc
- **General Formula**: A⁻¹ = (1/det(A)) × adj(A)
- **Product Inverse**: (AB)⁻¹ = B⁻¹A⁻¹ (order reversed!)
- **Determinant of Inverse**: det(A⁻¹) = 1/det(A)
- **Transpose Inverse**: (Aᵀ)⁻¹ = (A⁻¹)ᵀ
- **System Solution**: If Ax = b, then x = A⁻¹b (when A is invertible)

## Key Points
- A matrix is invertible if and only if its determinant is non-zero
- For 2×2 matrices, use the direct formula; for larger, use Gauss-Jordan
- Always verify AA⁻¹ = I after computing the inverse
- The inverse of an inverse returns the original: (A⁻¹)⁻¹ = A
- A full-rank matrix (rank = n) is always invertible
- Inverse provides unique solution to linear systems: x = A⁻¹b

## Common Mistakes to Avoid
- Forgetting to reverse order when finding inverse of product: (AB)⁻¹ ≠ A⁻¹B⁻¹
- Not checking determinant before attempting inverse computation
- Arithmetic errors in Gauss-Jordan elimination steps
- Confusing the adjugate (transpose of cofactor) with cofactor matrix itself
- Forgetting to divide by determinant in the 2×2 formula

## Revision Tips
- Practice 2×2 inverses until you can do them in under 30 seconds
- Memorize the Gauss-Jordan procedure step-by-step
- Always verify your computed inverse by multiplication
- Understand the connection: det ≠ 0 ⟺ rank = n ⟺ invertible
- Review previous years' DU exam questions on this topic