# **BRUTE FORCE APPROACHES: Selection Sort and Bubble Sort**

## **Introduction**

In algorithmic problem solving, a brute force approach is a simple and straightforward method to solve a problem. This approach involves trying all possible solutions to the problem until the correct one is found. While brute force methods can be simple to understand and implement, they often have a high time and space complexity, making them inefficient for large datasets.

## **Selection Sort**

### Definition

Selection sort is a brute force sorting algorithm that works by dividing the input into a sorted and an unsorted region. Each iteration, the smallest element from the unsorted region is swapped with the first element of the unsorted region.

### How it Works

1.  Start from the first element of the array.
2.  Find the smallest element in the unsorted region (from the second element to the last element).
3.  Swap the smallest element with the first element of the unsorted region.
4.  Repeat steps 1-3 until the entire array is sorted.

### Example

Suppose we have the following array: `[64, 25, 12, 22, 11]`

1.  Start from the first element (`64`). The smallest element in the unsorted region is `11`.
2.  Swap `64` with `11`: `[11, 25, 12, 22, 64]`
3.  Start from the first element (`11`). The smallest element in the unsorted region is `12`.
4.  Swap `11` with `12`: `[11, 12, 25, 22, 64]`
5.  Start from the first element (`11`). The smallest element in the unsorted region is `22`.
6.  Swap `11` with `22`: `[11, 12, 22, 25, 64]`
7.  Start from the first element (`11`). The smallest element in the unsorted region is `25`.
8.  Swap `11` with `25`: `[11, 12, 22, 25, 64]`
9.  Start from the first element (`11`). The smallest element in the unsorted region is `64`.
10. Swap `11` with `64`: `[11, 12, 22, 25, 64]`
11. Start from the first element (`11`). The smallest element in the unsorted region is `64`.
12. Swap `11` with `64`: `[11, 12, 22, 25, 64]` (already sorted)

### Time Complexity

- Best-case: O(n)
- Average-case: O(n^2)
- Worst-case: O(n^2)

### Space Complexity

- O(1)

### Implementation

```python
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
```

## **Bubble Sort**

### Definition

Bubble sort is a brute force sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.

### How it Works

1.  Start from the first element of the array.
2.  Compare the current element with the next element.
3.  If the current element is greater than the next element, swap them.
4.  Repeat steps 1-3 until the entire array is sorted.

### Example

Suppose we have the following array: `[64, 25, 12, 22, 11]`

1.  Start from the first element (`64`). Compare `64` with `25`. Since `64` is greater than `25`, swap them: `[25, 64, 12, 22, 11]`
2.  Start from the first element (`25`). Compare `25` with `12`. Since `25` is greater than `12`, swap them: `[12, 25, 64, 22, 11]`
3.  Start from the first element (`12`). Compare `12` with `22`. Since `12` is less than `22`, no swap: `[12, 25, 64, 22, 11]`
4.  Start from the first element (`12`). Compare `12` with `11`. Since `12` is greater than `11`, swap them: `[11, 12, 64, 22, 25]`
5.  Start from the first element (`11`). Compare `11` with `22`. Since `11` is less than `22`, no swap: `[11, 12, 64, 22, 25]`
6.  Start from the first element (`11`). Compare `11` with `25`. Since `11` is less than `25`, no swap: `[11, 12, 64, 22, 25]`
7.  Start from the first element (`11`). Compare `11` with `64`. Since `11` is less than `64`, no swap: `[11, 12, 64, 22, 25]`
8.  Start from the first element (`11`). Compare `11` with `22`. Since `11` is less than `22`, no swap: `[11, 12, 64, 22, 25]`
9.  Start from the first element (`11`). Compare `11` with `25`. Since `11` is less than `25`, no swap: `[11, 12, 64, 22, 25]`
10. Start from the first element (`11`). Compare `11` with `64`. Since `11` is less than `64`, no swap: `[11, 12, 64, 22, 25]`
11. Start from the first element (`11`). Compare `11` with `22`. Since `11` is less than `22`, no swap: `[11, 12, 64, 22, 25]`
12. Start from the first element (`11`). Compare `11` with `25`. Since `11` is less than `25`, no swap: `[11, 12, 64, 22, 25]`
13. Start from the first element (`11`). Compare `11` with `64`. Since `11` is less than `64`, no swap: `[11, 12, 64, 22, 25]`
14. Start from the first element (`11`). Compare `11` with `22`. Since `11` is less than `22`, no swap: `[11, 12, 64, 22, 25]`
15. Start from the first element (`11`). Compare `11` with `25`. Since `11` is less than `25`, no swap: `[11, 12, 64, 22, 25]`
16. Start from the first element (`11`). Compare `11` with `64`. Since `11` is less than `64`, no swap: `[11, 12, 64, 22, 25]`
17. Start from the first element (`11`). Compare `11` with `22`. Since `11` is less than `22`, no swap: `[11, 12, 64, 22, 25]`
18. Start from the first element (`11`). Compare `11` with `25`. Since `11` is less than `25`, no swap: `[11, 12, 64, 22, 25]`
19. Start from the first element (`11`). Compare `11` with `64`. Since `11` is less than `64`, no swap: `[11, 12, 64, 22, 25]`
20. Start from the first element (`11`). Compare `11` with `22`. Since `11` is less than `22`, no swap: `[11, 12, 64, 22, 25]`
21. Start from the first element (`11`). Compare `11` with `25`. Since `11` is less than `25`, no swap: `[11, 12, 64, 22, 25]`
22. Start from the first element (`11`). Compare `11` with `64`. Since `11` is less than `64`, no swap: `[11, 12, 64, 22, 25]`
    The array is already sorted: `[11, 12, 22, 25, 64]`

### Time Complexity

- Best-case: O(n)
- Average-case: O(n^2)
- Worst-case: O(n^2)

### Space Complexity

- O(1)

### Implementation

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
```

## **Comparison**

| Algorithm      | Best-case | Average-case | Worst-case | Space Complexity |
| -------------- | --------- | ------------ | ---------- | ---------------- |
| Selection Sort | O(n)      | O(n^2)       | O(n^2)     | O(1)             |
| Bubble Sort    | O(n)      | O(n^2)       | O(n^2)     | O(1)             |
