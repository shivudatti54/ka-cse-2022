# Counting Sort - Summary

## Key Definitions
- **Counting Sort**: A non-comparison based integer sorting algorithm that sorts by counting occurrences of each distinct value
- **Stability**: A sorting algorithm is stable if elements with equal keys maintain their relative order in the output
- **Transform-and-Conquer**: Algorithmic paradigm where a problem is transformed into a simpler form before solving
- **k (range)**: The difference between maximum and minimum input values plus one

## Important Formulas
- **Time Complexity**: T(n, k) = Θ(n + k)
- **Space Complexity**: S(n, k) = Θ(n + k)
- **Cumulative Count**: C[i] = Σ_{j=0}^{i} count[j]

## Key Points
1. Counting Sort is non-comparison based, achieving linear time O(n + k) for bounded integer ranges
2. The algorithm requires knowing the range k of input values beforehand
3. Four phases: Initialize counts → Count occurrences → Compute cumulative positions → Place elements
4. Stability is guaranteed by traversing input from right to left during placement
5. When k = O(n), overall complexity becomes Θ(n), beating the Ω(n log n) comparison sort lower bound
6. Used as stable subroutine in Radix Sort for sorting digit by digit
7. Space complexity Θ(n + k) can be prohibitive when k is large
8. Only works directly with non-negative integers; requires modification for other data types

## Common Mistakes
1. Calling Counting Sort a "comparison sort" - it is NON-comparison based
2. Forgetting that Phase 4 must traverse RIGHT TO LEFT for stability
3. Assuming Counting Sort works for any data type without preprocessing
4. Ignoring the space overhead when k >> n makes the algorithm impractical
5. Not recognizing that cumulative counts in Phase 3 represent positions, not frequencies