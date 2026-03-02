# **12.1 to 12.8: Quick Revision Notes**

### 12.1: Introduction to Arrays

- An array is a collection of elements of the same data type stored in contiguous memory locations.
- Arrays are used to store and manipulate large amounts of data.
- Arrays are denoted by square brackets `[]` and elements are accessed using indices.

### 12.2: One-Dimensional Arrays

- A one-dimensional array is an array with a single dimension, where each element is accessed by a single index.
- Example: `int arr[5] = {1, 2, 3, 4, 5};`
- Key operations:
  - Initialization: `int arr[5];`
  - Assignment: `arr[i] = value;`
  - Access: `arr[i];`

### 12.3: Two-Dimensional Arrays

- A two-dimensional array is an array with two dimensions, where each element is accessed by two indices.
- Example: `int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};`
- Key operations:
  - Initialization: `int arr[2][3];`
  - Assignment: `arr[i][j] = value;`
  - Access: `arr[i][j];`

### 12.4: Initializing Two-Dimensional Arrays

- There are two ways to initialize a two-dimensional array:
  - Row-major initialization: `int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};`
  - Column-major initialization: `int arr[3][2] = {{1, 4}, {2, 5}, {3, 6}};`

### 12.5: Data Types for Arrays

- Arrays can be initialized with the following data types:
  - `int`
  - `float`
  - `double`
  - `char`
  - `boolean`

### 12.6: Array Operations

- Key operations:
  - Indexing: `arr[i]` and `arr[i][j]`
  - Slicing: `arr[i:j]`
  - Iteration: `for (int i = 0; i < n; i++) { ... }`

### 12.7: Array Size and Bounds Checking

- Array size is the number of elements in an array.
- Bounds checking is the process of checking if an index is within the valid range of the array.

### 12.8: Common Pitfalls

- Out-of-bounds access
- Null pointer dereference
- Incorrect array initialization

### Important Formulas and Definitions

- Definition of an array: An array is a collection of elements of the same data type stored in contiguous memory locations.
- Formula for calculating array size: `n = sizeof(arr) / sizeof(arr[0])`

Note: This summary is a concise revision note and is meant to be a quick reference for the topic 12.1 to 12.8. It is not a comprehensive study guide.
