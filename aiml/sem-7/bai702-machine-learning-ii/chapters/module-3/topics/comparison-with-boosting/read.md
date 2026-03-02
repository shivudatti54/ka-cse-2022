# Comparison Sorting Algorithms

## Overview

Comparison sorts compare elements to determine order. Lower bound: Ω(n log n).

## Quick Sort

### Algorithm

1. Choose pivot
2. Partition: elements < pivot left, > pivot right
3. Recursively sort partitions

### Complexity

- Best/Average: O(n log n)
- Worst: O(n²) - already sorted with bad pivot
- Space: O(log n) stack

### Partition (Lomuto)

```
pivot = arr[high]
i = low - 1
for j = low to high-1:
    if arr[j] <= pivot:
        i++, swap(arr[i], arr[j])
swap(arr[i+1], arr[high])
return i+1
```

## Merge Sort

### Algorithm

1. Divide array into halves
2. Recursively sort halves
3. Merge sorted halves

### Complexity

- All cases: O(n log n)
- Space: O(n) for merging
- Stable: Yes

## Heap Sort

### Algorithm

1. Build max-heap
2. Extract max repeatedly

### Complexity

- All cases: O(n log n)
- Space: O(1) in-place
- Not stable

## Comparison Table

| Sort  | Best       | Average    | Worst      | Space    | Stable |
| ----- | ---------- | ---------- | ---------- | -------- | ------ |
| Quick | O(n log n) | O(n log n) | O(n²)      | O(log n) | No     |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n)     | Yes    |
| Heap  | O(n log n) | O(n log n) | O(n log n) | O(1)     | No     |
