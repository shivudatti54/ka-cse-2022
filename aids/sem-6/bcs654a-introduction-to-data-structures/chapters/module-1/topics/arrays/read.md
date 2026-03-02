# ARRAYS

## Introduction

Arrays are one of the most fundamental and widely used data structures in programming. In the C programming language, an array is a collection of elements of the same data type stored in contiguous memory locations. The concept of arrays allows programmers to store multiple values under a single variable name, making it possible to efficiently manage and process large amounts of related data.

The importance of arrays in computer science cannot be overstated. When a program needs to process hundreds or thousands of related values—such as test scores, temperature readings, or inventory items—declaring individual variables for each would be impractical and inefficient. Arrays solve this problem by providing a systematic way to organize and access related data using indices. This topic forms the foundation for understanding more complex data structures like matrices, linked lists, and stacks. In the context of the University of Delhi Computer Science curriculum, arrays are essential for problem-solving in competitive examinations and practical programming assignments.

## Key Concepts

### One-Dimensional Arrays

A one-dimensional array is a linear collection of elements of the same data type. It can be visualized as a single row of elements, where each element can be accessed by its position or index.

**Declaration Syntax:**
```c
data_type array_name[array_size];
```

For example:
```c
int marks[10];      // Array of 10 integers
float prices[5];   // Array of 5 floating-point numbers
char name[20];     // Array of 20 characters (string)
```

The array index in C always starts from 0. Therefore, for an array of size n, valid indices range from 0 to n-1. Accessing an element at index i is done using the syntax `array_name[i]`.

**Initialization:**
Arrays can be initialized at the time of declaration in several ways:

```c
// Method 1: Initialize all elements
int numbers[5] = {10, 20, 30, 40, 50};

// Method 2: Partial initialization (remaining elements set to 0)
int partial[5] = {1, 2};

// Method 3: Size deduction from initializer
int auto_size[] = {1, 2, 3, 4, 5};  // Creates array of size 5

// Method 4: Static initialization
int static_arr[3] = {0};  // All elements initialized to 0
```

### Two-Dimensional Arrays

A two-dimensional array represents a table or matrix with rows and columns. It is essentially an array of arrays.

**Declaration Syntax:**
```c
data_type array_name[rows][columns];
```

For example:
```c
int matrix[3][4];    // 3 rows, 4 columns
float table[2][3];   // 2 rows, 3 columns
```

**Initialization:**
```c
// Method 1: Row-wise initialization
int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};

// Method 2: Flat initialization (C fills row by row)
int arr2[2][3] = {1, 2, 3, 4, 5, 6};

// Method 3: Partial initialization
int arr3[3][3] = {{1}, {2, 3}, {4, 5, 6}};
```

Accessing elements is done using `array_name[row_index][col_index]`. The memory representation of a 2D array is still contiguous, with elements stored row by row (row-major order).

### Multidimensional Arrays

C supports arrays of three or more dimensions. While theoretically unlimited, practical use rarely exceeds three dimensions due to memory constraints.

**Three-Dimensional Array:**
```c
int cube[2][3][4];  // 2 layers, 3 rows, 4 columns
```

This represents 2×3×4 = 24 integers. Initialization follows the same pattern:
```c
int cube[2][2][2] = {
    {{1, 2}, {3, 4}},
    {{5, 6}, {7, 8}}
};
```

### Arrays and Pointers

An important relationship exists between arrays and pointers in C. The array name itself acts as a constant pointer to the first element of the array. This is fundamental to understanding how arrays are passed to functions and how pointer arithmetic works with arrays.

```c
int arr[5] = {10, 20, 30, 40, 50};
int *ptr = arr;  // Same as: int *ptr = &arr[0];

// Both expressions refer to the same element
printf("%d %d", arr[0], *ptr);   // Outputs: 10 10
printf("%d %d", *(arr+1), *(ptr+1));  // Outputs: 20 20
```

When an array is passed to a function, it decays to a pointer, meaning the function receives only the base address, not a copy of the entire array.

## Examples

### Example 1: Finding the Maximum Element in a One-Dimensional Array

**Problem:** Write a C program to find the maximum element in an array of 10 integers.

**Solution:**
```c
#include <stdio.h>

int main() {
    int arr[10] = {23, 45, 12, 67, 89, 34, 56, 78, 90, 11};
    int max = arr[0];  // Assume first element as maximum
    
    for (int i = 1; i < 10; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    
    printf("Maximum element: %d\n", max);
    return 0;
}
```

**Output:**
```
Maximum element: 90
```

**Step-by-step explanation:**
- Initialize `max` with the first element (arr[0] = 23)
- Iterate from index 1 to 9
- Compare each element with current max; update if greater
- After loop, max contains the largest value (90)

### Example 2: Matrix Addition using Two-Dimensional Arrays

**Problem:** Write a C program to add two 3×3 matrices.

**Solution:**
```c
#include <stdio.h>

int main() {
    int A[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int B[3][3] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
    int C[3][3];
    
    // Adding corresponding elements
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            C[i][j] = A[i][j] + B[i][j];
        }
    }
    
    // Printing result
    printf("Result Matrix:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}
```

**Output:**
```
Result Matrix:
10 10 10 
10 10 10 
10 10 10
```

### Example 3: Passing Array to Function

**Problem:** Write a function to calculate the average of n elements in an array.

**Solution:**
```c
#include <stdio.h>

float calculateAverage(int arr[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return (float)sum / n;
}

int main() {
    int numbers[] = {10, 20, 30, 40, 50};
    int size = sizeof(numbers) / sizeof(numbers[0]);
    
    float avg = calculateAverage(numbers, size);
    printf("Average: %.2f\n", avg);
    
    return 0;
}
```

**Output:**
```
Average: 30.00
```

## Exam Tips

1. **Array Indexing:** Remember that C arrays are zero-indexed. For an array of size n, valid indices are 0 to n-1. Accessing arr[n] causes buffer overflow.

2. **Array Size Calculation:** The number of elements in an array can be calculated as: `sizeof(array) / sizeof(array[0])`

3. **Memory Layout:** In C, 2D arrays are stored in row-major order. The inner dimension must always be specified in function parameters.

4. **Pointer-Arithmetic with Arrays:** When you add 1 to a pointer pointing to an array element, it moves to the next element, not the next byte. The increment is proportional to the data type size.

5. **Array vs Pointer Distinction:** While array name acts like a pointer, it is not a variable. You cannot assign to it (e.g., arr++ is invalid), but you can create a pointer and perform arithmetic.

6. **Bounds Checking:** C does not perform automatic bounds checking. Always ensure loop conditions stay within array bounds to avoid undefined behavior.

7. **Initialization Differences:** Uninitialized global arrays are zero-initialized, but local (automatic) arrays contain garbage values unless explicitly initialized.

8. **Multidimensional Array Parameters:** When passing 2D arrays to functions, you must specify the column size: `void func(int arr[][10])` but not `void func(int arr[][])`.