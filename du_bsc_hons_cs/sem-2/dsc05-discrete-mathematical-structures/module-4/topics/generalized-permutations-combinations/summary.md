# Generalized Permutations and Combinations - Summary

## Key Definitions and Concepts

- **Multi-set:** A collection where elements may repeat; represented as {n₁·a₁, n₂·a₂, ..., nₖ·aₖ}
- **Circular Permutation:** Arrangement of objects around a circle where rotations are considered equivalent
- **Stars and Bars:** Visual method for distributing identical objects into distinct boxes using stars (*) and bars (|)
- **Derangement:** A permutation where no element remains in its original position

## Important Formulas and Theorems

| Concept | Formula |
|---------|---------|
| Permutations with repetition | n! / (r₁! × r₂! × ... × rₖ!) |
| Combinations with repetition | C(n + r - 1, r) = (n + r - 1)! / [r!(n - 1)!] |
| Circular permutations (distinct) | (n - 1)! |
| Circular permutations (necklace) | (n - 1)!/2 for n > 2 |
| Distribution (distinct to distinct, boxes can be empty) | rⁿ |
| Distribution (distinct to distinct, no box empty) | r! × S(n, r) |
| Distribution (identical to distinct, no box empty) | C(n - 1, r - 1) |
| Derangements | D(n) = n! × Σ(-1)ᵏ/k! |

## Key Points

- For permutations, order matters; for combinations, order doesn't matter
- When identical objects are involved, divide by the factorial of each repetition count
- Stars and bars: distributing r identical items into n distinct boxes = C(n + r - 1, r)
- Circular arrangements reduce dimension by 1: (n - 1)! instead of n!
- Inclusion-exclusion is essential for "at least" and "none" type restrictions
- S(n, r) represents Stirling numbers of the second kind (partitions of n into r non-empty subsets)

## Common Mistakes to Avoid

1. **Confusing when to divide by factorials:** Only divide when objects are identical/permuting a multi-set
2. **Forgetting circular permutations reduce by 1:** Using n! instead of (n - 1)! is a common error
3. **Not distinguishing box types:** Using wrong formulas when boxes are identical vs. distinct
4. **Incorrect stars and bars placement:** Placing too many or too few bars; remember n boxes require n - 1 bars

## Revision Tips

1. Practice 3-4 problems from each category (multi-set permutations, combinations with repetition, circular arrangements, distributions)

2. Create a decision tree: Identify if objects are distinct/identical, boxes are distinct/identical, and if empty boxes are allowed

3. Remember: For combinations with replacement, think of it as finding non-negative integer solutions to x₁ + x₂ + ... + xₙ = r

4. Derangements can be quickly computed using the recurrence D(n) = (n - 1)[D(n-1) + D(n-2)] with D(0) = 1, D(1) = 0