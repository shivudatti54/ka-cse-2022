# Using Dynamic Arrays

## Introduction

Dynamic arrays represent one of the most fundamental concepts in computer programming and data structures. Unlike static arrays, which have a fixed size determined at compile time, dynamic arrays allow programmers to allocate memory during runtime, providing flexibility to grow and shrink based on actual data requirements. This capability is essential for building efficient data structures like stacks, queues, and various list implementations that need to handle variable amounts of data.

In the context of the University of Delhi Computer Science curriculum, understanding dynamic arrays is crucial because they form the backbone of many complex data structures studied in subsequent topics. When implementing stacks and queues, linked lists, and polynomial representations, the ability to manage memory dynamically becomes a critical skill. C, being the primary programming language in most DU Data Structures courses, provides powerful mechanisms like malloc(), calloc(), and free() for dynamic memory management. This topic explores the intricacies of dynamic arrays, their implementation, advantages, and common pitfalls that students must master to write efficient and bug-free code.

## Key Concepts

### Static vs Dynamic Arrays

Static arrays are allocated on the stack with a fixed size known at compile time. For example, declaring `int arr[100];` creates an array that can hold exactly 100 integers throughout the program's execution. This fixed size presents two major problems: first, if you need more space than allocated, you cannot accommodate additional elements; second, if you declare more space than needed, you waste precious memory.

Dynamic arrays, in contrast, are allocated on the heap using functions like malloc() or calloc(). The heap is a larger pool of memory that persists until explicitly freed, allowing for much larger allocations. When you allocate memory dynamically, you receive a pointer to the beginning of the allocated block, and you can store elements just as you would in a static array.

### Memory Allocation Functions in C

The malloc() function (memory allocation) is the primary method for allocating dynamic memory. Its syntax is: `void* malloc(size_t size);`. It allocates the specified number of bytes and returns a void pointer to the beginning of the allocated block. If allocation fails (due to insufficient memory), it returns NULL.

The calloc() function (contiguous allocation) is similar but initializes all bytes to zero. Its syntax is: `void* calloc(size_t num_elements, size_t element_size);`. For instance, `int* arr = (int*)calloc(10, sizeof(int));` allocates space for 10 integers and initializes them to zero.

The realloc() function allows you to resize an existing dynamic array. Its syntax is: `void* realloc(void* ptr, size_t new_size);`. This is particularly useful when you need to grow or shrink an array during runtime. The function attempts to resize the existing block, and if that's not possible, it allocates a new block and copies the existing data.

The free() function releases previously allocated memory back to the system. Every malloc(), calloc(), or realloc() call must have a corresponding free() to prevent memory leaks.

### How Dynamic Arrays Work

A dynamic array maintains three key pieces of information: a pointer to the beginning of the array, the current capacity (maximum number of elements that can be stored), and the current size (number of elements actually stored). When you create a dynamic array, you allocate an initial capacity, often using a strategy like starting with a small value (like 1 or 4) and doubling it whenever the array becomes full.

When adding an element to a dynamic array, the algorithm first checks if the current size equals the capacity. If so, it allocates a new, larger array (typically twice the current capacity), copies all existing elements to the new array, frees the old array, and then adds the new element. This amortized analysis shows that while individual operations may occasionally be expensive, the average cost per insertion remains constant.

### Implementing a Dynamic Array

To implement a dynamic array in C, you typically define a structure that encapsulates the array pointer and its metadata:

```c
typedef struct {
    int* data;      // pointer to array elements
    int size;       // current number of elements
    int capacity;   // maximum capacity
} DynamicArray;
```

Initialization involves allocating the initial array and setting size and capacity to appropriate starting values. Adding elements requires checking capacity, resizing if necessary, and inserting the new element at the appropriate index. Removing elements involves shifting subsequent elements and decrementing the size, though the capacity remains unchanged until you explicitly shrink it.

## Examples

### Example 1: Creating and Using a Simple Dynamic Array

Problem: Write a C program that dynamically allocates an integer array of initial capacity 5, adds 7 numbers to it, and prints all elements.

