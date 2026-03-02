# Dynamic Allocated Arrays - Summary

## Key Definitions and Concepts

- DYNAMIC ALLOCATION: Runtime memory allocation from the heap, allowing variable-sized data structures.
- HEAP: Memory segment available for dynamic allocation during program execution, larger than stack but requiring manual management.
- STACK: Compile-time allocated memory with fixed size; static arrays reside here.
- MEMORY LEAK: Failure to deallocate memory, causing gradual exhaustion of available heap space.

## Important Formulas and Theorems

- Memory for n elements: `n * sizeof(datatype)` bytes
- realloc behavior: Maintains old data when expanding; may return new pointer location.
- Array of pointers 2D: `rows * sizeof(int*)` for pointers + `rows * cols * sizeof(int)` for data
- Contiguous 2D: Single allocation of `rows * cols * sizeof(int)` + `rows * sizeof(int*)`

## Key Points

1. Dynamic arrays overcome static array limitations by allocating memory at runtime.

2. malloc returns uninitialized memory; calloc initializes all bytes to zero.

3. Always check malloc/calloc/realloc return value for NULL before use.

4. realloc can either expand in place or allocate new memory and copy data.

5. Use free() exactly once on each allocated pointer; set pointer to NULL afterward.

6. In C++, prefer new/delete over malloc/free for type safety and constructor/destructor support.

7. Two-dimensional dynamic arrays can use array-of-pointers (flexible rows) or contiguous allocation (better cache performance).

8. Dynamic arrays enable implementation of growable collections like vectors and dynamic lists.

## Common Mistakes to Avoid

- Not checking for NULL after memory allocation
- Using malloc instead of calloc when zero-initialization is required
- Forgetting to free memory, causing memory leaks
- Accessing memory after freeing it (dangling pointer)
- Calling free() twice on the same pointer (undefined behavior)
- Not updating pointer after realloc assigns new memory location
- Confusing delete with delete[] for arrays in C++

## Revision Tips

1. Practice writing code for 1D and 2D dynamic array creation and deletion until automatic.

2. Remember the mnemonic "MRCF" for memory management sequence: Malloc → Read/Write → Call free().

3. For exam questions, always show the NULL check—it demonstrates defensive programming.

4. Understand when to use calloc (need zero-initialized) versus malloc (performance priority).

5. Review the difference between stack allocation (automatic, fixed size) versus heap allocation (manual, variable size).