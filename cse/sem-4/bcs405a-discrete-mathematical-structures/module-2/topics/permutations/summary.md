# Permutations - Summary

## Key Definitions and Concepts

- **Permutation:** An ordered arrangement of r distinct objects selected from n distinct objects, where order matters.
- **Fundamental Principle of Counting:** If task A can be done in m ways and task B can be done in n ways, then both can be done in m × n ways.
- **Derangement:** A permutation where no element appears in its original position.
- **Circular Permutation:** Arrangement of objects in a closed loop where rotations are considered identical.

## Important Formulas and Theorems

| Concept                                    | Formula                    |
| ------------------------------------------ | -------------------------- |
| Permutation of n objects taken r at a time | P(n,r) = n!/(n-r)!         |
| Permutation of all n objects               | P(n,n) = n!                |
| Permutations with repetition               | n!/(n₁! × n₂! × ... × nk!) |
| Circular permutations                      | (n-1)!                     |
| Circular permutations (necklace)           | (n-1)!/2                   |
| Derangements                               | !n = n! × Σ(-1)ᵏ/ₖ!        |

## Key Points

- Permutations differ from combinations in that order is significant in permutations.
- For P(n,r), there are r factors: n, n-1, n-2, ..., n-r+1.
- When all objects are distinct and taken all at once, the answer is simply n!.
- In permutations with repetition, divide by factorials of repeated object counts.
- For circular arrangements, fix one position and arrange remaining (n-1) objects.
- Derangements follow the recursive formula: Dₙ = (n-1)(Dₙ₋₁ + Dₙ₋₂).

## Common Mistakes to Avoid

1. **Confusing permutations with combinations:** Always ask "Does order matter?" - if yes, use permutations; if no, use combinations.

2. **Forgetting to divide by n in circular arrangements:** Students often use n! instead of (n-1)! for circular problems.

3. **Ignoring repeated objects:** When arranging letters in a word like "BOOK," failing to divide by 2! gives incorrect answers.

4. **Incorrect factorial calculations:** Remember that 0! = 1, and be careful with large factorials.

## Revision Tips

1. Practice at least 5-10 permutation problems daily to build fluency with the formulas.

2. Create a formula sheet with all permutation formulas and review it before exams.

3. Solve previous year question papers to familiarize yourself with exam patterns.

4. For circular arrangements, always visualize or draw a diagram to avoid confusion.

5. Remember: When in doubt, use the fundamental principle of counting - list out the choices for each position and multiply them.
