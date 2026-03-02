# Dynamic Allocated Arrays

## Introduction

Dynamic Allocated Arrays represent a fundamental concept in data structures that enables programmers to create arrays whose size is determined at runtime rather than compile time. In the context of the University of Delhi's Computer Science curriculum, understanding dynamic memory allocation is essential for implementing efficient data structures and solving real-world programming problems.

Traditional static arrays require the programmer to specify their size during compilation. This limitation poses significant challenges when the exact amount of data is unknown beforehand or when memory requirements vary during program execution. Dynamic allocated arrays solve this problem by allocating memory from the heap during runtime, allowing the program to adapt to varying memory needs efficiently.

The concept builds directly upon the understanding of pointers and memory management in C/C++, which were introduced in the prerequisite topics. In this chapter, we will explore how to create, manipulate, and manage dynamic arrays, along with their advantages, limitations, and practical applications in data structure implementations.

## Key Concepts

### Understanding Dynamic Memory Allocation

Dynamic memory allocation refers to the process of allocating memory from the heap segment during program execution. Unlike stack memory, which is automatically managed, heap memory requires explicit allocation and deallocation by the programmer. In C, this is accomplished through four fundamental functions: malloc(), calloc(), realloc(), and free().

The malloc() function allocates a specified number of bytes and returns a pointer to the beginning of the allocated memory block. If the allocation fails, it returns NULL. The general syntax is: pointer = (data_type*)malloc(number_of_elements * sizeof(data_type));

The calloc() function is similar to malloc() but initializes all bytes to zero. It takes two parameters: the number of elements and the size of each element. This is particularly useful when creating arrays that will store numeric data.

The realloc() function allows modification of previously allocated memory size. This is crucial for implementing dynamic arrays that grow or shrink during program execution. If the new size is larger, existing data is preserved, and additional memory is allocated. If smaller, the block is truncated.

The free() function releases previously allocated memory, returning it to the heap for future use. Failure to free memory leads to memory leaks, a critical issue in long-running programs.

### One-Dimensional Dynamic Arrays

Creating a one-dimensional dynamic array involves declaring a pointer, allocating memory based on the required size, and using array notation to access elements. Consider the following implementation:

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    printf("Enter the size of array: ");
    scanf("%d", &n);
    
    // Dynamic allocation
    int *arr = (int*)malloc(n * sizeof(int));
    
    if (arr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }
    
    // Initialize and display elements
    for (int i = 0; i < n; i++) {
        arr[i] = i + 1;
    }
    
    printf("Array elements: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    
    free(arr);
    return 0;
}
```

The pointer `arr` now behaves like an array name, allowing access through both pointer arithmetic and array indexing. The memory remains valid until explicitly freed.

### Two-Dimensional Dynamic Arrays

Two-dimensional dynamic arrays require careful memory management. There are two primary approaches: contiguous allocation and array of pointers.

In the contiguous allocation method, a single block of memory is allocated to hold all elements, organized in row-major order:

```c
int **create2DArray(int rows, int cols) {
    int **arr = (int**)malloc(rows * sizeof(int*));
    
    if (arr == NULL) return NULL;
    
    // Allocate contiguous memory for all elements
    arr[0] = (int*)malloc(rows * cols * sizeof(int));
    
    if (arr[0] == NULL) {
        free(arr);
        return NULL;
    }
    
    // Set row pointers
    for (int i = 1; i < rows; i++) {
        arr[i] = arr[0] + i * cols;
    }
    
    return arr;
}
```

In the array of pointers method, each row is allocated separately:

```c
int **create2DArraySeparate(int rows, int cols) {
    int **arr = (int**)malloc(rows * sizeof(int*));
    
    for (int i = 0; i < rows; i++) {
        arr[i] = (int*)malloc(cols * sizeof(int));
    }
    
    return arr;
}
```

The contiguous allocation method offers better cache performance and allows deallocation with a single free() call, while the array of pointers method provides easier row operations but requires multiple free() calls.

### Resizing Dynamic Arrays

One of the most powerful features of dynamic arrays is the ability to resize them during execution. The realloc() function enables this functionality:

```c
int *resizeArray(int *arr, int oldSize, int newSize) {
    int *newArr = (int*)realloc(arr, newSize * sizeof(int));
    
    if (newArr == NULL) {
        printf("Reallocation failed\n");
        return arr;
    }
    
    return newArr;
}
```

When reallocating, if the new size is larger, newly allocated memory is uninitialized. If smaller, data beyond the new size is truncated. Understanding these behaviors is crucial for avoiding bugs.

### Memory Management Best Practices

Proper memory management is critical when working with dynamic arrays. Always check the return value of allocation functions for NULL. Initialize allocated memory before use, either through calloc() or explicit loops. Match every malloc() or calloc() with a corresponding free(). When dealing with dynamic arrays of structures, ensure nested allocations are properly freed in reverse order of creation.

## Examples

### Example 1: Creating a Dynamic Array of Structures

Consider implementing a dynamic array to store student records:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[50];
    int rollno;
    float marks;
} Student;

int main() {
    int n;
    printf("Enter number of students: ");
    scanf("%d", &n);
    
    // Dynamic allocation for array of structures
    Student *class = (Student*)malloc(n * sizeof(Student));
    
    if (class == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }
    
    // Input student data
    for (int i = 0; i < n; i++) {
        printf("\nEnter details for student %d:\n", i + 1);
        printf("Name: ");
        scanf("%s", class[i].name);
        printf("Roll No: ");
        scanf("%d", &class[i].rollno);
        printf("Marks: ");
        scanf("%f", &class[i].marks);
    }
    
    // Display student data
    printf("\nStudent Records:\n");
    for (int i = 0; i < n; i++) {
        printf("Name: %s, Roll No: %d, Marks: %.2f\n",
               class[i].name, class[i].rollno, class[i].marks);
    }
    
    free(class);
    return 0;
}
```

