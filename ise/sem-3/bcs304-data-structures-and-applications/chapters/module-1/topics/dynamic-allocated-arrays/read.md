# Dynamic Allocated Arrays

## Introduction

Dynamic Allocated Arrays represent a fundamental concept in computer science that bridges the gap between static memory management and flexible data structure design. Unlike static arrays whose size is fixed at compile time, dynamic arrays allow programmers to allocate memory during runtime based on actual program requirements. This capability is essential for building efficient and scalable software systems.

In the context of the University of Delhi's Computer Science curriculum, understanding dynamic memory allocation is crucial because it forms the backbone of many advanced data structures like linked lists, stacks, queues, trees, and graphs. The ability to efficiently manage memory at runtime enables developers to handle variable-sized data collections, process user inputs of unknown size, and implement algorithms that adapt to different input scales.

This topic builds directly on your understanding of pointers and memory concepts. In C and C++, the standard library functions malloc(), calloc(), realloc(), and free() provide the foundation for dynamic memory management. Mastering these concepts will not only help you in Data Structures but also in systems programming, operating systems, and embedded systems courses that you will encounter in later semesters.

## Key Concepts

### Static vs Dynamic Arrays

Static arrays are declared with a fixed size at compile time. For example, `int arr[100];` allocates 100 integers (400 bytes on most systems) permanently. The size cannot be changed during program execution. This approach wastes memory when less data is stored, and fails when more data is needed.

Dynamic arrays solve this problem by allocating memory at runtime using the heap. The heap is a large pool of unused memory that programs can request and release during execution. Unlike the stack (used for static allocations), the heap does not have size restrictions tied to function calls, making it ideal for storing large or variable-sized data.

### The malloc() Function

The `malloc()` (memory allocation) function is the primary method for requesting heap memory in C. Its syntax is:

```c
void* malloc(size_t size);
```

It accepts the number of bytes to allocate and returns a pointer to the allocated memory. If allocation fails (insufficient memory), it returns NULL. The return type is `void*`, which can be cast to any pointer type.

Example: Allocating an array of 10 integers:
```c
int *arr = (int*)malloc(10 * sizeof(int));
if (arr == NULL) {
    printf("Memory allocation failed\n");
    exit(1);
}
```

### The calloc() Function

The `calloc()` (contiguous allocation) function is similar to malloc() but has two key differences:
1. It initializes all bytes to zero
2. It takes two arguments: number of elements and size of each element

Syntax:
```c
void* calloc(size_t num_elements, size_t element_size);
```

Example:
```c
int *arr = (int*)calloc(10, sizeof(int));  // Allocates and initializes to 0
```

Use calloc() when you need zero-initialized memory, which is safer as it prevents reading uninitialized garbage values.

### The realloc() Function

The `realloc()` function resizes previously allocated memory. This is the key to implementing dynamic arrays that grow and shrink:

```c
void* realloc(void* ptr, size_t new_size);
```

It takes a pointer to existing memory and the new size. It can:
- Expand memory if space is available after the current block
- Allocate a new block and copy data if expansion is not possible
- Return NULL if reallocation fails (original memory is preserved)

Example of growing an array:
```c
int *new_arr = (int*)realloc(arr, 20 * sizeof(int));
if (new_arr == NULL) {
    printf("Reallocation failed\n");
    free(arr);  // Don't forget original memory
    exit(1);
}
arr = new_arr;  // Update pointer
```

### The free() Function

Memory allocated on the heap does not get automatically released when a function returns. The `free()` function releases previously allocated memory:

```c
void free(void* ptr);
```

Failing to free memory leads to memory leaks, where available memory gradually decreases until the program crashes. Always set pointers to NULL after freeing them to prevent dangling pointer bugs.

### One-Dimensional Dynamic Arrays

Creating a dynamic 1D array involves:
1. Calculating required bytes
2. Allocating memory
3. Checking for allocation failure
4. Using the array
5. Freeing memory when done

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    printf("Enter size: ");
    scanf("%d", &n);
    
    int *arr = (int*)malloc(n * sizeof(int));
    
    if (arr == NULL) {
        printf("Allocation failed\n");
        return 1;
    }
    
    // Use the array
    for (int i = 0; i < n; i++) {
        arr[i] = i * 10;
    }
    
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    
    free(arr);
    return 0;
}
```

### Two-Dimensional Dynamic Arrays

Creating 2D dynamic arrays requires either:
1. Array of pointers to arrays (contiguous memory not guaranteed)
2. Single contiguous block with row calculations

Method 1 - Array of pointers:
```c
int **create2DArray(int rows, int cols) {
    int **arr = (int**)malloc(rows * sizeof(int*));
    for (int i = 0; i < rows; i++) {
        arr[i] = (int*)malloc(cols * sizeof(int));
    }
    return arr;
}

void free2DArray(int **arr, int rows) {
    for (int i = 0; i < rows; i++) {
        free(arr[i]);
    }
    free(arr);
}
```

Method 2 - Contiguous block (better for cache performance):
```c
int *createContiguous2D(int rows, int cols) {
    return (int*)malloc(rows * cols * sizeof(int));
}

// Access element at (i, j): arr[i * cols + j]
```

## Examples

### Example 1: Implementing a Dynamic Array with Auto-Expansion

This example demonstrates how to create a dynamic array that automatically expands when full, similar to ArrayList in Java:

```c
#include <stdio.h>
#include <stdlib.h>

