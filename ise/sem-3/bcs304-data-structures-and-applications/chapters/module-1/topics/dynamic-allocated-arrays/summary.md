# Dynamic Allocated Arrays - Summary

## Key Definitions and Concepts

- **Dynamic Memory Allocation**: Memory allocation that occurs at runtime using the heap, allowing variable-sized data structures.
- **Heap**: A region of memory separate from the stack where dynamically allocated memory resides.
- **malloc()**: Function that allocates specified bytes of uninitialized memory.
- **calloc()**: Function that allocates memory for an array and initializes all bytes to zero.
- **realloc()**: Function that changes the size of previously allocated memory.
- **free()**: Function that releases allocated memory back to the system.
- **Memory Leak**: Failure to release allocated memory, causing gradual memory exhaustion.

## Important Formulas and Theorems

- **malloc syntax**: `void* malloc(size_t size)`
- **calloc syntax**: `void* calloc(size_t n, size_t size)`
- **realloc syntax**: `void* realloc(void* ptr, size_t new_size)`
- **Array element access**: For contiguous 2D array at row i, column j: `arr[i * cols + j]`
- **Amortized append cost**: O(1) - while occasional resizing is O(n), average cost remains constant.

## Key Points

- Dynamic arrays use heap memory unlike static arrays that use stack memory.
- Always cast malloc/calloc return to appropriate pointer type: `(int*)malloc(n * sizeof(int))`.
- Always check if malloc/calloc/realloc returns NULL before using the pointer.
- calloc() zeros memory making it safer for arrays; malloc() is faster as it skips initialization.
- realloc() may return a new pointer; always use a temporary variable to check for failure.
- 2D arrays can be created as array-of-pointers or single contiguous block.
- Free memory in reverse order of allocation for nested structures.
- Double-free and use-after-free are critical bugs that cause undefined behavior.

## Common Mistakes to Avoid

- Forgetting to cast malloc() return (required in C, but not in C++)
- Not checking for NULL after memory allocation
- Using sizeof on uninitialized pointers instead of dereferenced type
- Forgetting to free memory at the end of program
- Accessing memory after it has been freed (dangling pointer)
- Confusing bytes with number of elements in malloc argument

## Revision Tips

- Practice writing code to create 1D and 2D dynamic arrays from scratch.
- Trace through realloc() behavior with small examples to understand when new memory is allocated vs expanded.
- Remember the sequence: Allocate → Validate → Use → Free.
- Review pointer arithmetic for 2D array indexing: arr[i][j] vs arr[i * cols + j].
- Understand why dynamic arrays grow by doubling (amortized O(1) performance).