# Two Dimensional Arrays


## Table of Contents

- [Two Dimensional Arrays](#two-dimensional-arrays)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Declaration of Two Dimensional Arrays](#declaration-of-two-dimensional-arrays)
  - [Memory Representation](#memory-representation)
  - [Initialization](#initialization)
  - [Accessing Elements](#accessing-elements)
  - [Passing Two Dimensional Arrays to Functions](#passing-two-dimensional-arrays-to-functions)
- [Examples](#examples)
  - [Example 1: Matrix Addition](#example-1-matrix-addition)
  - [Example 2: Transpose of a Matrix](#example-2-transpose-of-a-matrix)
  - [Example 3: Row-wise Sum and Maximum Element](#example-3-row-wise-sum-and-maximum-element)
- [Exam Tips](#exam-tips)

## Introduction

Two dimensional arrays (2D arrays) represent one of the most fundamental data structures in C programming, extending the concept of linear arrays to incorporate tabular or matrix-like organization of data. While one dimensional arrays store elements in a single row, two dimensional arrays organize data in rows and columns, making them ideal for representing mathematical matrices, spreadsheets, grids, and various real-world tabular data structures. In the context of the University of Delhi Computer Science curriculum, mastery of two dimensional arrays is essential as they form the backbone for understanding more complex data structures and algorithms.

The importance of two dimensional arrays in problem solving cannot be overstated. When you need to process data that has natural row and column relationships—such as student marks across multiple subjects, pixel values in image processing, or game board states—two dimensional arrays provide an elegant and efficient solution. Unlike creating multiple one dimensional arrays for each row, a single two dimensional array consolidates all related data into a cohesive unit, enabling systematic access and manipulation through row and column indices. This chapter will establish a thorough understanding of declaration, initialization, memory representation, and practical applications of two dimensional arrays in C programming.

## Key Concepts

### Declaration of Two Dimensional Arrays

A two dimensional array in C is declared by specifying two dimensions: the number of rows and the number of columns. The general syntax for declaration is:

```
data_type array_name[number_of_rows][number_of_columns];
```

For example, to declare a matrix to store marks of 30 students across 5 subjects, you would write:

```c
int marks[30][5];
```

This allocates space for 150 integer values (30 rows × 5 columns) in contiguous memory locations. The first dimension (rows) is often referred to as the major dimension, while the second dimension (columns) is the minor dimension. It is crucial to note that both dimensions must be constant expressions or enum constants in standard C—variable length arrays (VLAs) were introduced in C99 but may not be supported in all compiler environments.

### Memory Representation

Understanding how two dimensional arrays are stored in memory is fundamental to becoming an efficient C programmer. C uses ROW-MAJOR ORDER for storing two dimensional arrays, meaning all elements of the first row are stored contiguously in memory, followed by all elements of the second row, and so on. This sequential storage has significant implications for cache performance and memory access patterns.

For instance, if you declare `int matrix[3][4]`, the memory layout would arrange the 12 elements as: matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3], matrix[1][0], matrix[1][1], and so forth. This linear arrangement explains why accessing elements row-by-row (iterating through columns within each row) is more memory-efficient than accessing them column-by-column, as the former maximizes spatial locality and minimizes cache misses.

### Initialization

Two dimensional arrays can be initialized at the time of declaration using nested braces. There are multiple approaches to initialization:

**1. Complete Initialization with All Elements:**
```c
int matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};
```

**2. Partial Initialization:**
```c
int matrix[2][3] = {{1, 2}, {4}};  // Remaining elements default to 0
```

**3. Flattened Initialization:**
```c
int matrix[2][3] = {1, 2, 3, 4, 5, 6};  // Row-major order
```

**4. Omitting First Dimension:**
```c
int matrix[][3] = {{1, 2, 3}, {4, 5, 6}};  // Compiler infers rows
```

When only the second dimension is specified, the compiler can automatically calculate the number of rows based on the initializer list. However, omitting both dimensions is not allowed in standard C.

### Accessing Elements

Individual elements in a two dimensional array are accessed using two indices: the row index and the column index, both of which are ZERO-BASED in C. The syntax is `array_name[row_index][column_index]`. For example, `marks[2][4]` refers to the element in the third row and fifth column. Attempting to access elements outside the valid index range (0 to rows-1 for rows, 0 to columns-1 for columns) results in undefined behavior, often leading to memory corruption or program crashes.

### Passing Two Dimensional Arrays to Functions

When passing a two dimensional array to a function, the column dimension must be explicitly specified. This requirement stems from C's memory model: the compiler needs to know the column width to calculate memory addresses correctly using pointer arithmetic. The function prototype can be written as:

```c
void printMatrix(int matrix[][3], int rows, int cols);
// or
void processMatrix(int (*matrix)[3], int rows, int cols);
```

The row dimension can be omitted in the parameter declaration because the compiler only needs the column width to compute offsets. However, you must pass the number of rows and columns as separate parameters since these values are not stored within the array itself.

## Examples

### Example 1: Matrix Addition

Write a C program to add two 3×3 matrices and display the result.

**Solution:**

```c
#include <stdio.h>

int main() {
    int A[3][3], B[3][3], C[3][3];
    int i, j;
    
    // Input for first matrix
    printf("Enter elements of first 3x3 matrix:\n");
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            scanf("%d", &A[i][j]);
        }
    }
    
    // Input for second matrix
    printf("Enter elements of second 3x3 matrix:\n");
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            scanf("%d", &B[i][j]);
        }
    }
    
    // Matrix addition
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            C[i][j] = A[i][j] + B[i][j];
        }
    }
    
    // Display result
    printf("Resultant matrix after addition:\n");
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            printf("%d\t", C[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}
```

**Step-by-step explanation:** The program uses three nested loops to handle input, computation, and output. The outer loop iterates through rows (i from 0 to 2), while the inner loop iterates through columns (j from 0 to 2). Each element of matrix C is computed as the sum of corresponding elements from matrices A and B.

### Example 2: Transpose of a Matrix

Write a program to find the transpose of a matrix. The transpose is obtained by interchanging rows and columns.

**Solution:**

```c
#include <stdio.h>

void transpose(int matrix[10][10], int trans[10][10], int n) {
    int i, j;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            trans[j][i] = matrix[i][j];
        }
    }
}

int main() {
    int matrix[10][10], trans[10][10], n;
    int i, j;
    
    printf("Enter size of square matrix (n x n): ");
    scanf("%d", &n);
    
    printf("Enter %d x %d matrix elements:\n", n, n);
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }
    
    // Find transpose
    transpose(matrix, trans, n);
    
    // Display transpose
    printf("\nTranspose of the matrix:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            printf("%d\t", trans[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}
```

**Key insight:** Notice that in the transpose function, we swap the indices: `trans[j][i] = matrix[i][j]`. This effectively exchanges the row and column positions, creating the transposed matrix.

### Example 3: Row-wise Sum and Maximum Element

Write a program to calculate the sum of each row and find the maximum element in each row of a matrix.

**Solution:**

```c
#include <stdio.h>
#include <limits.h>

int main() {
    int matrix[10][10], rows, cols;
    int i, j, row_sum, max_element;
    
    printf("Enter number of rows and columns: ");
    scanf("%d %d", &rows, &cols);
    
    printf("Enter matrix elements:\n");
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }
    
    // Calculate row-wise sum and maximum
    for (i = 0; i < rows; i++) {
        row_sum = 0;
        max_element = INT_MIN;  // Initialize to minimum possible value
        
        for (j = 0; j < cols; j++) {
            row_sum += matrix[i][j];
            if (matrix[i][j] > max_element) {
                max_element = matrix[i][j];
            }
        }
        
        printf("Row %d: Sum = %d, Maximum = %d\n", i + 1, row_sum, max_element);
    }
    
    return 0;
}
```

**Important note:** The initialization of `max_element` to `INT_MIN` (from limits.h) is crucial. This ensures that the first element encountered will always be greater than the initial value, making the comparison work correctly regardless of whether the matrix contains negative numbers.

## Exam Tips

1. **Index Boundaries Matter:** Remember that array indices in C start from 0, not 1. A matrix declared as `int arr[3][4]` has valid indices rows 0-2 and columns 0-3. Accessing arr[3][0] or arr[0][4] causes buffer overflow.

2. **Memory Layout is Row-Major:** When answering conceptual questions about memory representation, remember C stores 2D arrays in row-major order. The address of element `a[i][j]` can be calculated as: `base_address + (i * columns + j) * sizeof(element)`.

3. **Column Dimension is Mandatory in Function Parameters:** In exams, if asked about passing 2D arrays to functions, always remember that the second dimension must be specified while the first can be omitted.

4. **Initialize Before Use:** Uninitialized two dimensional arrays contain garbage values. Always initialize arrays either during declaration or using loops before using them in calculations.

5. **Time Complexity Awareness:** Common matrix operations like addition, subtraction, and element-wise operations take O(m×n) time. When analyzing algorithms involving 2D arrays, count the number of nested loops.

6. **Diagonal Elements Pattern:** For accessing main diagonal elements, use indices where row equals column (i.e., arr[i][i]). For the anti-diagonal, use arr[i][n-1-i] where n is the matrix size.

7. **Practice Matrix Multiplication:** This is a frequently asked exam problem. Remember it requires three nested loops and the result element C[i][j] is the dot product of the i-th row of A and j-th column of B.