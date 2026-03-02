# Review of Pointers and Dynamic Memory Allocation

## Overview

Pointers are variables that store memory addresses, enabling direct access to memory and efficient array manipulation. Dynamic memory allocation is a critical concept in data structures, allowing memory requests at runtime from the heap. This summary covers key concepts, syntax, and exam tips for pointers and dynamic memory allocation.

## Key Points

- Pointers store memory addresses of variables, and the `&` operator gets the address of a variable.
- The `*` operator dereferences a pointer, accessing the value at the stored address.
- Pointer arithmetic allows limited operations, such as moving forward or backward by a scaled number of bytes.
- The `->` operator accesses struct members via a pointer, equivalent to `(*ptr).member`.
- Dynamic memory allocation functions include `malloc`, `calloc`, `realloc`, and `free`.
- `malloc` allocates uninitialized memory, while `calloc` allocates zero-initialized memory.
- `realloc` resizes allocated memory, and `free` releases allocated memory.

## Important Definitions

- **Pointer**: A variable that stores the memory address of another variable.
- **Dereference**: Accessing the value stored at the address held by a pointer.
- **Dynamic Memory Allocation**: Requesting memory at runtime from the heap.
- **Dangling Pointer**: A pointer that refers to memory that has already been freed.
- **Memory Leak**: Dynamically allocated memory that is never freed.

## Key Formulas / Syntax

- `data_type *pointer_name;` declares a pointer.
- `int *p = (int *)malloc(5 * sizeof(int));` allocates memory for an array of 5 integers.
- `int *p = (int *)calloc(5, sizeof(int));` allocates zero-initialized memory for an array of 5 integers.
- `p = (int *)realloc(p, new_size);` resizes allocated memory.
- `free(p);` releases allocated memory.

## Comparisons

| Feature             | malloc              | calloc                |
| ------------------- | ------------------- | --------------------- |
| Syntax              | `malloc(size)`      | `calloc(count, size)` |
| Initialization      | No (garbage values) | Yes (all zeros)       |
| Number of arguments | 1                   | 2                     |

## Exam Tips

- Practice writing the syntax for `malloc`, `calloc`, `realloc`, and `free` from memory.
- Understand the difference between `malloc` and `calloc`.
- Be prepared to trace pointer arithmetic problems.
- Know why we set a pointer to `NULL` after calling `free()`.
- The arrow operator (`->`) vs dot operator (`.`) distinction is commonly tested.
- Questions on dynamic allocation of arrays and structures are common in exams.
