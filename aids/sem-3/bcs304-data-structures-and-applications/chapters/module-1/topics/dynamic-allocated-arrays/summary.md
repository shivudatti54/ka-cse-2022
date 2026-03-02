# Dynamic Allocated Arrays - Summary

## Key Definitions and Concepts

- **Dynamic Memory Allocation**: Memory allocated during runtime from the heap segment using functions like malloc(), calloc(), and realloc()
- **Heap Memory**: Reserved memory segment available for dynamic allocation, managed explicitly by the programmer
- **Memory Leak**: Failure to release allocated memory, causing gradual exhaustion of available memory
- **Dynamic Array**: An array whose size is determined at runtime rather than compile time

## Important Formulas and Theorems

- **malloc()**: `ptr = (type*)malloc(n * sizeof(type));` - Allocates n bytes, does not initialize
- **calloc()**: `ptr = (type*)calloc(n, sizeof(type));` - Allocates and initializes to zero
- **realloc()**: `ptr = (type*)realloc(old_ptr, new_size);` - Resizes previously allocated memory
- **free()**: `free(ptr);` - Releases allocated memory back to heap

## Key Points

- Dynamic arrays solve the problem of fixed-size static arrays by allocating memory at runtime
- Always check for NULL after memory allocation to handle allocation failures gracefully
- malloc() does not initialize memory (contains garbage values), calloc() initializes to zero
- realloc() may move data to a new memory location if insufficient space is available
- For 2D dynamic arrays, choose between contiguous allocation (single block) or array of pointers (multiple blocks)
- Every malloc() and calloc() must have a corresponding free() to prevent memory leaks
- Dynamic arrays enable implementation of flexible data structures like vectors, dynamic lists, and resizable containers
- The relationship arr[i] == *(arr + i) demonstrates the equivalence of array notation and pointer arithmetic

## Common Mistakes to Avoid

- Forgetting to check for NULL after allocation, leading to segmentation faults
- Not freeing memory in all code paths, especially in error handling scenarios
- Confusing stack allocation (automatic) with heap allocation (dynamic)
- Using sizeof on a pointer instead of the actual data type or allocated size
- Using freed memory (dangling pointers) which leads to undefined behavior

## Revision Tips

- Practice writing code for creating 1D and 2D dynamic arrays from scratch
- Trace through memory allocation and deallocation for sample programs
- Remember that dynamic allocation is essential for implementing data structures like stacks, queues, linked lists, and trees
- Understand when to use malloc() versus calloc() based on initialization requirements
- Review pointer concepts as they are fundamental to understanding dynamic arrays