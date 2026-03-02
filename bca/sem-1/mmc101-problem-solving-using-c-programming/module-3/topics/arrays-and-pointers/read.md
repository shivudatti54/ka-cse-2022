# Arrays and Pointers in C


## Table of Contents

- [Arrays and Pointers in C](#arrays-and-pointers-in-c)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [One-Dimensional Arrays](#one-dimensional-arrays)
  - [Two-Dimensional Arrays](#two-dimensional-arrays)
  - [Pointers and Pointer Operators](#pointers-and-pointer-operators)
  - [Pointer Arithmetic](#pointer-arithmetic)
  - [Relationship Between Arrays and Pointers](#relationship-between-arrays-and-pointers)
  - [Array of Pointers](#array-of-pointers)
  - [Pointers and Strings](#pointers-and-strings)
- [Examples](#examples)
  - [Example 1: Finding Maximum Element in an Array](#example-1-finding-maximum-element-in-an-array)
  - [Example 2: Pointer Arithmetic with Arrays](#example-2-pointer-arithmetic-with-arrays)
  - [Example 3: Sum of Two Matrices Using 2D Arrays](#example-3-sum-of-two-matrices-using-2d-arrays)
- [Exam Tips](#exam-tips)

## Introduction

Arrays and pointers are fundamental concepts in C programming that form the backbone of memory management and data structure implementation. In the context of Problem Solving Using C, mastering these concepts is essential as they enable efficient handling of collections of data and direct memory manipulation. Arrays provide a way to store multiple elements of the same type in contiguous memory locations, while pointers give programmers the power to access and manipulate memory addresses directly.

The relationship between arrays and pointers in C is particularly significant because array names themselves act as pointers to the first element of the array. This deep connection allows for efficient array traversal, dynamic memory allocation, and the implementation of complex data structures like linked lists, stacks, and queues. For students preparing for DU semester examinations, understanding this relationship is crucial as questions on arrays and pointers consistently appear in both theoretical and practical components of the exam.

In this topic, we will explore the declaration, initialization, and manipulation of arrays, the declaration and usage of pointers, and most importantly, how arrays and pointers interact with each other. We will also examine pointer arithmetic, which is a unique feature of C that distinguishes it from higher-level languages.

## Key Concepts

### One-Dimensional Arrays

A one-dimensional array is a collection of elements of the same data type stored in contiguous memory locations. The general syntax for declaring a one-dimensional array is:

```
data_type array_name[array_size];
```

For example, to declare an array of 10 integers, we write:
```c
int numbers[10];
```

Array indices in C start from 0, meaning the first element is accessed using index 0, the second with index 1, and so on. The last valid index is array_size minus 1. Accessing an element is done using the subscript operator:

```c
numbers[0] = 25;    // Assigning value to first element
int x = numbers[5]; // Accessing sixth element
```

Initialization of arrays can be done at the time of declaration:
```c
int marks[5] = {90, 85, 78, 92, 88};
```

If the number of initializers is less than the array size, the remaining elements are automatically initialized to zero. Also, when initializing an array at declaration, the size can be omitted:
```c
int digits[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
```

### Two-Dimensional Arrays

Two-dimensional arrays represent matrices or tables and are declared as:
```c
data_type array_name[rows][columns];
```

For instance, a 3x4 matrix can be declared as:
```c
int matrix[3][4];
```

Memory is stored in row-major order, meaning all elements of the first row are stored contiguously, followed by elements of the second row, and so on. Initialization can be done in multiple ways:
```c
int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};
int arr2[2][3] = {1, 2, 3, 4, 5, 6};
```

### Pointers and Pointer Operators

A pointer is a variable that stores the memory address of another variable. The asterisk (*) is used to declare a pointer variable:
```c
int *ptr;
char *cptr;
float *fptr;
```

The address-of operator (&) is used to obtain the address of a variable, while the dereference operator (*) is used to access the value at the address stored in the pointer:
```c
int num = 50;
int *ptr = &num;    // ptr now stores address of num
printf("%d", *ptr); // Prints 50 (value at address)
```

### Pointer Arithmetic

Pointer arithmetic allows pointers to be incremented and decremented. When a pointer is incremented, it points to the next memory location of its data type. For example, if an int occupies 4 bytes, incrementing an int pointer adds 4 to its address.

The following operations are valid on pointers:
- Addition of integer to pointer: ptr + n
- Subtraction of integer from pointer: ptr - n
- Subtraction of two pointers: ptr1 - ptr2 (gives number of elements between them)
- Comparison of pointers: ptr1 == ptr2, ptr1 < ptr2

Pointer addition and subtraction scale according to the size of the data type the pointer points to.

### Relationship Between Arrays and Pointers

In C, the name of an array (without brackets) acts as a pointer to the first element of the array. This is a fundamental concept:
```c
int arr[5] = {10, 20, 30, 40, 50};
int *ptr = arr;  // Equivalent to: int *ptr = &arr[0];
```

Both arr and ptr point to the same memory location (the first element). We can use pointer arithmetic to access array elements:
```c
printf("%d", *(ptr + 2));  // Prints 30, same as arr[2]
printf("%d", ptr[2]);      // Also prints 30
```

The relationship allows us to pass arrays to functions. When an array is passed to a function, it decays to a pointer, meaning the function receives a copy of the base address:
```c
void display(int *arr, int size) {
    for(int i = 0; i < size; i++) {
        printf("%d ", *(arr + i));
    }
}
```

This can also be written as:
```c
void display(int arr[], int size) { ... }
```

Both function signatures are equivalent in C.

### Array of Pointers

An array of pointers stores addresses as its elements, useful for handling strings or dynamic 2D arrays:
```c
char *names[] = {"Alice", "Bob", "Charlie"};
printf("%s", names[1]);  // Prints "Bob"
```

### Pointers and Strings

String literals in C are stored as arrays of characters with a null terminator '\0'. A character pointer can point to a string:
```c
char *str = "Hello";
printf("%c", str[0]);  // Prints 'H'
printf("%c", *(str+1)); // Prints 'e'
```

## Examples

### Example 1: Finding Maximum Element in an Array

Write a C program to find the maximum element and its position in an array of 10 integers.

```c
#include <stdio.h>

int main() {
    int arr[10] = {12, 45, 67, 89, 23, 56, 78, 34, 90, 11};
    int max = arr[0];
    int position = 0;
    
    for(int i = 1; i < 10; i++) {
        if(arr[i] > max) {
            max = arr[i];
            position = i;
        }
    }
    
    printf("Maximum element: %d\n", max);
    printf("Position: %d (index starting from 0)\n", position);
    
    return 0;
}
```

**Output:**
```
Maximum element: 90
Position: 8 (index starting from 0)
```

### Example 2: Pointer Arithmetic with Arrays

Write a program to demonstrate pointer arithmetic by printing array elements using pointer notation.

```c
#include <stdio.h>

int main() {
    int arr[] = {5, 10, 15, 20, 25};
    int *ptr = arr;
    int n = 5;
    
    printf("Array elements using pointer arithmetic:\n");
    for(int i = 0; i < n; i++) {
        printf("arr[%d] = %d, ", i, *(ptr + i));
        printf("Address: %p\n", (ptr + i));
    }
    
    printf("\nPointer subtraction: %ld\n", (ptr + 4) - ptr);
    
    return 0;
}
```

**Output:**
```
Array elements using pointer arithmetic:
arr[0] = 5, Address: 0x7ffd...
arr[1] = 10, Address: 0x7ffd...+4
arr[2] = 15, Address: 0x7ffd...+8
arr[3] = 20, Address: 0x7ffd...+12
arr[4] = 25, Address: 0x7ffd...+16

Pointer subtraction: 4
```

### Example 3: Sum of Two Matrices Using 2D Arrays

Write a program to add two 3x3 matrices and display the result.

```c
#include <stdio.h>

int main() {
    int A[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int B[3][3] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
    int C[3][3];
    
    // Matrix addition
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            C[i][j] = A[i][j] + B[i][j];
        }
    }
    
    // Display result
    printf("Resultant Matrix:\n");
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}
```

**Output:**
```
Resultant Matrix:
10 10 10 
10 10 10 
10 10 10 
```

## Exam Tips

1. REMEMBER THAT ARRAY INDICES START FROM 0, not 1. A common mistake is accessing arr[n] when the array size is n, which causes buffer overflow.

2. WHEN PASSING ARRAYS TO FUNCTIONS, always pass the size separately because sizeof operator on array parameter gives pointer size, not array size.

3. POINTER AND ARRAY NAMES ARE INTERCHANGEABLE in most contexts, but array names are not modifiable l-values while pointer variables can be reassigned.

4. POINTER ARITHMETIC AUTOMATICALLY SCALES by the size of the data type. Adding 1 to an int pointer actually adds sizeof(int) to the address.

5. ALWAYS INITIALIZE POINTERS before use. Uninitialized pointers contain garbage addresses and cause undefined behavior.

6. THE NULL POINTER is used to indicate that a pointer does not point to any valid memory location. Always check for NULL before dereferencing.

7. IN EXAM QUESTIONS, pay attention to the difference between sizeof(arr) and sizeof(ptr). In main, sizeof(arr) gives total bytes of array, but in a function, it gives pointer size.

8. FOR CHARACTER ARRAYS, remember to account for the null terminator '\0' when calculating the required size for string storage.