# Multidimensional Arrays

## Introduction to Multidimensional Arrays

A multidimensional array is an array of arrays. While one-dimensional arrays represent linear sequences of elements, multidimensional arrays extend this concept to represent data in multiple dimensions, such as tables (2D), cubes (3D), or higher-dimensional structures.

In programming, multidimensional arrays are particularly useful for representing:

- Matrices and grid-based data
- Game boards (chess, tic-tac-toe)
- Image pixel data
- Scientific data with multiple parameters
- Database-like tabular information

## Two-Dimensional Arrays

A two-dimensional array is the most common type of multidimensional array. It can be visualized as a table with rows and columns.

### Declaration Syntax

```c
data_type array_name[rows][columns];
```

**Example:**

```c
int matrix[3][4]; // A 3x4 integer matrix
```

### Memory Representation

In C, multidimensional arrays are stored in **row-major order**, meaning elements are stored row by row in contiguous memory locations.

```
Memory layout for int arr[2][3]:
+-------+-------+-------+-------+-------+-------+
| [0][0]| [0][1]| [0][2]| [1][0]| [1][1]| [1][2]|
+-------+-------+-------+-------+-------+-------+
Address: 1000 1004 1008 1012 1016 1020
```

### Accessing Elements

Elements are accessed using two indices: row index and column index.

```c
int value = matrix[1][2]; // Access element at row 1, column 2
matrix[0][3] = 42; // Set element at row 0, column 3 to 42
```

## Initializing Two-Dimensional Arrays

Two-dimensional arrays can be initialized during declaration in several ways:

### Method 1: Full Initialization

```c
int matrix[2][3] = {
 {1, 2, 3}, // Row 0
 {4, 5, 6} // Row 1
};
```

### Method 2: Partial Initialization

```c
int matrix[2][3] = {
 {1, 2}, // Row 0: [1, 2, 0]
 {4, 5, 6} // Row 1: [4, 5, 6]
};
```

### Method 3: Flattened Initialization

```c
int matrix[2][3] = {1, 2, 3, 4, 5, 6};
```

### Method 4: Omitting Row Size

```c
int matrix[][3] = {
 {1, 2, 3},
 {4, 5, 6}
};
// Compiler infers row size as 2
```

## Three-Dimensional Arrays

Three-dimensional arrays extend the concept further, adding a third dimension. They can be visualized as a cube or a collection of tables.

### Declaration and Initialization

```c
int cube[2][3][4] = {
 { // Layer 0
 {1, 2, 3, 4},
 {5, 6, 7, 8},
 {9, 10, 11, 12}
 },
 { // Layer 1
 {13, 14, 15, 16},
 {17, 18, 19, 20},
 {21, 22, 23, 24}
 }
};
```

### Memory Representation

3D arrays are stored in **layer-row-column** order:

```
Memory layout for int arr[2][2][2]:
+-----------+-----------+-----------+-----------+
|[0][0][0] |[0][0][1] |[0][1][0] |[0][1][1] |
+-----------+-----------+-----------+-----------+
|[1][0][0] |[1][0][1] |[1][1][0] |[1][1][1] |
+-----------+-----------+-----------+-----------+
```

## Higher-Dimensional Arrays

While rarely used beyond three dimensions, C supports arrays with more dimensions:

```c
int hypercube[2][3][4][5]; // 4-dimensional array
```

Each additional dimension increases the complexity exponentially, both in terms of memory usage and computational requirements.

## Working with Multidimensional Arrays

### Iterating Through Elements

**Nested loops** are essential for accessing all elements in multidimensional arrays:

```c
// 2D array iteration
for (int i = 0; i < rows; i++) {
 for (int j = 0; j < columns; j++) {
 printf("matrix[%d][%d] = %d\n", i, j, matrix[i][j]);
 }
}

// 3D array iteration
for (int i = 0; i < layers; i++) {
 for (int j = 0; j < rows; j++) {
 for (int k = 0; k < columns; k++) {
 printf("cube[%d][%d][%d] = %d\n", i, j, k, cube[i][j][k]);
 }
 }
}
```

### Passing to Functions

When passing multidimensional arrays to functions, you must specify all dimensions except the first:

```c
void printMatrix(int arr[][3], int rows) {
 for (int i = 0; i < rows; i++) {
 for (int j = 0; j < 3; j++) {
 printf("%d ", arr[i][j]);
 }
 printf("\n");
 }
}

// Function call
printMatrix(matrix, 2);
```

## Practical Applications

### Matrix Operations

```c
// Matrix addition
void addMatrices(int A[][3], int B[][3], int result[][3], int rows) {
 for (int i = 0; i < rows; i++) {
 for (int j = 0; j < 3; j++) {
 result[i][j] = A[i][j] + B[i][j];
 }
 }
}
```

### Image Processing

```c
// Simple image brightness adjustment
void adjustBrightness(int image[][100][3], int height, int width, int factor) {
 for (int i = 0; i < height; i++) {
 for (int j = 0; j < width; j++) {
 for (int k = 0; k < 3; k++) { // RGB channels
 image[i][j][k] = min(255, image[i][j][k] + factor);
 }
 }
 }
}
```

## Memory Management Considerations

### Static vs Dynamic Allocation

**Static allocation** (compile-time):

```c
int staticArray[10][10]; // Fixed size, stack memory
```

**Dynamic allocation** (run-time):

```c
// Allocate a 2D array dynamically
int** dynamicArray = malloc(rows * sizeof(int*));
for (int i = 0; i < rows; i++) {
 dynamicArray[i] = malloc(columns * sizeof(int));
}

// Don't forget to free memory!
for (int i = 0; i < rows; i++) {
 free(dynamicArray[i]);
}
free(dynamicArray);
```

## Comparison Table: Array Types

| Dimension | Declaration              | Memory Usage                     | Common Use Cases                |
| --------- | ------------------------ | -------------------------------- | ------------------------------- |
| 1D        | `int arr[size]`          | size × sizeof(int)               | Lists, sequences                |
| 2D        | `int arr[rows][cols]`    | rows × cols × sizeof(int)        | Tables, matrices, grids         |
| 3D        | `int arr[x][y][z]`       | x × y × z × sizeof(int)          | Volumetric data, RGB images     |
| nD        | `int arr[d1][d2]...[dn]` | d1 × d2 × ... × dn × sizeof(int) | Scientific data, complex models |

## Common Errors and Pitfalls

1. **Index out of bounds**: Accessing `arr[i][j]` when i or j exceeds array dimensions
2. **Memory overconsumption**: Higher-dimensional arrays can consume memory rapidly
3. **Forgetting to free dynamically allocated memory**
4. **Incorrect function parameter declarations**: Omitting sizes for dimensions after the first

## Performance Considerations

- Accessing elements in row-major order is faster due to **cache locality**
- The time complexity for accessing an element is O(1) for any dimension
- The space complexity is O(n^k) for k-dimensional arrays

## Exam Tips

1. **Memory layout**: Remember that C uses row-major order for multidimensional arrays
2. **Initialization**: Know all the different ways to initialize multidimensional arrays
3. **Function parameters**: When passing to functions, only the first dimension can be omitted
4. **Pointer equivalence**: Understand that `arr[i][j]` is equivalent to `*(*(arr + i) + j)`
5. **Dynamic allocation**: Practice the pattern for dynamically allocating and freeing 2D arrays
6. **Common applications**: Be prepared to give examples of where multidimensional arrays are used in real-world applications
