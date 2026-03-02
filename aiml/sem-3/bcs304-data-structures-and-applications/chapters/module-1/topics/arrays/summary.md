# Arrays - Summary

## Key Definitions and Concepts

- **Array**: A homogeneous collection of elements stored at contiguous memory locations, allowing random access through indices
- **One-Dimensional Array**: Linear collection of elements accessed using a single index
- **Two-Dimensional Array**: Collection of elements organized in rows and columns, accessed using two indices
- **Dynamic Array**: A resizable array data structure that grows or shrinks during program execution
- **Base Address**: The starting memory address where an array begins

## Important Formulas and Theorems

- **1D Array Address**: Address of arr[i] = Base Address + (i × size of element)
- **2D Array Address (Row-Major)**: Address of arr[i][j] = Base Address + ((i × n) + j) × size of element
- **Binary Search Time Complexity**: O(log n) for sorted arrays
- **Linear Search Time Complexity**: O(n)
- **Array Traversal Time Complexity**: O(n)

## Key Points

- Arrays provide O(1) constant time access to any element using index
- All elements in an array must be of the same data type
- Array indices start from 0 in most programming languages
- Static arrays have fixed sizes, while dynamic arrays can resize during execution
- 2D arrays can be stored in row-major or column-major order
- Insertion and deletion require shifting elements, taking O(n) time
- Binary search requires a pre-sorted array and has logarithmic time complexity
- Multidimensional arrays are used for matrix operations and spatial data representation

## Common Mistakes to Avoid

- Confusing array indices with array lengths (first valid index is 0, not 1)
- Forgetting that array size must be known at compile time for static arrays
- Not checking array bounds before accessing elements, leading to undefined behavior
- Using binary search on unsorted arrays, which produces incorrect results

## Revision Tips

- Practice at least 5 numerical problems on address calculation formulas
- Write and execute C programs for common operations: sum, maximum, linear search, binary search, matrix addition
- Memorize the time complexities of all basic operations on arrays
- Understand the difference between static and dynamic memory allocation for arrays
- Review previous year DU question papers to identify the pattern and types of questions asked