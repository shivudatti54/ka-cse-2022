# Recursive Functions, Linear and Binary Search

## Introduction
This summary covers three essential topics in Data Structures as per the Delhi University BSc Physical Science (CS) NEP 2024 syllabus: Recursive Functions, Linear Search, and Binary Search. These concepts form the foundation for efficient problem-solving and algorithm design.

## Key Concepts

### Recursive Functions
- **Definition**: A function that calls itself to solve a problem by breaking it into smaller subproblems.
- **Essential Components**:
  - **Base Case**: The condition that terminates recursion (prevents infinite loops).
  - **Recursive Case**: The part where the function calls itself with reduced parameters.
- **Working Mechanism**: Uses a stack (call stack) to store return addresses and local variables during execution.
- **Advantages**: Simplifies complex problems like tree traversals, factorial, and Fibonacci series.
- **Disadvantages**: Slower than iteration; risk of stack overflow with deep recursion.
- **Examples**: Factorial calculation, Tower of Hanoi, recursive tree traversal.

### Linear Search (Sequential Search)
- **Definition**: Searches elements one by one until target is found or list ends.
- **Time Complexity**: O(n) in worst and average cases.
- **Space Complexity**: O(1) for iterative version.
- **Recursive Implementation**:
  - Check first element; if matches, return index.
  - Otherwise, recursively search the remaining list.
  - Base case: Element found or list becomes empty.
- **Best Case**: O(1) when element is at the first position.
- **Applications**: Unsorted data, small datasets.

### Binary Search
- **Definition**: Efficiently searches a **sorted** array by repeatedly dividing the search interval in half.
- **Prerequisite**: Data must be in sorted order.
- **Time Complexity**: O(log n) — significantly faster than linear search.
- **Space Complexity**: O(1) for iterative; O(log n) for recursive (stack usage).
- **Recursive Algorithm**:
  - Find middle element; compare with target.
  - If equal, return index.
  - If target < middle, search left half; else search right half.
  - Base case: Subarray becomes empty (element not found).
- **Best Case**: O(1) when element is at middle position.
- **Applications**: Large sorted datasets, dictionary searches, binary search trees.

## Conclusion
Mastering recursion and searching algorithms is crucial for the Delhi University Data Structures exam. Recursion provides an elegant problem-solving approach, while Linear and Binary Search are fundamental for data retrieval. Remember: use Linear Search for unsorted data and Binary Search for sorted data to optimize performance.