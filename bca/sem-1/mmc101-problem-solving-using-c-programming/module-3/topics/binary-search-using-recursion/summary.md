# Binary Search Using Recursion - Summary

## Key Definitions and Concepts

- BINARY SEARCH: An efficient O(log n) searching algorithm that works on sorted arrays by repeatedly dividing the search interval in half.

- RECURSION: A programming technique where a function calls itself to solve smaller instances of the same problem.

- DIVIDE AND CONQUER: An algorithmic paradigm that breaks a problem into smaller subproblems, solves them, and combines the results.

- BASE CASE: The termination condition in a recursive function that stops further recursion.

- LOW AND HIGH: Boundary indices defining the current search range in the array.

- MID: The middle index calculated as low + (high - low) / 2.

## Important Formulas and Theorems

- MIDDLE INDEX: mid = low + (high - low) / 2 (prevents integer overflow)

- TIME COMPLEXITY: O(log n) — search space halves at each step

- SPACE COMPLEXITY: O(log n) — due to recursive call stack

- RECURRENCE RELATION: T(n) = T(n/2) + O(1), solved as T(n) = O(log n)

## Key Points

- Binary search requires a SORTED array as a prerequisite condition

- The base case returns -1 when low > high (element not found)

- Each recursive call reduces the problem size by approximately half

- Using (low + high) / 2 can cause overflow; use low + (high - low) / 2 instead

- Recursive binary search uses more memory than iterative due to function call overhead

- The algorithm compares middle element with key and recurses on the appropriate half

- First occurrence in duplicates requires checking arr[mid-1] when arr[mid]==key

## Common Mistakes to Avoid

- Applying binary search on unsorted arrays—always verify the array is sorted first

- Using (low + high) / 2 for middle index—causes integer overflow in large arrays

- Missing base case or incorrect base case condition—leads to infinite recursion

- Forgetting to adjust indices (mid-1 or mid+1) in recursive calls—causes infinite loops

- Not handling the case when element is found at boundaries (first or last position)

## Revision Tips

- Practice writing the recursive binary search function from memory multiple times

- Trace through examples by hand: try searching for elements in sorted arrays of size 8, 16, or 32

- Compare iterative and recursive versions side-by-side to understand the differences

- Remember the key characteristics: O(log n) time, O(log n) space for recursive, O(1) for iterative

- Review examination questions from previous years to understand the pattern of questions asked