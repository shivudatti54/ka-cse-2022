# Fundamentals of Data Structures in C - Summary

## Key Definitions and Concepts

- **Data Structure**: A way of organizing and storing data that enables efficient access and modification
- **Primitive Data Types**: Basic types including int, float, char, double in C
- **Array**: A contiguous collection of elements of the same data type with O(1) random access
- **Pointer**: A variable that stores the memory address of another variable
- **Structure**: A composite data type grouping variables of different types
- **Dynamic Memory Allocation**: Runtime memory allocation using malloc(), calloc(), realloc()
- **Array Decay**: Array name converts to pointer to first element when passed to functions

## Important Formulas and Theorems

- **Array Element Address**: `Address(arr[i]) = BaseAddress + i × sizeof(element_type)`
- **2D Array Row-Major**: `Address(arr[i][j]) = Base + (i × n + j) × sizeof(element)`
- **Time Complexity - Array Access**: O(1) for index-based access
- **Time Complexity - Array Search**: O(n) for linear search
- **Structure Size**: May include padding bytes for memory alignment

## Key Points

- C provides char, int, float, double as primitive types with specific memory sizes
- Arrays are zero-indexed; valid indices range from 0 to size-1
- 2D arrays in C are stored in row-major order
- Pointers store addresses; pointer arithmetic scales by sizeof(pointed type)
- Structure members are accessed using dot (.) operator; arrow (->) for pointer to structure
- malloc() returns uninitialized memory; calloc() initializes to zero
- Always check NULL after malloc/calloc and free memory when done
- Arrays pass to functions as pointers, losing size information
- Linked structures overcome fixed-size limitation of arrays

## Common Mistakes to Avoid

- Confusing sizeof() with strlen() - sizeof includes null terminator
- Forgetting to free dynamically allocated memory, causing memory leaks
- Using uninitialized pointers leading to undefined behavior
- Array indices out of bounds - accessing arr[n] when size is n
- Confusing pointer to pointer scenarios with 2D arrays
- Not checking for NULL after memory allocation

## Revision Tips

- Practice drawing memory layouts for arrays and structures
- Write and trace code involving pointer arithmetic repeatedly
- Memorize time complexities for basic operations on arrays
- Focus on differences between malloc/calloc/realloc and their use cases
- Review structure padding concept with practical examples
- Solve previous year CUET and semester exam questions on this topic