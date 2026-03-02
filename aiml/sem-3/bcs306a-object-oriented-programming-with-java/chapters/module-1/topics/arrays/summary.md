# Arrays in Java - Summary

## Key Definitions and Concepts

- **Array**: A data structure that stores multiple elements of the same type in contiguous memory locations, accessible through indices.
- **One-Dimensional Array**: A linear array with elements accessed by a single index (0 to length-1).
- **Multi-Dimensional Array**: An array of arrays, commonly a 2D array visualized as rows and columns.
- **Jagged Array**: A multi-dimensional array where each row can have a different number of columns.
- **Array Index**: The numerical position of an element in an array, starting from 0.

## Important Formulas and Theorems

- Array element access: `arrayName[index]`
- Array length: `arrayName.length` (property, not method)
- Linear search time complexity: O(n)
- Binary search time complexity: O(log n) - requires sorted array
- Sorting time complexity: O(n log n)
- Maximum valid index: `arrayName.length - 1`

## Key Points

- Arrays in Java are objects stored in heap memory with a fixed size once created.
- Default initialization: 0 for numeric types, false for boolean, null for reference types.
- Both `int[] arr` and `int arr[]` are valid declaration syntaxes.
- Arrays provide direct access to elements via indices with O(1) time complexity.
- The enhanced for-each loop cannot modify array elements (works with copies).
- Java performs runtime bounds checking and throws ArrayIndexOutOfBoundsException for invalid access.
- Arrays can store either primitive types or object references.
- The Arrays utility class provides useful methods: sort(), binarySearch(), toString(), copyOf().

## Common Mistakes to Avoid

- Confusing array length with the last valid index (remember: indices go from 0 to length-1).
- Attempting to resize an array after creation (arrays have fixed length in Java).
- Using `.length` with parentheses like a method call (arrays use property, strings use method).
- Forgetting that enhanced for-loop creates a copy and modifications won't affect the original array.
- Not handling null arrays before accessing elements, which causes NullPointerException.

## Revision Tips

- Practice declaring and initializing arrays in multiple ways to solidify syntax.
- Write programs to find sum, average, maximum, and minimum from array elements.
- Implement both linear and binary search algorithms manually before using built-in methods.
- Understand the difference between 1D and 2D array memory representation.
- Remember to use Arrays.deepToString() for printing multi-dimensional arrays.
- Review default values for different array types as this is a common exam question.