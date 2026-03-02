# The Principle of Inclusion and Exclusion - Summary

## Key Definitions and Concepts

- **Union of Sets**: The collection of all elements that belong to at least one of the sets
- **Intersection of Sets**: The collection of elements common to all sets
- **Derangement**: A permutation where no element appears in its original position
- **LCM (Least Common Multiple)**: Used to find numbers divisible by multiple integers

## Important Formulas and Theorems

- **Two Sets**: |A ∪ B| = |A| + |B| - |A ∩ B|
- **Three Sets**: |A ∪ B ∪ C| = |A| + |B| + |C| - |A∩B| - |A∩C| - |B∩C| + |A∩B∩C|
- **General PIE**: |A₁ ∪ ... ∪ Aₙ| = Σ|Aᵢ| - Σ|Aᵢ∩Aⱼ| + Σ|Aᵢ∩Aⱼ∩Aₖ| - ... + (-1)ⁿ⁻¹|A₁∩...∩Aₙ|
- **Derangements**: D(n) = n! × Σ(-1)ᵏ/ᵏ! or D(n) = ⌊n!/e + 1/2⌋
- **Recurrence**: D(n) = (n-1)[D(n-1) + D(n-2)] with D(1)=0, D(2)=1

## Key Points

- PIE corrects overcounting by alternating between adding and subtracting intersections
- The number of terms grows as 2ⁿ for n sets—choose n ≤ 3 for manual calculation
- For "not divisible by" problems, find the complement: Total - |A ∪ B ∪ C|
- Derangements approach n!/e as n increases (approximately 36.8% of all permutations)
- Always calculate intersections using LCM for divisibility problems

## Common Mistakes to Avoid

- Forgetting to alternate signs (always start with addition for single sets)
- Using GCD instead of LCM when finding intersections of divisible sets
- Not subtracting the intersection counts when computing union size
- Confusing "at least one" with "exactly one"—PIE handles "at least one"
- Using the wrong base cases for derangement recurrence (D(1) = 0, not 1)

## Revision Tips

- Practice at least 3 problems from each category: divisibility, arrangements, and survey-type problems
- Memorize the first 5 derangement values: D(1)=0, D(2)=1, D(3)=2, D(4)=9, D(5)=44
- Remember: PIE = Add singles − Add pairs + Add triples − Add quadruples + ...
- For quick verification, test small cases where you can enumerate manually
