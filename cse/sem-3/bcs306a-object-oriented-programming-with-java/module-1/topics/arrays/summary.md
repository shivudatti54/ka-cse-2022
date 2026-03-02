# Arrays in Java - Summary

## Key Definitions and Concepts

- **Array:** A fixed-size indexed data structure that stores multiple values of the same type in contiguous memory locations.
- **Single-dimensional Array:** A linear collection of elements accessed using a single index.
- **Multi-dimensional Array:** An array of arrays, commonly used for matrices and tables.
- **Jagged Array:** A 2D array where each row can have a different number of columns.
- **Array Index:** The numeric position of an element in an array, starting from 0.

## Important Formulas and Theorems

- **Array Declaration:** `type[] arrayName = new type[size];`
- **Array Initialization:** `type[] arrayName = {value1, value2, ...};`
- **Valid Index Range:** 0 to (array.length - 1)
- **2D Array Access:** `arrayName[rowIndex][colIndex]`
- **Array Length:** `arrayName.length` (property, not method)

## Key Points

- Arrays in Java are objects stored in heap memory with zero-based indexing.
- Default initializations: 0 for numeric primitives, false for boolean, null for references.
- The `.length` property gives the number of elements, not the last index.
- Enhanced for loop (for-each) cannot modify array elements or access indices.
- The Arrays class (java.util.Arrays) provides utility methods: sort(), binarySearch(), fill(), toString(), equals().
- Attempting to access invalid indices throws ArrayIndexOutOfBoundsException.
- 2D arrays in Java are arrays of arrays, allowing for jagged/uneven structures.

## Common Mistakes to Avoid

1. Using `i <= array.length` in loops instead of `i < array.length` (causes ArrayIndexOutOfBoundsException)
2. Confusing array's `.length` (property) with String's `.length()` (method)
3. Thinking array size can be changed after initialization—arrays have fixed size
4. Forgetting that array indices start at 0, not 1
5. Using the C-style `int arr[]` declaration instead of Java-preferred `int[] arr`

## Revision Tips

1. Practice writing declaration, initialization, and traversal code for both 1D and 2D arrays.
2. Memorize the syntax for common Arrays class methods as they frequently appear in exams.
3. Draw memory representations of arrays to understand how they store data.
4. Solve at least 3-4 programming problems involving array manipulation before the exam.
5. Remember the key difference between `int[] arr = new int[5]` (creates array with defaults) and `int[] arr = {1,2,3}` (creates and initializes).
