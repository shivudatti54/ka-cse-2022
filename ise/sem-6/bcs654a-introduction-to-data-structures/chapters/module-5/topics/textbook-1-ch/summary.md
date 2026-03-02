# Textbook 1: Ch - Introduction to Data Structures (Sorting)

===========================================================

### Module: Sorting

- **Introduction to Sorting**
  - Definition: An algorithm that rearranges elements in a list to achieve a specific order (e.g., ascending or descending order).
  - Importance: Efficient sorting is crucial for many applications, including data analysis, visualization, and storage.

- **Bubble Sort**
  - **Algorithm:** Repeatedly iterates through the list, comparing adjacent elements and swapping them if they are in the wrong order.
  - **Time Complexity:** O(n^2) in the worst case, making it inefficient for large datasets.
  - **Example:** `arr = [64, 34, 25, 12, 22, 11, 90];` Bubble sort will sort the array as `[11, 12, 22, 25, 34, 64, 90]`.

- **Selection Sort**
  - **Algorithm:** Iterates through the list, selecting the smallest (or largest) element and swapping it with the first unsorted element.
  - **Time Complexity:** O(n^2) in the worst case, making it less efficient than bubble sort.
  - **Example:** `arr = [64, 34, 25, 12, 22, 11, 90];` Selection sort will sort the array as `[11, 12, 22, 25, 34, 64, 90]`.

- **Insertion Sort**
  - **Algorithm:** Iterates through the list one element at a time, inserting each element into its proper position within the previously sorted portion of the list.
  - **Time Complexity:** O(n^2) in the worst case, but generally more efficient than bubble sort for small datasets.
  - **Example:** `arr = [64, 34, 25, 12, 22, 11, 90];` Insertion sort will sort the array as `[11, 12, 22, 25, 34, 64, 90]`.

### Important Formulas and Definitions

- **Big O Notation:** A mathematical notation used to describe the performance or complexity of an algorithm.
- **Time Complexity:** The amount of time an algorithm takes to complete, often expressed as a function of the input size (e.g., n).
- **Space Complexity:** The amount of memory an algorithm requires, often expressed as a function of the input size (e.g., n).

### Important Theorems

- **Stable Sorting:** A sorting algorithm that maintains the relative order of equal elements.
- **Unstable Sorting:** A sorting algorithm that does not maintain the relative order of equal elements.
