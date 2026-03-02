# Polynomials of Matrices - Summary

## Key Definitions and Concepts

- **Characteristic Polynomial**: For an n×n matrix A, p(λ) = det(A - λI), a polynomial of degree n whose roots are the eigenvalues of A.

- **Cayley-Hamilton Theorem**: Every square matrix A satisfies its own characteristic equation: p(A) = O (zero matrix).

- **Minimal Polynomial**: The monic polynomial of least degree m(λ) such that m(A) = O; it divides every annihilating polynomial of A.

- **Matrix Polynomial**: f(A) = aₘAᵐ + aₘ₋₁Aᵐ⁻¹ + ... + a₀I, obtained by substituting matrix A into polynomial f(x).

## Important Formulas and Theorems

- **Characteristic Equation**: p(λ) = det(A - λI) = 0
- **Cayley-Hamilton**: Aⁿ + cₙ₋₁Aⁿ⁻¹ + ... + c₁A + c₀I = O
- **Power Reduction**: Aⁿ = -cₙ₋₁Aⁿ⁻¹ - ... - c₀I (from CH Theorem)
- **Inverse Formula**: If A is invertible, A⁻¹ = -(1/c₀)(Aⁿ⁻¹ + cₙ₋₁Aⁿ⁻² + ... + c₁I)

## Key Points

- The characteristic polynomial is always of degree n for an n×n matrix.

- Cayley-Hamilton Theorem provides a powerful tool for computing matrix powers without direct multiplication.

- The minimal polynomial divides the characteristic polynomial and has the same distinct eigenvalues.

- High powers like A¹⁰⁰ can be expressed as linear combination of I, A, A², ..., Aⁿ⁻¹.

- The constant term c₀ in the characteristic polynomial equals (-1)ⁿ det(A).

- For a 2×2 matrix [[a, b], [c, d]], characteristic polynomial is λ² - (a+d)λ + (ad-bc).

## Common Mistakes to Watch

- Forgetting to subtract λI when forming (A - λI) before taking the determinant.

- Not including the identity matrix I when substituting A into polynomial terms.

- Incorrect sign while computing determinant of (A - λI), especially with larger matrices.

- Trying to compute Aⁿ directly instead of using the reduction formula from CH Theorem.

## Revision Tips

- Practice finding characteristic polynomials for 2×2 and 3×3 matrices until comfortable.

- Memorize the reduction formula: A² = (a+d)A - (ad-bc)I for 2×2 matrices.

- Always verify your answer by checking if p(A) approximately equals zero matrix.

- For exam, memorize the standard form: A² = trace(A)A - det(A)I for 2×2 matrices.
