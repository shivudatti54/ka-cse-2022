# Arrays and Structures - Summary

## Key Definitions and Concepts

- **Array:** A collection of elements of the same data type stored in contiguous memory locations, accessed via indices starting from 0

- **Structure:** A user-defined data type that groups related variables of different types under a single name, defined using the `struct` keyword

- **Dynamic Array:** An array whose size is determined at runtime using dynamic memory allocation functions

- **Array of Structures:** A collection of structure variables, used extensively for storing database records

- **Pointer Arithmetic:** Operations on pointers that move through memory locations based on the size of the data type being pointed to

## Important Formulas and Theorems

- **1D Array Address:** `Address(arr[i]) = Base + (i × size_of_element)`

- **2D Array Address (Row-Major):** `Address(arr[i][j]) = Base + [(i × n + j) × size]`

- **2D Array Address (Column-Major):** `Address(arr[i][j]) = Base + [(j × m + i) × size]`

- **Dynamic Array Growth:** When capacity is reached, typically double the capacity: `new_capacity = old_capacity × 2`

## Key Points

- Arrays store homogeneous data; structures store heterogeneous data
- Array indices start from 0 and go up to (size - 1)
- Array name acts as a constant pointer to the first element
- Structures use dot (.) operator for direct member access and arrow (->) operator for pointer-to-structure access
- Dynamic memory allocation uses heap memory; must be explicitly freed to prevent memory leaks
- malloc does not initialize memory; calloc initializes to zero
- realloc can both increase and decrease allocated memory
- Arrays of structures are fundamental for implementing file handling and database systems

## Common Mistakes to Avoid

- Confusing array indices: Remember first element is at index 0, not 1
- Not checking for NULL after dynamic memory allocation
- Using uninitialized pointers for dynamic memory operations
- Forgetting to free dynamically allocated memory, causing memory leaks
- Accessing array elements beyond declared bounds (buffer overflow)
- Confusing row-major and column-major storage in 2D arrays

## Revision Tips

1. Practice writing programs for array operations: searching, sorting, finding maximum/minimum

2. Memorize the address calculation formulas for both 1D and 2D arrays

3. Create a comparison table of array vs structure characteristics

4. Write programs implementing dynamic arrays from scratch

5. Solve previous year DU examination questions on this topic