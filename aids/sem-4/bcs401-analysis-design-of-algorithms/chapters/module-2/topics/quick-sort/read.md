# Quick Sort

## Concept
Divide and conquer: Choose pivot, partition array around pivot, recursively sort partitions.

## Algorithm
```
quickSort(arr, low, high):
    if low < high:
        pivotIndex = partition(arr, low, high)
        quickSort(arr, low, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, high)
```

## Partition (Lomuto)
```
partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j = low to high-1:
        if arr[j] <= pivot:
            i++
            swap(arr[i], arr[j])
    swap(arr[i+1], arr[high])
    return i+1
```

## Complexity
| Case | Time | Space |
|------|------|-------|
| Best | O(n log n) | O(log n) |
| Average | O(n log n) | O(log n) |
| Worst | O(n²) | O(n) |

**Stable**: No | **In-place**: Yes | **Adaptive**: No

## Pivot Selection
| Strategy | Description |
|----------|-------------|
| Last element | Simple, but O(n²) for sorted input |
| Random | Good average case |
| Median-of-three | Middle of first, middle, last |

## Key Properties
- Fastest in practice (cache efficient)
- In-place (unlike merge sort)
- Worst case O(n²) with bad pivots
- Not stable

> **Exam Tip**: Quick sort is fastest on average but O(n²) worst case. Use randomized pivot to avoid worst case.
