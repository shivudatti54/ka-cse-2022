# **DECREASE-AND-CONQUER: Insertion Sort**

### Introduction

- **Definition:** Insertion Sort is a simple sorting algorithm that works by dividing the input into a sorted and an unsorted region.
- **Time Complexity:** O(n^2) in the worst case, making it inefficient for large datasets.

### Key Steps

- **Initialization:**
  - Create a sorted array of size n
  - Initialize the sorted array with the first element of the input array
- **Decrease-and-Conquer:**
  - Compare the current element with the sorted array
  - Shift elements in the sorted array to make room for the current element
  - Insert the current element into the sorted array
- **Recurse:**
  - Repeat the process for the remaining elements in the input array

### Important Formulas

- **Insertion Sort Formula:** `T(n) = 2T(n/2) + n`
- **Master Theorem Solution:** `T(n) = O(n^2)`

### Theorems

- **Big O Notation Theorem:** `T(n) = O(f(n))` if `f(n)` is a computationally efficient function

### Key Definitions

- **Divide and Conquer Algorithm:** A problem-solving strategy that breaks down a complex problem into smaller sub-problems
- **Exponential Time Complexity:** When the running time of an algorithm grows exponentially with the size of the input

### Key Concepts

- **Unstable Sorting Algorithm:** Sorts elements based on their key, but preserves the relative order of equal elements
- **Worst-Case Time Complexity:** The maximum amount of time an algorithm takes to complete

### Important Terminology

- **Big O Notation:** A way to describe the upper bound of an algorithm's time or space complexity
- **Polynomial Time Complexity:** An algorithm with a time complexity of `O(n^k)`, where `k` is a constant.
