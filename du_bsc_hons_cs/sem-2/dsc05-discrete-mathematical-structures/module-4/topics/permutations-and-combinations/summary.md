# Permutations and Combinations - Summary

## Key Definitions and Concepts

- **Permutation:** An arrangement of objects where the order matters. Denoted as P(n,r) or nPr.
- **Combination:** A selection of objects where the order does not matter. Denoted as C(n,r) or nCr.
- **Factorial:** n! = n × (n-1) × ... × 2 × 1, with 0! = 1.
- **Fundamental Principle of Counting:** If task A can be done in m ways and task B in n ways, both can be done in m × n ways.

## Important Formulas and Theorems

- **Permutation Formula:** P(n,r) = n!/(n-r)!
- **Combination Formula:** C(n,r) = n!/(r!(n-r)!)
- **Circular Permutations:** (n-1)! for distinct objects
- **Permutations with Repetition:** n!/(n₁!n₂!...nk!)
- **Pascal's Identity:** C(n,r) + C(n,r-1) = C(n+1,r)
- **Symmetry Property:** C(n,r) = C(n,n-r)
- **Binomial Theorem:** (a+b)^n = Σ C(n,r)a^(n-r)b^r

## Key Points

- Order matters → Permutation; Order doesn't matter → Combination
- P(n,n) = n! gives arrangements of all n objects
- C(n,0) = C(n,n) = 1
- Sum of all binomial coefficients: C(n,0) + C(n,1) + ... + C(n,n) = 2^n
- For circular arrangements, fix one position to eliminate rotational symmetry
- When restrictions exist (items must be together), treat them as a single unit first

## Common Mistakes to Avoid

- Confusing permutations with combinations and applying wrong formulas
- Forgetting to multiply by internal arrangements when treating groups as units
- Not simplifying factorial expressions before calculating
- Overcounting in selection problems with overlapping conditions
- Incorrectly applying the division principle in circular permutations

## Revision Tips

1. Practice identifying whether problems require permutation or combination by asking "Does order matter?"
2. Memorize the relationship between permutations and combinations: P(n,r) = C(n,r) × r!
3. Use Pascal's triangle for quick binomial coefficient verification during exams
4. Solve at least 10 mixed problems covering all scenarios before the exam
5. Remember: when in doubt, think about whether swapping two elements creates a new arrangement