struct DynamicArray {
    int *data;
    int size;      // Current number of elements
    int capacity; // Total allocated space
};

void init(struct DynamicArray *arr, int initial_capacity) {
    arr->data = (int*)malloc(initial_capacity * sizeof(int));
    arr->size = 0;
    arr->capacity = initial_capacity;
}

void push(struct DynamicArray *arr, int value) {
    // Expand if needed
    if (arr->size == arr->capacity) {
        arr->capacity *= 2;
        arr->data = (int*)realloc(arr->data, arr->capacity * sizeof(int));
    }
    arr->data[arr->size++] = value;
}

void display(struct DynamicArray *arr) {
    printf("Array: ");
    for (int i = 0; i < arr->size; i++) {
        printf("%d ", arr->data[i]);
    }
    printf("\nSize: %d, Capacity: %d\n", arr->size, arr->capacity);
}

int main() {
    struct DynamicArray arr;
    init(&arr, 2);  // Start with capacity 2
    
    push(&arr, 10);  // [10]
    push(&arr, 20);  // [10, 20]
    display(arr);   // Size: 2, Capacity: 2
    
    push(&arr, 30);  // Triggers expansion: [10, 20, 30]
    display(arr);   // Size: 3, Capacity: 4
    
    push(&arr, 40);
    push(&arr, 50);  // Triggers expansion again
    display(arr);   // Size: 5, Capacity: 8
    
    free(arr.data);
    return 0;
}
```

**Output:**
```
Array: 10 20 
Size: 2, Capacity: 2
Array: 10 20 30 
Size: 3, Capacity: 4
Array: 10 20 30 40 50 
Size: 5, Capacity: 8
```

### Example 2: Creating and Processing a Sparse Matrix using Dynamic Arrays

This example shows dynamic allocation for a sparse matrix representation:

```c
#include <stdio.h>
#include <stdlib.h>

struct Element {
    int row;
    int col;
    int value;
};

struct SparseMatrix {
    int rows;
    int cols;
    int num_elements;
    struct Element *elements;
};

struct SparseMatrix createSparseMatrix(int r, int c, int n) {
    struct SparseMatrix sm;
    sm.rows = r;
    sm.cols = c;
    sm.num_elements = n;
    sm.elements = (struct Element*)malloc(n * sizeof(struct Element));
    return sm;
}

void displaySparse(struct SparseMatrix sm) {
    printf("Sparse Matrix (%dx%d) with %d non-zero elements:\n", 
           sm.rows, sm.cols, sm.num_elements);
    printf("Row\tCol\tValue\n");
    for (int i = 0; i < sm.num_elements; i++) {
        printf("%d\t%d\t%d\n", 
               sm.elements[i].row, 
               sm.elements[i].col, 
               sm.elements[i].value);
    }
}

int main() {
    // Create a 4x4 sparse matrix with 3 non-zero elements
    struct SparseMatrix sm = createSparseMatrix(4, 4, 3);
    
    sm.elements[0] = (struct Element){0, 1, 5};
    sm.elements[1] = (struct Element){2, 2, 8};
    sm.elements[2] = (struct Element){3, 0, 12};
    
    displaySparse(sm);
    
    free(sm.elements);
    return 0;
}
```

### Example 3: Memory Allocation Comparison (malloc vs calloc)

This example demonstrates the difference between malloc() and calloc():

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    // Using malloc - memory contains garbage values
    int *arr1 = (int*)malloc(5 * sizeof(int));
    printf("Using malloc (uninitialized):\n");
    for (int i = 0; i < 5; i++) {
        printf("arr1[%d] = %d\n", i, arr1[i]);  // Undefined behavior
    }
    
    // Using calloc - memory initialized to zero
    int *arr2 = (int*)calloc(5, sizeof(int));
    printf("\nUsing calloc (initialized to zero):\n");
    for (int i = 0; i < 5; i++) {
        printf("arr2[%d] = %d\n", i, arr2[i]);  // All zeros
    }
    
    free(arr1);
    free(arr2);
    return 0;
}
```

## Exam Tips

1. **Always check for NULL after malloc/calloc/realloc**: In exams, always include NULL checks. This demonstrates memory safety awareness and prevents segmentation faults.

2. **Remember to free memory**: Failing to free allocated memory causes memory leaks. In exam answers, always show the corresponding `free()` statement.

3. **malloc vs calloc distinction**: malloc() is faster for uninitialized memory; calloc() zeros the memory. Use calloc when you need initialized arrays or want safer code.

4. **realloc can fail**: When using realloc(), store the result in a temporary pointer first. If realloc fails, you still have the original pointer to free.

5. **Size calculations**: Remember that `malloc(n * sizeof(type))` is the correct pattern. Never do `malloc(n)` as it allocates only n bytes, not n elements.

6. **Pointer arithmetic**: In dynamic arrays, `*(arr + i)` is equivalent to `arr[i]`. Understand both notations for exam questions.

7. **2D dynamic array memory layout**: Know both methods - array of pointers (easier syntax) vs contiguous allocation (better performance). Contiguous: element at (i,j) = arr[i * cols + j].

8. **Common errors to avoid**: Using uninitialized pointers, dereferencing NULL pointers, double-freeing memory, and accessing memory after freeing (dangling pointers).

9. **Time complexity**: Appending to a dynamic array is O(1) amortized. When the array fills up and needs resizing, it becomes O(n), but this happens infrequently.

10. **Alignment considerations**: Memory allocation functions return addresses aligned for any data type. Don't worry about alignment in basic implementations.