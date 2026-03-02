# Static and Dynamic Memory Allocation - Summary

## Key Definitions and Concepts

- **Static Memory Allocation**: Memory allocated at compile time on the stack; size must be known beforehand; automatic allocation/deallocation by compiler.
- **Dynamic Memory Allocation**: Memory allocated at runtime on the heap using `new`; size can be determined during execution; requires manual deallocation with `delete`.
- **Stack Memory**: LIFO-based memory region for local variables, function parameters, and return addresses; fast but limited size.
- **Heap Memory**: Larger memory pool for dynamic allocation; slower access but flexible sizing; requires explicit management.
- **Memory Leak**: Failure to deallocate dynamically allocated memory, causing gradual loss of available memory.

## Important Formulas and Theorems

- `new T` - Allocates sizeof(T) bytes for single object
- `new T[n]` - Allocates n × sizeof(T) bytes for array
- `delete ptr` - Deallocates single object
- `delete[] ptr` - Deallocates array
- Stack size: typically 1-8 MB (system-dependent)
- Heap: limited by virtual memory of the system

## Key Points

- Static allocation uses stack memory and is automatically managed; dynamic allocation uses heap and requires manual `delete`.
- Always pair `new` with `delete`, and `new[]` with `delete[]` to prevent undefined behavior.
- Smart pointers (`unique_ptr`, `shared_ptr`) provide automatic memory management in modern C++.
- C-style `malloc`/`free` don't call constructors/destructors; `new`/`delete` do.
- After `delete`, set pointer to `nullptr` to avoid dangling pointer issues.
- Large arrays should be dynamically allocated to avoid stack overflow.
- Memory leaks occur when allocated memory is never freed, especially in error-handling paths.

## Common Mistakes to Avoid

- Using `delete` instead of `delete[]` for arrays (undefined behavior)
- Forgetting to delete dynamically allocated memory (memory leak)
- Deleting memory that wasn't allocated with `new` (undefined behavior)
- Using dangling pointers (pointers to freed memory)
- Not checking if `new` failed (though it throws exception by default)

## Revision Tips

1. Practice writing code with both `new`/`delete` and smart pointers to understand the difference.
2. Trace through exam code to identify all allocation/deallocation paths.
3. Remember: stack = automatic = static; heap = manual = dynamic.
4. In exam questions, always check if every code path leads to proper deallocation.
5. Review difference between `malloc` family and `new`/`delete` operators.