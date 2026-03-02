# **17.2.6 Insertion Sort**

## **Introduction**

Insertion sort is a simple sorting algorithm that works by dividing the input into a sorted and an unsorted region. Each subsequent element from the unsorted region is inserted into the sorted region in its correct position.

## **How Insertion Sort Works**

The algorithm can be broken down into the following steps:

- Start with the first element of the unsorted region.
- Compare the current element with the elements in the sorted region.
- Insert the current element into the sorted region at its correct position.
- Move to the next element in the unsorted region and repeat the process.

### Example

Suppose we have the following unsorted array: `[5, 2, 8, 3, 1, 6]`.

- Start with the first element `5`.
- Compare `5` with the sorted region `[ ]`. Since `5` is the first element, it is inserted into the sorted region.
- Move to the next element `2` and compare it with the sorted region `[5]`. Since `2` is smaller than `5`, it is inserted into the sorted region at the beginning.
- Move to the next element `8` and compare it with the sorted region `[2, 5]`. Since `8` is greater than `5`, it is inserted into the sorted region at the end.
- Move to the next element `3` and compare it with the sorted region `[2, 5, 8]`. Since `3` is between `2` and `5`, it is inserted into the sorted region at the correct position.
- Move to the next element `1` and compare it with the sorted region `[2, 3, 5, 8]`. Since `1` is smaller than `2`, it is inserted into the sorted region at the beginning.
- Move to the next element `6` and compare it with the sorted region `[1, 2, 3, 5, 8]`. Since `6` is greater than `5`, it is inserted into the sorted region at the end.

The final sorted array is `[1, 2, 3, 5, 6, 8]`.

### Time Complexity

The time complexity of insertion sort is:

- Best-case: O(n)
- Average-case: O(n^2)
- Worst-case: O(n^2)

### Space Complexity

The space complexity of insertion sort is O(1), since it only requires a single additional memory space for the temporary variable used to store the current element.

### Code Implementation

Here is an example implementation of insertion sort in Python:

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Test the implementation
arr = [5, 2, 8, 3, 1, 6]
print(insertion_sort(arr))  # Output: [1, 2, 3, 5, 6, 8]
```

### Advantages

- Insertion sort is a stable sorting algorithm, meaning that equal elements will maintain their original order.
- Insertion sort is a simple algorithm to implement, especially for small arrays.
- Insertion sort is an in-place sorting algorithm, meaning that it does not require any additional memory space.

### Disadvantages

- Insertion sort has a high time complexity, especially for large arrays.
- Insertion sort is not suitable for real-time systems, where speed is critical.

### Use Cases

- Insertion sort is suitable for small arrays or nearly sorted arrays.
- Insertion sort is suitable for systems where memory is limited.
- Insertion sort can be used as a building block for more complex sorting algorithms.
