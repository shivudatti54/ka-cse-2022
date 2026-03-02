# Pointer Arithmetic - Summary

## Key Definitions and Concepts

- **Pointer Arithmetic**: Operations performed on pointers that automatically scale based on the size of the data type pointed to, enabling efficient array and memory traversal.

- **Pointer Scaling**: When adding n to a pointer, the address advances by n × sizeof(data_type) bytes, not by n bytes.

- **Pointer Decay**: Array name without brackets decays to a pointer to the first element, making arrays and pointers interchangeable in many contexts.

## Important Formulas and Theorems

- `ptr + n` → advances pointer by n elements
- `ptr - n` → moves pointer backward by n elements
- `ptr1 - ptr2` → yields number of elements between two pointers (must be same type)
- `* (arr + i)` ≡ `arr[i]` → fundamental equivalence between pointer arithmetic and array subscripting
- Size advancement: `sizeof(data_type)` bytes per increment/decrement

## Key Points

- Only five arithmetic operations are valid on pointers in C: addition of integer, subtraction of integer, pointer subtraction, increment (++), and decrement (--).

- Pointer addition of two pointers is NOT valid and will cause compilation errors.

- Pointer arithmetic on NULL pointers leads to undefined behavior and program crashes.

- Void pointers require casting to a specific type before performing arithmetic operations.

- Character pointers advance by 1 byte, integer pointers by 4 bytes (typically), and double pointers by 8 bytes (typically).

- Array indexing and pointer arithmetic are mathematically equivalent: `arr[5]` and `*(arr + 5)` access the same memory location.

- The result of pointer subtraction is an integer representing the number of elements between the two positions.

## Common Mistakes to Avoid

- Forgetting that pointer arithmetic scales by data type size instead of assuming it adds exactly 1 to the address.

- Performing arithmetic on uninitialized or NULL pointers, which causes undefined behavior.

- Adding two pointers together, which is not allowed in C and results in compilation error.

- Attempting pointer arithmetic on void pointers without proper type casting.

- Going out of array bounds when using pointer arithmetic, leading to buffer overflow and undefined behavior.

## Revision Tips

- Practice tracing through code examples that use pointer arithmetic in loops to build intuition.

- Memorize the equivalence between array subscript notation and pointer arithmetic expressions.

- Write small programs to verify how different pointer types scale when incremented.

- Review previous years' DU examination questions on pointer arithmetic for pattern recognition.

- Create a table showing pointer advancement for different data types on your system.