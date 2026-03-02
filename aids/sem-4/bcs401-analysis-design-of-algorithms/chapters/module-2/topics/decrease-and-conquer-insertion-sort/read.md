# DECREASE-AND-CONQUER: Insertion Sort

=====================================

## Overview

---

### Introduction

Insertion Sort is a simple sorting algorithm that works by dividing the input into a sorted and an unsorted region. Each subsequent element from the unsorted region is inserted into the sorted region in its correct position. The algorithm is efficient for small data sets and has a time complexity of O(n^2), making it suitable for scenarios where the data size is relatively small.

### Key Concepts

- **Insertion Sort Algorithm:**
  - Works by iterating through the input array one element at a time.
  - For each element, it shifts all elements greater than the current element to the right.
  - Then, it inserts the current element into its correct position within the sorted portion of the array.
- **Decrease and Conquer:** This approach involves dividing the problem into smaller sub-problems and solving each one recursively.

## How Insertion Sort Works

---

### Step-by-Step Explanation

1.  **Start at the beginning of the array**: Begin with the first element, which is already sorted.
2.  **Compare the current element with the next element**: Compare the current element with the next element in the unsorted region.
3.  **Shift elements to the right until the correct position is found**: If the next element is greater than the current element, shift it to the right until a smaller element is found.
4.  **Insert the current element into its correct position**: Insert the current element into the sorted region at its correct position.
5.  **Repeat the process for the remaining elements**: Repeat steps 2-4 for the remaining elements in the unsorted region.

## Example Walkthrough

---

Suppose we have an array of integers `[5, 2, 8, 1, 9]`. We'll perform insertion sort on this array.

1.  Start with the first element `5`.
2.  Compare `5` with `2`. Since `2` is smaller, shift `5` to the right.
    - Unsorted region: `[5, 8, 1, 9]`
    - Sorted region: `[]`
3.  Compare `2` with `8`. Since `8` is greater, shift `2` to the right.
    - Unsorted region: `[5, 8, 9]`
    - Sorted region: `[5, 2]`
4.  Compare `2` with `1`. Since `1` is smaller, shift `2` to the right.
    - Unsorted region: `[5, 8, 9]`
    - Sorted region: `[5, 2, 1]`
5.  Compare `1` with `9`. Since `9` is greater, shift `1` to the right.
    - Unsorted region: `[5, 8]`
    - Sorted region: `[5, 2, 1, 9]`
6.  Insert `9` into its correct position.
    - Unsorted region: `[]`
    - Sorted region: `[5, 2, 1, 9]`
7.  Repeat the process for the remaining elements (`8`).
8.  Insert `8` into its correct position.
    - Unsorted region: `[]`
    - Sorted region: `[5, 2, 1, 8, 9]`
9.  The array is now sorted.

## Implementation

---

Here is a Python implementation of the insertion sort algorithm:

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
arr = [5, 2, 8, 1, 9]
sorted_arr = insertion_sort(arr)
print(sorted_arr)  # Output: [1, 2, 5, 8, 9]
```

## Time Complexity

---

The time complexity of insertion sort is O(n^2), making it less efficient than other sorting algorithms like quicksort or mergesort for large data sets. However, it has the advantage of being simple to implement and having a low overhead in terms of extra memory required.

## Space Complexity

---

The space complexity of insertion sort is O(1), as it only requires a single additional memory space to store the temporary key variable.
