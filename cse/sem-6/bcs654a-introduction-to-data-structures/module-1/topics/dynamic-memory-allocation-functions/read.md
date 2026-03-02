# Dynamic Memory Allocation Functions in C

## Introduction

Dynamic memory allocation is a fundamental concept in Data Structures that allows programs to request memory from the heap at runtime. In C programming, this is essential for creating dynamic data structures like linked lists, trees, and graphs. Unlike static allocation where memory is allocated at compile time, dynamic allocation provides flexibility to allocate and deallocate memory as needed during program execution.

## The Four Dynamic Memory Functions

C provides four library functions in `<stdlib.h>` for dynamic memory management:

### 1. malloc() - Memory Allocation

**Syntax:**

```c
void* malloc(size_t size);
```

**Description:**

- Allocates a block of memory of specified size in bytes
- Returns a pointer to the first byte of allocated memory
- Returns NULL if allocation fails
- Memory content is uninitialized (contains garbage values)

**Example:**

```c
int *ptr = (int*)malloc(5 * sizeof(int));
if (ptr == NULL) {
 printf("Memory allocation failed\n");
 exit(1);
}
```

### 2. calloc() - Contiguous Allocation

**Syntax:**

```c
void* calloc(size_t n, size_t size);
```

**Description:**

- Allocates memory for an array of n elements, each of specified size
- Returns a pointer to the allocated memory
- Initializes all bytes to zero (unlike malloc)
- Returns NULL if allocation fails

**Example:**

```c
int *arr = (int*)calloc(10, sizeof(int));
// All 10 integers are initialized to 0
```

### 3. realloc() - Reallocation

**Syntax:**

```c
void* realloc(void *ptr, size_t new_size);
```

**Description:**

- Changes the size of previously allocated memory block
- Preserves the content of the old block (up to the minimum of old and new sizes)
- May move the memory block to a new location
- Returns pointer to the new location (may be same as old location)

**Example:**

```c
int *ptr = (int*)malloc(5 * sizeof(int));
// ... use ptr ...
ptr = (int*)realloc(ptr, 10 * sizeof(int)); // Resize to 10 integers
```

### 4. free() - Deallocation

**Syntax:**

```c
void free(void *ptr);
```

**Description:**

- Deallocates previously allocated memory
- Makes the memory available for future allocations
- Does not change the pointer value itself
- Calling free on a NULL pointer is safe (does nothing)

**Example:**

```c
free(ptr);
ptr = NULL; // Good practice to avoid dangling pointers
```

## Comparison Table

| Feature             | malloc        | calloc                         | realloc               |
| ------------------- | ------------- | ------------------------------ | --------------------- |
| Number of arguments | 1             | 2                              | 2                     |
| Initialization      | Uninitialized | Zeroed                         | Preserves old data    |
| Speed               | Faster        | Slower (due to initialization) | Varies                |
| Use case            | Single block  | Array of elements              | Resize existing block |

## Importance in Data Structures

Dynamic memory allocation is crucial for implementing:

1. **Linked Lists**: Each node is created using malloc

```c
struct Node {
 int data;
 struct Node* next;
};
struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
```

2. **Dynamic Arrays**: Arrays that can grow or shrink

```c
int *dynamicArray = (int*)malloc(initialSize * sizeof(int));
dynamicArray = (int*)realloc(dynamicArray, newSize * sizeof(int));
```

3. **Trees and Graphs**: Creating nodes dynamically as needed
4. **Stacks and Queues**: Dynamic implementations

## Common Errors and Best Practices

### Common Errors:

1. **Memory Leaks**: Forgetting to call free()

```c
// BAD
void function() {
 int *p = malloc(100);
 // ... use p ...
 return; // Memory leak! free() not called
}
```

2. **Dangling Pointers**: Using pointer after free()

```c
// BAD
free(ptr);
*ptr = 5; // Accessing freed memory
```

3. **Double Free**: Freeing the same memory twice

```c
// BAD
free(ptr);
free(ptr); // Undefined behavior
```

### Best Practices:

1. **Always check return value**

```c
int *ptr = (int*)malloc(size);
if (ptr == NULL) {
 // Handle error
}
```

2. **Set pointer to NULL after free**

```c
free(ptr);
ptr = NULL;
```

3. **Match every malloc/calloc with a free**

4. **Use sizeof() for portability**

```c
int *p = (int*)malloc(n * sizeof(int)); // Good
int *p = (int*)malloc(n * 4); // Bad - assumes int is 4 bytes
```

## Complete Example

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
 int n, i;
 int *arr;

 printf("Enter size: ");
 scanf("%d", &n);

 // Allocate array using calloc
 arr = (int*)calloc(n, sizeof(int));
 if (arr == NULL) {
 printf("Memory allocation failed\n");
 return 1;
 }

 // Input values
 for (i = 0; i < n; i++) {
 arr[i] = i + 1;
 }

 // Resize array
 printf("Enter new size: ");
 scanf("%d", &n);
 arr = (int*)realloc(arr, n * sizeof(int));
 if (arr == NULL) {
 printf("Reallocation failed\n");
 return 1;
 }

 // Free memory
 free(arr);
 arr = NULL;

 return 0;
}
```

## Exam Tips

1. Understand the syntax and return types of all four functions
2. Know the differences between malloc and calloc
3. Remember that malloc returns void\* (needs typecasting in C++)
4. Understand when to use each function
5. Be able to identify memory leaks and dangling pointers in code
6. Practice writing code that creates and manipulates dynamic data structures
