# Linear Search - Summary

## Key Definitions and Concepts
- **Linear Search**: A searching algorithm that examines each element sequentially until the target is found or the array is exhausted.
- **Sequential Search**: Another name for Linear Search, emphasizing the step-by-step examination of elements.
- **Sentinel Linear Search**: An optimized version that places the target at the end of the array to eliminate bounds checking.

## Important Formulas and Theorems
- **Best Case Time Complexity**: O(1) — when target is at first position
- **Worst Case Time Complexity**: O(n) — when target is at last position or absent
- **Average Case Time Complexity**: O(n) — approximately n/2 comparisons
- **Space Complexity**: O(1) — constant extra space required
- **Number of comparisons in worst case**: n comparisons
- **Number of comparisons in average case**: n/2 comparisons

## Key Points
- Linear Search works on both sorted and unsorted arrays.
- The algorithm returns the index of the first occurrence of the target if found, otherwise returns -1.
- For small datasets (n < 20), Linear Search often outperforms more complex algorithms due to lower overhead.
- Linear Search is the only practical search method for linked lists.
- The iterative implementation is preferred over recursion due to absence of call stack overhead.
- When searching sorted arrays, Binary Search with O(log n) complexity is preferable.
- The sentinel optimization reduces one comparison per iteration but does not change asymptotic complexity.

## Common Mistakes to Avoid
- Confusing 0-based indexing: returning 0 for the first element, not 1.
- Forgetting to restore the original element when using sentinel search.
- Using Binary Search on unsorted data, which produces incorrect results.
- Incorrect loop boundary conditions leading to array index out of bounds.

## Revision Tips
- Practice tracing through at least 5 different arrays manually before the exam.
- Memorize the complexity formulas and be able to derive them.
- Write the complete C code from memory and test it with sample inputs.
- Focus on understanding when to apply Linear Search versus other algorithms.