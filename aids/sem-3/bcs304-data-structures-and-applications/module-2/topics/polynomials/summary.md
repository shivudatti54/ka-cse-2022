# Polynomials - Summary

## Key Definitions

- **Polynomial**: A mathematical expression P(x) = a₀ + a₁x + a₂x² + ... + aₙxⁿ where coefficients are constants and n is the degree.
- **Dense Polynomial**: A polynomial where most exponent values have non-zero coefficients.
- **Sparse Polynomial**: A polynomial with relatively few non-zero terms compared to its degree.
- **Degree of Polynomial**: The highest exponent with a non-zero coefficient.
- **Horner's Rule**: An efficient evaluation method P(x) = a₀ + x(a₁ + x(a₂ + ... + x(aₙ)...)).

## Important Formulas

- **Polynomial Addition**: For same exponent terms: new_coef = coef₁ + coef₂
- **Polynomial Multiplication**: Degree of product = degree(P) + degree(Q)
- **Horner's Rule Evaluation**: result = (((aₙ × x + aₙ₋₁) × x + aₙ₋₂) × x + ... + a₀)
- **Array Memory**: O(n) where n is the degree
- **Linked List Memory**: O(k) where k is number of non-zero terms

## Key Points

1. Array representation suits dense polynomials; linked lists suit sparse polynomials.
2. Linked list representation stores only non-zero terms, saving memory when k << n.
3. Polynomial addition using linked lists has time complexity O(m + n).
4. Horner's Rule reduces evaluation from O(n²) to O(n) time complexity.
5. Polynomial multiplication of degrees m and n yields degree m+n.
6. Each node in linked representation contains: coefficient, exponent, and next pointer.
7. Polynomial subtraction is performed by negating coefficients before addition.
8. Combining like terms after multiplication is essential for correct results.

## Common Mistakes

1. **Forgetting to combine like terms** after multiplication, resulting in incorrect results.
2. **Not handling zero coefficients** when creating new terms in linked list representation.
3. **Incorrect pointer manipulation** in linked list operations leading to memory leaks.
4. **Using array index as exponent** without considering the actual degree of the polynomial.
5. **Not handling the zero polynomial** (polynomial with no terms or all zero coefficients) as a special case.
