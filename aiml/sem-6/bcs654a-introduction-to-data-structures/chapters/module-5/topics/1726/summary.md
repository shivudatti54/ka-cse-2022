# **17.2.6 Quick Revision Notes**

## **Introduction**

- Data structures are collections of data elements, each of which represents a value or information.
- Sorting is the process of arranging data in a specific order, such as ascending or descending.

## **Sorting Algorithms**

### Bubble Sort

- Simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
- Time complexity: O(n^2)
- Space complexity: O(1)

### Selection Sort

- Algorithm that selects the smallest (or largest) element from the unsorted portion of the list and swaps it with the first element of the unsorted portion.
- Time complexity: O(n^2)
- Space complexity: O(1)

### Insertion Sort

- Algorithm that builds the final sorted array (or list) one item at a time.
- Time complexity: O(n^2)
- Space complexity: O(1)

## **Formulas and Definitions**

- **Stability**: A sorting algorithm is stable if it maintains the relative order of equal elements.
- **In-place sorting**: A sorting algorithm that can be performed without using additional storage, other than a small amount for the temporary swap of elements.
- **Big O notation**:
  - O(1): constant time complexity
  - O(log n): logarithmic time complexity
  - O(n): linear time complexity
  - O(n log n): linearithmic time complexity
  - O(n^2): quadratic time complexity

## **Theorems**

- **Buchanan's Theorem**:
  - For any comparison-based sorting algorithm, there exists a sequence of elements that can be sorted in O(n log n) time.
- **Minimal number of comparisons required**:
  - Any comparison-based sorting algorithm must perform at least n log n comparisons in the worst case.

## **Important Terms**

- **Sorted array**: an array of elements that are arranged in a specific order, such as ascending or descending.
- **Unsorted array**: an array of elements that are not arranged in a specific order.
- **List**: a collection of elements that are ordered in some way.
