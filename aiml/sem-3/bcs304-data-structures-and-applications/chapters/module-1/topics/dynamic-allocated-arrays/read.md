# Dynamic Allocated Arrays

## Introduction

Static arrays in C and C++ require the programmer to specify the size at compile time, which presents a significant limitation when the required memory is unknown until runtime. Dynamic allocated arrays solve this fundamental problem by allowing memory allocation during program execution, giving programmers flexibility to handle varying input sizes and optimize memory usage.

In the context of data structures, understanding dynamic memory allocation is essential because most sophisticated data structures—stacks, queues, linked lists, trees, and hash tables—rely on dynamically allocated memory to grow and shrink as needed. The ability to allocate arrays dynamically forms the foundation upon which these complex structures are built. This topic builds directly upon your knowledge of pointers and explores how C's memory allocation functions (malloc, calloc, realloc, and free) and C++'s operators (new and delete) enable the creation of flexible, runtime-sized arrays.

For University of Delhi examinations, this topic frequently appears in practical programming questions and theoretical concepts regarding memory management. A thorough understanding of dynamic array allocation demonstrates proficiency in memory manipulation—a skill essential for efficient algorithm implementation and system-level programming.

## Key Concepts

### Static Versus Dynamic Arrays

Static arrays allocate memory at compile time with a fixed size determined in advance. The memory for static arrays comes from the stack segment, and the size cannot change during execution. Consider a static integer array declaration:

```c
int numbers[100];  // Size fixed at compile time
```

This approach suffers from two critical limitations: first, if the actual data requires fewer than 100 elements, valuable stack memory goes to waste; second, if more than 100 elements are needed, the program cannot accommodate the overflow, leading to undefined behavior or memory corruption.

Dynamic arrays overcome these limitations by allocating memory from the heap (also called the free store) during runtime. The heap is a larger memory segment that can grow and shrink as the program executes. Dynamic allocation enables precise memory usage based on actual requirements.

### Memory Allocation Functions in C

The standard library provides four primary functions for dynamic memory management, declared in the header file `<stdlib.h>`:

**malloc (Memory Allocation)**

The malloc function allocates a specified number of bytes from the heap and returns a pointer to the beginning of the allocated block. Its prototype is:

```c
void* malloc(size_t size);
```

If allocation succeeds, malloc returns a pointer to the allocated memory; if it fails (insufficient memory available), it returns NULL. Always check the return value before using the pointer.

Example: Allocating an array of 10 integers:

```c
int* arr = (int*)malloc(10 * sizeof(int));
if (arr == NULL) {
    printf("Memory allocation failed\n");
    exit(1);
}
```

The casting of void* to int* is necessary in C (though not in C++), and sizeof(int) ensures portability across different systems.

**calloc (Contiguous Allocation)**

The calloc function allocates memory for an array of elements and initializes all bytes to zero. Its prototype is:

```c
void* calloc(size_t num_elements, size_t element_size);
```

Example: Allocating and initializing an array of 10 integers to zero:

```c
int* arr = (int*)calloc(10, sizeof(int));
```

Unlike malloc, which leaves the allocated memory uninitialized (containing garbage values), calloc guarantees all elements are zero-initialized. This safety comes with a slight performance overhead.

**realloc (Reallocation)**

The realloc function changes the size of previously allocated memory. Its prototype is:

```c
void* realloc(void* ptr, size_t new_size);
```

If the function succeeds, it returns a pointer to the newly allocated memory (which may be different from the original pointer) and copies the existing data to the new location. If ptr is NULL, realloc behaves like malloc. If new_size is 0, it frees the memory block.

Example: Expanding an array from 10 to 20 elements:

```c
int* new_arr = (int*)realloc(arr, 20 * sizeof(int));
if (new_arr == NULL) {
    printf("Reallocation failed\n");
    free(arr);
    exit(1);
}
arr = new_arr;  // Update pointer to new memory location
```

**free Function**

