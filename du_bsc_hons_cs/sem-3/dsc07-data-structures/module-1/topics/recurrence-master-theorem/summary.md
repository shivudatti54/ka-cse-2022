# Recurrence Relations and Master Theorem - Summary

## Key Definitions and Concepts

- **Recurrence Relation:** An equation that defines a sequence recursively, expressing T(n) in terms of T of smaller inputs
- **Divide-and-Conquer Recurrence:** T(n) = aT(n/b) + f(n), where a ≥ 1 is the number of subproblems, b > 1 is the shrinkage factor, and f(n) is the cost of dividing and combining
- **Master Theorem:** Provides asymptotic solutions for recurrences of the form T(n) = aT(n/b) + f(n)

## Important Formulas and Theorems

**Master Theorem - Case 1:** If f(n) = O(n^(log_b a - ε)), then T(n) = Θ(n^(log_b a))

**Master Theorem - Case 2:** If f(n) = Θ(n^(log_b a) · log^k n), then T(n) = Θ(n^(log_b a) · log^(k+1) n)

**Master Theorem - Case 3:** If f(n) = Ω(n^(log_b a + ε)) and a·f(n/b) ≤ c·f(n) for some c < 1, then T(n) = Θ(f(n))

## Key Points

- The critical term n^(log_b a) represents the "work done by the recursion" at each level
- Binary Search: T(n) = T(n/2) + O(1) → Θ(log n) - Case 2 with k=0
- Merge Sort: T(n) = 2T(n/2) + Θ(n) → Θ(n log n) - Case 2 with k=0
- Strassen's: T(n) = 7T(n/2) + Θ(n²) → Θ(n^(log₂ 7)) ≈ Θ(n^2.807) - Case 1
- The regularity condition (Case 3) ensures that f(n) grows polynomially faster than n^(log_b a)
- Master Theorem cannot handle boundary cases where f(n) is between the polynomial bounds

## Common Mistakes to Avoid

1. **Incorrectly calculating log_b a** - Many students confuse log_b(a) with log_a(b); remember it's the exponent to which b must be raised to get a
2. **Forgetting the regularity condition in Case 3** - Simply having f(n) larger is not enough; the regularity condition must hold
3. **Applying Master Theorem when it doesn't apply** - Always verify the recurrence fits the form T(n) = aT(n/b) + f(n)
4. **Mixing up Big-O and Θ notations** - The Master Theorem provides Θ (tight bounds), not just O

## Revision Tips

1. **Practice identifying a, b, and f(n)** from given recurrences - This is the first step in every problem
2. **Memorize the three Master Theorem cases** with their conditions and results
3. **Solve at least 5-6 problems** using both Master Theorem and substitution methods
4. **Remember standard results:** Binary Search is Θ(log n), Merge Sort is Θ(n log n), Quick Sort average case is Θ(n log n)
5. **Draw recursion trees** when stuck - they provide excellent visualization and can help verify answers