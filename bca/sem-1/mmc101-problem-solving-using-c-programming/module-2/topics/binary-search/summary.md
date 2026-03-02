# Binary Search - Summary

## Key Definitions and Concepts

- **Binary Search:** An efficient searching algorithm that finds the position of a target value within a sorted array by repeatedly dividing the search interval in half.

- **Prerequisite:** Binary search ONLY works on sorted arrays (ascending or descending order).

- **Search Interval:** Defined by two pointers - 'low' (starting index) and 'high' (ending index).

- **Middle Element:** The pivot element calculated as mid = low + (high - low) / 2.

## Important Formulas and Theorems

- **Time Complexity:** O(log₂ n) - logarithmic time
- **Space Complexity (Iterative):** O(1) - constant
- **Space Complexity (Recursive):** O(log n) - due to call stack
- **Maximum Comparisons:** ⌊log₂ n⌋ + 1

## Key Points

- Binary search eliminates half of remaining elements in each iteration, making it vastly superior to linear search for large datasets.

- The loop condition must be `low <= high` to correctly handle boundary elements.

- Use `mid = low + (high - low) / 2` instead of `(low + high) / 2` to prevent integer overflow.

- Return -1 indicates element not found; otherwise return the index of found element.

- Best case time complexity is O(1) when element is at middle position.

- Binary search requires sorted data as input - this is not optional.

- Iterative implementation is preferred in practice due to O(1) space complexity.

## Common Mistakes to Avoid

1. Using `<` instead of `<=` in the while condition - misses boundary elements
2. Applying binary search to unsorted arrays - produces incorrect results
3. Forgetting to update both low AND high correctly in each iteration
4. Not handling the case when array is empty
5. Using `(low + high) / 2` which can cause overflow with large indices

## Revision Tips

1. Practice dry running binary search on at least 3-4 examples by hand.
2. Memorize the iterative implementation code - it's frequently asked in exams.
3. Remember the comparison: Linear Search O(n) vs Binary Search O(log n).
4. Know why sorted array is mandatory and be ready to explain in viva.
5. Review boundary conditions: empty array, single element, first/last element cases.