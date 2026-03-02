# Combinations and the Binomial Theorem - Summary

## Key Definitions and Concepts

- **Combination:** Selection of objects from a set where order does not matter. Denoted as C(n, r) or nCr.
- **Binomial Theorem:** Formula for expanding (a + b)^n = Σ C(n, r)a^(n-r)b^r for r = 0 to n.
- **Pascal's Triangle:** Triangular array of binomial coefficients where each entry is the sum of two entries above it.
- **Multinomial Theorem:** Extension of binomial theorem for multiple terms: (x₁ + x₂ + ... + x_k)^n.

## Important Formulas and Theorems

- **Combination Formula:** C(n, r) = n! / (r!(n-r)!)
- **Symmetry Property:** C(n, r) = C(n, n-r)
- **Pascal's Identity:** C(n, r) + C(n, r-1) = C(n+1, r)
- **General Term:** T(r+1) = C(n, r)a^(n-r)b^r
- **Sum of Coefficients:** (1 + 1)^n = 2^n
- **Multinomial Coefficient:** n! / (n₁! n₂! ... n_k!)

## Key Points

- Combinations differ from permutations in that order is irrelevant.
- C(n, 0) = C(n, n) = 1 is always true.
- The expansion of (a + b)^n contains exactly n+1 terms.
- Pascal's Triangle provides a quick reference for binomial coefficients.
- For large n, use symmetry property to simplify calculations.
- The coefficient of any term can be found using the general term formula.
- Total number of subsets of an n-element set is 2^n, equal to sum of all C(n, r).

## Common Mistakes to Avoid

- Confusing combinations with permutations - always check if order matters.
- Forgetting to simplify factorials before multiplying large numbers.
- Incorrectly identifying the value of r when finding specific terms in binomial expansion.
- Using C(n, r) for selections with repetition (which requires different formula).

## Revision Tips

- Practice at least 5 combination problems focusing on committee formation and selection.
- Memorize the first 6-7 rows of Pascal's Triangle for quick reference during exams.
- Practice identifying the term number (r+1) correctly from the exponent pattern.
- Solve previous year university exam questions on this topic for pattern familiarity.
