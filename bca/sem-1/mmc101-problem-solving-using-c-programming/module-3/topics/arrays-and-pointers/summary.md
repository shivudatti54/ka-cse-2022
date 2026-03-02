# Arrays and Pointers - Summary

## Key Definitions and Concepts

- ARRAY: A collection of elements of the same data type stored in contiguous memory locations
- POINTER: A variable that stores the memory address of another variable
- POINTER ARITHMETIC: Operations on pointers that automatically scale based on the data type size
- ARRAY DECAY: The phenomenon where an array name in expressions converts to a pointer to its first element

## Important Formulas and Theorems

- Array element access: arr[i] is equivalent to *(arr + i)
- Address of element: &arr[i] is equivalent to (arr + i)
- Pointer difference: (ptr2 - ptr1) gives number of elements between them
- Size calculation: sizeof(array) = number_of_elements × sizeof(element_type)

## Key Points

- Array indices in C START FROM 0, not 1
- Array names act as CONSTANT POINTERS to the first element
- Pointer increment/decrement scales by sizeof(data_type)
- Two-dimensional arrays are stored in ROW-MAJOR ORDER
- When passing arrays to functions, SIZE MUST BE PASSED SEPARATELY
- Uninitialized pointers contain GARBAGE VALUES and cause undefined behavior
- NULL pointer indicates "no valid address"
- String literals are read-only; use character arrays for mutable strings

## Common Mistakes to Avoid

- CONFUSING ARRAY SIZE with last valid index (size n means indices 0 to n-1)
- FORGETTING TO INITIALIZE pointers before use
- USING POINTER ARITHMETIC on pointers to different arrays
- NOT ACCOUNTING for null terminator '\0' in character arrays
- ASSUMING sizeof gives array size in function parameters (it gives pointer size)

## Revision Tips

- Practice writing programs that traverse arrays using both subscript and pointer notation
- MEMORIZE THE EQUIVALENCE: arr[i] ≡ *(arr + i)
- Draw memory layouts for array-pointer relationships
- Solve at least 5 problems involving 2D arrays and pointer arithmetic
- Review previous year DU question papers for pattern and difficulty level