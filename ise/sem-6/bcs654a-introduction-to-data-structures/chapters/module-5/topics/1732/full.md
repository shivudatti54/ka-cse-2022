# 17.3.2: Merge Sort

=====================================

## Introduction

---

Merge sort is a popular and efficient sorting algorithm that uses a divide-and-conquer approach to sort lists of elements. It is known for its stability, simplicity, and efficiency, making it a widely used algorithm in many applications.

## History

---

Merge sort was first proposed by John von Neumann in 1945 as part of a more general algorithm for sorting large lists of numbers. However, it was not until the 1950s that the algorithm was further developed and implemented.

## How Merge Sort Works

---

Merge sort works by dividing the list of elements into smaller sublists, sorting each sublist recursively, and then merging the sorted sublists back together to form the final sorted list.

Here is a step-by-step overview of the merge sort algorithm:

1.  If the list has only one element, return the list (since it is already sorted).
2.  Divide the list into two halves, `left` and `right`.
3.  Recursively sort `left` and `right`.
4.  Merge the sorted `left` and `right` halves into a single sorted list.

The merge step involves comparing elements from `left` and `right` and placing the smaller element into the merged list.

## Example: Merge Sort Algorithm

---

Suppose we have the following list of elements: `[5, 2, 8, 3, 1, 6, 4]`.

Here is how merge sort would sort this list:

1.  Divide the list into two halves: `[5, 2, 8]` and `[3, 1, 6, 4]`.
2.  Recursively sort each half:
    - `[5, 2, 8]` becomes `[2, 5, 8]`.
    - `[3, 1, 6, 4]` becomes `[1, 3, 4, 6]`.
3.  Merge the sorted halves: `[2, 5, 8]` and `[1, 3, 4, 6]`.
    - Compare `2` and `1`: `1` is smaller, so add `1` to the merged list.
    - Compare `2` and `3`: `2` is smaller, so add `2` to the merged list.
    - Compare `2` and `4`: `2` is smaller, so add `2` to the merged list.
    - Compare `2` and `6`: `2` is smaller, so add `2` to the merged list.
    - Compare `5` and `1`: `1` is smaller, so add `1` to the merged list.
    - Compare `5` and `3`: `3` is smaller, so add `3` to the merged list.
    - Compare `5` and `4`: `4` is smaller, so add `4` to the merged list.
    - Compare `5` and `6`: `5` is smaller, so add `5` to the merged list.
    - Add the remaining elements (`8`) to the end of the merged list.
4.  The final sorted list is: `[1, 2, 3, 4, 5, 6, 8]`.

## Time and Space Complexity

---

Merge sort has a time complexity of O(n log n) in the worst case, making it one of the most efficient sorting algorithms for large datasets.

The space complexity of merge sort is O(n), as we need to create temporary lists to store the sorted halves.

## Applications

---

Merge sort is widely used in many applications, including:

- Database sorting: Merge sort is often used to sort large databases of data.
- File systems: Merge sort is used in some file systems to sort files and directories.
- Web search engines: Merge sort is used to sort search results.
- Data analytics: Merge sort is used in data analytics to sort large datasets.

## Implementation

---

Here is an example implementation of merge sort in Python:

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    merged = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(left)
    merged.extend(right)
    return merged

# Example usage:
arr = [5, 2, 8, 3, 1, 6, 4]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # [1, 2, 3, 4, 5, 6, 8]
```

## Further Reading

---

- "Introduction to Algorithms" by Thomas H. Cormen
- "The Algorithm Design Manual" by Steven S. Skiena
- "Merge Sort" by Wikipedia

Note: This is a comprehensive guide to merge sort, covering its history, algorithm, time and space complexity, applications, implementation, and further reading.
