# 17.2.6 Insertion Sort

=====================================

## Table of Contents

- [Introduction](#introduction)
- [How Insertion Sort Works](#how-insertion-sort-works)
- [Algorithm Steps](#algorithm-steps)
- [Example Implementation](#example-implementation)
- [Time and Space Complexity](#time-and-space-complexity)
- [Advantages and Disadvantages](#advantages-and-disadvantages)

## Introduction

---

Insertion sort is a simple sorting algorithm that works by dividing the input list into a sorted and an unsorted region. Each subsequent element from the unsorted region is inserted into the sorted region in its correct position.

## How Insertion Sort Works

---

Insertion sort works by iterating through the list one element at a time, inserting each element into its correct position in the sorted region. Here's a step-by-step breakdown of the algorithm:

1.  Start with the first element, which is already sorted.
2.  Iterate through the remaining elements, comparing each element to the previous elements in the sorted region.
3.  For each element, find its correct position in the sorted region by shifting elements to make room for it.
4.  Insert the element into its correct position in the sorted region.
5.  Repeat steps 2-4 until the entire list is sorted.

## Algorithm Steps

---

Here are the algorithm steps for insertion sort:

1.  Initialize the sorted region with the first element.
2.  Iterate through the remaining elements.
3.  For each element, find its correct position in the sorted region.
4.  Shift elements to make room for the element.
5.  Insert the element into its correct position.
6.  Repeat steps 2-5 until the entire list is sorted.

## Example Implementation

---

Here's an example implementation of insertion sort in Python:

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
arr = [5, 2, 8, 3, 1, 6, 4]
sorted_arr = insertion_sort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 4, 5, 6, 8]
```

## Time and Space Complexity

---

The time complexity of insertion sort is O(n^2) in the worst-case scenario, where n is the number of elements in the list. However, in the best-case scenario (when the input list is already sorted), the time complexity is O(n).

The space complexity of insertion sort is O(1), as it only uses a constant amount of additional memory to store the key and indices.

## Advantages and Disadvantages

---

**Advantages:**

- **Simple implementation**: Insertion sort has a relatively simple implementation compared to other sorting algorithms.
- **Stable**: Insertion sort is a stable sorting algorithm, meaning that equal elements will maintain their original order.

**Disadvantages:**

- **Slow performance**: Insertion sort has a time complexity of O(n^2) in the worst-case scenario, making it slower than other algorithms like quicksort or mergesort for large datasets.
- **Not efficient for large datasets**: Insertion sort is not suitable for large datasets due to its high time complexity.

In summary, insertion sort is a simple and stable sorting algorithm that works well for small datasets or nearly sorted lists. However, it's not efficient for large datasets due to its high time complexity.
