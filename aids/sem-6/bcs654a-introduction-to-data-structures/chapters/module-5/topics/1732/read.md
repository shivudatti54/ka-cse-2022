# 17.3.2 Insertion Sort

=====================================================

## Introduction

---

Insertion sort is a simple sorting algorithm that works by dividing the input into a sorted and an unsorted region. Each subsequent element from the unsorted region is inserted into the sorted region in its correct position.

## How Insertion Sort Works

---

### Step 1: Initialize the sorted region

- Start with the first element of the input array as the sorted region.
- The remaining elements are initially considered part of the unsorted region.

### Step 2: Iterate through the unsorted region

- For each element in the unsorted region:
  - Compare the current element with the first element of the sorted region.
  - If the current element is smaller, shift the first element of the sorted region to the right.
  - Insert the current element into the correct position in the sorted region.

### Example Walkthrough

---

Suppose we have the following input array:

| Index | Element |
| ----- | ------- |
| 0     | 5       |
| 1     | 2       |
| 2     | 8       |
| 3     | 3       |
| 4     | 1       |

**Step 1:** Initialize the sorted region with the first element (5).

| Index | Element | Sorted Region   |
| ----- | ------- | --------------- |
| 0     | 5       | [5]             |
| 1     | 2       | [5, 2]          |
| 2     | 8       | [5, 2, 8]       |
| 3     | 3       | [5, 2, 8, 3]    |
| 4     | 1       | [5, 2, 8, 3, 1] |

**Step 2:** Iterate through the unsorted region (starting from the second element).

- Compare 2 with the first element of the sorted region (5). Since 2 is smaller, shift 5 to the right and insert 2 into the correct position.
-
- Compare 8 with the first element of the sorted region (5). Since 8 is larger, no shift is needed.
-
- Compare 3 with the first element of the sorted region (5). Since 3 is smaller, shift 5 to the right and insert 3 into the correct position.
-
- Compare 1 with the first element of the sorted region (5). Since 1 is smaller, shift 5 to the right and insert 1 into the correct position.

| Index | Element | Sorted Region   |
| ----- | ------- | --------------- |
| 0     | 5       | [5]             |
| 1     | 2       | [2, 5]          |
| 2     | 8       | [2, 5, 8]       |
| 3     | 3       | [2, 3, 5, 8]    |
| 4     | 1       | [1, 2, 3, 5, 8] |

The sorted array is now complete.

## Time and Space Complexity

---

### Time Complexity:

- Best-case: O(n) (when the input is already sorted)
- Average-case: O(n^2)
- Worst-case: O(n^2) (when the input is reverse sorted)

### Space Complexity: O(1)

Insertion sort requires a single additional pointer to keep track of the current element being inserted into the sorted region. The space complexity is therefore constant.

## Advantages and Disadvantages

---

### Advantages:

- Simple to implement
- Stable sorting algorithm (preserves the order of equal elements)
- Can be efficient for small datasets

### Disadvantages:

- Not suitable for large datasets due to its quadratic time complexity
- Not efficient for datasets with a large number of unique elements

## Real-World Applications

---

Insertion sort is commonly used in:

- Small datasets or nearly sorted data
- Real-time systems where predictability and simplicity are crucial
- Embedded systems with limited resources

However, for larger datasets, other sorting algorithms like quicksort, mergesort, or heapsort are generally more efficient.
