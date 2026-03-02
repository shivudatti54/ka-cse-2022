# Arrays

## Introduction

Arrays are the most fundamental and widely used data structure in computer programming. An array is a collection of elements of the same data type stored in contiguous memory locations, which can be accessed randomly using an index. The concept of arrays forms the backbone of many advanced data structures and algorithms, making it essential for any computer science student to master this topic thoroughly.

In the context of the University of Delhi's Computer Science curriculum, arrays represent the gateway to understanding how data is organized and manipulated in memory. Since arrays provide constant-time access to elements through their index, they offer significant advantages over linear data structures like linked lists when random access is required. The contiguous memory allocation of arrays also leads to better cache performance, which is crucial for writing efficient programs. This topic becomes particularly important when studying sorting algorithms, searching techniques, and matrix operations, all of which are core components of the DU semester examinations.

## Key Concepts

### Definition and Characteristics of Arrays

An array is a homogeneous collection of elements, meaning all elements must be of the same data type such as int, float, char, or user-defined structures. Each element in an array can be accessed directly using its index, which typically starts from 0 in most programming languages including C, C++, and Java. The size of an array must be declared at compile time in static arrays, though dynamic arrays allow memory allocation at runtime. The fundamental advantage of arrays lies in their O(1) access time, making them ideal for applications requiring frequent element retrieval.

### One-Dimensional Arrays

A one-dimensional array, also known as a linear array, is the simplest form of array that stores elements in a single row. In memory, a one-dimensional array is stored in consecutive memory locations. For example, an array named "marks" containing five integer elements would be stored as marks[0], marks[1], marks[2], marks[3], and marks[4]. The address of any element can be calculated using the formula: Address of marks[i] = Base Address + (i × size of each element). This formula is particularly important for understanding how arrays work at the memory level and is frequently tested in DU examinations.

### Two-Dimensional Arrays

A two-dimensional array represents data in a matrix or table format with rows and columns. It is essentially an array of arrays where each row is itself a one-dimensional array. Two-dimensional arrays are extensively used in mathematical matrix operations, image processing, and spreadsheet applications. In memory, two-dimensional arrays can be stored using either row-major order (where elements of each row are stored consecutively) or column-major order (where elements of each column are stored consecutively). C and C++ typically use row-major order, while Fortran uses column-major order.

For a two-dimensional array A[m][n] stored in row-major order, the address of element A[i][j] is calculated as: Address of A[i][j] = Base Address + ((i × n) + j) × size of element. Understanding this calculation is crucial for exam success, as it tests the student's understanding of memory organization.

### Multi-Dimensional Arrays

Multi-dimensional arrays extend the concept of two-dimensional arrays to three or more dimensions. A three-dimensional array can be visualized as a cube of data, while higher dimensions become difficult to visualize but are useful in specialized applications. For instance, a three-dimensional array temperature[10][20][30] could represent temperature readings at 10 different times, 20 different locations, and 30 different depths. The address calculation for multi-dimensional arrays follows the same principles as one and two-dimensional arrays, with the formula expanding to accommodate additional dimensions.

### Static vs Dynamic Arrays

Static arrays have a fixed size determined at compile time, meaning the exact number of elements must be known before the program runs. While this provides faster access and simpler syntax, it leads to inefficient memory utilization when the exact number of elements is unknown. Dynamic arrays, on the other hand, allow memory allocation at runtime using functions like malloc() and calloc() in C, or the new keyword in C++. Dynamic arrays can grow and shrink as needed, providing flexibility at the cost of additional overhead for memory management.

### Arrays and Pointers

In C and C++, arrays and pointers have a very close relationship. The name of an array acts as a pointer to its first element. When you declare an array int arr[10], the variable arr points to the first element arr[0]. This relationship is fundamental to understanding how arrays are passed to functions and how pointer arithmetic works. However, it is important to note that while arr and &arr[0] point to the same location, they have different types: arr has type int* while &arr has type int(*)[10].

### Structures and Arrays

Arrays can contain elements of user-defined data types, including structures. An array of structures is commonly used to store records such as student information, employee details, or inventory items. For example, an array struct Student students[100] can store information about 100 students, where each student record contains fields like name, roll number, and marks. This combination of arrays and structures is powerful for database-like applications.

## Examples

### Example 1: Address Calculation in One-Dimensional Array

Problem: An integer array arr[50] starts at memory address 1000. Each integer occupies 4 bytes. Find the address of arr[25].

Solution:
Using the formula: Address of arr[i] = Base Address + (i × size of element)

Given:
- Base Address = 1000
- Index i = 25
- Size of each element = 4 bytes

Address of arr[25] = 1000 + (25 × 4) = 1000 + 100 = 1100

Therefore, arr[25] is stored at memory location 1100.

### Example 2: Address Calculation in Two-Dimensional Array (Row-Major)

Problem: A 2D array int A[3][4] is stored in row-major order starting at memory address 2000. Each integer occupies 2 bytes. Find the address of A[2][3].

Solution:
For row-major storage: Address of A[i][j] = Base Address + ((i × n) + j) × size

Given:
- Base Address = 2000
- Number of columns (n) = 4
- Row index (i) = 2
- Column index (j) = 3
- Size of each element = 2 bytes

Address of A[2][3] = 2000 + ((2 × 4) + 3) × 2
= 2000 + (8 + 3) × 2
= 2000 + 11 × 2
= 2000 + 22
= 2022

Therefore, A[2][3] is stored at memory location 2022.

### Example 3: Dynamic Array Implementation in C

Problem: Write a C program to create a dynamic array of n integers and initialize all elements to zero.

Solution:
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i;
    int *arr;
    
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    
    // Dynamically allocate memory using calloc
    // calloc initializes all bytes to zero
    arr = (int*)calloc(n, sizeof(int));
    
    if (arr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }
    
    // Display the array elements
    printf("Array elements are: ");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    // Free the allocated memory
    free(arr);
    
    return 0;
}
```

The key points in this program are:
- Using calloc instead of malloc ensures automatic initialization to zero
- Always checking if malloc/calloc returns NULL prevents segmentation faults
- Calling free() after use prevents memory leaks

## Exam Tips

For success in DU semester examinations, keep the following points in mind:

1. MEMORY ADDRESS FORMULAS ARE FREQUENTLY TESTED. Practice both one-dimensional and two-dimensional address calculation problems thoroughly, as they appear in almost every examination paper.

2. UNDERSTAND THE DIFFERENCE BETWEEN MALLOC AND CALLOC. malloc allocates memory but does not initialize it, while calloc allocates and initializes to zero. This distinction is often tested in objective questions.

3. ARRAY INDEXING STARTS FROM 0, NOT 1. This fundamental concept is tested repeatedly, and mistakes in indexing lead to incorrect answers.

4. KNOW ROW-MAJOR VS COLUMN-MAJOR ORDER. When a question specifies the storage order, use the appropriate formula. The default assumption in C is usually row-major.

5. POINTER-ARRAY RELATIONSHIP IS IMPORTANT. Remember that array name is a constant pointer, and pointer arithmetic works differently than regular arithmetic.

6. TIME COMPLEXITY OF ARRAY OPERATIONS. Access is O(1), search is O(n), insertion and deletion at the beginning are O(n), and at the end can be O(1) for dynamic arrays.

7. ALWAYS CHECK FOR MEMORY ALLOCATION FAILURE. In practical programming questions, always verify that malloc/calloc returns a valid pointer before using it.

8. MULTI-DIMENSIONAL ARRAY PARAMETERS. When passing 2D arrays to functions, you must specify the number of columns, but rows can be left unspecified.