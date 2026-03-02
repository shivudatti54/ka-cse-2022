# Selection Sort

## Concept

Find the minimum element in unsorted portion and swap with first unsorted position.

## Algorithm

```
for i = 0 to n-1:
 minIdx = i
 for j = i+1 to n-1:
 if arr[j] < arr[minIdx]:
 minIdx = j
 swap(arr[i], arr[minIdx])
```

## Complexity

| Case    | Time  | Space |
| ------- | ----- | ----- |
| Best    | O(n²) | O(1)  |
| Average | O(n²) | O(1)  |
| Worst   | O(n²) | O(1)  |

**Stable**: No | **In-place**: Yes | **Adaptive**: No

## Key Properties

- Always makes exactly n-1 swaps
- Useful when writes are expensive
- Not stable (can be made stable with modification)

> **Exam Tip**: Selection sort minimizes swaps (n-1). Good when writing to memory is costly.
