# Bubble Sort

## Concept

Compare adjacent elements and swap if out of order. Largest elements "bubble up" to the end.

## Algorithm

```
for i = 0 to n-1:
 for j = 0 to n-i-2:
 if arr[j] > arr[j+1]:
 swap(arr[j], arr[j+1])
```

## Complexity

| Case    | Time  | Space |
| ------- | ----- | ----- |
| Best    | O(n)  | O(1)  |
| Average | O(n²) | O(1)  |
| Worst   | O(n²) | O(1)  |

**Stable**: Yes | **In-place**: Yes | **Adaptive**: Yes (with optimization)

## Optimization

Add a flag to detect if no swaps occurred (array already sorted):

```
swapped = false
for j = 0 to n-i-2:
 if arr[j] > arr[j+1]:
 swap; swapped = true
if not swapped: break
```

## When to Use

- Educational purposes
- Very small arrays
- Nearly sorted arrays (with optimization)

> **Exam Tip**: Bubble sort makes n-1 passes. After i passes, last i elements are sorted.
