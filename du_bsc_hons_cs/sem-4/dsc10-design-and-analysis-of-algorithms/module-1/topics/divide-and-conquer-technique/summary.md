# Divide and Conquer Technique - Summary

## Key Definitions and Concepts

- **Divide and Conquer**: An algorithm design paradigm that recursively breaks a problem into smaller subproblems, solves them, and combines their solutions
- **Recurrence Relation**: An equation that defines a sequence recursively, expressing T(n) in terms of T(n/b)
- **Master Theorem**: A tool for solving recurrence relations of the form T(n) = aT(n/b) + f(n)
- **Base Case**: The condition at which the recursion stops, typically when n ≤ c (a small constant)

## Important Formulas and Theorems

- **General Recurrence**: T(n) = aT(n/b) + D(n) + C(n)
- **Master Theorem Cases**:
  - Case 1: f(n) = O(n^log_b(a-ε)) → T(n) = Θ(n^log_b(a))
  - Case 2: f(n) = Θ(n^log_b(a)) → T(n) = Θ(n^log_b(a) log n)
  - Case 3: f(n) = Ω(n^log_b(a+ε)) with regularity condition → T(n) = Θ(f(n))
- **Binary Search**: T(n) = T(n/2) + O(1) → Θ(log n)
- **Merge Sort**: T(n) = 2T(n/2) + O(n) → Θ(n log n)
- **Quick Sort (Average)**: T(n) = 2T(n/2) + O(n) → Θ(n log n)
- **Strassen's Matrix Multiplication**: T(n) = 7T(n/2) + O(n²) → Θ(n^2.807)

## Key Points

- Divide and conquer involves three steps: Divide, Conquer, and Combine
- The technique is particularly effective when subproblems are independent and substantially smaller than the original problem
- Merge sort guarantees O(n log n) time complexity; Quick sort averages O(n log n) but degrades to O(n²) in worst case
- Binary search achieves logarithmic time complexity by halving the search space each iteration
- The Master Theorem provides asymptotic bounds without solving the recurrence by iteration
- Space complexity is an important consideration: Merge Sort requires O(n) auxiliary space
- Regularity condition in Master Theorem Case 3 requires af(n/b) ≤ cf(n) for some c < 1

## Common Mistakes to Avoid

- Confusing the conditions of Master Theorem cases (especially distinguishing Case 1 from Case 3)
- Forgetting to include the combining step's cost in the recurrence relation
- Mixing up Quick Sort and Merge Sort characteristics (stability, in-place vs auxiliary space)
- Not considering the base case when analyzing recursive algorithms
- Applying Master Theorem when the conditions are not met (e.g., when f(n) is not polynomially different from n^log_b(a))

## Revision Tips

1. Practice writing recurrence relations for at least 5 different divide and conquer algorithms
2. Memorize the three cases of Master Theorem with their boundary conditions
3. Trace through Merge Sort and Quick Sort on small arrays to understand the difference in partitioning
4. Solve at least 3-4 previous year DU exam questions on recurrence solving
5. Create a comparison table of all divide and conquer algorithms covering time, space, and practical considerations