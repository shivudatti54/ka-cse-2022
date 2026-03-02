# One-Dimensional Arrays

## Overview

A one-dimensional array stores a fixed-size, sequential collection of elements of the same data type in contiguous memory locations. It provides direct access to elements using a single index and is fundamental for implementing various algorithms and data structures.

## Key Points

- **Declaration Syntax**: `data_type array_name[array_size];` specifies type, name, and size
- **Memory Allocation**: Total memory = number_of_elements × size_of_each_element
- **Initialization Methods**: Complete, partial, or without specifying size using curly braces
- **Index Range**: Valid indices range from 0 to size-1, out-of-bounds access causes undefined behavior
- **Basic Operations**: Traversal (O(n)), insertion (O(n)), deletion (O(n)), searching (O(n)), sorting (O(n²) bubble sort)
- **Pointer Relationship**: Array name is pointer constant holding address of first element
- **Common Uses**: Storing lists, implementing stacks/queues, string handling, matrix operations

## Important Concepts

- Elements accessed using zero-based indexing with syntax array_name[index]
- Uninitialized arrays contain garbage values unless declared globally/statically
- Array elements can be accessed using pointer notation: \*(arr + i) equals arr[i]
- Linear search checks each element sequentially, bubble sort uses nested loops
- Cannot assign whole array with = operator after declaration

## Notes

- Practice drawing memory diagrams with addresses, indices, and values
- Know how to implement linear search and bubble sort algorithms
- Understand the relationship between arrays and pointers thoroughly
- Remember common errors: index out of bounds, forgetting zero-based indexing
- Be able to calculate array size using sizeof operator