The free function releases previously allocated heap memory, returning it to the system for reuse. Its prototype is:

```c
void free(void* ptr);
```

Calling free on a pointer that was not obtained from malloc, calloc, or realloc, or calling free on the same pointer twice, results in undefined behavior. After freeing memory, set the pointer to NULL to prevent accidental use of the dangling pointer.

### Dynamic Arrays in C++

C++ provides operators new and delete as alternatives to C's functions, offering cleaner syntax and better integration with object-oriented features.

**new Operator**

The new operator allocates memory and (for objects) calls constructors:

```c
int* arr = new int[10];        // Array of 10 integers
int* single = new int(5);       // Single integer initialized to 5
```

**delete Operator**

The delete operator frees memory and (for objects) calls destructors:

```c
delete[] arr;   // Free array allocated with new[]
delete single;  // Free single object
```

Always use delete[] for arrays and delete for single objects to ensure proper cleanup.

### One-Dimensional Dynamic Arrays

Creating a 1D dynamic array involves three steps: calculating required bytes, allocating memory, and checking for allocation failure.

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    printf("Enter array size: ");
    scanf("%d", &n);
    
    // Allocate memory for n integers
    int* arr = (int*)malloc(n * sizeof(int));
    
    if (arr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }
    
    // Initialize and use the array
    for (int i = 0; i < n; i++) {
        arr[i] = i * 10;
    }
    
    // Print elements
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    
    // Free memory
    free(arr);
    arr = NULL;
    
    return 0;
}
```

### Two-Dimensional Dynamic Arrays

Two-dimensional dynamic arrays can be implemented using two primary approaches:

**Method 1: Array of Pointers**

This approach creates an array of row pointers, where each pointer points to a separately allocated array of elements.

```c
int** create2DArray(int rows, int cols) {
    int** arr = (int**)malloc(rows * sizeof(int*));
    if (arr == NULL) return NULL;
    
    for (int i = 0; i < rows; i++) {
        arr[i] = (int*)malloc(cols * sizeof(int));
        if (arr[i] == NULL) {
            // Handle partial allocation failure
            for (int j = 0; j < i; j++) {
                free(arr[j]);
            }
            free(arr);
            return NULL;
        }
    }
    return arr;
}

void free2DArray(int** arr, int rows) {
    for (int i = 0; i < rows; i++) {
        free(arr[i]);
    }
    free(arr);
}
```

This method offers flexibility: each row can be independently resized. However, the memory is not contiguous, which can affect cache performance.

**Method 2: Contiguous Allocation**

This approach allocates a single block of memory for the entire 2D array, providing better memory locality.

```c
int** createContiguous2DArray(int rows, int cols) {
    int** arr = (int**)malloc(rows * sizeof(int*));
    if (arr == NULL) return NULL;
    
    arr[0] = (int*)malloc(rows * cols * sizeof(int));
    if (arr[0] == NULL) {
        free(arr);
        return NULL;
    }
    
    // Set up row pointers to point into the contiguous block
    for (int i = 1; i < rows; i++) {
        arr[i] = arr[i-1] + cols;
    }
    return arr;
}
```

This method requires only two free() calls: one for the data block and one for the pointer array.

## Examples

### Example 1: Creating a Dynamic Integer Array with Initialization

Problem: Write a C program to dynamically allocate an integer array of size n, initialize it with values 1 through n, and display the sum.

Solution:

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, sum = 0;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    
    // Allocate memory using calloc (automatically initialized to 0)
    int* arr = (int*)calloc(n, sizeof(int));
    
    if (arr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }
    
    // Initialize array with values 1 to n
    for (int i = 0; i < n; i++) {
        arr[i] = i + 1;
        sum += arr[i];
    }
    
    printf("Array elements: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\nSum: %d\n", sum);
    
    free(arr);
    return 0;
}
```

The use of calloc ensures all elements start at zero before assignment. The time complexity is O(n) for both initialization and summation.

