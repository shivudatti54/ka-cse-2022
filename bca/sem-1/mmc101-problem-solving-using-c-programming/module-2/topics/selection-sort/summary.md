# Selection Sort - Summary

## Key Definitions and Concepts

- **Selection Sort:** A comparison-based sorting algorithm that repeatedly selects the minimum (or maximum) element from the unsorted portion and places it at the beginning of the sorted portion.

- **In-place Sorting:** An algorithm that requires only O(1) auxiliary space, modifying the array directly through swaps rather than creating new data structures.

- **Stable Sorting:** A sorting algorithm that preserves the relative order of equal elements from the original array.

## Important Formulas and Theorems

- **Total Comparisons:** n(n-1)/2 = (n²-n)/2, which is O(n²)
- **Number of Passes:** n-1 (the last pass is unnecessary)
- **Number of Swaps:** Minimum possible (at most n-1 swaps)
- **Time Complexity:** O(n²) for all cases (best, average, worst)
- **Space Complexity:** O(1) auxiliary space
- **Adaptive:** NO - performance does not improve with pre-sorted input

## Key Points

1. Selection Sort divides the array into sorted portion (beginning) and unsorted portion (remaining elements).

2. In each pass, the algorithm finds the minimum element in the unsorted portion and swaps it with the first unsorted element.

3. The algorithm requires exactly n(n-1)/2 comparisons regardless of initial arrangement.

4. It performs at most n-1 swaps, making it efficient in terms of write operations compared to algorithms like Bubble Sort.

5. Selection Sort is NOT stable because swapping distant elements can change the relative order of equal elements.

6. The algorithm works efficiently for small datasets and is simple to understand and implement.

7. For descending order, simply change the comparison from arr[j] < arr[min_idx] to arr[j] > arr[max_idx].

8. Selection Sort is particularly suitable when memory write operations are expensive (e.g., flash memory).

## Common Mistakes to Avoid

1. **Forgetting the swap condition:** Always check if min_idx != i before swapping to avoid unnecessary operations when the minimum is already in position.

2. **Incorrect loop boundaries:** The outer loop should run from 0 to n-2 (not n-1), and the inner loop should start from i+1.

3. **Confusing with other O(n²) algorithms:** Students often mix up Selection Sort with Bubble Sort or Insertion Sort characteristics.

4. **Missing the base case:** Not handling arrays of size 0 or 1 properly in implementations.

## Revision Tips

1. Practice tracing Selection Sort on paper with at least 3-4 different arrays to master the pass-by-pass execution.

2. Memorize that time complexity is O(n²) for all cases and space complexity is O(1).

3. Remember the key advantage: minimum number of swaps (at most n-1).

4. Remember the key disadvantage: NOT stable and always O(n²) comparisons.

5. Write the C code from memory multiple times until you can do it without errors.