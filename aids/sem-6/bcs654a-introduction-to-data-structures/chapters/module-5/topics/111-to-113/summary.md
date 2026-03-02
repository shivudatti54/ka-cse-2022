# **Summary of 11.1 to 11.3: Sorting Algorithms**

### 11.1 Introduction to Sorting

- Sorting is the process of arranging elements in a specific order
- Essential for efficient data retrieval and manipulation
- Types of sorting: Natural sorting, Radix sort, Alphabetical sorting

### 11.2 Bubble Sort

- Simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order
- Worst-case time complexity: O(n^2)
- Best-case time complexity: O(n)
- Example: `Bubble Sort (A[0...n-1])`
  - For i = 1 to n-1
    - For j = 0 to n-i-1
      - If A[j] > A[j+1] then swap A[j] and A[j+1]

### 11.3 Selection Sort

- Another simple sorting algorithm that works by repeatedly finding the minimum element from unsorted part and putting it at the beginning
- Worst-case time complexity: O(n^2)
- Best-case time complexity: O(n^2)
- Example: `Selection Sort (A[0...n-1])`
  - For i = 1 to n
    - Find the minimum element in unsorted part of the array
    - Swap the found minimum element with the first element of the unsorted part

### Important Formulas and Definitions

- **Time complexity:** The amount of time an algorithm takes to complete as a function of the size of the input.
- **Space complexity:** The amount of memory an algorithm uses as a function of the size of the input.

### Theorem:

- **Big O notation:** A way to describe the upper limit of an algorithm's time or space complexity, often used to measure the performance of an algorithm.

Revision Key:

- Review Bubble Sort and Selection Sort algorithms.
- Understand time and space complexity.
- Practice solving problems involving sorting algorithms.
