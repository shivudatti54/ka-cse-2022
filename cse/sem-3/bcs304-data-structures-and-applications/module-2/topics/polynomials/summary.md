# Polynomials - Summary

## Key Definitions

- **Polynomial**: A mathematical expression of the form P(x) = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₁x + a₀ where aₙ ≠ 0 and n is the degree.
- **Dense Polynomial**: A polynomial with non-zero coefficients for most exponent values within its range.
- **Sparse Polynomial**: A polynomial with few non-zero coefficients relative to its degree.
- **Term**: A single component of a polynomial consisting of a coefficient and an exponent.
- **Like Terms**: Terms in a polynomial that have the same exponent.

## Important Formulas

- **Polynomial Evaluation (Horner's Rule)**: P(x) = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₀ can be evaluated as (((aₙx + aₙ₋₁)x + aₙ₋₂)x + ... + a₀)
- **Degree of Polynomial Sum**: deg(P + Q) ≤ max(deg(P), deg(Q))
- **Degree of Polynomial Product**: deg(P × Q) = deg(P) + deg(Q)

## Key Points

1. Polynomials can be represented using arrays (sequential storage) or linked lists (linked storage), each with distinct advantages.

2. Array representation provides O(1) access to any coefficient but wastes space for sparse polynomials with many zero coefficients.

3. Linked list representation stores only non-zero terms, making it space-efficient for sparse polynomials and allowing dynamic growth.

4. In linked list representation, nodes are typically maintained in descending order of exponents to simplify operations.

5. Polynomial addition using linked lists has time complexity O(m + n) where m and n are the number of non-zero terms.

6. Polynomial multiplication is more complex than addition, requiring multiplication of all term pairs and then combining like terms.

7. Horner's rule enables efficient polynomial evaluation in O(n) time using the array representation.

8. The choice between representations depends on the density of the polynomial and the operations to be performed.

## Common Mistakes

1. **Confusing sparse and dense representations**: Using array representation for highly sparse polynomials leads to unnecessary memory allocation.

2. **Incorrect handling of like terms**: Forgetting to combine terms with the same exponent during addition or after multiplication.

3. **Ignoring the order of terms**: Not maintaining the descending order of exponents in linked list representation can complicate operations.

4. **Forgetting edge cases**: Not handling polynomials of different degrees, zero polynomials, or negative coefficients properly.
5. **Space allocation errors**: In array representation, allocating space for degree n when the actual storage needed is degree n+1 (for coefficients from 0 to n).