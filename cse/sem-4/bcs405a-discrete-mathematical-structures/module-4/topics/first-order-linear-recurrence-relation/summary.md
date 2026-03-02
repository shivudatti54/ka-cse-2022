# First Order Linear Recurrence Relation - Summary

## Key Definitions and Concepts

- **Recurrence Relation**: An equation defining a sequence where each term is expressed in terms of preceding terms.
- **First Order Linear Recurrence**: The form aₙ = c × aₙ₋₁ + d, where each term depends only on the immediately preceding term.
- **Homogeneous Relation**: When d = 0, giving aₙ = c × aₙ₋₁
- **Non-Homogeneous Relation**: When d ≠ 0, giving aₙ = c × aₙ₋₁ + d

## Important Formulas and Theorems

**For aₙ = caₙ₋₁ + d with a₀ = a:**

When c ≠ 1:

- **aₙ = a × cⁿ + d(cⁿ - 1)/(c - 1)**

When c = 1:

- **aₙ = a + nd** (Arithmetic Progression)

**With initial condition a₁:**

- aₙ = a₁cⁿ⁻¹ + d(cⁿ⁻¹ - 1)/(c - 1) for c ≠ 1

**Homogeneous case (d = 0):**

- **aₙ = a₀ × cⁿ**

## Key Points

1. The coefficient c determines the growth/decay behavior - c > 1 means growth, 0 < c < 1 means decay, c < 0 means alternating signs.

2. For c = 1, the sequence follows arithmetic progression with common difference d.

3. The particular solution for constant non-homogeneous term d is P = d/(1-c) when c ≠ 1.

4. Always verify solutions by substituting back into the original recurrence.

5. Initial conditions (a₀ or a₁) are essential to determine the unique sequence.

6. The iteration method works by repeatedly substituting and observing patterns.

7. First-order recurrences are fundamental to understanding higher-order recurrence relations.

## Common Mistakes to Avoid

1. Forgetting to use (cⁿ - 1) instead of cⁿ when solving non-homogeneous cases.

2. Using the wrong formula when c = 1 - this is a frequent examination error.

3. Confusing a₀ and a₁ initial conditions - check whether sequence starts from n=0 or n=1.

4. Not simplifying the final answer - always factor and simplify expressions.

## Revision Tips

1. Practice writing out 3-4 terms manually before applying formulas to understand the pattern.

2. Memorize both formulas (c ≠ 1 and c = 1 cases) and be able to derive them.

3. Solve at least 5 problems covering all cases: homogeneous, non-homogeneous, and c = 1.

4. Focus on word problems involving compound interest and population models as these appear frequently in exams.
