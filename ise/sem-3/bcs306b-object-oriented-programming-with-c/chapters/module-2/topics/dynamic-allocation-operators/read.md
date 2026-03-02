# Dynamic Memory Allocation

## Introduction

Dynamic memory allocation is a process that allows programs to request memory from the operating system at runtime. This is in contrast to static memory allocation, where memory is allocated at compile time. Dynamic memory allocation is essential when the amount of data to be stored is not known at compile time.

## Functions for Dynamic Memory Allocation

C provides four library functions for dynamic memory management, defined in the header file `<stdlib.h>`:

1. `malloc()`: Allocates a block of memory of specified size and returns a pointer to the first byte of the allocated space.
2. `calloc()`: Allocates multiple blocks of memory, each of the same size, and initializes all bytes to zero.
3. `realloc()`: Changes the size of previously allocated memory.
4. `free()`: Deallocates previously allocated memory.

### malloc()

Syntax:

```c
void *malloc(size_t size);
```

Example:

```c
int *ptr = (int *)malloc(5 * sizeof(int));
if (ptr == NULL) {
    // Memory allocation failed
}
```

### calloc()

Syntax:

```c
void *calloc(size_t num, size_t size);
```

Example:

```c
int *ptr = (int *)calloc(5, sizeof(int));
// Allocates and initializes 5 integers to zero
```

### realloc()

Syntax:

```c
void *realloc(void *ptr, size_t new_size);
```

Example:

```c
ptr = realloc(ptr, 10 * sizeof(int));
// Resizes the previously allocated memory to 10 integers
```

### free()

Syntax:

```c
void free(void *ptr);
```

Example:

```c
free(ptr);
ptr = NULL; // Good practice to avoid dangling pointers
```

## Differences between Static and Dynamic Memory Allocation

| Feature     | Static Allocation        | Dynamic Allocation             |
| ----------- | ------------------------ | ------------------------------ |
| Memory Size | Fixed at compile time    | Determined at runtime          |
| Lifetime    | Entire program execution | Until explicitly freed         |
| Flexibility | Limited                  | High                           |
| Efficiency  | More efficient           | Less efficient due to overhead |
| Management  | Compiler                 | Programmer                     |

## Common Errors and Best Practices

### Common Errors

1. **Memory Leaks**: Forgetting to free allocated memory.
2. **Dangling Pointers**: Using pointers that point to freed memory.
3. **Buffer Overflow**: Writing beyond allocated memory.
4. **Double Free**: Freeing the same memory block twice.

### Best Practices

1. Always check if memory allocation was successful (i.e., pointer is not NULL).
2. Free allocated memory when no longer needed.
3. Avoid dangling pointers by setting pointers to NULL after freeing.
4. Use `realloc` carefully to avoid data loss.

## Examples

### Example 1: Using malloc and free

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i, *ptr, sum = 0;
    printf("Enter number of elements: ");
    scanf("%d", &n);

    ptr = (int *)malloc(n * sizeof(int));
    if (ptr == NULL) {
        printf("Error! memory not allocated.");
        exit(0);
    }

    printf("Enter elements: ");
    for (i = 0; i < n; ++i) {
        scanf("%d", ptr + i);
        sum += *(ptr + i);
    }

    printf("Sum = %d", sum);
    free(ptr);
    return 0;
}
```

### Example 2: Using calloc and realloc

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr;
    int n, i;

    printf("Enter initial number of elements: ");
    scanf("%d", &n);

    arr = (int *)calloc(n, sizeof(int));
    if (arr == NULL) {
        printf("Memory allocation failed.");
        return 1;
    }

    printf("Enter %d elements:\n", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter new size: ");
    scanf("%d", &n);
    arr = (int *)realloc(arr, n * sizeof(int));
    if (arr == NULL) {
        printf("Memory reallocation failed.");
        return 1;
    }

    printf("Enter %d elements:\n", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Elements are: ");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    free(arr);
    return 0;
}
```

## Exam Tips

- Understand the syntax and usage of `malloc`, `calloc`, `realloc`, and `free`.
- Be able to differentiate between static and dynamic memory allocation.
- Practice writing code that uses dynamic memory allocation and deallocation.
- Be aware of common errors and how to avoid them.
