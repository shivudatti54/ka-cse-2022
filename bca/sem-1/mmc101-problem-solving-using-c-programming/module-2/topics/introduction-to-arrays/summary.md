# Introduction to Arrays - Summary

## Key Definitions and Concepts

- ARRAY: A contiguous collection of elements of the same data type, stored in memory and accessed using indices.

- ONE-DIMENSIONAL ARRAY: A linear collection of elements accessed using a single index, declared as data_type array_name[size].

- ZERO-BASED INDEXING: The C programming convention where the first array element is accessed using index 0.

- ARRAY DECAY: The phenomenon where an array name used in expressions converts to a pointer to the first element.

- CONTIGUOUS MEMORY STORAGE: Arrays store all elements in consecutive memory locations, enabling efficient random access.

## Important Formulas and Theorems

- Array element address calculation: ADDRESS = BASE_ADDRESS + (INDEX × SIZE_OF_ELEMENT)

- Array size in bytes: TOTAL_BYTES = NUMBER_OF_ELEMENTS × SIZE_OF(each element)

- Valid index range: 0 to (ARRAY_SIZE - 1)

## Key Points

- Arrays allow storage of multiple values of the same type under a single variable name.

- Array size must be a constant expression in standard C (though C99 supports variable-length arrays).

- Initialization can use initializer lists: int arr[5] = {10, 20, 30, 40, 50}; Partial initialization sets remaining elements to zero.

- Omitting array size during initialization automatically determines size: int arr[] = {1, 2, 3}; creates array of size 3.

- Arrays provide O(1) constant time complexity for element access due to address calculation formula.

- The array name represents the base address (pointer to first element), but arrays and pointers are distinct entities.

- Multi-dimensional arrays in C use row-major storage order.

## Common Mistakes to Avoid

- Forgetting zero-based indexing and starting loop indices from 1 instead of 0.

- Accessing array elements using indices outside the valid range (0 to n-1), causing undefined behavior.

- Confusing array declaration with initialization—using uninitialized arrays leads to garbage values.

- Assuming arrays are passed by value to functions; they are actually passed by reference (as pointers).

- Declaring array size using variables without understanding Variable Length Array (VLA) limitations.

## Revision Tips

- Practice declaring and initializing arrays with different data types (int, float, char).

- Write programs to find sum, average, maximum, and minimum from array elements—these are frequently examined.

- Trace through array address calculations by hand to reinforce memory representation concepts.

- Remember that the exam often tests conceptual understanding through questions on memory layout and address calculation.