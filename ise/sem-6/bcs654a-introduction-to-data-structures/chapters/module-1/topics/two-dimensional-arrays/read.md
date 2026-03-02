# Two-Dimensional Arrays

## Introduction to Two-Dimensional Arrays

A two-dimensional (2D) array is a data structure that stores elements in a **tabular format** consisting of rows and columns. It can be visualized as a matrix or a grid. While a one-dimensional array represents a single list of elements, a 2D array extends this concept to two dimensions, creating a structure that is particularly useful for representing data that naturally forms a table, such as:

- Game boards (chess, tic-tac-toe)
- Digital images (pixel matrices)
- Spreadsheet data
- Mathematical matrices
- Seating arrangements

## Declaration of Two-Dimensional Arrays

In the C programming language, a two-dimensional array is declared using the following syntax:

```c
data_type array_name[number_of_rows][number_of_columns];
```

**Example:**

```c
int matrix[3][4];  // Declares a 2D array with 3 rows and 4 columns
float temperatures[7][24]; // 7 days, 24 hourly temperatures each
char gameBoard[3][3]; // A 3x3 tic-tac-toe board
```

### Memory Allocation

A 2D array is stored in **row-major order** in memory. This means that all elements of row 0 are stored first, followed by all elements of row 1, and so on. The entire array occupies a contiguous block of memory.

**Memory Representation:**

```
Row 0: [element[0][0], element[0][1], element[0][2], element[0][3]]
Row 1: [element[1][0], element[1][1], element[1][2], element[1][3]]
Row 2: [element[2][0], element[2][1], element[2][2], element[2][3]]
```

The total memory required is calculated as:
`Total Memory = rows × columns × sizeof(data_type)`

## Initializing Two-Dimensional Arrays

Two-dimensional arrays can be initialized during declaration in several ways:

### Method 1: Fully Specified Initialization

```c
int matrix[2][3] = {
    {1, 2, 3},    // Row 0
    {4, 5, 6}     // Row 1
};
```

### Method 2: Partial Initialization

Unspecified elements are automatically set to zero.

```c
int matrix[2][3] = {
    {1, 2},        // Row 0: [1, 2, 0]
    {4, 5, 6}      // Row 1: [4, 5, 6]
};
```

### Method 3: Flattened Initialization

Elements are filled row-wise, but this approach is less readable.

```c
int matrix[2][3] = {1, 2, 3, 4, 5, 6};
// Results in: Row 0: [1, 2, 3], Row 1: [4, 5, 6]
```

### Method 4: Omitting Row Dimension

The compiler can deduce the number of rows from the initialization.

```c
int matrix[][3] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}    // Compiler understands this is a 3x3 array
};
```

**Note:** While the row dimension can be omitted, the column dimension must always be specified.

## Accessing Array Elements

Elements in a 2D array are accessed using two indices: row index and column index, both starting from 0.

```c
int value = matrix[1][2];  // Accesses element at row 1, column 2
matrix[0][1] = 10;        // Modifies element at row 0, column 1
```

### ASCII Diagram of Array Access

```
Column: 0    1    2
Row 0: [10] [20] [30]
Row 1: [40] [50] [60]
Row 2: [70] [80] [90]

matrix[1][2] → 60
matrix[2][0] → 70
```

## Processing Two-Dimensional Arrays

Processing 2D arrays typically involves nested loops: an outer loop for rows and an inner loop for columns.

### Example: Printing a 2D Array

```c
#include <stdio.h>

int main() {
    int matrix[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    printf("Matrix elements:\n");
    for(int i = 0; i < 3; i++) {        // Row iteration
        for(int j = 0; j < 3; j++) {    // Column iteration
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }

    return 0;
}
```

**Output:**

```
Matrix elements:
1       2       3
4       5       6
7       8       9
```

### Example: Finding Sum of All Elements

```c
int sum = 0;
for(int i = 0; i < rows; i++) {
    for(int j = 0; j < columns; j++) {
        sum += matrix[i][j];
    }
}
printf("Sum of all elements: %d\n", sum);
```

