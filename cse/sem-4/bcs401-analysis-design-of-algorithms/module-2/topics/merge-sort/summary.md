# Merge Sort - Summary

## Key Definitions
- **Divide and Conquer**: Algorithmic paradigm that divides problem into subproblems, conquers them recursively, and combines solutions
- **Stable Sorting Algorithm**: An algorithm that preserves the relative order of equal elements
- **External Sorting**: Sorting data that exceeds available memory, requiring sequential access patterns

## Important Formulas
- **Recurrence Relation**: T(n) = 2T(n/2) + Θ(n), with T(1) = Θ(1)
- **Time Complexity**: Θ(n log n) in all cases (best, average, worst)
- **Space Complexity**: Θ(n) auxiliary space for merge operation; O(log n) for recursion stack
- **Merge Comparisons**: Maximum of (n₁ + n₂ - 1) comparisons for merging subarrays of sizes n₁ and n₂

## Key Points
1. Merge Sort follows the divide-conquer paradigm: divide into halves, recursively sort, then merge
2. The merge operation is the core procedure requiring O(n) time and O(n) auxiliary space
3. Time complexity proof uses recurrence relation T(n) = 2T(n/2) + Θ(n), solved by Master Theorem to yield Θ(n log n)
4. Merge Sort is STABLE — equal elements maintain their relative order in the sorted output
5. Unlike brute-force approaches (exponential complexity), divide-and-conquer achieves polynomial time
6. Requires O(n) extra space, making it non-in-place — a key disadvantage versus Quick Sort
7. Bottom-up (iterative) implementation avoids recursion overhead
8. Ideal for external sorting due to sequential access patterns and predictable performance
9. Works well for linked lists (can be implemented in-place) but requires random access for arrays

## Common Mistakes
1. **Confusing Merge Sort with brute force**: Merge Sort is divide-and-conquer, not exhaustive search
2. **Forgetting auxiliary space**: Many students overlook that Merge Sort requires O(n) extra memory
3. **Assuming in-place**: Unlike Quick Sort, standard Merge Sort is not in-place; the merge procedure needs temporary arrays
4. **Ignoring stability**: Merge Sort's stability is a key advantage over Quick Sort for certain applications