# **Pointers: Introduction and Revision Notes**

### Introduction

- Pointers are a fundamental concept in programming that allow a variable to store the memory address of another variable.
- Pointers are declared using the asterisk symbol (\*) before the pointer variable name.
- The syntax for declaring a pointer variable: `type *pointer_variable_name;`

### Pointer Concepts

- **Dereferencing**: The operation of accessing the value stored at the memory address held by a pointer. `*pointer_variable_name`
- **Pointers to Pointers**: A pointer that holds the address of another pointer. `type \***pointer_variable_name;`
- **Null Pointer**: A pointer that does not point to any valid memory location. `NULL`

### Accessing Variables through Pointers

- **Direct Access**: Assigning a value to a variable through a pointer using the dereference operator (\*). `*pointer_variable_name = value;`
- **Indirect Access**: Accessing the value stored at the memory address held by a pointer using the dereference operator (\*). `pointer_variable_name = value;`

### Pointer Applications

- **Arrays**: Pointers can be used to access and manipulate array elements.
- **Dynamic Memory Allocation**: Pointers are used to allocate and deallocate memory dynamically.
- **String Manipulation**: Pointers are used to manipulate strings in C.

### Dynamic Memory Allocation Functions

- **`malloc()`**: Allocates a block of memory of a specified size. `void *malloc(size_t size);`
- **`calloc()`**: Allocates a block of memory and initializes all bits to zero. `void *calloc(size_t num, size_t size);`
- **`realloc()`**: Resizes a block of memory. `void *realloc(void *ptr, size_t size);`
- **`free()`**: Deallocates a block of memory. `void free(void *ptr);`

### Important Formulas and Definitions

- **`sizeof()`**: Returns the size of a variable or data type in bytes. `sizeof(type);`
- **`address-of()`**: Returns the memory address of a variable. `&variable_name;`
- **`typedef`**: Allows the declaration of new data types. `typedef type alias_name;`

### Theorems and Properties

- **Pointer Arithmetic**: The rules governing pointer arithmetic. `pointer_variable_name + offset = new_pointer_variable_name`
- **Pointer Comparison**: The rules governing pointer comparison. `!=`, `==`
