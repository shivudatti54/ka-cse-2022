# **DECREASE-AND-CONQUER: Insertion Sort**

## **Introduction**

Insertion Sort is a simple sorting algorithm that works by dividing the input into a sorted and an unsorted region. Each subsequent element from the unsorted region is inserted into the sorted region in its correct position. This algorithm is efficient for small data sets and is often used as a teaching tool due to its simplicity.

## **How Insertion Sort Works**

### Decrease-and-Conquer Approach

Insertion Sort can be viewed as a decrease-and-conquer algorithm, where we repeatedly divide the input into two regions: a sorted region and an unsorted region. We then compare elements from the unsorted region with the sorted region and shift elements in the sorted region that are greater than the current element to the right. This process continues until the entire input is sorted.

### Step-by-Step Process

Here are the steps involved in the Insertion Sort algorithm:

1.  **Initialize the sorted region**: Start with the first element as the sorted region.
2.  **Iterate through the unsorted region**: Iterate through the remaining elements in the input, considering each one as the next element to be inserted into the sorted region.
3.  **Compare and shift**: Compare the current element with the elements in the sorted region. If the current element is smaller, shift the larger elements to the right to make space for it.
4.  **Insert the element**: Insert the current element into the correct position in the sorted region.
5.  **Repeat**: Repeat steps 2-4 until the entire input is sorted.

## **Example**

Suppose we want to sort the following list using Insertion Sort:

```
[5, 2, 8, 3, 1, 4, 6]
```

Here's how the algorithm works:

1.  Initialize the sorted region: `[5]`
2.  Iterate through the unsorted region: `2, 8, 3, 1, 4, 6`
3.  Compare and shift:
    - Compare `2` with `5`: shift `5` to the right
    - Compare `8` with `5` and `2`: shift `5` and `2` to the right
    - Compare `3` with `5`, `2`, and `8`: shift `5`, `2`, and `8` to the right
    - Compare `1` with `5`, `2`, `8`, and `3`: shift `5`, `2`, `8`, and `3` to the right
    - Compare `4` with `5`, `2`, `8`, `3`, and `1`: shift `5`, `2`, `8`, `3`, and `1` to the right
    - Compare `6` with `5`, `2`, `8`, `3`, `1`, and `4`: shift `5`, `2`, `8`, `3`, `1`, and `4` to the right
4.  Insert the elements:
    - Insert `2` into `[5]`: `[2, 5]`
    - Insert `8` into `[2, 5]`: `[2, 5, 8]`
    - Insert `3` into `[2, 5, 8]`: `[2, 3, 5, 8]`
    - Insert `1` into `[2, 3, 5, 8]`: `[1, 2, 3, 5, 8]`
    - Insert `4` into `[1, 2, 3, 5, 8]`: `[1, 2, 3, 4, 5, 8]`
    - Insert `6` into `[1, 2, 3, 4, 5, 8]`: `[1, 2, 3, 4, 5, 6, 8]`

The sorted list is `[1, 2, 3, 4, 5, 6, 8]`.

## **Time and Space Complexity**

- **Time complexity**: The time complexity of Insertion Sort is O(n^2) in the worst case, where n is the number of elements in the input. However, it can be O(n) in the best case, when the input is already sorted.
- **Space complexity**: The space complexity of Insertion Sort is O(1), since it only uses a single additional array to store the sorted region.

## **Implementation**

Here is an example implementation of Insertion Sort in Python:

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
print(insertion_sort(arr))  # Output: [1, 2, 3, 4, 5, 6, 8]
```

This implementation uses a simple loop to iterate through the input array and shift elements to make space for the current element. The `key` variable stores the current element to be inserted, and the `j` variable keeps track of the last element in the sorted region.