### Example 2: Dynamic Resizing of an Array

Problem: Implement a dynamic array that doubles its size when full, using realloc.

Solution:

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int capacity = 5;
    int size = 0;
    int* arr = (int*)malloc(capacity * sizeof(int));
    
    if (arr == NULL) {
        printf("Allocation failed\n");
        return 1;
    }
    
    // Insert 12 elements to demonstrate resizing
    for (int i = 1; i <= 12; i++) {
        if (size == capacity) {
            capacity *= 2;
            int* new_arr = (int*)realloc(arr, capacity * sizeof(int));
            if (new_arr == NULL) {
                printf("Reallocation failed\n");
                free(arr);
                return 1;
            }
            arr = new_arr;
            printf("Array resized to capacity: %d\n", capacity);
        }
        arr[size++] = i * 10;
    }
    
    printf("Final array (size %d, capacity %d): ", size, capacity);
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    free(arr);
    return 0;
}
```

This example demonstrates the fundamental principle behind vector implementations in C++ and similar dynamic array containers. The array starts with capacity 5 and doubles to 10, then 20, accommodating 12 elements with two reallocations.

### Example 3: Transpose of a Matrix Using Dynamic Arrays

Problem: Create a dynamic 2D array to store a matrix, compute its transpose, and display both matrices.

Solution:

```c
#include <stdio.h>
#include <stdlib.h>

int** createMatrix(int rows, int cols) {
    int** matrix = (int**)malloc(rows * sizeof(int*));
    for (int i = 0; i < rows; i++) {
        matrix[i] = (int*)malloc(cols * sizeof(int));
    }
    return matrix;
}

void freeMatrix(int** matrix, int rows) {
    for (int i = 0; i < rows; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

void transpose(int** original, int** transposed, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            transposed[j][i] = original[i][j];
        }
    }
}

int main() {
    int rows = 3, cols = 4;
    
    int** matrix = createMatrix(rows, cols);
    int** transposed = createMatrix(cols, rows);
    
    // Initialize matrix with values
    int count = 1;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            matrix[i][j] = count++;
        }
    }
    
    // Compute transpose
    transpose(matrix, transposed, rows, cols);
    
    // Display original matrix
    printf("Original Matrix (%dx%d):\n", rows, cols);
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }
    
    // Display transposed matrix
    printf("\nTransposed Matrix (%dx%d):\n", cols, rows);
    for (int i = 0; i < cols; i++) {
        for (int j = 0; j < rows; j++) {
            printf("%d\t", transposed[i][j]);
        }
        printf("\n");
    }
    
    freeMatrix(matrix, rows);
    freeMatrix(transposed, cols);
    
    return 0;
}
```

This example demonstrates practical 2D dynamic array manipulation, essential for matrix operations in numerical computing and image processing applications.

## Exam Tips

For DU semester examinations, keep these essential points in mind:

1. ALWAYS check for NULL after malloc/calloc/realloc before using the pointer. This is the most common mistake leading to runtime crashes.

2. Remember that malloc allocates uninitialized memory (contains garbage values), while calloc initializes all bytes to zero.

3. When using realloc, ALWAYS assign the result to a temporary pointer first, then update the original pointer. This prevents memory leaks if realloc fails.

4. Forgetting to call free() results in memory leaks—accumulated memory that remains allocated until program termination.

5. The sizeof operator should be used instead of hardcoded values (use sizeof(int) not 4) for portable code.

6. In C++, prefer std::vector over manual dynamic arrays when possible—it handles memory management automatically and provides bounds-checked access.

7. Understand the difference between stack and heap memory: stack is limited and fast, heap is larger but requires explicit management.

8. When implementing 2D dynamic arrays, remember that contiguous allocation provides better cache performance than array-of-pointers.

9. After calling free(), always set the pointer to NULL to avoid use-after-free bugs.

10. For exam questions involving dynamic arrays, clearly show the allocation, usage, and deallocation phases in your code.