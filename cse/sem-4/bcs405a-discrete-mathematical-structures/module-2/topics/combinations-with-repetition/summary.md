# Combinations with Repetition - Summary

## Key Definitions and Concepts

- **Combinations with Repetition**: Selecting k items from n distinct items where repetitions are allowed and order doesn't matter. Also called "multiset combinations" or "combinations with replacement."

- **Stars and Bars Method**: A visualization technique where stars (★) represent selected items and bars (|) separate different types. Requires (n-1) bars to separate n types.

- **Non-negative Integer Solutions**: Solutions where variables can take values ≥ 0, typically found using the stars and bars method.

## Important Formulas and Theorems

- **Basic Formula**: C(n + k - 1, k) = (n + k - 1)! / (k! × (n - 1)!)

- **Symmetry Property**: C(n + k - 1, k) = C(n + k - 1, n - 1) — choose the smaller value for easier calculation.

- **Positive Integer Transformation**: For x₁ + x₂ + ... + xₙ = k with each xᵢ ≥ 1, substitute yᵢ = xᵢ - 1, giving y₁ + y₂ + ... + yₙ = k - n with yᵢ ≥ 0.

## Key Points

- Combinations with repetition applies when: repetition allowed, order irrelevant, items of same type are identical.

- The formula C(n + k - 1, k) counts the number of ways to distribute k identical objects among n distinct boxes.

- Stars and bars requires placing k stars and (n-1) bars in (k + n - 1) positions.

- For positive integer solutions to x₁ + x₂ + ... + xₙ = k, the answer is C(k - 1, n - 1).

- For non-negative integer solutions, the answer is C(n + k - 1, k).

## Common Mistakes to Avoid

- Confusing combinations with repetition [C(n + k - 1, k)] with combinations without repetition [C(n, k)].

- Forgetting to transform positive integer problems to non-negative before applying the formula.

- Using permutations instead of combinations when order doesn't matter.

- Not checking if the problem satisfies all conditions for combinations with repetition.

## Revision Tips

- Memorize the standard formula and its symmetric form for quick calculation.

- Practice converting between problem statements and the underlying combinatorial model.

- For problems with constraints, always break into cases and sum the results.

- Use stars and bars as a verification method for all your answers.
