# Arrays in Java - Summary

## Key Definitions and Concepts

- **Array**: A fixed-size data structure that stores multiple values of the same type in contiguous memory locations, accessed via indices.

- **Array Declaration**: Creating a reference variable that points to an array object, using syntax like `int[] arr` or `int arr[]`.

- **Array Initialization**: Creating the actual array object using `new` keyword or direct initialization with curly braces `{...}`.

- **Index**: The numeric position of an element in an array, starting from 0 (zero-indexed).

- **Multi-Dimensional Array**: An array of arrays, commonly used for matrices and tabular data representation.

- **Jagged Array**: A multi-dimensional array where each row can have a different number of columns.

## Important Formulas and Concepts

- Array index range: 0 to (length - 1)
- Array element access: `arrayName[index]`
- Default values: 0 for numbers, null for objects, false for boolean
- Array length: accessed via `arrayName.length` property (note: no parentheses, unlike String's length() method)

## Key Points

- Arrays in Java are objects stored in heap memory with a fixed size determined at creation time.

- Java arrays support only one-dimensional, two-dimensional, and three-dimensional structures natively; higher dimensions require array-of-arrays.

- The enhanced for-each loop provides cleaner syntax but cannot modify array elements or access indices directly.

- The Arrays class from java.util provides static methods: sort(), binarySearch(), fill(), equals(), and toString().

- When passing arrays to methods, the reference is passed, meaning modifications affect the original array.

- Two-dimensional arrays are stored as arrays of arrays, allowing unequal row lengths (jagged arrays).

## Common Mistakes to Avoid

- Confusing `length` (array property) with `length()` (String method) - a frequent source of compilation errors.

- Attempting to access indices outside the valid range (0 to length-1), which causes ArrayIndexOutOfBoundsException.

- Separating array declaration from initialization when using curly brace syntax: `int[] arr; arr = {1,2,3};` is invalid.

- Forgetting that array indices start at 0, not 1, when writing loops or accessing elements.

## Revision Tips

- Practice declaring, initializing, and iterating through arrays until the syntax becomes automatic.

- Remember the three main steps: declare the array reference, create the array object with new, then assign values.

- Use the Arrays.toString() method for quick debugging instead of manually printing elements.

- For exams, memorize the common Arrays class methods and their requirements (especially that binarySearch requires a sorted array).