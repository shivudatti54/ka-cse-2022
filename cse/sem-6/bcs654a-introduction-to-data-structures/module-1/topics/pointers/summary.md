# Introduction to Pointers

## Overview

Pointers are variables that store memory addresses of other variables rather than data values directly. They provide powerful capabilities for dynamic memory allocation, efficient array manipulation, and implementation of complex data structures like linked lists and trees.

## Key Points

- **Memory Address Storage**: Pointer holds the address where actual data is stored in memory
- **Address-of Operator (&)**: Returns the memory address of a variable
- **Dereference Operator (\*)**: Accesses the value stored at the address held by pointer
- **Declaration Syntax**: `data_type *pointer_name;` where type specifies pointed data type
- **Pointer Arithmetic**: Adding n to pointer advances by n × sizeof(datatype) bytes
- **Array Relationship**: Array name is constant pointer to first element
- **Dynamic Allocation**: malloc, calloc, realloc, free functions enable runtime memory management

## Important Concepts

- Pointers enable call-by-reference simulation for function parameters
- Uninitialized (wild) pointers cause undefined behavior when dereferenced
- Dangling pointers reference freed memory and must be set to NULL
- Memory leaks occur when allocated memory is not freed before pointer is lost
- Function pointers can point to functions for callback mechanisms
- Structure pointers use arrow operator (->) for member access

## Notes

- Always initialize pointers before use to avoid wild pointers
- Check if malloc/calloc returns NULL before using allocated memory
- Match every malloc/calloc with corresponding free to prevent memory leaks
- Set pointers to NULL immediately after freeing memory
- Understand that ptr + 1 moves by data type size, not one byte
