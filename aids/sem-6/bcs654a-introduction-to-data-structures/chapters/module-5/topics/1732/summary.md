# Revision Notes for 17.3.2: Insertion Sort

=============================================

## Definition and Overview

- Insertion Sort is a simple comparison-based sorting algorithm.
- It works by dividing the input into a sorted and an unsorted region.
- Each subsequent element from the unsorted region is inserted into the sorted region in its correct position.

## Key Steps

- Iterate through the unsorted region of the array.
- Compare the current element with the elements in the sorted region.
- Shift elements greater than the current element to the right.
- Insert the current element into the sorted region.

## Time and Space Complexity

- Time Complexity: O(n^2)
- Space Complexity: O(1)

## Important Formulas and Definitions

- **Insertion Sort**: `insertion_sort(arr) = { for i = 1 to n-1 { for j = 0 to i-1 { if arr[j] > arr[i] { shift arr[j] to the right } } insert arr[i] into the sorted region }`
- **Shift operation**: `shift(x, i) = { arr[i] = arr[i-1]; i = i - 1 }`

## Theorems

- **Stability**: Insertion Sort is a stable sorting algorithm, meaning that equal elements will remain in their original order.

## Example

- Suppose we have the following array: `[5, 2, 9, 1, 7]`
- We sort the array using Insertion Sort:
  1.  Compare `2` with `5`, shift `5` to the right.
  2.  Compare `2` with `2`, no shift.
  3.  Compare `9` with `2`, shift `2` to the right.
  4.  Compare `9` with `9`, no shift.
  5.  Compare `7` with `9`, shift `9` to the right.
  6.  Compare `7` with `7`, no shift.
  7.  Insert `1` into the sorted region.
  8.  Insert `5` into the sorted region.
  9.  Insert `2` into the sorted region.
  10. Insert `9` into the sorted region.
  11. Insert `7` into the sorted region.
- The sorted array is: `[1, 2, 5, 7, 9]`
