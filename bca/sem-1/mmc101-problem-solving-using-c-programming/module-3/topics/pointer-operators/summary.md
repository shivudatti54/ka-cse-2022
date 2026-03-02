# Pointer Operators in C - Summary

## Key Definitions and Concepts

- **Address-of Operator (&)**: Unary operator that returns the memory address of its operand, yielding a pointer to that variable.
- **Dereference Operator (*)**: Unary operator that accesses the value stored at the memory location pointed to by a pointer.
- **Pointer Arithmetic**: Operations of addition, subtraction, increment, and decrement on pointers; automatically scales by the size of the pointed-to type.
- **NULL Pointer**: A pointer that does not point to any valid memory location, typically represented by the macro NULL or literal 0.
- **Pointer Comparison**: Using relational (>, <, >=, <=) and equality (==, !=) operators to compare pointer values.

## Important Formulas and Theorems

- If ptr is a pointer to type T, then ptr + n points to the n-th element after ptr (address: ptr + n * sizeof(T))
- Pointer subtraction: ptr2 - ptr1 = number of elements between the two addresses
- Array name "arr" is equivalent to &arr[0] in most expressions
- Size relationship: sizeof(pointer) is typically 4 or 8 bytes depending on architecture

## Key Points

- THE ADDRESS-OOPERATOR (&) RETURNS AN ADDRESS, NOT A VALUE
- THE DEREFERENCE OPERATOR (*) ACCESSES THE VALUE AT AN ADDRESS
- POINTER ARITHMETIC AUTOMATICALLY MULTIPLIES BY SIZEOF(POINTED-TYPE)
- POINTER ADDITION OF TWO POINTERS IS INVALID IN C
- POINTER SUBTRACTION RETURNS THE NUMBER OF ELEMENTS BETWEEN ADDRESSES
- ALWAYS VERIFY POINTER IS NOT NULL BEFORE DEREFERENCING
- POINTERS TO DIFFERENT TYPES ARE INCOMPATIBLE WITHOUT CASTING
- INCREMENTING A POINTER MOVES IT TO THE NEXT ELEMENT OF ITS TYPE

## Common Mistakes to Avoid

- CONFUSING & AND * OPERATORS: Using & when * is needed or vice versa
- FORGETTING TO INITIALIZE POINTERS: Using uninitialized pointers causes undefined behavior
- IGNORING POINTER TYPE MISMATCH: Assigning incompatible pointer types leads to errors
- DEREFERENCING NULL POINTERS: Causes segmentation faults and program crashes
- ASSUMING POINTER ARITHMETIC WORKS LIKE INTEGER ARITHMETIC: Remember the scaling factor

## Revision Tips

- PRACTICE WRITING CODE: Implement small programs to understand address and dereference operations
- TRACE THROUGH EXAMPLES: Manually compute pointer values and address changes step-by-step
- MEMORIZE THE RULES: Focus on what operations are valid and what causes undefined behavior
- STUDY ARRAY-POINTER RELATIONSHIP: This connection frequently appears in exams
- REVIEW COMMON PATTERNS: Function parameter passing using pointers, array traversal with pointers