Solution:

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int capacity = 5;
    int size = 0;
    int* arr = (int*)malloc(capacity * sizeof(int));
    
    if (arr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }
    
    // Add 7 numbers (exceeds initial capacity)
    int numbers[] = {10, 20, 30, 40, 50, 60, 70};
    
    for (int i = 0; i < 7; i++) {
        if (size == capacity) {
            // Double the capacity
            capacity *= 2;
            arr = (int*)realloc(arr, capacity * sizeof(int));
            if (arr == NULL) {
                printf("Reallocation failed\n");
                return 1;
            }
        }
        arr[size] = numbers[i];
        size++;
    }
    
    // Print all elements
    printf("Array contents: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\nFinal size: %d, Final capacity: %d\n", size, capacity);
    
    free(arr);
    return 0;
}
```

Output:
```
Array contents: 10 20 30 40 50 60 70 
Final size: 7, Final capacity: 10
```

This example demonstrates how the array automatically grows from capacity 5 to 10 when we try to add the 6th element.

### Example 2: Dynamic Array for Stack Implementation

Problem: Implement a stack using a dynamic array that automatically grows when full.

Solution:

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int* array;
    int top;
    int capacity;
} DynamicStack;

void initStack(DynamicStack* s, int initialCapacity) {
    s->array = (int*)malloc(initialCapacity * sizeof(int));
    s->top = -1;
    s->capacity = initialCapacity;
}

bool isFull(DynamicStack* s) {
    return s->top == s->capacity - 1;
}

void push(DynamicStack* s, int value) {
    if (isFull(s)) {
        s->capacity *= 2;
        s->array = (int*)realloc(s->array, s->capacity * sizeof(int));
    }
    s->array[++s->top] = value;
}

int pop(DynamicStack* s) {
    if (s->top < 0) {
        printf("Stack underflow\n");
        return -1;
    }
    return s->array[s->top--];
}

void display(DynamicStack* s) {
    printf("Stack (top to bottom): ");
    for (int i = s->top; i >= 0; i--) {
        printf("%d ", s->array[i]);
    }
    printf("\n");
}

int main() {
    DynamicStack s;
    initStack(&s, 2);
    
    push(&s, 5);
    push(&s, 10);
    push(&s, 15);  // Triggers resize
    display(&s);
    
    printf("Popped: %d\n", pop(&s));
    display(&s);
    
    free(s.array);
    return 0;
}
```

### Example 3: Managing Memory Correctly

Problem: Demonstrate proper memory management including allocation, reallocation, and freeing.

Solution:

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    // Step 1: Initial allocation for 3 integers
    int* numbers = (int*)malloc(3 * sizeof(int));
    if (numbers == NULL) {
        fprintf(stderr, "Allocation failed\n");
        return 1;
    }
    
    numbers[0] = 100;
    numbers[1] = 200;
    numbers[2] = 300;
    
    printf("Initial array: %d %d %d\n", numbers[0], numbers[1], numbers[2]);
    
    // Step 2: Resize to hold 5 integers
    int* temp = (int*)realloc(numbers, 5 * sizeof(int));
    if (temp == NULL) {
        free(numbers);  // Free original before exiting
        fprintf(stderr, "Reallocation failed\n");
        return 1;
    }
    numbers = temp;
    
    numbers[3] = 400;
    numbers[4] = 500;
    
    printf("After resize: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");
    
    // Step 3: Important - always free memory
    free(numbers);
    numbers = NULL;  // Good practice to avoid dangling pointers
    
    return 0;
}
```

## Exam Tips

For DU semester examinations, several critical points about dynamic arrays frequently appear in questions. First, always check if malloc() or realloc() returns NULL before using the pointer; failing to do so can cause segmentation faults when memory is exhausted. Second, remember that free() only releases memory but does not set the pointer to NULL, so always set pointers to NULL after freeing to avoid dangling pointer bugs.

Third, understand the difference between stack and heap allocation: stack allocation is faster but limited in size, while heap allocation is slower but can handle much larger data. Fourth, when using realloc(), always assign to a temporary variable first, then check for failure before updating the original pointer. Fifth, remember that realloc() may move the entire block to a new location, so any other pointers to the old location become invalid.

Sixth, be aware of memory leaks: every malloc() must have a corresponding free(), and remember that returning from a function without freeing memory in certain scenarios causes leaks. Seventh, for competitive exam questions, remember the amortized cost analysis: while individual operations may be expensive, the average cost per operation in a growing dynamic array is O(1). Eighth, when implementing data structures like stacks and queues using dynamic arrays, always handle both overflow (array full) and underflow (array empty) conditions explicitly.