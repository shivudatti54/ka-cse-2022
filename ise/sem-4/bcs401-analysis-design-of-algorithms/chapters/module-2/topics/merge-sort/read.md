# Merge Sort

## Concept

Divide and conquer: Split array in half, recursively sort both halves, merge sorted halves.

## Algorithm

```
mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) / 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)
        merge(arr, left, mid, right)
```

## Complexity

| Case    | Time       | Space |
| ------- | ---------- | ----- |
| Best    | O(n log n) | O(n)  |
| Average | O(n log n) | O(n)  |
| Worst   | O(n log n) | O(n)  |

**Stable**: Yes | **In-place**: No | **Adaptive**: No

## Key Properties

- Guaranteed O(n log n) - no bad cases
- Stable sorting
- Good for linked lists (no random access needed)
- External sorting (large files)

## Merge Operation

```
Compare first elements of both halves
Take smaller, advance that pointer
Repeat until one half exhausted
Copy remaining elements
```

> **Exam Tip**: Merge sort is guaranteed O(n log n) and stable. Extra O(n) space is the trade-off.
