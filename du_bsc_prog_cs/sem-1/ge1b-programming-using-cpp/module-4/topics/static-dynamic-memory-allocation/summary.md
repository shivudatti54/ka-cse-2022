# Static and Dynamic Memory Allocation - Summary

## Key Definitions and Concepts

- **Static Memory Allocation**: Memory allocated at compile time in stack or data segment; size must be known beforehand
- **Dynamic Memory Allocation**: Memory allocated at runtime using heap segment; size can be determined during execution
- **Stack**: Memory segment for function calls, local variables; automatic allocation/deallocation (LIFO)
- **Heap**: Free store for dynamic memory; programmer-controlled allocation/deallocation
- **Memory Leak**: Failure to deallocate dynamically allocated memory, causing gradual memory exhaustion
- **Dangling Pointer**: Pointer referencing freed memory; accessing it causes undefined behavior
- **Smart Pointers**: C++11 objects that automatically manage memory (unique_ptr, shared_ptr)

## Important Formulas and Concepts

- **Memory Layout**: Code Segment → Data Segment → Heap → Stack
- **new operator**: `ptr = new type;` or `ptr = new type(value);`
- **delete operator**: `delete ptr;` (for single object)
- **new[] operator**: `ptr = new type[size];`
- **delete[] operator**: `delete[] ptr;` (for arrays)

## Key Points

1. Static allocation is faster but inflexible; dynamic allocation is flexible but requires manual management
2. Stack memory is limited (~8MB typical); heap can use available system RAM
3. Always pair `new` with `delete` and `new[]` with `delete[]`
4. After `delete`, set pointer to `nullptr` to prevent dangling pointer bugs
5. For 2D dynamic arrays: allocate row pointers first, then each row; deallocate in reverse order
6. Smart pointers (C++11+) provide automatic memory management and prevent leaks
7. Common allocations: `int* p = new int;`, `int* arr = new int[n];`, `int** mat = new int*[rows];`
8. Memory leaks occur when allocated memory is never freed before program ends

## Common Mistakes to Avoid

1. Forgetting to use `delete[]` for arrays allocated with `new[]`
2. Using `delete` instead of `delete[]` for arrays (causes undefined behavior)
3. Not setting pointer to nullptr after deletion
4. Accessing memory after it has been freed (dangling pointer)
5. Not checking if `new` succeeded (can throw `std::bad_alloc` on failure)

## Revision Tips

1. Practice writing code for 1D and 2D dynamic arrays multiple times
2. Trace through code with paper to identify memory leaks
3. Remember: "For every new, there must be a delete"
4. Compare stack vs heap allocation with diagrams
5. Review smart pointer syntax and when to use each type
6. Solve previous year DU exam questions on this topic