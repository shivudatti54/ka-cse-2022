# Selection Sort

## Overview

Selection sort divides the array into sorted and unsorted portions, repeatedly selecting the minimum element from the unsorted portion and placing it at the beginning. It performs well on small lists but is inefficient for large datasets.

## Key Points

- **Find Minimum**: Select minimum element from unsorted portion in each pass
- **Swap to Front**: Swap minimum with first element of unsorted portion
- **Sorted Portion Grows**: Sorted portion at beginning expands with each pass
- **Time Complexity**: O(n²) for all cases (best, average, worst)
- **Space Complexity**: O(1) in-place sorting
- **Stability**: Unstable (relative order of equal elements may change)
- **Number of Swaps**: At most n-1 swaps, fewer than bubble sort

## Important Concepts

- Each pass finds minimum and places it in correct position
- After i passes, first i elements are sorted
- Number of comparisons always (n-1) + (n-2) + ... + 1 = n(n-1)/2
- Unlike bubble sort, performance doesn't improve on nearly sorted data
- Minimizes number of swaps compared to other simple sorts
- Useful when swap operation is expensive

## Notes

- Practice tracing showing minimum selection in each pass
- Understand why it's unstable (swap may skip equal elements)
- Know that it always makes same number of comparisons regardless of input
- Remember advantage: minimum number of swaps
- Be able to count exact comparisons for n elements
