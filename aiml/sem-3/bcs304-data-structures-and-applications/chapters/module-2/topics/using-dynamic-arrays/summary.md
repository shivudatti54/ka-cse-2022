# Using Dynamic Arrays - Summary

## Key Definitions and Concepts

- **Dynamic Array**: A resizable array data structure that allocates memory at runtime from the heap, allowing the array to grow or shrink as needed.
- **Heap Memory**: A region of process memory used for dynamic allocation, managed explicitly by the programmer.
- **Capacity**: The maximum number of elements a dynamic array can hold before requiring resizing.
- **Size**: The current number of elements actually stored in the dynamic array.
- **Amortized Analysis**: A method of analyzing time complexity where expensive operations are averaged over a sequence of operations.

## Important Formulas and Theorems

- **Amortized Cost**: The average cost per insertion in a dynamic array that doubles its capacity is O(1), despite occasional O(n) resizing operations.
- **Growth Factor**: Most dynamic array implementations double capacity when full, resulting in sizes of 1, 2, 4, 8, 16, 32...
- **Memory Calculation**: `total_bytes = number_of_elements × sizeof(element_type)`

## Key Points

- Dynamic arrays use malloc(), calloc(), and realloc() for heap memory allocation in C.
- Always check for NULL return values after memory allocation functions.
- Set pointers to NULL after calling free() to prevent dangling pointer bugs.
- realloc() may move memory to a new location; always use a temporary variable.
- Dynamic arrays provide O(1) random access like static arrays but with flexibility.
- The standard growth strategy is to double capacity when full, achieving amortized O(1) insertion.
- Every malloc() or calloc() must have a corresponding free() to prevent memory leaks.
- Dynamic arrays are the foundation for implementing stacks, queues, and other advanced data structures.

## Common Mistakes to Avoid

- Not checking for NULL after malloc() can lead to segmentation faults when memory is exhausted.
- Forgetting to free() allocated memory causes memory leaks that accumulate over time.
- Using a pointer after free() (dangling pointer) leads to undefined behavior.
- Not assigning realloc() result to a temporary variable causes memory leaks if realloc() fails.
- Confusing stack allocation (automatic, limited size) with heap allocation (manual, large).

## Revision Tips

- Practice writing code that allocates, uses, and frees dynamic arrays repeatedly until it becomes automatic.
- Draw memory diagrams showing how data is arranged in heap versus stack.
- Memorize the four memory allocation functions and their specific use cases.
- Review past DU examination questions on this topic to understand the pattern of questions asked.
- Implement your own dynamic array from scratch without looking at reference solutions.