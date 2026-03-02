# Bubble Sort

## Overview

Bubble sort is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in wrong order. The largest element "bubbles up" to the end in each pass.

## Key Points

- **Adjacent Comparison**: Compare and swap adjacent elements if out of order
- **Multiple Passes**: Requires n-1 passes for n elements
- **Bubble Up**: Largest element reaches correct position after each pass
- **Time Complexity**: O(n²) worst and average case, O(n) best case if already sorted
- **Space Complexity**: O(1) in-place sorting algorithm
- **Stability**: Stable sort preserving order of equal elements
- **Optimization**: Stop early if no swaps occur in a pass (already sorted)

## Important Concepts

- Each pass moves largest unsorted element to its final position
- After i passes, last i elements are in correct positions
- Best case occurs with already sorted array, one pass with no swaps
- Worst case occurs with reverse sorted array, maximum swaps
- Inner loop can be optimized to reduce comparisons after each pass
- Simple to implement but inefficient for large datasets

## Notes

- Practice tracing algorithm showing element movements in each pass
- Understand optimization with flag to detect early completion
- Know why called bubble sort (elements bubble to position)
- Remember it's stable and in-place but inefficient
- Be able to count comparisons and swaps for given input
