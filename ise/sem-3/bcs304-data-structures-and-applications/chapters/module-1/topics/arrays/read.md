# ARRAYS

## Introduction

Arrays are one of the most fundamental and widely used non-primitive data structures in computer science. An array is a collection of elements of the same data type stored in contiguous memory locations, where each element can be accessed directly using its index. The concept of arrays forms the backbone of many advanced data structures and algorithms, making it essential for any computer science student to master this topic thoroughly.

In the context of data structures, arrays represent the simplest form of structured data storage. They provide constant-time access to any element through its index, which is their most significant advantage over other data structures like linked lists. Arrays are extensively used in mathematical computations, database operations, image processing, and countless other applications. For students at the University of Delhi, understanding arrays is crucial as they appear frequently in practical programming assignments and form the foundation for more complex topics like stacks, queues, and trees.

This chapter explores single-dimensional arrays, multi-dimensional arrays, sparse matrices, and dynamic memory allocation for arrays. We will examine how arrays are represented in memory, the operations that can be performed on them, and their practical applications in representing polynomials and sparse matrices.

## Key Concepts

### Definition and Characteristics of Arrays

An array is a homogeneous collection of elements, meaning all elements must be of the same data type. The key characteristics of arrays include:

1. **Fixed Size**: Once declared, the size of an array typically remains constant (in static arrays)
2. **Contiguous Memory**: All elements are stored in consecutive memory locations
3. **Direct Access**: Any element can be accessed in O(1) time using its index
4. **Zero-based Indexing**: In most programming languages including C and C++, array indices start from 0

### One-Dimensional Arrays

A one-dimensional array (1D array) is a linear collection of elements accessible through a single index. The syntax for declaring a one-dimensional array in C is:

```c
data_type array_name[size];
```

For example, to store 10 integer values:
```c
int marks[10];
```

The memory representation shows that `marks[0]` is stored at the base address, and each subsequent element is stored at consecutive addresses. If the base address is `B` and each integer occupies `w` bytes, then the address of `marks[i]` is calculated as:

```
Address(marks[i]) = B + i × w
```

### Two-Dimensional Arrays

A two-dimensional array can be visualized as a table with rows and columns. It is essentially an array of arrays. In C, declaration takes the form:

```c
data_type array_name[rows][cols];
```

For example:
```c
int matrix[3][4];  // A 3×4 matrix with 3 rows and 4 columns
```

### Memory Representation of 2D Arrays

Two-dimensional arrays can be stored in memory using two methods:

**Row-Major Order**: Elements are stored row by row. This is the default in C and C++.

For a 3×4 matrix:
```
Row 0: a[0][0], a[0][1], a[0][2], a[0][3]
Row 1: a[1][0], a[1][1], a[1][2], a[1][3]
Row 2: a[2][0], a[2][1], a[2][2], a[2][3]
```

**Column-Major Order**: Elements are stored column by column. This is used in Fortran and MATLAB.

Address calculation in row-major order:
```
Address(a[i][j]) = B + (i × n + j) × w
```
where B is base address, n is number of columns, and w is word size.

### Multidimensional Arrays

Arrays can have more than two dimensions. A three-dimensional array can be visualized as a cube of data. Declaration:

```c
int cube[2][3][4];  // 2 planes, 3 rows, 4 columns
```

The address formula for a 3D array in row-major order:
```
Address(a[i][j][k]) = B + ((i × m + j) × n + k) × w
```

### Dynamic Memory Allocation for Arrays

Static arrays have fixed sizes determined at compile time. Dynamic arrays allow memory allocation at runtime using pointers. In C, dynamic allocation is done using `malloc()`, `calloc()`, and memory is freed using `free()`.

```c
// Dynamic 1D array
int *arr = (int*)malloc(n * sizeof(int));

// Dynamic 2D array
int **matrix = (int**)malloc(rows * sizeof(int*));
for(int i = 0; i < rows; i++)
    matrix[i] = (int*)malloc(cols * sizeof(int));
```

### Sparse Matrices

A sparse matrix is a matrix in which most elements are zero. Instead of storing all elements, we store only non-zero elements to save memory. Common representations include:

1. **Coordinate List (COO)**: Stores row, column, and value triplets
2. **Compressed Sparse Row (CSR)**: Uses three arrays - values, column indices, and row pointers

### Polynomials Using Arrays

