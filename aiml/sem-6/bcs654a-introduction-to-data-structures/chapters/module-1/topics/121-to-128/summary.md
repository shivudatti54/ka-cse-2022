# **Revision Notes for 12.1 to 12.8: Introduction to Arrays**

### Key Concepts

- **One-Dimensional Arrays**:
  - Definition: An array of elements of the same data type stored in contiguous memory locations.
  - Example: `int arr[5] = {1, 2, 3, 4, 5};`
- **Two-Dimensional Arrays**:
  - Definition: An array of elements of the same data type stored in rows and columns of contiguous memory locations.
  - Example: `int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};`
- **Initializing Two-Dimensional Arrays**:
  - Using curly brackets `{}`: `int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};`
  - Using assignment operators: `int arr[2][3]; arr[0][0] = 1; arr[0][1] = 2;`
- **Array Indexing and Bounds Checking**:
  - Definition: Accessing an element in an array using its index.
  - Formula: `arr[index]`
  - Bounds checking: Ensures that the index is within the valid range of the array.

### Important Formulas and Theorems

- **Array Index Formula**: `arr[index]`
- **Bounds Checking**: `if (0 <= index && index < size) { ... }`
- **Two-Dimensional Array Index Formula**: `arr[row][column]`

### Key Definitions

- **Data Type**: The type of value an array can hold, such as `int`, `char`, etc.
- **Memory Location**: The physical location in memory where the array is stored.

### Key Theorems

- **Array Size**: The number of elements an array can hold, denoted by `size`.
- **Array Index Range**: The range of valid indices for an array, denoted by `0 <= index < size`.
