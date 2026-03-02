# Pointers - Summary

## Key Definitions and Concepts

- POINTER: A variable that stores the memory address of another variable
- POINTER DECLARATION: `data_type *pointer_name;` indicates the type of data the pointer can reference
- ADDRESS-OF OPERATOR (&): Returns the memory address of a variable
- INDIRECTION/DEREFERENCE OPERATOR (*): Accesses the value stored at the address contained in a pointer
- VOID POINTER (void *): Generic pointer type that can hold any data type address
- DYNAMIC MEMORY ALLOCATION: Runtime memory allocation using malloc() and free()

## Important Formulas and Techniques

- Pointer declaration: `int *ptr;`
- Initialize with address: `ptr = &variable;`
- Access value through pointer: `*ptr` or `ptr[i]`
- Pointer arithmetic: `ptr + n` moves n elements forward
- Dynamic array: `int *arr = (int *)malloc(n * sizeof(int));`
- Pass by reference: `function(&variable);` with parameter type `int *param`

## Key Points

- Every pointer has a specific type that determines how pointer arithmetic is performed
- Array name is a constant pointer to the first element; arrays and pointers are closely related but NOT identical
- Pointer arithmetic automatically scales by the size of the pointed-to data type
- Uninitialized pointers contain garbage values and must be initialized before use
- Pass-by-reference in C is achieved by passing pointers to variables
- malloc() returns NULL on failure; always check for this
- Each malloc() must have a corresponding free() to prevent memory leaks
- A pointer to pointer (int **ptr) creates multiple levels of indirection

## Common Mistakes to Avoid

- Declaring pointers incorrectly: `int *a, b;` makes only 'a' a pointer
- Dereferencing NULL pointers causes program crashes
- Forgetting to free dynamically allocated memory
- Using pointers to local variables after the function returns (dangling pointers)
- Assuming pointer arithmetic works in bytes rather than elements

## Revision Tips

- Practice declaring pointers for different data types including char, float, and custom types
- Trace through code with pointers using actual memory addresses
- Draw memory diagrams showing variables, addresses, and pointer relationships
- Write functions that swap values, find array minimum/maximum using pointers
- Review the relationship between array notation `arr[i]` and pointer notation `*(arr + i)`