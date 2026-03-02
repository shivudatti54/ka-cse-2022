# Asymptotic Analysis - Summary

## Key Definitions and Concepts

- **Asymptotic Analysis:** A method of evaluating algorithm efficiency by examining how resource requirements grow as input size approaches infinity
- **Time Complexity:** Measures the amount of time an algorithm takes as a function of input size
- **Space Complexity:** Measures the memory usage of an algorithm as a function of input size

## Important Formulas and Theorems

- **Big-O (Upper Bound):** f(n) = O(g(n)) if ∃ c, n₀ such that 0 ≤ f(n) ≤ c×g(n) for all n ≥ n₀
- **Big-Omega (Lower Bound):** f(n) = Ω(g(n)) if ∃ c, n₀ such that 0 ≤ c×g(n) ≤ f(n) for all n ≥ n₀
- **Big-Theta (Tight Bound):** f(n) = Θ(g(n)) if ∃ c₁, c₂, n₀ such that 0 ≤ c₁×g(n) ≤ f(n) ≤ c₂×g(n) for all n ≥ n₀
- **Master Theorem:** For T(n) = aT(n/b) + f(n), compare f(n) with n^(log_b(a))

## Common Growth Rates (Ordered)
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)

## Key Points

- Big-O represents worst-case, Big-Ω represents best-case, Big-Θ represents average/tight bound
- Always drop constants and lower-order terms when expressing complexity
- Loop analysis: multiply the complexity of loop body by number of iterations
- Recursive algorithms are analyzed using recurrence relations
- Binary search and merge sort both have O(n log n) time complexity
- Space complexity includes both auxiliary space and input space
- Practical significance: O(n²) becomes impractical for n > 10,000; O(2ⁿ) becomes useless for n > 30

## Common Mistakes to Avoid

- Confusing Big-O (upper bound) with Big-Ω (lower bound)
- Including constant factors in asymptotic notation (write O(n), not O(3n))
- Forgetting that Big-Θ requires both upper and lower bounds
- Ignoring space complexity when it is as important as time complexity
- Misapplying the Master Theorem by incorrectly identifying a, b, or f(n)

## Revision Tips

1. Practice analyzing at least 5 different loop structures daily
2. Create a cheat sheet of common algorithm complexities (sorting, searching, etc.)
3. Solve previous 5 years' DU question papers on this topic
4. Understand the mathematical proofs behind asymptotic notations
5. Focus on the Master Theorem - it's frequently tested in exams