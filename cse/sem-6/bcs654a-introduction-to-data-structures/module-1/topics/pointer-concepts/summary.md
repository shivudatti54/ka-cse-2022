# Pointer Concepts and Applications

## Overview

Pointers are powerful features in C that store memory addresses and enable efficient data manipulation, dynamic memory allocation, and implementation of complex data structures. Understanding pointer concepts is fundamental for mastering data structures and low-level programming.

## Key Points

- **Declaration**: `data_type *pointer_name;` creates pointer to specific data type
- **Address-of Operator (&)**: Returns memory address of variable for pointer assignment
- **Dereference Operator (\*)**: Accesses or modifies value at memory address
- **Pointer Arithmetic**: Adding integer n moves pointer by n elements, not n bytes
- **Array-Pointer Equivalence**: arr[i] is equivalent to \*(arr + i) in C
- **Pass-by-Reference**: Pointers enable functions to modify original variable values
- **Dynamic Memory**: malloc, calloc, realloc, free for runtime memory management

## Important Concepts

- Pointer to pointer (\*\*pptr) stores address of another pointer
- String manipulation efficiently performed using character pointers
- Array of pointers useful for storing multiple strings or variable-length data
- Function pointers enable callback mechanisms and dynamic function calls
- Structure pointers use arrow operator (->) as shorthand for (\*ptr).member

## Notes

- Draw memory diagrams showing addresses and pointer relationships
- Remember pointer arithmetic is type-dependent (ptr + 1 advances by sizeof(type))
- Always check malloc return value for NULL before use
- Pair every allocation (malloc/calloc) with corresponding free
- Watch for dangling pointers, memory leaks, and uninitialized pointers in exams