This example demonstrates how dynamic allocation enables storage of variable-sized collections of complex data types.

### Example 2: Implementing a Dynamic Array with Auto-Expansion

This example demonstrates implementing a dynamic array that automatically expands when full:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *array;
    int size;
    int capacity;
} DynamicArray;

void init(DynamicArray *arr, int initialCapacity) {
    arr->capacity = initialCapacity;
    arr->size = 0;
    arr->array = (int*)malloc(arr->capacity * sizeof(int));
}

void resize(DynamicArray *arr) {
    arr->capacity *= 2;
    arr->array = (int*)realloc(arr->array, arr->capacity * sizeof(int));
}

void append(DynamicArray *arr, int value) {
    if (arr->size == arr->capacity) {
        resize(arr);
    }
    arr->array[arr->size++] = value;
}

void display(DynamicArray *arr) {
    printf("Array (size: %d, capacity: %d): ", arr->size, arr->capacity);
    for (int i = 0; i < arr->size; i++) {
        printf("%d ", arr->array[i]);
    }
    printf("\n");
}

int main() {
    DynamicArray arr;
    init(&arr, 2);
    
    append(&arr, 10);
    append(&arr, 20);
    display(&arr);
    
    append(&arr, 30);  // Triggers resize
    display(&arr);
    
    append(&arr, 40);
    append(&arr, 50);  // Triggers resize again
    display(&arr);
    
    free(arr.array);
    return 0;
}
```

This pattern is the foundation for implementing vectors in C++ and ArrayList in Java, demonstrating the practical utility of dynamic arrays in real-world applications.

### Example 3: Handling Sparse Matrices Using Dynamic Arrays

Sparse matrices, where most elements are zero, can be efficiently stored using dynamic arrays:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int row;
    int col;
    int value;
} Element;

typedef struct {
    int rows;
    int cols;
    int num;
    Element *elements;
} SparseMatrix;

SparseMatrix createSparseMatrix(int rows, int cols, int num) {
    SparseMatrix sm;
    sm.rows = rows;
    sm.cols = cols;
    sm.num = num;
    sm.elements = (Element*)malloc(num * sizeof(Element));
    return sm;
}

void displaySparse(SparseMatrix sm) {
    printf("\nSparse Matrix (%dx%d with %d non-zero elements):\n",
           sm.rows, sm.cols, sm.num);
    printf("Row\tCol\tValue\n");
    for (int i = 0; i < sm.num; i++) {
        printf("%d\t%d\t%d\n",
               sm.elements[i].row,
               sm.elements[i].col,
               sm.elements[i].value);
    }
}

int main() {
    SparseMatrix sm = createSparseMatrix(4, 4, 3);
    
    sm.elements[0] = (Element){0, 0, 5};
    sm.elements[1] = (Element){1, 2, 10};
    sm.elements[2] = (Element){3, 3, 7};
    
    displaySparse(sm);
    
    free(sm.elements);
    return 0;
}
```

This implementation shows how dynamic arrays enable efficient memory usage for special data structures like sparse matrices.

## Exam Tips

For the University of Delhi semester examinations, keep the following points in mind:

1. **Function Differences**: Memorize the differences between malloc(), calloc(), realloc(), and free(). malloc() does not initialize memory, calloc() initializes to zero, realloc() changes size, and free() releases memory.

2. **Syntax Matters**: Remember the correct syntax including the casting and sizeof() operator. Common errors include forgetting to cast the return value or using wrong size calculations.

3. **NULL Check**: Always emphasize the importance of checking for NULL after allocation. This is a common exam requirement and demonstrates good programming practice.

4. **Memory Leak Prevention**: Understand how memory leaks occur and how to prevent them. Every malloc() must have a corresponding free().

5. **2D Array Allocation**: Be prepared to write code for creating 2D dynamic arrays using both contiguous and pointer-to-pointer methods. Understand when each approach is preferable.

6. **Realloc Behavior**: Know what happens when realloc() fails, how it handles partial success, and the implications of using NULL as the first argument.

7. **Pointer-Arithmetic Connection**: Understand the relationship between pointers and arrays. The expression arr[i] is equivalent to *(arr+i).

8. **Common Errors**: Avoid common mistakes like using sizeof on a pointer, forgetting to free memory in all code paths, and confusing stack allocation with heap allocation.

9. **Time Complexity**: Know the time complexity of allocation operations. malloc() and calloc() have O(1) average case complexity, while realloc() may require O(n) for copying data.

10. **Practical Applications**: Be prepared to explain real-world applications like dynamic arrays in data structures, handling variable-sized input, and implementing ADTs.