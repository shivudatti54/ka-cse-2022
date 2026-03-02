# **BRUTE FORCE APPROACHES: Selection Sort and Bubble Sort**

### Overview

- Brute force approaches are simple sorting algorithms that work by checking every element in the list, one by one, to find the correct position.
- Selection Sort and Bubble Sort are two common examples of brute force sorting algorithms.

### Key Points

#### Selection Sort

- Algorithm:
  - Iterate through the list, selecting the smallest (or largest, depending on the sort order) element from the unsorted portion of the list.
  - Swap the selected element with the first element of the unsorted portion.
- Time complexity:
  - Best-case: O(n)
  - Average-case: O(n^2)
  - Worst-case: O(n^2)
- Space complexity: O(1)
- Example:
  - `arr = [5, 2, 8, 3, 1]`
  - `arr = [1, 2, 3, 5, 8]`

#### Bubble Sort

- Algorithm:
  - Iterate through the list, comparing adjacent elements and swapping them if they are in the wrong order.
  - Repeat the process until no more swaps are needed, indicating that the list is sorted.
- Time complexity:
  - Best-case: O(n)
  - Average-case: O(n^2)
  - Worst-case: O(n^2)
- Space complexity: O(1)
- Example:
  - `arr = [5, 2, 8, 3, 1]`
  - `arr = [1, 2, 3, 5, 8]`

### Important Formulas and Definitions

- **Time complexity**: A measure of an algorithm's performance, usually expressed as a function of the input size `n`.
- **Space complexity**: A measure of an algorithm's memory usage, usually expressed as a function of the input size `n`.
- **Big O notation**: A way to describe the upper bound of an algorithm's time complexity.

### Theorems

- **No free lunch theorem**: Any algorithm has a trade-off between time and space complexity.
- **Little's law**: The time complexity of an algorithm depends on the input size `n`.
