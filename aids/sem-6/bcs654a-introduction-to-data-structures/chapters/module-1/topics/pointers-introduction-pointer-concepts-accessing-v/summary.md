# **Pointers: Introduction and Revision Notes**

### Introduction

- A pointer is a variable that stores the memory address of another variable.
- Pointers allow indirect addressing, enabling efficient use of memory.

### Pointer Concepts

- **Null Pointer**: A pointer that does not point to a valid memory location (e.g., `NULL`).
- **Dereferencing**: Accessing the value stored at the memory address pointed to by a pointer.
- **Pointer Arithmetic**: Performing arithmetic operations on pointers (e.g., incrementing a pointer to move to the next memory location).

### Accessing Variables through Pointers

- To access a variable through a pointer, use the `*` operator: `*pointer = variable_value`.
- To store a variable address in a pointer, use the `&` operator: `pointer = &variable`.

### Pointer Applications

- **Passing Pointers as Arguments**: Passing a pointer to a function to modify the original variable.
- **Returning Pointers from Functions**: Returning a pointer from a function to access modified data.
- **Arrays of Pointers**: Declaring arrays of pointers to store multiple addresses in a single memory location.

### Dynamic Memory Allocation Functions

- **`malloc()`**: Allocates memory on the heap and returns a pointer to the allocated memory block.
- **`calloc()`**: Allocates memory on the heap and initializes all bytes to zero.
- **`realloc()`**: Resizes an existing memory block allocated with `malloc()` or `calloc()`.
- **`free()`**: Releases memory allocated with `malloc()` or `calloc()` from the heap.

Key Formulas and Definitions:

- `&` operator: Address-of operator (e.g., `&x` returns the address of `x`).
- `*` operator: Dereference operator (e.g., `*x` returns the value stored at the address pointed to by `x`).

Important Theorems:

- None specific to pointers.

Revision Tips:

- Practice pointer arithmetic and dereferencing.
- Understand when to use dynamic memory allocation functions.
- Be cautious with null pointers and pointer comparisons.
