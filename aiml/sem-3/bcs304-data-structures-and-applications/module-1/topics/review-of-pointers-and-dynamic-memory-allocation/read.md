# Pointers and Dynamic Memory Allocation


## Table of Contents

- [Pointers and Dynamic Memory Allocation](#pointers-and-dynamic-memory-allocation)
- [1. Introduction](#1-introduction)
- [2. Fundamental Concepts](#2-fundamental-concepts)
  - [2.1 Definition and Declaration](#21-definition-and-declaration)
  - [2.2 Initialization Using Address-of Operator](#22-initialization-using-address-of-operator)
  - [2.3 Dereferencing](#23-dereferencing)
  - [2.4 NULL Pointer](#24-null-pointer)
- [3. Pointer Arithmetic](#3-pointer-arithmetic)
  - [Arithmetic Operations](#arithmetic-operations)
- [4. Pointers and Arrays](#4-pointers-and-arrays)
  - [Passing Arrays to Functions](#passing-arrays-to-functions)
- [5. Pointers to Structures](#5-pointers-to-structures)
  - [5.1 Arrow Operator](#51-arrow-operator)
  - [5.2 Self-Referential Structures](#52-self-referential-structures)
- [6. Double Pointers (Pointer to Pointer)](#6-double-pointers-pointer-to-pointer)
  - [Application: Dynamic 2D Arrays](#application-dynamic-2d-arrays)
- [7. Dynamic Memory Allocation](#7-dynamic-memory-allocation)
  - [7.1 malloc() - Memory Allocation](#71-malloc---memory-allocation)
  - [7.2 calloc() - Contiguous Allocation](#72-calloc---contiguous-allocation)
  - [7.3 realloc() - Reallocation](#73-realloc---reallocation)
  - [7.4 free() - Deallocation](#74-free---deallocation)
- [8. Memory Management Pitfalls](#8-memory-management-pitfalls)
  - [8.1 Memory Leaks](#81-memory-leaks)
  - [8.2 Dangling Pointers](#82-dangling-pointers)
  - [8.3 Uninitialized Pointers](#83-uninitialized-pointers)
  - [8.4 Buffer Overflows](#84-buffer-overflows)
- [9. Application: Implementing a Dynamic Stack](#9-application-implementing-a-dynamic-stack)
- [10. Summary of Key Concepts](#10-summary-of-key-concepts)
- [Practice Questions](#practice-questions)
  - [Multiple Choice Questions](#multiple-choice-questions)

## 1. Introduction

Pointers constitute one of the most powerful and distinctive features of the C programming language, enabling direct memory manipulation, efficient array and string operations, and most critically, dynamic memory allocation—a fundamental prerequisite for implementing advanced data structures such as linked lists, stacks, queues, trees, and graphs. A thorough understanding of pointers is therefore essential for any programmer working with data structures and applications.

## 2. Fundamental Concepts

### 2.1 Definition and Declaration

A pointer is a variable that stores the **memory address** of another variable rather than a data value. The data type of a pointer must correspond to the type of data it references, ensuring proper pointer arithmetic and type safety.

**Syntax for pointer declaration:**

```c
data_type *pointer_name;
```

**Examples:**

```c
int *ptr;           /* pointer to integer */
float *fptr;        /* pointer to float */
char *cptr;         /* pointer to character */
struct Node *np;    /* pointer to structure */
```

### 2.2 Initialization Using Address-of Operator

Pointers must be initialized before use. The unary address-of operator (`&`) returns the memory address of its operand:

```c
int x = 25;
int *p = &x;  /* p now holds address of x */
```

**Critical Rule:** Always initialize pointers. Uninitialized pointers contain arbitrary garbage addresses and dereferencing them causes undefined behavior (typically segmentation faults).

### 2.3 Dereferencing

The indirection operator (`*`), when applied to a pointer, accesses the value stored at the address it contains:

```c
int x = 25;
int *p = &x;

printf("Address: %p\n", (void*)p);  /* prints address of x */
printf("Value: %d\n", *p);          /* prints 25 */
*p = 100;                           /* modifies x through pointer */
printf("Modified x: %d\n", x);      /* prints 100 */
```

### 2.4 NULL Pointer

A pointer that does not reference any valid object should be initialized to `NULL` (defined as zero in `<stddef.h>`):

```c
int *p = NULL;
if (p == NULL) {
    printf("Pointer not initialized.\n");
}
```

**Important:** Dereferencing a NULL pointer invokes undefined behavior. Always check for NULL before dereferencing.

## 3. Pointer Arithmetic

C permits limited arithmetic operations on pointers. The arithmetic operations are **scaled** by the size of the pointed-to data type, which is fundamental to array traversal.

**Theorem:** If `p` is a pointer to type `T`, and `sizeof(T)` is `s` bytes, then `p + n` computes the address `p + (n × s)`.

**Proof:** Consider an integer array `int arr[5]` at base address 1000, where `sizeof(int) = 4`. When we execute `p + 1`, the pointer must advance to the next integer element. Since each integer occupies 4 bytes, the address calculation becomes: `1000 + (1 × 4) = 1004`. This ensures that dereferencing `*(p + 1)` correctly accesses `arr[1]`. ∎

### Arithmetic Operations

| Operation     | Effect                                      |
| ------------- | ------------------------------------------- |
| `p + n`       | Advances pointer by n elements              |
| `p - n`       | Moves pointer backward by n elements        |
| `p++` / `++p` | Advances to next element                    |
| `p--` / `--p` | Moves to previous element                   |
| `p2 - p1`     | Returns number of elements between pointers |

```c
int arr[] = {10, 20, 30, 40, 50};
int *p = arr;

printf("%d\n", *p);           /* 10 - first element */
printf("%d\n", *(p + 2));     /* 30 - third element */
printf("%ld\n", p - arr);     /* 0 - offset from base */

p++;                          /* advances to arr[1] */
printf("%d\n", *p);           /* 20 */
```

## 4. Pointers and Arrays

In C, the array name decays to a pointer to its first element. This relationship is fundamental:

```c
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;  /* equivalent to: int *p = &arr[0] */

/* These expressions are equivalent: */
arr[2] == *(arr + 2) == *(p + 2) == p[2]
```

**Theorem:** For any array `arr` and index `i`, the expression `arr[i]` is semantically equivalent to `*(arr + i)`.

**Proof:** The C standard defines array subscripting such that `E1[E2]` is equivalent to `(*((E1) + (E2)))`. When `arr` is used in an expression (except `sizeof` and `&`), it converts to a pointer to the first element. Thus `arr[i]` becomes `*(arr + i)`. ∎

### Passing Arrays to Functions

When arrays are passed to functions, they decay to pointers, enabling two equivalent function signatures:

```c
void processArray(int *arr, int n) { }
void processArray(int arr[], int n) { }  /* equivalent declaration */
```

## 5. Pointers to Structures

Structure pointers are essential for implementing linked lists, trees, and other dynamic data structures.

### 5.1 Arrow Operator

The arrow operator (`->`) provides convenient access to structure members through a pointer:

```c
struct Student {
    char name[50];
    int rollNo;
    float marks;
};

struct Student s1 = {"Alice", 101, 92.5};
struct Student *ptr = &s1;

/* Using arrow operator (preferred) */
printf("Name: %s\n", ptr->name);
printf("Roll: %d\n", ptr->rollNo);

/* Equivalent using dereference */
printf("Name: %s\n", (*ptr).name);
```

**Theorem:** The expression `ptr->member` is equivalent to `(*ptr).member`.

**Proof:** The arrow operator is defined as a syntactic convenience. The expression `ptr->m` is transformed by the compiler to `(*ptr).m`, where the dereference operator `*` obtains the structure object, and the dot operator `.` accesses member `m`. ∎

### 5.2 Self-Referential Structures

The most critical application of structure pointers in data structures is the **self-referential structure**, which contains a pointer to a structure of the same type:

```c
struct Node {
    int data;
    struct Node *next;  /* pointer to next node */
};

struct Node *head = NULL;

/* Creating a new node dynamically */
struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
newNode->data = 25;
newNode->next = NULL;
```

This pattern forms the foundation of linked lists, stacks, and queues implemented dynamically.

## 6. Double Pointers (Pointer to Pointer)

A double pointer stores the address of another pointer, enabling:

- Modification of pointer values within functions
- Dynamic allocation of 2D arrays
- Implementation of linked list operations

```c
int x = 100;
int *p = &x;    /* single pointer */
int **pp = &p;  /* double pointer */

printf("%d\n", **pp);  /* prints 100 - dereference twice */
```

### Application: Dynamic 2D Arrays

Double pointers enable runtime determination of array dimensions:

```c
int rows = 3, cols = 4;
int **matrix = (int**)malloc(rows * sizeof(int*));

for (int i = 0; i < rows; i++) {
    matrix[i] = (int*)malloc(cols * sizeof(int));
}

/* Access elements */
matrix[1][2] = 42;  /* equivalent to *(*(matrix + 1) + 2) */

/* Free memory (reverse order) */
for (int i = 0; i < rows; i++) {
    free(matrix[i]);
}
free(matrix);
```

## 7. Dynamic Memory Allocation

Dynamic memory allocation is the process of allocating memory at runtime rather than compile time, allowing programs to adapt to varying data sizes. The standard library functions `<stdlib.h>` provide four primary allocation functions.

### 7.1 malloc() - Memory Allocation

```c
void* malloc(size_t size);
```

Allocates `size` bytes of uninitialized memory. Returns a `void*` pointer that must be cast to the appropriate type.

**Example: Allocating an integer array of n elements**

```c
int n = 5;
int *arr = (int*)malloc(n * sizeof(int));

if (arr == NULL) {
    fprintf(stderr, "Memory allocation failed\n");
    exit(EXIT_FAILURE);
}

/* Array is allocated but uninitialized */
for (int i = 0; i < n; i++) {
    arr[i] = i * 10;
}
```

### 7.2 calloc() - Contiguous Allocation

```c
void* calloc(size_t nmemb, size_t size);
```

Allocates memory for `nmemb` elements of `size` bytes each and initializes all bytes to zero.

**Example: Allocating and zero-initializing an array**

```c
int n = 5;
int *arr = (int*)calloc(n, sizeof(int));

/* All elements are initialized to 0 */
printf("%d\n", arr[0]);  /* prints 0 */
```

**Theorem:** `calloc(n, s)` is equivalent to `malloc(n * s)` followed by zero-initialization, but `calloc` may be more efficient as it optimizes for zero-filled memory.

### 7.3 realloc() - Reallocation

```c
void* realloc(void *ptr, size_t size);
```

Resizes previously allocated memory block to the new `size`. The function may:

- Return the same pointer if expansion is possible in-place
- Return a new pointer and copy data if relocation is necessary
- Return NULL if reallocation fails (original memory remains valid)

**Example: Expanding a dynamic array**

```c
int *arr = (int*)malloc(5 * sizeof(int));
/* ... populate array ... */

/* Expand to 10 elements */
int *newArr = (int*)realloc(arr, 10 * sizeof(int));

if (newArr == NULL) {
    /* Original arr is still valid */
    free(arr);
    exit(EXIT_FAILURE);
}
arr = newArr;  /* Update pointer */
```

### 7.4 free() - Deallocation

```c
void free(void *ptr);
```

Releases previously allocated memory. The pointer becomes invalid (dangling) after `free()`.

**Critical Rules:**

1. Every `malloc`/`calloc`/`realloc` must have a corresponding `free`
2. Never access memory after freeing it
3. Never free the same pointer twice (double-free)

```c
int *ptr = (int*)malloc(sizeof(int));
*ptr = 100;
printf("%d\n", *ptr);

free(ptr);
ptr = NULL;  /* Good practice: prevent dangling pointer */
```

## 8. Memory Management Pitfalls

### 8.1 Memory Leaks

A memory leak occurs when allocated memory is never freed, causing gradual exhaustion of available memory:

```c
void leakExample() {
    int *ptr = (int*)malloc(sizeof(int));
    *ptr = 42;

    /* Missing: free(ptr); */
    /* Memory leak on function return */
}
```

**Detection and Prevention:**

- Always pair allocation with deallocation
- Use tools like `valgrind` for detection
- Set pointers to NULL after freeing

### 8.2 Dangling Pointers

A dangling pointer references memory that has been freed:

```c
int *ptr = (int*)malloc(sizeof(int));
free(ptr);
/* ptr now points to freed memory - DANGEROUS */
*ptr = 100;  /* Undefined behavior */
```

**Prevention:** Always set pointers to NULL after freeing:

```c
free(ptr);
ptr = NULL;  /* Now safe to check: if (ptr != NULL) */
```

### 8.3 Uninitialized Pointers

```c
int *ptr;      /* uninitialized - contains garbage */
*ptr = 100;    /* Undefined behavior - may crash */
```

**Prevention:** Always initialize pointers:

```c
int *ptr = NULL;           /* initialize to NULL */
int *ptr2 = &existingVar;  /* or point to valid address */
```

### 8.4 Buffer Overflows

Accessing memory beyond allocated bounds can corrupt data or cause security vulnerabilities:

```c
int *arr = (int*)malloc(5 * sizeof(int));
arr[10] = 100;  /* Buffer overflow - undefined behavior */
```

## 9. Application: Implementing a Dynamic Stack

This example demonstrates the practical integration of pointers, structures, and dynamic memory in data structures:

```c
typedef struct {
    int *array;
    int top;
    int capacity;
} Stack;

Stack* createStack(int capacity) {
    Stack *stack = (Stack*)malloc(sizeof(Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->array = (int*)malloc(capacity * sizeof(int));
    return stack;
}

void push(Stack *stack, int item) {
    if (stack->top == stack->capacity - 1) {
        /* Double capacity - demonstration of realloc */
        stack->array = (int*)realloc(stack->array,
                           2 * stack->capacity * sizeof(int));
        stack->capacity *= 2;
    }
    stack->array[++stack->top] = item;
}

void destroyStack(Stack *stack) {
    free(stack->array);  /* Free inner array first */
    free(stack);         /* Then free structure */
}
```

## 10. Summary of Key Concepts

| Concept               | Description                                   |
| --------------------- | --------------------------------------------- |
| Pointer               | Variable storing memory address               |
| & (address-of)        | Operator that returns operand's address       |
| \* (dereference)      | Operator that accesses value at address       |
| Pointer Arithmetic    | Operations scale by `sizeof(type)`            |
| Array-Pointer Duality | Array name decays to pointer to first element |
| `->` Operator         | Access structure members through pointer      |
| `malloc`              | Allocate uninitialized memory                 |
| `calloc`              | Allocate zero-initialized memory              |
| `realloc`             | Resize existing allocation                    |
| `free`                | Deallocate memory                             |
| Memory Leak           | Failure to free allocated memory              |
| Dangling Pointer      | Pointer to freed memory                       |

---

## Practice Questions

### Multiple Choice Questions

**Question 1:** Given `int arr[10]; int *p = arr;`, what is the value of `p` after executing `p += 5` (assuming `sizeof(int) = 4`)?

A) Original address + 5 bytes
B) Original address + 5 × sizeof(int) bytes
C) Original address + 10 bytes
D) Original address + 20 bytes

**Answer:** B) Original address + 5 × sizeof(int) bytes

**Explanation:** Pointer arithmetic automatically scales by the size of the pointed-to type. Adding 5 to an int pointer advances by 5 × 4 = 20 bytes, pointing to arr[5].

---

**Question 2:** Consider the following code:

```c
int **createMatrix(int rows, int cols) {
    int **matrix = (int**)malloc(rows * sizeof(int*));
    for (int i = 0; i < rows; i++) {
        matrix[i] = (int*)malloc(cols * sizeof(int));
    }
    return matrix;
}
```

If we call `int **mat = createMatrix(3, 4);` and subsequently `free(mat);` without freeing the individual rows, what problem occurs?

A) No problem occurs
B) Segmentation fault immediately
C) Memory leak for all row allocations
D) Dangling pointer created

**Answer:** C) Memory leak for all row allocations

**Explanation:** The outer `malloc` for the array of row pointers is freed, but each `matrix[i]` (allocated via inner malloc calls) becomes unreachable—a classic memory leak. The inner arrays cannot be freed after the outer pointer is lost.

---

**Question 3:** What will be the output of the following code?

```c
struct Student {
    int roll;
    char name[20];
};

struct Student s = {101, "Alice"};
struct Student *ptr = &s;

printf("%d, %s\n", ptr->roll, (*ptr).name);
```

A) 101, Alice
B) Compilation error
C) Garbage values
D) 101, (null)

**Answer:** A) 101, Alice

**Explanation:** The arrow operator `ptr->roll` is equivalent to `(*ptr).roll`, and `(*ptr).name` accesses the name member. Both expressions correctly access the structure members, printing "101, Alice".

---

**Question 4:** After executing the following code, what is the value of `x`?

```c
int x = 10;
int *p = &x;
int **pp = &p;
**pp = 20;
```

A) 10
B) 20
C) Address of x
D) Undefined

**Answer:** B) 20

**Explanation:** `pp` points to `p`, which points to `x`. Dereferencing `pp` once gives `p`, and dereferencing again gives `x`. The assignment `**pp = 20` modifies `x` through two levels of indirection.

---

**Question 5:** Which of the following is the MOST likely cause of a segmentation fault in C programs using pointers?

A) Using uninitialized variables
B) Dereferencing a NULL pointer
C) Using malloc with size 0
D) Calling free on a NULL pointer

**Answer:** B) Dereferencing a NULL pointer

**Explanation:** Dereferencing NULL attempts to access memory address 0, which is typically protected by the operating system, causing a segmentation fault. While uninitialized variables can cause issues, NULL dereference is the most direct cause of crashes. Freeing NULL is safe (it becomes a no-op per C standard).

---
