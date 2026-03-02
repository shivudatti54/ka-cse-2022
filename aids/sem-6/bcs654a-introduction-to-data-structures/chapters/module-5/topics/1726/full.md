# 17.2.6: Merge Sort

=====================================

## Introduction

---

Merge Sort is a popular sorting algorithm that uses the divide-and-conquer technique to sort elements in an array. It is known for its efficiency, stability, and ease of implementation. In this section, we will delve into the world of Merge Sort, exploring its historical context, working principles, and applications.

## Historical Context

---

Merge Sort was first proposed by John von Neumann in 1945 as a part of his work on the EDVAC computer. However, it wasn't until the 1960s that the algorithm gained popularity due to its efficiency and stability. Since then, Merge Sort has become a fundamental algorithm in computer science, used in a wide range of applications.

## Working Principles

---

Merge Sort works by dividing the input array into smaller subarrays, sorting each subarray individually, and then merging the sorted subarrays back together. The algorithm uses a divide-and-conquer approach, recursively splitting the array into two halves until each subarray contains only one element. The sorted subarrays are then merged using a temporary array.

### Step 1: Divide

The first step in Merge Sort is to divide the input array into two halves. This is done by selecting a pivot element and partitioning the array around it. The elements less than the pivot are placed in the left subarray, and the elements greater than the pivot are placed in the right subarray.

### Step 2: Conquer

Once the array is divided, the algorithm recursively calls itself on each subarray. This process continues until each subarray contains only one element. At this point, the subarray is considered sorted.

### Step 3: Merge

The final step is to merge the sorted subarrays back together. This is done using a temporary array, where the elements from each subarray are alternately placed. The algorithm continues until the entire array is sorted.

## Algorithm

---

Here is a step-by-step representation of the Merge Sort algorithm:

1.  If the array has only one element, return the array (since it is already sorted).
2.  Select a pivot element and partition the array around it.
3.  Recursively call Merge Sort on the left and right subarrays.
4.  Merge the sorted subarrays back together using a temporary array.

### Example

---

Suppose we have the following array: `[5, 2, 8, 3, 1, 6, 4]`

1.  Divide the array into two halves: `[5, 2, 8]` and `[3, 1, 6, 4]`
2.  Recursively call Merge Sort on each subarray:
    - `[5, 2, 8]` -> `[5, 2]` and `[8]`
    - `[3, 1, 6, 4]` -> `[3, 1]` and `[6, 4]`
3.  Merge the sorted subarrays back together:
    - `[5, 2]` and `[8]` -> `[2, 5, 8]`
    - `[3, 1]` and `[6, 4]` -> `[1, 3, 4, 6]`
4.  Merge the two sorted arrays: `[2, 5, 8]` and `[1, 3, 4, 6]` -> `[1, 2, 3, 4, 5, 6, 8]`

## Time and Space Complexity

---

Merge Sort has a time complexity of O(n log n) in all cases (best, average, and worst). The space complexity is O(n), which is the space required for the temporary array used during the merge process.

## Applications

---

Merge Sort has a wide range of applications in computer science, including:

- Sorting large datasets
- Data compression
- Database indexing
- Compilers and interpreters

## Code Implementation

---

Here is a Python implementation of the Merge Sort algorithm:

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# Example usage
arr = [5, 2, 8, 3, 1, 6, 4]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # [1, 2, 3, 4, 5, 6, 8]
```

## Further Reading

---

- "Introduction to Algorithms" by Thomas H. Cormen
- "Algorithms" by Robert Sedgewick and Kevin Wayne
- "Merge Sort" by Wikipedia (https://en.wikipedia.org/wiki/Merge_sort)

Note: The above code is a Python implementation of the Merge Sort algorithm. It uses a recursive approach to sort the array. The time complexity of this implementation is O(n log n), which is the expected time complexity of the Merge Sort algorithm.
