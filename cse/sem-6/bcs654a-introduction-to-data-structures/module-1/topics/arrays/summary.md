# Introduction to Arrays

## Overview

An array is a fundamental data structure that stores a collection of elements of the same data type in contiguous memory locations. Each element can be accessed directly using its index, providing O(1) random access time.

## Key Points

- **Fixed Size**: Size is determined at creation and cannot change during program execution
- **Homogeneous Elements**: All elements must be of the same data type
- **Contiguous Memory**: Elements stored in adjacent memory locations for efficient access
- **Random Access**: Any element accessible in O(1) time using index calculation
- **Address Calculation**: Address(arr[i]) = Base_Address + (i × Size_of_Element)
- **Time Complexities**: Access O(1), Search O(n) unsorted/O(log n) sorted, Insert/Delete at beginning O(n)
- **Memory Efficiency**: No extra memory for pointers, cache-friendly due to contiguous storage

## Important Concepts

- Arrays use zero-based indexing (first element at index 0)
- Memory allocation is contiguous block of size n × element_size
- Insertion and deletion operations require shifting elements
- Array name is a pointer constant to the first element
- Suitable for fixed-size collections with frequent access operations

## Notes

- Know the address calculation formula for exam questions
- Understand the trade-offs: fast access but costly insertion/deletion
- Be prepared to draw memory diagrams showing addresses and indices
- Remember that arrays cannot change size after declaration
- Practice calculating time complexities for different array operations
