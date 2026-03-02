# Boolean Algebra - Summary

## Key Definitions and Concepts

- **Boolean Algebra**: An algebraic system with two binary operations (AND denoted by ·, OR denoted by +) and one unary operation (NOT denoted by ' or overline) defined over the set B = {0, 1}

- **Boolean Function**: A mapping from binary input variables to a binary output, represented as F: {0,1}^n → {0,1}

- **Minterm**: A product term containing all n variables or their complements; true for exactly one input combination

- **Maxterm**: A sum term containing all n variables or their complements; false for exactly one input combination

- **Universal Gates**: NAND and NOR gates capable of implementing any Boolean function alone

## Important Formulas and Theorems

| Theorem | Formula |
|---------|---------|
| Identity Laws | 0 + A = A, 1 · A = A |
| Null Laws | 1 + A = 1, 0 · A = 0 |
| Idempotent Laws | A + A = A, A · A = A |
| Complement Laws | A + A' = 1, A · A' = 0 |
| De Morgan's | (A + B)' = A' · B', (A · B)' = A' + B' |
| Consensus | AB + A'C + BC = AB + A'C |
| Absorption | A + A·B = A, A·(A + B) = A |

## Key Points

- Boolean algebra operates on binary values: 0 represents false, 1 represents true
- AND (·) has higher precedence than OR (+) in Boolean expressions
- K-Maps simplify Boolean functions by grouping adjacent 1s (for SOP) or 0s (for POS)
- Groups in K-Map must be powers of 2: 1, 2, 4, 8, 16 cells
- Gray code ordering ensures only one variable changes between adjacent cells
- NAND and NOR are universal gates - any Boolean function can be implemented using only one type
- Don't care conditions (X) can be grouped with 1s or 0s to create larger groups
- The dual of a Boolean expression is obtained by swapping + with · and 0 with 1

## Common Mistakes to Avoid

- Confusing AND (·) with OR (+) operations in simplification
- Not complementing all variables when writing minterms or maxterms
- Forming groups that are not powers of 2 in K-Maps
- Missing edge-wrapping groups in K-Maps (top-bottom, left-right edges wrap)
- Incorrectly applying De Morgan's Theorem (forgetting to complement each term)
- Not using don't care conditions when available for larger groupings

## Revision Tips

1. Practice writing truth tables for various Boolean functions until automatic
2. Draw 3-variable and 4-variable K-Maps repeatedly to build speed
3. Memorize the NAND and NOR gate conversion identities
4. Solve at least 5 Boolean simplification problems daily before exams
5. Focus on understanding why theorems work, not just memorizing them