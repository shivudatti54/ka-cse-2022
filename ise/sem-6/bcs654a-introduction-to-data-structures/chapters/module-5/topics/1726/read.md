# 17.2.6 Insertion Sort

=====================================

## Introduction

---

Insertion sort is a simple sorting algorithm that works by dividing the input into a sorted and an unsorted region. Each subsequent element from the unsorted region is inserted into the sorted region at its correct position.

## How Insertion Sort Works

---

### Step 1: Initialize the Sorted Region

- Start with the first element of the unsorted region as the sorted region.
- The first element is considered sorted.

### Step 2: Iterate Through the Unsorted Region

- For each element in the unsorted region (starting from the second element):
  - Compare the current element with the elements in the sorted region.
  - Shift elements in the sorted region that are greater than the current element to the right.
  - Insert the current element into the sorted region at its correct position.

### Step 3: Repeat Until the Entire Unsorted Region is Sorted

- Continue iterating through the unsorted region until all elements have been sorted.

## Example

---

Suppose we have the following unsorted array:

```
[5, 2, 8, 3, 1, 4, 6]
```

### Step 1: Initialize the Sorted Region

- The first element (5) is considered sorted.

```
Sorted: [5]
Unsorted: [2, 8, 3, 1, 4, 6]
```

### Step 2: Iterate Through the Unsorted Region

- Compare the second element (2) with the sorted region:
  - Shift elements in the sorted region that are greater than 2 to the right.
  - Insert 2 into the sorted region at its correct position.

```
Sorted: [2, 5]
Unsorted: [8, 3, 1, 4, 6]
```

- Compare the third element (8) with the sorted region:
  - Shift elements in the sorted region that are greater than 8 to the right.
  - Insert 8 into the sorted region at its correct position.

```
Sorted: [2, 5, 8]
Unsorted: [3, 1, 4, 6]
```

- Compare the fourth element (3) with the sorted region:
  - Shift elements in the sorted region that are greater than 3 to the right.
  - Insert 3 into the sorted region at its correct position.

```
Sorted: [2, 3, 5, 8]
Unsorted: [1, 4, 6]
```

- Compare the fifth element (1) with the sorted region:
  - Shift elements in the sorted region that are greater than 1 to the right.
  - Insert 1 into the sorted region at its correct position.

```
Sorted: [1, 2, 3, 5, 8]
Unsorted: [4, 6]
```

- Compare the sixth element (4) with the sorted region:
  - Shift elements in the sorted region that are greater than 4 to the right.
  - Insert 4 into the sorted region at its correct position.

```
Sorted: [1, 2, 3, 4, 5, 8]
Unsorted: [6]
```

- Compare the seventh element (6) with the sorted region:
  - Shift elements in the sorted region that are greater than 6 to the right.
  - Insert 6 into the sorted region at its correct position.

```
Sorted: [1, 2, 3, 4, 5, 6, 8]
```

The array is now sorted.

## Code Implementation

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
arr = [5, 2, 8, 3, 1, 4, 6]
print("Original array:", arr)
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
```

## Time Complexity

---

The time complexity of insertion sort is:

- Best-case: O(n)
- Average-case: O(n^2)
- Worst-case: O(n^2)

## Space Complexity

---

The space complexity of insertion sort is O(1), as it only uses a single additional array to store the sorted elements.

## Advantages

---

- Insertion sort is simple to implement and understand.
- It has a best-case time complexity of O(n), making it suitable for nearly sorted data.

## Disadvantages

---

- Insertion sort has an average-case and worst-case time complexity of O(n^2), making it less efficient for large datasets.
- It is not a stable sorting algorithm, meaning that equal elements may not maintain their original order.
