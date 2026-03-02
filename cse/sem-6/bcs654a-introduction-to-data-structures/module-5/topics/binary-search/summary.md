# Binary Search

## Overview

Binary search is an efficient divide-and-conquer algorithm for finding elements in sorted arrays. It repeatedly divides the search space in half, achieving O(log n) time complexity by eliminating half the remaining elements at each step.

## Key Points

- **Prerequisite**: Array must be sorted in ascending or descending order
- **Divide and Conquer**: Compare target with middle element, eliminate half of array
- **Time Complexity**: O(log n) for search, much faster than linear search
- **Space Complexity**: O(1) iterative, O(log n) recursive due to call stack
- **Algorithm**: Find middle, compare with target, search left or right half
- **Implementation**: Both iterative and recursive versions possible
- **Termination**: Element found or search space becomes empty

## Important Concepts

- Each comparison eliminates half the remaining elements
- Middle calculated as (low + high) / 2 or low + (high - low) / 2 to avoid overflow
- If target < middle, search left half; if target > middle, search right half
- Worst case: log₂(n) comparisons for array of size n
- Requires random access, works on arrays not linked lists
- Dramatically faster than linear search for large datasets

## Notes

- Practice both iterative and recursive implementations
- Understand why sorted data is prerequisite
- Trace algorithm showing how search space halves each step
- Know overflow-safe middle calculation formula
- Remember O(log n) means doubling input only adds one comparison
