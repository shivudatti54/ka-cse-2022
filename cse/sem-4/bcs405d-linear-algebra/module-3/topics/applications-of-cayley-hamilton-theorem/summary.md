# Applications of Cayley-Hamilton Theorem - Summary

## Key Definitions and Concepts

- **Cayley-Hamilton Theorem**: Every square matrix A satisfies its own characteristic equation p(A) = 0, where p(λ) = det(λI - A)

- **Characteristic Polynomial**: For an n×n matrix A, p(λ) = det(λI - A) is a polynomial of degree n

- **Minimal Polynomial**: The monic polynomial of least degree m(λ) such that m(A) = 0; always divides the characteristic polynomial

## Important Formulas and Theorems

- **For 2×2 matrix A = [[a,b],[c,d]]**: p(λ) = λ² - tr(A)λ + det(A), where tr(A) = a+d

- **Inverse formula (2×2)**: A⁻¹ = (1/det(A))[tr(A)I - A]

- **General power reduction**: Aⁿ = -[cₙ₋₁Aⁿ⁻¹ + ... + c₁I] for characteristic polynomial p(λ) = λⁿ + cₙ₋₁λⁿ⁻¹ + ... + c₀

## Key Points

- The Cayley-Hamilton Theorem provides an efficient method to compute matrix powers without repeated multiplication

- Any power of A can be expressed as a linear combination of I, A, A², ..., Aⁿ⁻¹

- The theorem offers an alternative method to find matrix inverses, especially useful when direct methods are cumbersome

- The minimal polynomial divides the characteristic polynomial (Cayley-Hamilton guarantees characteristic polynomial annihilates A)

- For 2×2 matrices, the inverse formula A⁻¹ = (1/det(A))[tr(A)I - A] is the quickest approach

- The theorem is particularly valuable in solving systems of linear differential equations

## Common Mistakes to Forget

- Forgetting to include the identity matrix I when rearranging terms from p(A) = 0

- Computing determinant of (λI - A) incorrectly—remember to subtract the matrix, not add

- Not verifying that det(A) ≠ 0 before attempting to find inverse

- Confusing the characteristic polynomial with minimal polynomial—they are related but different

## Revision Tips

1. Practice computing characteristic polynomials for 2×2 and 3×3 matrices until comfortable

2. Memorize the 2×2 inverse formula: it's the most frequently tested concept

3. Always express higher powers in terms of I, A, A², ... systematically

4. Verify answers by direct multiplication when time permits