Polynomials can be efficiently represented using arrays where the index represents the power and the value represents the coefficient. For a polynomial of degree n:

```
P(x) = a₀ + a₁x + a₂x² + ... + aₙxⁿ
```

Representation:
```c
float coefficients[n+1];  // coefficients[0] = a₀, coefficients[1] = a₁, etc.
```

## Examples

### Example 1: Finding the Sum of Elements in a 1D Array

**Problem**: Write a C program to calculate the sum of all elements in an integer array.

**Solution**:
```c
#include <stdio.h>

int main() {
    int n, sum = 0;
    printf("Enter number of elements: ");
    scanf("%d", &n);
    
    int arr[n];
    printf("Enter %d elements: ", n);
    for(int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }
    
    printf("Sum = %d\n", sum);
    return 0;
}
```

**Step-by-step explanation**:
1. Accept the number of elements from user
2. Create an array of that size
3. Iterate through each element and add to sum variable
4. Display the final sum

Time Complexity: O(n), Space Complexity: O(n)

### Example 2: Matrix Addition using 2D Arrays

**Problem**: Add two 3×3 matrices and store the result in a third matrix.

**Solution**:
```c
#include <stdio.h>

#define ROWS 3
#define COLS 3

int main() {
    int A[ROWS][COLS], B[ROWS][COLS], C[ROWS][COLS];
    
    // Input for matrix A
    printf("Enter elements of matrix A (3×3):\n");
    for(int i = 0; i < ROWS; i++)
        for(int j = 0; j < COLS; j++)
            scanf("%d", &A[i][j]);
    
    // Input for matrix B
    printf("Enter elements of matrix B (3×3):\n");
    for(int i = 0; i < ROWS; i++)
        for(int j = 0; j < COLS; j++)
            scanf("%d", &B[i][j]);
    
    // Addition
    for(int i = 0; i < ROWS; i++)
        for(int j = 0; j < COLS; j++)
            C[i][j] = A[i][j] + B[i][j];
    
    // Output
    printf("Resultant matrix C:\n");
    for(int i = 0; i < ROWS; i++) {
        for(int j = 0; j < COLS; j++)
            printf("%d ", C[i][j]);
        printf("\n");
    }
    return 0;
}
```

### Example 3: Sparse Matrix Representation

**Problem**: Represent a sparse matrix using arrays and display the compressed form.

**Solution**:
```c
#include <stdio.h>

int main() {
    // Example sparse matrix (4×4)
    // 0  0  3  0
    // 0  0  0  0
    // 0  5  0  0
    // 0  0  0  7
    
    int sparse[4][4] = {
        {0, 0, 3, 0},
        {0, 0, 0, 0},
        {0, 5, 0, 0},
        {0, 0, 0, 7}
    };
    
    int nonZero = 0;
    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            if(sparse[i][j] != 0)
                nonZero++;
    
    // COO format: row, col, value
    printf("Sparse Matrix in COO format:\n");
    printf("Row\tCol\tValue\n");
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            if(sparse[i][j] != 0)
                printf("%d\t%d\t%d\n", i, j, sparse[i][j]);
        }
    }
    printf("\nTotal non-zero elements: %d\n", nonZero);
    printf("Space saved: %d elements\n", 16 - nonZero);
    
    return 0;
}
```

## Exam Tips

1. **Index Formula Mastery**: Remember the address calculation formulas for 1D and 2D arrays. In row-major: Address(A[i][j]) = B + (i×n + j)×w. This is frequently asked in exams.

2. **Time Complexities**: Know that array access is O(1), searching is O(n), and sorting algorithms applied to arrays have their standard complexities.

3. **Sparse Matrix Benefits**: Understand why sparse matrices use less memory and be able to explain the COO and CSR representations with examples.

4. **Dynamic vs Static Arrays**: Know the differences - static arrays have fixed size at compile time, dynamic arrays allocate memory at runtime using malloc/calloc.

5. **Row-Major vs Column-Major**: Be able to identify which language uses which order (C uses row-major, Fortran uses column-major) and calculate addresses accordingly.

6. **Polynomial Representation**: Remember that in array representation of polynomials, index represents the exponent and value represents the coefficient.

7. **Pointer Relationship**: Understand how array names act as pointers to the first element (base address) in C.

8. **Memory Layout**: Be able to draw or explain how elements are arranged in memory for 1D, 2D, and 3D arrays.