# 17.3.2 Insertion Sort

=====================================

## Introduction

---

Insertion sort is a simple sorting algorithm that works by dividing the input into a sorted and an unsorted region. Each subsequent element from the unsorted region is inserted into the sorted region in its correct position.

## How Insertion Sort Works

---

Here's a step-by-step explanation of the insertion sort algorithm:

1.  **Start with the first element**: The first element is already in its sorted position, so we can move on to the next element.
2.  **Compare with previous elements**: Compare the current element with the elements in the sorted region.
3.  **Shift elements to make room**: If the current element is smaller than the elements in the sorted region, shift those elements to the right to make room for the current element.
4.  **Insert the current element**: Insert the current element into the correct position in the sorted region.
5.  **Repeat the process**: Repeat the process for the remaining elements in the unsorted region.

## Example

---

Suppose we want to sort the following list of integers using insertion sort:

```
5 2 8 3 1 6 4
```

Here's how the insertion sort algorithm would work:

1.  Start with the first element: `5`
2.  Compare with previous elements: `5` is greater than `2`, so we move on to the next element.
3.  Compare with previous elements: `5` is greater than `8`, so we move on to the next element.
4.  Compare with previous elements: `5` is greater than `3`, so we move on to the next element.
5.  Compare with previous elements: `5` is greater than `1`, so we move on to the next element.
6.  Compare with previous elements: `5` is greater than `6`, so we move on to the next element.
7.  Compare with previous elements: `5` is greater than `4`, so we move on to the next element.

Here's the updated list after each step:

```
5
2 5
8 5
3 5
1 5
6 5
4 5
```

8.  Insert the last element: `1` is the smallest element, so we insert it at the beginning of the sorted region.

```
1 2 3 4 5 6 8
```

## Implementation

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

# Test the implementation
arr = [5, 2, 8, 3, 1, 6, 4]
print("Original array:", arr)
print("Sorted array:", insertion_sort(arr))
```

## Time Complexity

---

The time complexity of insertion sort is O(n^2), where n is the number of elements in the input array. This is because we need to compare each element with every other element in the array.

## Space Complexity

---

The space complexity of insertion sort is O(1), because we only need a single additional memory space to store the key element.

## Advantages and Disadvantages

---

Advantages:

- Insertion sort is a stable sorting algorithm, meaning that the order of equal elements is preserved.
- Insertion sort is relatively simple to implement.
- Insertion sort can be used for small datasets.

Disadvantages:

- Insertion sort has a high time complexity of O(n^2), making it less efficient for large datasets.
- Insertion sort is not suitable for datasets with many duplicate elements.

## Conclusion

---

Insertion sort is a simple sorting algorithm that works by dividing the input into a sorted and an unsorted region. While it has some advantages, such as being stable and relatively simple to implement, it also has some disadvantages, such as having a high time complexity. However, it can still be useful for small datasets or datasets with many duplicate elements.
