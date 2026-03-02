# Arrays

## Overview

An array is a fundamental data structure that stores a fixed number of elements of the same data type in contiguous memory locations, allowing for O(1) random access. Arrays are used to implement other data structures and are essential in computer science.

## Key Points

- **Random Access**: Arrays allow for constant-time access to any element using its index.
- **Fixed Size**: Arrays have a fixed size that cannot be changed after creation.
- **Homogeneous**: All elements in an array must be of the same data type.
- **Memory Efficient**: Arrays store elements in contiguous memory locations, making them memory efficient.
- **Cache Friendly**: The contiguous memory layout of arrays benefits spatial locality.
- **Costly Insertion and Deletion**: Insertion and deletion operations in the middle of an array are O(n).

## Important Definitions

- **Base Address**: The memory address of the first element in an array.
- **Element Size**: The size of each element in an array in bytes.
- **Index**: A unique identifier for each element in an array.

## Key Formulas / Syntax

- **Address Calculation Formula**: `Address = B + i * w`, where B is the base address, i is the index, and w is the element size.
- **Array Declaration**: `int arr[5];` declares an array of 5 integers.
- **Array Initialization**: `int arr[5] = {10, 20, 30, 40, 50};` initializes an array with 5 elements.

## Comparisons

| Feature            | Array | Linked List |
| ------------------ | ----- | ----------- |
| Access by Index    | O(1)  | O(n)        |
| Insertion/Deletion | O(n)  | O(1)        |
| Memory Efficiency  | High  | Low         |
| Cache Friendliness | High  | Low         |

## Exam Tips

- Be prepared to compute addresses using the address calculation formula.
- Understand the difference between linear search and binary search.
- Remember to mention the shifting of elements during insertion and deletion operations.
- Always include boundary checks when writing C code for arrays.
- Understand that arrays are passed by reference in C.
- Be prepared to compare arrays with linked lists.
