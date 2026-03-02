# Sorting

## Overview

Sorting is the process of arranging data elements in a particular order (ascending or descending). It is fundamental to computer science, enabling efficient searching, data presentation, and serving as preprocessing for many algorithms.

## Key Points

- **Purpose**: Arrange elements in ascending or descending order
- **Algorithm Classes**: Simple O(n²) sorts, efficient O(n log n) sorts, linear O(n) sorts
- **Comparison-Based**: Most sorts compare elements to determine order
- **Stability**: Stable sorts preserve relative order of equal elements
- **In-Place**: In-place sorts use O(1) extra space, out-of-place use O(n)
- **Adaptive**: Some sorts perform better on partially sorted data
- **Applications**: Enabling binary search, data presentation, database indexing

## Important Concepts

- Simple sorts (bubble, selection, insertion) easy to understand but inefficient
- Efficient sorts (merge, quick, heap) complex but handle large data well
- Merge sort always O(n log n), stable, but requires extra space
- Quick sort average O(n log n), in-place, but O(n²) worst case
- Heap sort O(n log n) worst case, in-place, but unstable
- Insertion sort efficient for small or nearly sorted arrays

## Notes

- Create comparison table with time/space complexity for all algorithms
- Understand stability concept and when it matters
- Know which sorts are in-place vs out-of-place
- Practice choosing appropriate sort for given requirements
- Remember trade-offs between time, space, and stability
