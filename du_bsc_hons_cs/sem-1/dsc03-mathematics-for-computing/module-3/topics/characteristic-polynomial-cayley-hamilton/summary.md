# Characteristic Polynomial and Cayley-Hamilton Theorem - Summary

## Key Definitions and Concepts

- **Characteristic Polynomial**: For an n×n matrix A, p(λ) = det(A - λI), where λ is a scalar and I is the identity matrix.

- **Eigenvalues**: Roots of the characteristic polynomial, satisfying Av = λv for non-zero eigenvector v.

- **Cayley-Hamilton Theorem**: Every square matrix satisfies its own characteristic equation—substituting the matrix A for λ in p(λ) yields the zero matrix.

## Important Formulas and Theorems

- **2×2 Matrix**: For A = [[a, b], [c, d]], p(λ) = λ² - (a+d)λ + (ad-bc)

- **CH Theorem**: If p(λ) = λⁿ + c_{n-1}λ^{n-1} + ... + c₀, then p(A) = Aⁿ + c_{n-1}A^{n-1} + ... + c₀I = O

- **Trace-Determinant Relation**: For characteristic polynomial λⁿ + c_{n-1}λ^{n-1} + ... + c₀, we have c_{n-1} = -tr(A) and c₀ = (-1)ⁿ det(A)

- **Matrix Inverse via CH**: A⁻¹ = -(1/det(A))(c₁I + c₂A + ... + c_{n-1}A^{n-2} + (-1)ⁿA^{n-1}) for invertible A

## Key Points

- The characteristic polynomial is always monic (leading coefficient 1 when expressed as λⁿ + ...)

- The eigenvalues determine whether a matrix is diagonalizable and the stability of systems

- Cayley-Hamilton allows reducing any power Aᵏ to linear combination of A, A², ..., Aⁿ⁻¹ and I

- Complex eigenvalues in real matrices always occur in conjugate pairs

- The theorem provides an alternative method for computing matrix inverses without using row operations

- Higher powers of matrices can be computed efficiently using the recurrence relation from the characteristic equation

## Common Mistakes to Remember

1. Forgetting to subtract λI from A when forming the characteristic polynomial

2. Confusing the trace (sum of diagonal elements) with the determinant

3. Not including the identity matrix I when substituting A into the characteristic polynomial

4. Sign errors when expanding determinants, especially for 3×3 matrices

5. Forgetting that the characteristic polynomial has degree equal to the matrix order

## Revision Tips

1. Practice finding characteristic polynomials for at least 5 different 2×2 matrices

2. Memorize the verification steps: find p(λ), compute p(A), show result is zero matrix

3. Create a formula sheet with the 2×2 and 3×3 characteristic polynomial forms

4. Solve at least one problem computing A⁴ or higher using Cayley-Hamilton

5. Understand the connection: eigenvalues → characteristic polynomial → Cayley-Hamilton applications