# Arrays: Operations and Implementation - Summary

## Key Definitions and Concepts

- **Array**: A linear data structure storing elements of the same type in contiguous memory locations, accessible via indices.
- **Traversal**: Visiting each element exactly once, typically using a loop.
- **Insertion**: Adding an element at a specified position; requires shifting elements right.
- **Deletion**: Removing an element from a specified position; requires shifting elements left.
- **Linear Search**: Sequential search checking each element - O(n) time complexity.
- **Binary Search**: Divide-and-conquer search on sorted arrays - O(log n) time complexity.
- **Overflow**: Condition when attempting to insert into a full array.
- **Underflow**: Condition when attempting to delete from an empty array.

## Important Formulas and Theorems

- **Array Address Calculation (1D)**: `BaseAddress + (index × ElementSize)`
- **Array Address Calculation (2D - Row Major)**: `BaseAddress + ((row × COLS) + col) × ElementSize`
- **Binary Search Mid Index**: `mid = low + (high - low) / 2` (prevents integer overflow)
- **Bubble Sort Passes**: `n-1` passes required for n elements

## Key Points

1. Arrays provide O(1) random access to elements via index, but insertion/deletion is O(n) due to shifting.

2. Linear search works on unsorted arrays; binary search requires sorted arrays.

3. Time complexity of linear search is O(n), binary search is O(log n).

4. Basic sorting algorithms (bubble, selection) have O(n²) time complexity; space complexity is O(1).

5. In C/C++, array indices start from 0 and go up to (size-1).

6. Two-dimensional arrays can be stored in row-major or column-major order.

7. Always check for overflow before insertion and underflow before deletion.

8. Bubble sort repeatedly swaps adjacent elements if in wrong order; selection sort finds minimum and places at beginning.

9. For n elements, bubble sort performs approximately n(n-1)/2 comparisons.

10. Binary search reduces search space by half with each iteration.

## Common Mistakes to Avoid

1. Using binary search on unsorted arrays - always sort first or ensure array is sorted.

2. Not checking boundary conditions (position < 0 or position > n) in insert/delete functions.

3. Forgetting to return the updated size after insertion or deletion.

4. Using `(low + high) / 2` instead of `low + (high - low) / 2` for mid calculation (overflow risk).

5. Confusing array indices with positions (index starts at 0, position starts at 1 for user input).

6. Not initializing arrays before use, leading to garbage values.

## Revision Tips

1. Practice writing all array operations (traversal, insert, delete, search, sort) from memory.

2. Trace through sorting algorithms step-by-step on paper with small arrays.

3. Memorize time complexities: Linear Search O(n), Binary Search O(log n), Bubble/Selection Sort O(n²).

4. Understand the difference between worst-case, average-case, and best-case scenarios.

5. Solve previous year DU question papers to understand the exam pattern and difficulty level.