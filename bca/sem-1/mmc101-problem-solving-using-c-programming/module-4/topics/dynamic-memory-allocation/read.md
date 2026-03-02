# Dynamic Memory Allocation


## Table of Contents

- [Dynamic Memory Allocation](#dynamic-memory-allocation)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Memory Layout of a C Program](#memory-layout-of-a-c-program)
  - [Functions for Dynamic Memory Allocation](#functions-for-dynamic-memory-allocation)
  - [Memory Allocation with Structures](#memory-allocation-with-structures)
  - [Dynamic Arrays](#dynamic-arrays)
  - [Self-Referential Structures and Dynamic Memory](#self-referential-structures-and-dynamic-memory)
  - [Dangling Pointers and Memory Leaks](#dangling-pointers-and-memory-leaks)
- [Examples](#examples)
  - [Example 1: Dynamic Array Creation and Usage](#example-1-dynamic-array-creation-and-usage)
  - [Example 2: Dynamic Structure Array](#example-2-dynamic-structure-array)
  - [Example 3: Using calloc vs malloc](#example-3-using-calloc-vs-malloc)
- [Exam Tips](#exam-tips)

## Introduction

Dynamic Memory Allocation is a fundamental concept in C programming that allows programs to request and release memory at runtime, rather than having fixed memory sizes determined at compile time. Unlike static memory allocation where memory is allocated in the stack segment (fixed size), dynamic memory allocation utilizes the heap segment of the program's memory layout, providing flexibility to handle varying amounts of data.

In the context of Problem Solving Using C Programming, understanding dynamic memory allocation is essential for building flexible data structures like linked lists, trees, graphs, and for implementing various algorithms that require memory to be allocated based on user input or runtime conditions. This becomes particularly important when working with structures, arrays of structures, and self-referential structures - topics closely related to dynamic memory allocation in Module 4.

The ability to dynamically manage memory is a critical skill for any C programmer. It enables efficient use of available memory, allows programs to handle large datasets without wasting resources, and forms the foundation for advanced data structure implementations. In real-world applications, dynamic memory allocation is used in database systems, memory management subsystems, operating systems, and application software that need to handle unpredictable amounts of data.

## Key Concepts

### Memory Layout of a C Program

When a C program is executed, the memory is divided into several segments:

1. **Text Segment**: Contains the executable code
2. **Data Segment**: Stores global and static variables
3. **Stack Segment**: Used for function call management, local variables, and automatic memory
4. **Heap Segment**: Free memory pool available for dynamic allocation

Static variables and arrays with fixed sizes are allocated in the stack or data segment at compile time. However, when the size of data is not known beforehand or varies during program execution, we need dynamic memory allocation from the heap.

### Functions for Dynamic Memory Allocation

C provides four main library functions for dynamic memory management, all defined in the header file `<stdlib.h>`:

**malloc() - Memory Allocation**

The `malloc()` function allocates a specified number of bytes from the heap and returns a pointer to the beginning of the allocated block. The function signature is:

```c
void *malloc(size_t size);
```

If successful, `malloc()` returns a pointer to the first byte of allocated memory. If insufficient memory is available, it returns NULL. The returned pointer is of type `void*`, which must be typecast to the appropriate pointer type.

**calloc() - Contiguous Allocation**

The `calloc()` function allocates memory for an array of elements and initializes all bytes to zero. Its signature is:

```c
void *calloc(size_t num_elements, size_t element_size);
```

While `malloc()` allocates a single block, `calloc()` allocates multiple blocks and initializes them to zero. This is particularly useful when allocating arrays or structures where zero-initialization is desired.

**realloc() - Reallocation**

The `realloc()` function changes the size of previously allocated memory block. Its signature is:

```c
void *realloc(void *ptr, size_t new_size);
```

If the new size is larger, the existing data is preserved. If the new size is smaller, the beginning portion is preserved. If `ptr` is NULL, `realloc()` behaves like `malloc()`. If `new_size` is 0, it frees the memory block.

**free() - Memory Deallocation**

The `free()` function releases previously allocated memory, returning it to the heap for reuse:

```c
void free(void *ptr);
```

It is crucial to call `free()` for every memory block allocated to prevent memory leaks. Once freed, the pointer becomes dangling - it still holds the address but the memory is no longer valid.

### Memory Allocation with Structures

When allocating memory for structures, the `sizeof` operator is essential to determine the correct amount of memory:

```c
struct Student {
    int rollno;
    char name[50];
    float marks;
};

struct Student *ptr = (struct Student *)malloc(sizeof(struct Student));
```

The typecast `(struct Student *)` converts the `void*` returned by `malloc()` to a pointer to `struct Student`.

### Dynamic Arrays

Dynamic memory allocation allows creation of arrays whose size is determined at runtime:

```c
int *arr;
int n;

printf("Enter the number of elements: ");
scanf("%d", &n);

arr = (int *)malloc(n * sizeof(int));

if (arr == NULL) {
    printf("Memory allocation failed\n");
    exit(1);
}
```

### Self-Referential Structures and Dynamic Memory

Self-referential structures, which contain pointers to structures of the same type, are the building blocks for linked lists, trees, and graphs. Dynamic memory allocation is essential for creating nodes:

```c
struct Node {
    int data;
    struct Node *next;
};

// Creating a new node
struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
newNode->data = 10;
newNode->next = NULL;
```

### Dangling Pointers and Memory Leaks

**Dangling Pointer**: A pointer that points to memory that has been freed. This occurs when a pointer still references memory that has been deallocated using `free()`. To avoid this, set the pointer to NULL after freeing:

```c
free(ptr);
ptr = NULL;  // Prevents dangling pointer
```

**Memory Leak**: Memory that has been allocated but never freed before the program terminates. This gradually consumes available heap memory and can lead to program failure. Always pair every `malloc()`/`calloc()` with a corresponding `free()`.

## Examples

### Example 1: Dynamic Array Creation and Usage

Problem: Write a program to accept n integers from user, store them in dynamically allocated array, and display their sum.

Solution:

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, *arr, sum = 0;
    
    printf("Enter the number of integers: ");
    scanf("%d", &n);
    
    // Allocate memory for n integers
    arr = (int *)malloc(n * sizeof(int));
    
    if (arr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }
    
    printf("Enter %d integers:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }
    
    printf("Sum of all elements: %d\n", sum);
    
    // Free the allocated memory
    free(arr);
    arr = NULL;
    
    return 0;
}
```

**Step-by-step explanation**:
1. Accept the number of elements from user
2. Allocate memory using `malloc(n * sizeof(int))` - allocates n bytes where each int occupies sizeof(int) bytes
3. Check if allocation succeeded (NULL check)
4. Accept elements and calculate sum
5. Free the memory and set pointer to NULL

### Example 2: Dynamic Structure Array

Problem: Create a program to store information of n students (roll number, name, marks) using dynamic memory allocation.

Solution:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Student {
    int rollno;
    char name[50];
    float marks;
};

int main() {
    int n;
    struct Student *students;
    
    printf("Enter the number of students: ");
    scanf("%d", &n);
    
    // Allocate memory for n students
    students = (struct Student *)malloc(n * sizeof(struct Student));
    
    if (students == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }
    
    // Accept student details
    for (int i = 0; i < n; i++) {
        printf("\nEnter details for student %d:\n", i + 1);
        printf("Roll Number: ");
        scanf("%d", &students[i].rollno);
        printf("Name: ");
        scanf("%s", students[i].name);
        printf("Marks: ");
        scanf("%f", &students[i].marks);
    }
    
    // Display student details
    printf("\n--- Student Details ---\n");
    for (int i = 0; i < n; i++) {
        printf("Roll: %d, Name: %s, Marks: %.2f\n", 
               students[i].rollno, students[i].name, students[i].marks);
    }
    
    free(students);
    students = NULL;
    
    return 0;
}
```

### Example 3: Using calloc vs malloc

Problem: Demonstrate the difference between malloc and calloc by creating an integer array.

Solution:

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n = 5;
    int *arr_malloc, *arr_calloc;
    
    // Using malloc - memory contains garbage values
    arr_malloc = (int *)malloc(n * sizeof(int));
    
    printf("Using malloc (uninitialized): ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr_malloc[i]);  // Contains garbage values
    }
    printf("\n");
    
    // Using calloc - memory initialized to zero
    arr_calloc = (int *)calloc(n, sizeof(int));
    
    printf("Using calloc (initialized to zero): ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr_calloc[i]);  // All zeros
    }
    printf("\n");
    
    // Realloc example - increase array size
    arr_malloc = (int *)realloc(arr_malloc, 10 * sizeof(int));
    printf("After realloc to size 10: new capacity = 10\n");
    
    free(arr_malloc);
    free(arr_calloc);
    
    return 0;
}
```

## Exam Tips

1. **ALWAYS check for NULL after malloc/calloc/realloc**: This is the most common exam question. Always verify that memory allocation was successful before using the pointer.

2. **Remember to free memory**: In exam programs, always include `free()` for every `malloc()`/`calloc()`. Not doing so indicates memory leak and loses marks.

3. **Set pointer to NULL after freeing**: This prevents dangling pointer bugs and is considered good programming practice.

4. **sizeof operator usage**: Use `sizeof(data_type)` rather than hardcoded values. This ensures portability across different systems.

5. **malloc vs calloc selection**: Use calloc when you want zero-initialized memory (especially for arrays), use malloc for general allocation. Calloc takes two arguments (number of elements, size of each element) while malloc takes one (total size).

6. **realloc edge cases**: Remember that realloc can return a different address than the original pointer. Always assign realloc's return to a temporary variable first.

7. **Common error**: Forgetting to include `<stdlib.h>` results in implicit declaration warnings. Always include the proper header.

8. **Understanding memory layout**: Know the difference between stack (automatic/local variables) and heap (dynamically allocated) memory for exam questions on memory management.