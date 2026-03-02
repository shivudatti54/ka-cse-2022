# 17.3.2 Introduction to Insertion Sort

=====================================

## Overview

---

Insertion sort is a simple sorting algorithm that works by dividing the input into a sorted and an unsorted region. Each subsequent element from the unsorted region is inserted into the sorted region in its correct position.

## How Insertion Sort Works

---

### Step 1: Divide the Input into Sorted and Unsorted Regions

- The input is divided into two regions: a sorted region and an unsorted region.
- The sorted region is initially empty, and the unsorted region contains all the elements of the input.

### Step 2: Iterate through the Unsorted Region

- The algorithm iterates through each element in the unsorted region.
- For each element, the algorithm checks where it should be inserted in the sorted region to maintain sorted order.

### Step 3: Insert the Element into the Sorted Region

- The element is inserted into the sorted region in its correct position.
- This process continues until the entire unsorted region has been processed.

## Example Walkthrough

---

Suppose we have the following input array: `[5, 2, 8, 3, 1, 4]`

### Step 1: Divide the Input into Sorted and Unsorted Regions

- Sorted region: `[]`
- Unsorted region: `[5, 2, 8, 3, 1, 4]`

### Step 2: Iterate through the Unsorted Region and Insert Elements into the Sorted Region

- Iterate through the unsorted region and insert each element into the sorted region in its correct position:
  - Insert `2` into the sorted region: `[2]`
  - Insert `5` into the sorted region: `[2, 5]`
  - Insert `3` into the sorted region: `[2, 3, 5]`
  - Insert `1` into the sorted region: `[1, 2, 3, 5]`
  - Insert `4` into the sorted region: `[1, 2, 3, 4, 5]`

### Step 3: The Entire Unsorted Region has been Processed

- The entire unsorted region has been processed, and the input array is now sorted: `[1, 2, 3, 4, 5]`

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
arr = [5, 2, 8, 3, 1, 4]
sorted_arr = insertion_sort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 4, 5]
```

## Time Complexity

---

- Best-case time complexity: O(n)
- Average-case time complexity: O(n^2)
- Worst-case time complexity: O(n^2)

## Space Complexity

---

- Space complexity: O(1)

## Advantages and Disadvantages

---

Advantages:

- Insertion sort is a stable sorting algorithm, which means that the order of equal elements is preserved.
- Insertion sort is simple to implement and understand.
- Insertion sort is suitable for small datasets.

Disadvantages:

- Insertion sort has a high time complexity for large datasets, making it less efficient than other sorting algorithms like quicksort or mergesort.
- Insertion sort requires additional space for the temporary storage of elements during the sorting process.

## Conclusion

---

Insertion sort is a simple and efficient sorting algorithm that works by dividing the input into a sorted and an unsorted region. While it has some disadvantages, insertion sort is suitable for small datasets and has many advantages, including being stable and easy to implement.
