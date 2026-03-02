# Fundamentals of Data Structures in C - Summary

## Key Definitions and Concepts

- PRIMITIVE DATA TYPES: Basic data types in C including int, float, double, and char with specific memory sizes
- ARRAY: A contiguous block of memory storing elements of the same type, accessed via index with O(1) time complexity
- STRUCTURE: A composite data type that groups heterogeneous variables under one name using the struct keyword
- POINTER: A variable that stores the memory address of another variable, enabling dynamic memory management
- LINKED LIST: A linear data structure where nodes contain data and pointers to subsequent (and possibly previous) nodes
- DYNAMIC MEMORY ALLOCATION: Memory requested at runtime using functions like malloc(), calloc(), and realloc()

## Important Formulas and Theorems

- Array element address: base_address + (index × size_of_element)
- Pointer arithmetic: ptr + n moves by n × sizeof(*ptr) bytes
- Structure total size may include padding bytes for alignment
- Linked list node size: sizeof(data) + sizeof(pointer)

## Key Points

1. C provides direct memory access through pointers, making it ideal for implementing low-level data structures

2. Arrays offer O(1) access time but have fixed size, while linked lists grow dynamically at O(1) insertion cost

3. Dynamic memory allocation (malloc/calloc) returns memory from the heap, not the stack

4. Always pair malloc() with free() to prevent memory leaks

5. Structure padding occurs when compilers align data for faster access, affecting total structure size

6. Linked lists eliminate the need for contiguous memory but require traversal for element access

7. Pointers can point to any data type; void pointers work with generic data

8. Array names decay to pointers in most contexts but are not interchangeable with pointers

## Common Mistakes to Avoid

1. FORGETTING TO FREE MEMORY: Always release dynamically allocated memory to prevent leaks

2. POINTER NOT INITIALIZED: Never use uninitialized pointers; always assign valid addresses

3. ARRAY BOUNDS VIOLATION: C does not check array bounds; accessing invalid indices causes undefined behavior

4. CONFUSING STRUCTURE AND POINTER ACCESS: Use . for structures, -> for pointers to structures

5. MEMORY ALLOCATION FAILURE: Always check if malloc() returns NULL before using the pointer

## Revision Tips

1. PRACTICE WRITING CODE: Write programs implementing arrays, structures, pointers, and linked lists from scratch

2. MEMORY DIAGRAMS: Draw memory layouts to understand how data structures are organized internally

3. ANALYZE COMPLEXITY: For each operation (insert, delete, search), determine the time complexity

4. TRACE CODE: Manually trace through pointer manipulations and linked list operations to understand flow

5. COMPARE APPROACHES: Understand when to use arrays versus linked lists based on requirements