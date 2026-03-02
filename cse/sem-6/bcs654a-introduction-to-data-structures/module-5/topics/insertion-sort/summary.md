# Insertion Sort

## Overview

Insertion sort builds the sorted array one element at a time by repeatedly taking the next element and inserting it into its correct position among the already sorted elements. It is efficient for small datasets and nearly sorted arrays.

## Key Points

- **Build Sorted Portion**: Maintain sorted portion at beginning, insert elements one by one
- **Insert Operation**: Take next element, shift larger sorted elements right, insert at correct position
- **Time Complexity**: O(n²) worst and average case, O(n) best case for sorted data
- **Space Complexity**: O(1) in-place sorting
- **Stability**: Stable sort maintaining order of equal elements
- **Adaptive**: Performs well on nearly sorted data
- **Online**: Can sort data as it arrives

## Important Concepts

- Similar to how people sort playing cards in hand
- Best case: array already sorted, each element needs one comparison
- Worst case: reverse sorted array, each element compared with all sorted elements
- After i iterations, first i+1 elements are sorted
- Efficient for small arrays or nearly sorted data
- Better than bubble/selection for practical use

## Notes

- Practice showing insertion and shifting process for each element
- Understand why it's adaptive (efficient on nearly sorted data)
- Know that it's online algorithm (can add elements during sorting)
- Remember it's stable and in-place
- Be able to analyze best, average, worst case scenarios
