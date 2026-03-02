# Counting Principles, Permutations, and Combinations - Summary

## Key Definitions and Concepts

- **Product Rule**: If task 1 has m ways and task 2 has n ways (independently), then both can be performed in m × n ways.

- **Addition Rule**: If tasks are mutually exclusive (cannot occur together), and task 1 has m ways and task 2 has n ways, then either can be performed in m + n ways.

- **Permutation**: Ordered arrangement of distinct objects where order matters. P(n,r) = n!/(n-r)!.

- **Combination**: Selection of objects where order does NOT matter. C(n,r) = n!/(r!(n-r)!) = binomial coefficient "n choose r".

- **Pigeonhole Principle**: If n items are placed into m containers and n > m, then some container has ≥2 items. Generalized: at least ⌈n/m⌉ items in one container.

- **Inclusion-Exclusion**: For two sets A, B: |A ∪ B| = |A| + |B| - |A ∩ B|.

## Important Formulas and Theorems

| Concept | Formula |
|---------|---------|
| Permutation (no repetition) | P(n,r) = n!/(n-r)! |
| Permutation (with repetition) | n!/(n₁!n₂!...nₖ!) |
| Combination (no repetition) | C(n,r) = n!/(r!(n-r)!) |
| Combination (with repetition) | C(n+r-1, r) |
| Circular permutation | (n-1)! |
| Binomial coefficient | C(n,r) = C(n, n-r) |

## Key Points

- Order matters → Permutations; Order doesn't matter → Combinations
- Repetition allowed multiplies choices; No repetition reduces available choices
- For circular arrangements, fix one position to eliminate rotational symmetry
- Pigeonhole principle proves existence, not quantity (except bounds)
- Inclusion-exclusion adds sizes, subtracts intersections, adds triple intersections
- "At least" problems often split into cases; complementary counting: total - none
- The identity P(n,r) = C(n,r) × r! connects permutations and combinations
- C(n,0) = C(n,n) = 1; C(n,1) = C(n,n-1) = n

## Common Mistakes to Avoid

1. **Confusing permutations with combinations**: Using combinations when order matters, or vice versa. Always ask: "Does the order of selection matter?"

2. **Forgetting to account for repetition**: Not checking whether elements can be repeated changes the entire approach.

3. **Overcounting in multi-step problems**: Not recognizing that sequential choices may create dependent situations.

4. **Ignoring circular symmetry**: Using n! instead of (n-1)! for circular arrangements.

5. **Incorrect application of addition rule**: Adding when tasks are not mutually exclusive (overlapping cases).

## Revision Tips

1. **Practice with word problems**: Translate English phrases ("arrange," "choose," "at least") into mathematical operations.

2. **Create a decision tree**: For complex problems, visualize the sequential decisions needed before calculating.

3. **Memorize key identities**: C(n,r) = C(n,n-r), P(n,r) = C(n,r) × r!, and the sum of binomial coefficients equals 2ⁿ.

4. **Solve backwards**: After solving, verify with small values where you can manually enumerate all possibilities.

5. **Practice circular arrangements separately**: This is a common trick question—always remember to fix one position or divide by n.