# Pointer Arithmetic


## Table of Contents

- [Pointer Arithmetic](#pointer-arithmetic)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Fundamental Principle of Pointer Arithmetic](#fundamental-principle-of-pointer-arithmetic)
  - [Arithmetic Operations Supported](#arithmetic-operations-supported)
  - [Pointer Arithmetic and Data Types](#pointer-arithmetic-and-data-types)
  - [Relationship Between Pointers and Arrays](#relationship-between-pointers-and-arrays)
  - [Pointer Arithmetic with Structures](#pointer-arithmetic-with-structures)
  - [Void Pointers and Pointer Arithmetic](#void-pointers-and-pointer-arithmetic)
  - [Null Pointer Arithmetic](#null-pointer-arithmetic)
- [Examples](#examples)
  - [Example 1: Array Traversal Using Pointer Arithmetic](#example-1-array-traversal-using-pointer-arithmetic)
  - [Example 2: Reverse Array Traversal](#example-2-reverse-array-traversal)
  - [Example 3: Pointer Subtraction for Distance Calculation](#example-3-pointer-subtraction-for-distance-calculation)
  - [Example 4: Character Array Traversal](#example-4-character-array-traversal)
- [Exam Tips](#exam-tips)

## Introduction

Pointer arithmetic is one of the most powerful and distinctive features of the C programming language. It allows programmers to manipulate memory addresses directly, enabling efficient array traversal, dynamic memory management, and implementation of complex data structures like linked lists and trees. In the context of Problem Solving Using C Programming, understanding pointer arithmetic is essential for writing efficient, memory-conscious code that is a hallmark of professional C programming.

The concept stems from the fact that pointers store memory addresses, and these addresses can be manipulated arithmetically just like regular numbers. However, pointer arithmetic is not like ordinary integer arithmetic—when you add 1 to a pointer, it does not simply increment the address by 1 byte. Instead, it advances by the size of the data type it points to. This behavior is what makes pointers and arrays in C so intimately connected, and it is the foundation for many advanced programming techniques.

For students preparing for DU semester examinations, pointer arithmetic frequently appears in both theoretical questions and practical programming problems. A solid grasp of this topic enables you to write more efficient code and debug pointer-related issues that are common in C programs.

## Key Concepts

### Fundamental Principle of Pointer Arithmetic

When you perform arithmetic operations on pointers, the operations are scaled by the size of the data type being pointed to. If you have an integer pointer `ptr` pointing to address 1000 (assuming integers are 4 bytes), then `ptr + 1` will point to address 1004, not 1001. This scaling behavior is automatic and handled by the C compiler.

The reason for this scaling is intuitive: if you have an array of integers and you want to access the next element, you need to skip over the entire integer (4 bytes on most systems), not just one byte. Pointer arithmetic abstracts away this calculation, allowing you to treat arrays as contiguous memory blocks that can be traversed with simple addition and subtraction operations.

### Arithmetic Operations Supported

C supports five specific arithmetic operations on pointers:

**1. Addition of Integer to Pointer**
You can add an integer value to a pointer using the `+` operator. The operation `ptr + n` moves the pointer forward by n elements of the type pointed to. For example, if `ptr` points to the first element of an integer array, `ptr + 3` points to the fourth element.

**2. Subtraction of Integer from Pointer**
Similar to addition, subtracting an integer from a pointer moves it backward. The operation `ptr - n` moves the pointer backward by n elements. This is useful for traversing arrays in reverse order.

**3. Subtraction of Two Pointers**
When you subtract one pointer from another of the same type, the result is an integer representing the number of elements between them. If `ptr1` points to element 5 and `ptr2` points to element 2 of the same array, then `ptr1 - ptr2` equals 3. This operation is particularly useful for calculating array indices and buffer sizes.

**4. Increment Operator (++)**
The increment operator moves the pointer to the next element of the type it points to. `ptr++` is equivalent to `ptr + 1`. This is frequently used in loops to traverse arrays.

**5. Decrement Operator (--)**
The decrement operator moves the pointer to the previous element. `ptr--` is equivalent to `ptr - 1`. This is useful for reverse traversal.

### Pointer Arithmetic and Data Types

The behavior of pointer arithmetic depends critically on the data type being pointed to. Consider the following code:

```c
char *cptr;
int *iptr;
double *dptr;
```

Assuming a system where char is 1 byte, int is 4 bytes, and double is 8 bytes:
- `cptr + 1` advances by 1 byte
- `iptr + 1` advances by 4 bytes
- `dptr + 1` advances by 8 bytes

This behavior is automatic and one of the most powerful features of pointers in C. It allows you to write generic traversal code that works correctly regardless of the data type.

### Relationship Between Pointers and Arrays

In C, arrays and pointers have a very close relationship. The name of an array (without brackets) decays to a pointer to the first element of the array. This means you can use pointer arithmetic to access array elements, and conversely, you can use array subscript notation with pointers.

For an array `int arr[10]`, the expression `arr` is equivalent to `&arr[0]`, and `arr + i` is equivalent to `&arr[i]`. Furthermore, `*(arr + i)` is equivalent to `arr[i]`. This equivalence is fundamental to understanding how C handles arrays and is a frequent source of examination questions.

### Pointer Arithmetic with Structures

When performing pointer arithmetic with pointers to structures, the same scaling principle applies. If you have a pointer to a structure and you increment it, it moves to the next structure in memory, skipping over the entire structure. This is particularly important when working with arrays of structures or linked data structures.

### Void Pointers and Pointer Arithmetic

Void pointers (`void *`) are generic pointers that can point to any data type. However, you cannot perform pointer arithmetic directly on void pointers in standard C because the compiler does not know the size of the data type. To perform arithmetic on void pointers, you must first cast them to a specific pointer type.

### Null Pointer Arithmetic

It is crucial to understand that performing arithmetic on null pointers leads to undefined behavior. A null pointer does not point to any valid memory location, and attempting to manipulate it is a serious error that can cause program crashes. Always ensure pointers are valid before performing arithmetic operations.

## Examples

### Example 1: Array Traversal Using Pointer Arithmetic

Consider an integer array and the task of finding the sum of all elements using pointer arithmetic:

```c
#include <stdio.h>

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int *ptr = arr;  // Points to first element (equivalent to &arr[0])
    int sum = 0;
    int n = sizeof(arr) / sizeof(arr[0]);
    
    for (int i = 0; i < n; i++) {
        sum += *(ptr + i);  // Equivalent to arr[i]
    }
    
    printf("Sum = %d\n", sum);
    return 0;
}
```

Output: Sum = 150

In this example, `ptr + i` computes the address of the i-th element, and `*(ptr + i)` dereferences that address to obtain the value. The pointer `ptr` itself remains unchanged throughout the loop.

### Example 2: Reverse Array Traversal

This example demonstrates using pointer arithmetic to traverse an array in reverse:

```c
#include <stdio.h>

int main() {
    int arr[] = {5, 10, 15, 20, 25};
    int n = sizeof(arr) / sizeof(arr[0]);
    int *ptr = arr + n - 1;  // Points to last element
    
    printf("Array in reverse: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", *ptr);
        ptr--;  // Move to previous element
    }
    printf("\n");
    
    return 0;
}
```

Output: Array in reverse: 25 20 15 10 5

Here, we initialize the pointer to point past the last element, then use the decrement operator to move backward through the array. Each iteration prints the current value and moves the pointer one element back.

### Example 3: Pointer Subtraction for Distance Calculation

This example shows how to calculate the distance between two pointers:

```c
#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int *ptr1 = &arr[2];  // Points to element with value 3
    int *ptr2 = &arr[7];  // Points to element with value 8
    
    // Calculate the number of elements between ptr2 and ptr1
    int distance = ptr2 - ptr1;
    
    printf("ptr1 points to: %d\n", *ptr1);
    printf("ptr2 points to: %d\n", *ptr2);
    printf("Distance (ptr2 - ptr1): %d elements\n", distance);
    
    return 0;
}
```

Output:
ptr1 points to: 3
ptr2 points to: 8
Distance (ptr2 - ptr1): 5 elements

The subtraction `ptr2 - ptr1` yields 5 because there are 5 elements between positions 2 and 7 in the array. This is a practical way to calculate indices and buffer distances.

### Example 4: Character Array Traversal

Pointer arithmetic works identically with character arrays:

```c
#include <stdio.h>

int main() {
    char str[] = "DELHI UNIVERSITY";
    char *ptr = str;
    
    // Print string character by character
    while (*ptr != '\0') {
        printf("%c", *ptr);
        ptr++;
    }
    printf("\n");
    
    // Calculate string length using pointer arithmetic
    char *start = str;
    while (*ptr != '\0') {
        ptr++;
    }
    int length = ptr - start;
    printf("Length: %d\n", length);
    
    return 0;
}
```

Output:
DELHI UNIVERSITY
Length: 16

This example demonstrates that pointer arithmetic works the same way regardless of the data type, whether integers, doubles, or characters.

## Exam Tips

1. **Remember the Scaling Rule**: When you add 1 to a pointer, it advances by sizeof(data_type) bytes, not 1 byte. This is the most fundamental concept in pointer arithmetic and frequently tested in examinations.

2. **Array-Pointer Equivalence**: The expressions `arr[i]`, `*(arr + i)`, `*(i + arr)`, and `i[arr]` are all equivalent in C. Understanding this helps in debugging and writing compact code.

3. **Pointer Subtraction is Valid**: Only pointer subtraction (not addition) of two pointers to the same array yields meaningful results. Adding two pointers is not allowed in C.

4. **Initialize Pointers**: Always initialize pointers before use. Uninitialized pointers contain garbage addresses and can cause undefined behavior.

5. **NULL Pointer Check**: Before performing any pointer arithmetic, check if the pointer is not NULL. Dereferencing a NULL pointer causes program crashes.

6. **Type Matters**: The result of pointer arithmetic depends on the type of pointer. An `int *` and a `char *` will advance by different amounts when incremented.

7. **Void Pointer Arithmetic**: You cannot perform arithmetic directly on void pointers. Cast them to a specific type first: `((int *)void_ptr) + 1`.

8. **Boundary Conditions**: When using pointer arithmetic to traverse arrays, be careful not to go beyond array bounds. Accessing `arr[n]` where n is the array size leads to buffer overflow.

9. **Const Correctness**: Remember that pointer arithmetic on pointers to const data is allowed, but you cannot modify the data through such pointers.

10. **Practice Pointer Arithmetic in Loops**: Many exam questions involve predicting the output of code snippets containing pointer arithmetic in loops. Practice writing and tracing such code carefully.