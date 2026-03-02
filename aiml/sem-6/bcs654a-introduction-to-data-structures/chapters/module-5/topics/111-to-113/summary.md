# **11.1 to 11.3: Introduction to Data Structures (Sorting)**

### 11.1: Introduction to Sorting

- Sorting is the process of arranging elements in a specific order
- Importance of sorting:
  - Efficient data retrieval and manipulation
  - Reduces complexity of algorithms
  - Improves performance of data structures
- Types of sorting:
  - **Comparative sort**: compares elements and rearranges them based on comparison
  - **Non-comparative sort**: rearranges elements without comparing them

### 11.2: Bubble Sort

- **Bubble sort algorithm**:
  - Works by repeatedly swapping adjacent elements if they are in the wrong order
  - Time complexity: O(n^2)
  - Space complexity: O(1)
- **Example**: arr = [64, 34, 25, 12, 22, 11, 90]
  - Iteration 1: arr = [11, 34, 25, 12, 22, 64, 90]
  - Iteration 2: arr = [11, 12, 22, 25, 34, 64, 90]
  - ...

### 11.3: Selection Sort

- **Selection sort algorithm**:
  - Works by selecting the smallest (or largest) element and swapping it with the first element
  - Time complexity: O(n^2)
  - Space complexity: O(1)
- **Example**: arr = [64, 34, 25, 12, 22, 11, 90]
  - Step 1: Select 11 (smallest) and swap with first element (64)
  - Step 2: Select 12 and swap with second element (34)
  - ...

## **Important Formulas and Definitions**

- **Time complexity**: measures the amount of time an algorithm takes to complete
- **Space complexity**: measures the amount of memory an algorithm uses
- **Big O notation**: a way to describe the upper bound of an algorithm's time complexity
- **Stable sort**: a sorting algorithm that maintains the relative order of equal elements

## **Key Theorems**

- **Hadamard's inequality**: provides a lower bound for the time complexity of certain sorting algorithms
- **Kruskal's algorithm**: a greedy algorithm for constructing a minimum spanning tree
