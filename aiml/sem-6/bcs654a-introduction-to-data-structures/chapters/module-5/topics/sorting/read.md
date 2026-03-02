# Introduction to Sorting

## What is Sorting?
Sorting is arranging elements in a specific order (ascending/descending) based on a comparison criterion.

## Why Sorting Matters
- **Search efficiency**: Binary search requires sorted data O(log n)
- **Data organization**: Easier to find, merge, analyze
- **Prerequisite**: Many algorithms need sorted input

## Classification of Sorting Algorithms

### By Comparison
| Type | Examples | Lower Bound |
|------|----------|-------------|
| **Comparison-based** | Bubble, Merge, Quick | Ω(n log n) |
| **Non-comparison** | Counting, Radix, Bucket | O(n) possible |

### By Space Usage
| Type | Space | Examples |
|------|-------|----------|
| **In-place** | O(1) | Bubble, Selection, Quick |
| **Out-of-place** | O(n) | Merge Sort |

### By Stability
| Type | Property | Examples |
|------|----------|----------|
| **Stable** | Equal elements keep relative order | Merge, Insertion, Bubble |
| **Unstable** | May change relative order | Quick, Heap, Selection |

### By Adaptivity
| Type | Property | Examples |
|------|----------|----------|
| **Adaptive** | Faster on nearly sorted | Insertion, Bubble (optimized) |
| **Non-adaptive** | Same time regardless | Selection, Merge |

## Algorithm Comparison

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |

## When to Use What

| Scenario | Recommended |
|----------|-------------|
| Small arrays (n < 50) | Insertion Sort |
| Nearly sorted | Insertion Sort |
| Memory constrained | Heap Sort or Quick Sort |
| Stability required | Merge Sort |
| Average-case performance | Quick Sort |
| Guaranteed O(n log n) | Merge Sort or Heap Sort |
| Integer keys in range | Counting Sort |

## Key Concepts

### Inversions
Number of pairs (i, j) where i < j but arr[i] > arr[j].
- Sorted array: 0 inversions
- Reverse sorted: n(n-1)/2 inversions

### Lower Bound
Comparison-based sorting cannot be faster than Ω(n log n) in worst case.
**Proof**: Decision tree has n! leaves, height ≥ log(n!) = Ω(n log n)

> **Exam Tip**: Know complexity, stability, and in-place property of each algorithm. Quick Sort is fastest in practice, Merge Sort guarantees O(n log n).
