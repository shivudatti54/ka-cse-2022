# Dynamic Memory Allocation - Summary

## Key Definitions and Concepts

- **Dynamic Memory Allocation**: Process of allocating memory at runtime from the heap segment, allowing variable-sized data structures.
- **Heap**: Free memory pool in a program's address space used for dynamic allocation.
- **malloc()**: Function that allocates specified bytes of uninitialized memory.
- **calloc()**: Function that allocates memory for array and initializes to zero.
- **realloc()**: Function that resizes previously allocated memory block.
- **free()**: Function that deallocates previously allocated memory.
- **Memory Leak**: Condition where allocated memory is not freed before program termination.
- **Dangling Pointer**: Pointer referencing freed memory, leading to undefined behavior.

## Important Formulas and Techniques

```c
// Basic memory allocation
ptr = (type *)malloc(size * sizeof(type));

// Array allocation
ptr = (type *)malloc(n * sizeof(type));

// Structure allocation
struct_name *ptr = (struct_name *)malloc(sizeof(struct_name));

// Contiguous allocation (zero-initialized)
ptr = (type *)calloc(n, sizeof(type));

// Reallocation
ptr = (type *)realloc(ptr, new_size);

// Deallocation
free(ptr);
ptr = NULL;
```

## Key Points

- Dynamic memory allocation provides flexibility over static allocation by allowing runtime-determined memory sizes.
- Always check for NULL after memory allocation to handle allocation failures gracefully.
- The four functions (malloc, calloc, realloc, free) are declared in `<stdlib.h>`.
- malloc allocates uninitialized memory; calloc allocates zero-initialized memory.
- calloc takes two arguments (number of elements, element size); malloc takes one (total bytes).
- Every malloc/calloc MUST have a corresponding free() to prevent memory leaks.
- Set pointer to NULL after calling free() to avoid dangling pointer bugs.
- sizeof operator should be used for portability rather than hardcoded values.

## Common Mistakes to Avoid

1. **Not checking for NULL**: Always verify allocation success before using the pointer.
2. **Forgetting to free memory**: Leads to memory leaks and reduced program efficiency.
3. **Using freed memory (dangling pointer)**: Access memory only between allocation and free.
4. **Double-freeing memory**: Calling free() twice on the same pointer causes undefined behavior.
5. **Typecasting malloc incorrectly**: While optional in C, incorrect typecasting can cause issues.

## Revision Tips

- Practice writing programs that allocate memory for arrays and structures of varying sizes.
- Memorize the function signatures and differences between malloc, calloc, realloc, and free.
- Always follow the pattern: allocate → check NULL → use memory → free → set NULL.
- Understand when to use calloc (need zero-initialization) vs malloc (general use).
- Review self-referential structure examples as they are commonly combined with dynamic allocation in exam questions.