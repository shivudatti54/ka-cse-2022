# Insertion Sort

## Concept

Build sorted array one element at a time by inserting each element into its correct position.

## Algorithm

```
for i = 1 to n-1:
 key = arr[i]
 j = i - 1
 while j >= 0 and arr[j] > key:
 arr[j+1] = arr[j]
 j = j - 1
 arr[j+1] = key
```

## Complexity

| Case    | Time  | Space |
| ------- | ----- | ----- |
| Best    | O(n)  | O(1)  |
| Average | O(n²) | O(1)  |
| Worst   | O(n²) | O(1)  |

**Stable**: Yes | **In-place**: Yes | **Adaptive**: Yes

## Key Properties

- Best for small arrays (n < 50)
- Efficient for nearly sorted arrays
- Online algorithm (can sort as data arrives)
- Used in hybrid algorithms (Timsort, Introsort)

> **Exam Tip**: Insertion sort is O(n) for nearly sorted data. Often used as base case in Merge/Quick sort.
