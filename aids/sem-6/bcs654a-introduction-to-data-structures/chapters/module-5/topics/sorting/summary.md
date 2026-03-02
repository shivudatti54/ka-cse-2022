# Sorting - Summary

## Key Definitions and Concepts

- **Sorting**: The process of arranging data elements in a specific order (ascending or descending)
- **In-place sorting**: Algorithms requiring only O(1) auxiliary space
- **Stable sorting**: Algorithms that preserve the relative order of equal elements
- **Adaptive algorithm**: An algorithm whose performance improves with favorable input characteristics

## Important Formulas and Theorems

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |

## Key Points

- All three algorithms (Bubble, Selection, Insertion) use comparison-based sorting with O(1) space complexity
- Bubble Sort and Insertion Sort are stable; Selection Sort is typically unstable
- Selection Sort makes exactly n-1 swaps regardless of input arrangement
- Insertion Sort achieves O(n) best case on sorted or nearly sorted data, making it adaptive
- Selection Sort minimizes the number of writes/swaps, ideal for memory-constrained environments
- Bubble Sort can be optimized with a swap flag to achieve O(n) best case
- For small datasets (n < 50), Insertion Sort often outperforms more complex algorithms
- Time complexity analysis using Big-O notation is essential for algorithm comparison

## Common Mistakes to Avoid

- Confusing best/average/worst case complexities—each algorithm performs differently based on input
- Assuming all O(n²) algorithms perform identically—they differ in constants and practical behavior
- Forgetting that Selection Sort is non-adaptive despite having the same asymptotic complexity as other algorithms
- Overlooking stability requirements when sorting records with multiple fields

## Revision Tips

1. Practice tracing each algorithm step-by-step on at least 3-4 different input arrays to build intuition
2. Create a comparison table memorizing all complexities and properties for quick recall
3. Understand the reasoning behind stability—know which algorithms preserve element order and why
4. Focus on Insertion Sort's adaptive behavior—examine why nearly sorted data requires minimal operations
5. Review previous year DU examination questions on sorting to understand the question patterns and marking scheme