### Example: Row-wise and Column-wise Sum

```c
// Row-wise sum
for(int i = 0; i < rows; i++) {
    int rowSum = 0;
    for(int j = 0; j < columns; j++) {
        rowSum += matrix[i][j];
    }
    printf("Sum of row %d: %d\n", i, rowSum);
}

// Column-wise sum
for(int j = 0; j < columns; j++) {
    int colSum = 0;
    for(int i = 0; i < rows; i++) {
        colSum += matrix[i][j];
    }
    printf("Sum of column %d: %d\n", j, colSum);
}
```

## Relationship with Pointers

A 2D array has a special relationship with pointers. The array name is a pointer to the first row, and each row is itself an array.

```c
int matrix[3][4];

// matrix points to the first row (matrix[0])
// matrix[i] points to the first element of the i-th row
// *(matrix[i] + j) is equivalent to matrix[i][j]
```

### Pointer Notation for 2D Arrays

```c
// These all access the same element:
matrix[i][j]
*(matrix[i] + j)
*(*(matrix + i) + j)
```

## Multidimensional Arrays

C programming language supports arrays with more than two dimensions. The concept extends naturally from 2D arrays.

### Declaration of 3D Array

```c
int threeD[2][3][4]; // 2 layers, each with 3 rows and 4 columns
```

### Initialization of 3D Array

```c
int threeD[2][3][2] = {
    { {1, 2}, {3, 4}, {5, 6} },     // Layer 0
    { {7, 8}, {9, 10}, {11, 12} }   // Layer 1
};
```

## Applications of Two-Dimensional Arrays

1. **Mathematical Operations**: Matrix addition, multiplication, transposition
2. **Image Processing**: Storing and manipulating pixel values
3. **Game Development**: Board games, grid-based games
4. **Spreadsheet Applications**: Tabular data storage and calculation
5. **Graph Algorithms**: Adjacency matrix representation of graphs

## Comparison: 1D vs 2D Arrays

| Aspect            | One-Dimensional Array   | Two-Dimensional Array               |
| ----------------- | ----------------------- | ----------------------------------- |
| **Declaration**   | `data_type array[size]` | `data_type array[rows][columns]`    |
| **Dimensions**    | Single dimension        | Two dimensions (rows and columns)   |
| **Access**        | Single index `array[i]` | Two indices `array[i][j]`           |
| **Memory**        | Contiguous block        | Contiguous block in row-major order |
| **Visualization** | Linear list             | Table/grid/matrix                   |
| **Common Use**    | Lists of items          | Tabular data, matrices              |

## Common Operations and Their Complexities

| Operation             | Time Complexity | Description                               |
| --------------------- | --------------- | ----------------------------------------- |
| **Access**            | O(1)            | Direct access using indices               |
| **Traversal**         | O(n×m)          | Visiting all elements (n rows, m columns) |
| **Searching**         | O(n×m)          | Linear search through all elements        |
| **Row Operations**    | O(m)            | Operations on a single row                |
| **Column Operations** | O(n)            | Operations on a single column             |

## Exam Tips

1. **Memory Layout**: Remember that 2D arrays are stored in row-major order in contiguous memory locations.

2. **Index Boundaries**: Always be mindful of array boundaries. Accessing `array[i][j]` where i ≥ rows or j ≥ columns causes undefined behavior.

3. **Initialization**: When initializing, you can omit the row dimension but not the column dimension.

4. **Pointer Relationship**: Understand how 2D arrays relate to pointers: `array[i][j] ≡ *(*(array + i) + j)`.

5. **Efficiency**: For better cache performance, process elements in row-major order (row-by-row) rather than column-by-column.

6. **Dynamic Allocation**: For large or variable-sized arrays, consider dynamic memory allocation using pointers to pointers.

7. **Common Errors**: Watch out for off-by-one errors, especially when using loops to process arrays.
