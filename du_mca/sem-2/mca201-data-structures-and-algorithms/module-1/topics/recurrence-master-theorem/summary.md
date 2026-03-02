# Recurrence Relations and Master Theorem - Summary

## Key Definitions and Concepts

- **Recurrence Relation:** A mathematical definition of a sequence where each term is defined in terms of previous terms; used to express running time of recursive algorithms.

- **Divide-and-Conquer Recurrence:** T(n) = aT(n/b) + f(n), where 'a' is number of subproblems, 'b' is the factor by which problem size reduces, and f(n) is the cost of combining results.

- **Master Theorem:** Provides asymptotic solutions for recurrences of the form T(n) = aT(n/b) + f(n) with a ≥ 1, b > 1.

## Important Formulas and Theorems

**Master Theorem Cases:**

1. **Case 1:** If f(n) = O(n^log_b(a-ε)), then T(n) = Θ(n^log_b(a))

2. **Case 2:** If f(n) = Θ(n^log_b(a) × log^k(n)), then T(n) = Θ(n^log_b(a) × log^(k+1)(n))

3. **Case 3:** If f(n) = Ω(n^log_b(a+ε)) and regularity condition holds, then T(n) = Θ(f(n))

**Regularity Condition (Case 3):** a f(n/b) ≤ c f(n) for some c < 1 and sufficiently large n.

## Key Points

- Master Theorem applies only to recurrences in the specific form T(n) = aT(n/b) + f(n)
- Binary search: T(n) = T(n/2) + O(1) → Θ(log n)
- Merge sort: T(n) = 2T(n/2) + O(n) → Θ(n log n)
- Strassen's: T(n) = 7T(n/2) + O(n^2) → Θ(n^log_2(7)) ≈ Θ(n^2.81)
- Always compare f(n) with n^log_b(a) using polynomial difference (n^ε)
- Case 2 adds one extra logarithm factor when k ≥ 0
- Substitution method serves as a fallback for non-standard recurrences

## Common Mistakes to Avoid

- Applying Master Theorem to recurrences not in T(n) = aT(n/b) + f(n) form
- Forgetting to check the regularity condition for Case 3
- Confusing polynomial difference with logarithmic difference
- Not identifying the correct value of k in Case 2
- Using Big-O notation inconsistently (confusing O, Ω, and Θ)

## Revision Tips

1. Memorize the three cases of Master Theorem with their conditions
2. Practice identifying a, b, and f(n) from algorithm descriptions
3. Verify Master Theorem results using recursion trees
4. Focus on common patterns: log n, n log n, n^c for various c
5. Solve at least 5 diverse recurrence problems before the exam