# Arrays in Java

## Overview

Arrays are fixed-size, homogeneous data structures that store multiple values of the same type in contiguous memory locations with zero-based indexing. Arrays in Java are objects that provide efficient random access but cannot change size after creation.

## Key Points

- **Fixed Size**: Array size cannot be changed after creation
- **Zero-Based Indexing**: First element at index 0, last at length-1
- **Length Property**: Use arr.length (not a method) to get size
- **Declaration Methods**: Type[] name or Type name[], initialization with {} or new
- **Multi-Dimensional**: Java supports arrays of arrays (jagged arrays allowed)
- **Arrays Class**: Utility methods like sort(), binarySearch(), fill(), equals(), toString()
- **Default Values**: int arrays initialize to 0, boolean to false, objects to null
- **Copying**: Use clone(), System.arraycopy(), or Arrays.copyOf()

## Important Concepts

- Enhanced for-loop best for read-only traversal
- Arrays.toString() for printing array contents
- ArrayIndexOutOfBoundsException when accessing invalid index
- Arrays vs Collections: arrays fixed-size and can hold primitives
- Command-line arguments stored in String[] args
- Two-dimensional arrays: int[][] matrix = new int[rows][cols]

## Notes

- Remember: .length is property, not method (no parentheses)
- Arrays can store primitives, Collections only store objects
- Practice multi-dimensional array declaration and access for exams
