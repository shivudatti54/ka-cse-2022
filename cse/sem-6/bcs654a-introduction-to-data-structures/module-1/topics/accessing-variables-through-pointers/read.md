# Accessing Variables through Pointers

## Introduction

Pointers are fundamental tools in C programming that store memory addresses of variables. They enable **indirect access** to data, providing fine-grained control over memory management – a critical skill for implementing efficient data structures. Understanding pointers is mandatory for dynamic memory allocation, array manipulation, and building complex structures like linked lists and trees.

In 's syllabus, this concept directly supports Module 1 (Arrays) and Module 2 (Linked Lists). Real-world applications include:

- Operating systems development (memory management)
- Game engines (optimized resource handling)
- Embedded systems (direct hardware access)

## Key Concepts

### 1. Pointer Declaration & Initialization

**Syntax:**

```c
data_type *pointer_name; // Declaration
pointer_name = &variable; // Initialization
```

**Components:**

- `data_type`: Type of variable the pointer points to (int, float, etc.)
- `*`: Indirection operator (used in declaration and dereferencing)
- `&`: Address-of operator (returns memory address of a variable)

### 2. Accessing Variables

**Process Flow:**

1. Declare a variable: `int num = 25;`
2. Declare pointer: `int *ptr;`
3. Assign address: `ptr = &num;`
4. Access value: `printf("%d", *ptr);` → Output: 25

### 3. Pointer Arithmetic

Operations are scaled by the size of the data type:

```c
int arr[3] = {10, 20, 30};
int *ptr = arr;

// ptr + 1 moves 4 bytes ahead (for int = 4 bytes)
printf("%d", *(ptr + 1)); // Output: 20
```

### 4. NULL Pointers & Dangling Pointers

- **NULL Pointer:** `int *ptr = NULL;` (Points to address 0)
- **Dangling Pointer:** Pointer pointing to deallocated memory (common in dynamic allocation)

## Examples

### Example 1: Basic Pointer Operations

```c
#include <stdio.h>

int main() {
 int num = 50;
 int *ptr = &num;

 printf("Value via variable: %d\n", num); // Direct access
 printf("Address stored in ptr: %p\n", ptr); // Memory address
 printf("Value via pointer: %d\n", *ptr); // Dereferencing

 *ptr = 75; // Modify value through pointer
 printf("Modified value: %d", num); // Output: 75
 return 0;
}
```

**Memory Diagram:**

```
Variable | Address | Value
num | 0x7ffd | 50 → 75
ptr | 0x7ffc | 0x7ffd
```

### Example 2: Array Traversal with Pointers

```c
#include <stdio.h>

int main() {
 int arr[3] = {10, 20, 30};
 int *ptr = arr; // Equivalent to &arr[0]

 for(int i=0; i<3; i++) {
 printf("Element %d: Address=%p, Value=%d\n",
 i, (ptr + i), *(ptr + i));
 }
 return 0;
}
```

**Output:**

```
Element 0: Address=0x7ffd, Value=10
Element 1: Address=0x7ffd+4, Value=20
Element 2: Address=0x7ffd+8, Value=30
```

### Example 3: Pointer-to-Pointer

```c
#include <stdio.h>

int main() {
 int num = 100;
 int *ptr1 = &num;
 int **ptr2 = &ptr1;

 printf("Value via ptr1: %d\n", *ptr1); // 100
 printf("Value via ptr2: %d\n", **ptr2); // 100
 return 0;
}
```

## Exam Tips

1. **Syntax Focus:** Always declare pointers with `*` and initialize with `&`

- Wrong: `int ptr = &num;` → Missing `*`

2. **Operator Precedence:** `*ptr++` vs `(*ptr)++`

- `*ptr++`: Increment pointer first, then dereference
- `(*ptr)++`: Increment the value being pointed to

3. **Pointer Arithmetic Formula:**

```
New Address = Base Address + (n * sizeof(data_type))
```

4. **Common Question Types:**

- Predict output of pointer manipulation code
- Find errors in pointer declarations
- Calculate addresses in array pointer operations

5. **NULL vs Uninitialized Pointers:**

- Always initialize pointers to NULL if not immediately assigned
- Uninitialized pointers contain garbage addresses (segmentation fault risk)

6. **Pointer Size:** Use `sizeof(ptr)` to get pointer size (4 bytes in 32-bit, 8 bytes in 64-bit systems)

7. **Application Questions:** Be ready to explain how pointers enable linked lists (next node address storage)
