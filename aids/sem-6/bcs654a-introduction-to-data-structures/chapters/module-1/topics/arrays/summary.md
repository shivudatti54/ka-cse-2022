# Arrays - Summary

## Key Definitions and Concepts

- **Array:** A collection of elements of the same data type stored in contiguous memory locations, accessible through indices.
- **One-Dimensional Array:** Linear arrangement of elements accessed using a single index.
- **Two-Dimensional Array:** Table-like structure with rows and columns, accessed using two indices.
- **Array Index:** The position number used to access elements; in C, indices start from 0.
- **Array Decay:** The phenomenon where array names convert to pointers when passed to functions.

## Important Formulas and Theorems

- **Array Element Access:** `array_name[index]` or `*(array_name + index)`
- **Array Size Calculation:** `number_of_elements = sizeof(array) / sizeof(array[0])`
- **Total Bytes:** `total_bytes = sizeof(data_type) × number_of_elements`
- **2D Array Memory:** Elements stored in row-major order (first row complete, then second row, etc.)

## Key Points

- C arrays are zero-indexed; valid indices range from 0 to (size-1).
- Array name acts as a constant pointer to the first element.
- Arrays can be initialized using curly braces {} or element-by-element.
- Two-dimensional arrays require specification of column size in function parameters.
- Uninitialized global arrays are automatically zero-initialized; local arrays contain garbage values.
- Array elements are stored in contiguous memory locations.
- Multidimensional arrays follow the same principles extended to multiple dimensions.
- Passing arrays to functions passes the address, not a copy of the array.

## Common Mistakes to Avoid

- Forgetting that array indices start at 0 instead of 1
- Accessing elements beyond array bounds (buffer overflow)
- Not specifying column size when declaring 2D array parameters in functions
- Confusing array name with a pointer variable (array name is constant)
- Using uninitialized local arrays without assigning values
- Confusing row-major and column-major storage order

## Revision Tips

- Practice declaring and initializing arrays of different data types.
- Draw memory representations to visualize array storage.
- Memorize the relationship between arrays and pointers.
- Solve at least 5-10 problems involving array traversal and manipulation.
- Remember: array[0] and *(array+0) are equivalent expressions.