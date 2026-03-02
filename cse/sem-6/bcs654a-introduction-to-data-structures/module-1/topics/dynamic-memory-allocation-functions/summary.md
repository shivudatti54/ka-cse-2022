# Dynamic Memory Allocation Functions

## Overview

Dynamic memory allocation allows programs to request memory from the heap at runtime rather than compile time. C provides four library functions (malloc, calloc, realloc, free) in stdlib.h for flexible memory management essential for implementing dynamic data structures.

## Key Points

- **malloc(size)**: Allocates specified bytes, returns pointer to uninitialized memory or NULL if fails
- **calloc(n, size)**: Allocates array of n elements, initializes all bytes to zero
- **realloc(ptr, new_size)**: Resizes existing memory block, preserves content, may relocate
- **free(ptr)**: Deallocates previously allocated memory, making it available for reuse
- **Return Type**: All allocation functions return void\* requiring typecasting in C++
- **Heap Memory**: Allocated on heap with lifetime controlled by programmer via free
- **NULL Check**: Always verify allocation success before using returned pointer

## Important Concepts

- malloc faster than calloc but returns uninitialized garbage values
- calloc slower due to zero-initialization but safer for arrays
- realloc may move memory block to new location if current area insufficient
- Memory leaks occur when allocated memory not freed before pointer lost
- Dangling pointers reference freed memory causing undefined behavior
- Double free (freeing same memory twice) causes serious errors

## Notes

- Always check return value for NULL before using allocated memory
- Match every malloc/calloc with corresponding free to prevent leaks
- Set pointer to NULL immediately after free to avoid dangling pointers
- Use sizeof() for portability rather than hardcoding type sizes
- Essential for implementing linked lists, trees, dynamic arrays, and graphs
