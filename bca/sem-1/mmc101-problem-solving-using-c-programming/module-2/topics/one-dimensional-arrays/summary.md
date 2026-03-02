# One Dimensional Arrays - Summary

## Key Definitions and Concepts

- **Array**: A collection of elements of the same data type stored in contiguous memory locations, accessed by a common name and unique indices
- **Base Address**: The memory address of the first element of an array, represented by the array name
- **Index/Subscript**: An integer value used to access a specific element, ranging from 0 to (size-1) in C
- **Contiguous Memory**: Array elements are stored in successive memory locations, enabling efficient random access
- **Array Declaration**: `data_type array_name[size];` allocates memory for the specified number of elements
- **Array Initialization**: Providing initial values at declaration time using curly braces

## Important Formulas and Theorems

- **Memory Address Calculation**: `Address of arr[i] = Base Address + (i × sizeof(element_type))`
- **Total Array Size**: `Total bytes = array_size × sizeof(data_type)`
- **Array name behavior**: In most contexts, array name decays to pointer to first element
- **Index bounds**: Valid indices are 0 through (n-1) for an array of n elements

## Key Points

- C arrays have zero-based indexing, meaning the first element is at index 0
- Arrays are passed to functions by reference, not by value—only the base address is passed
- Uninitialized local arrays contain garbage values; global/static arrays are zero-initialized
- Array size must be known at compile time for static arrays, but C99/C11 supports Variable Length Arrays (VLA)
- The subscript operator `[]` has higher precedence than the address operator `&`
- Array parameters are equivalent to pointer parameters in function definitions
- Multi-dimensional arrays in C are stored in row-major order

## Common Mistakes to Avoid

- Accessing array elements beyond the declared size (buffer overflow)
- Confusing array size with the highest valid index
- Assuming array size is passed automatically to functions
- Using uninitialized array indices in loops
- Attempting to assign a new address to an array name

## Revision Tips

- Practice writing declarations, initializations, and basic operations repeatedly
- Trace through code examples manually to understand index manipulation
- Memorize the formula for calculating element addresses in memory
- Review pointer-array relationship as it frequently appears in advanced questions
- Solve previous year University examination questions on this topic
- Write and debug programs involving array manipulation to gain practical confidence