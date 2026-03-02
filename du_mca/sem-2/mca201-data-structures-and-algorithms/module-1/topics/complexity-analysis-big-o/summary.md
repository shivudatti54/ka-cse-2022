# Complexity Analysis - Summary

## Key Definitions and Concepts
- **Big O**: Worst-case growth rate (Upper bound)
- **Omega (Ω)**: Best-case growth rate (Lower bound)
- **Theta (Θ)**: Average-case tight bound
- **Amortized Analysis**: Average cost over sequence of operations
- **Space Complexity**: Memory growth relative to input size

## Important Formulas and Theorems
- **Master Theorem**: For T(n) = aT(n/b) + O(nᵏ)
  - If a > bᵏ: O(n^(log_b a))
  - If a = bᵏ: O(nᵏ log n)
  - If a < bᵏ: O(nᵏ)
- **Common Complexities**:
  - O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)

## Key Points
- Complexity measures growth rate, not absolute time
- Worst-case analysis (Big O) is most crucial for system design
- Nested loops multiply complexities
- Recursive complexity depends on recursion depth and branching factor
- Space complexity includes auxiliary space for algorithm execution
- Amortized analysis is key for dynamic arrays and hash tables
- O(n log n) is optimal for comparison-based sorting

## Common Mistakes to Avoid
- Confusing Big O with actual runtime measurements
- Forgetting to consider all variables in multi-input functions
- Misapplying Master Theorem to non-divide-and-conquer recurrences
- Overlooking space complexity in recursive algorithms (stack space)

## Revision Tips
- Practice deriving complexities from code snippets
- Create flashcards for complexity classes and their relationships
- Solve previous years' DU papers focusing on recurrence relations
- Use visualization tools to compare growth rates graphically