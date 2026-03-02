# Pointers and Structures - Summary

## Key Definitions and Concepts

- **Pointer to Structure**: A variable that stores the memory address of a structure variable, declared as `struct StructureName *pointerName;`

- **Arrow Operator (->)**: A binary operator that combines dereferencing and member access in a single operation. `ptr->member` is equivalent to `(*ptr).member` but more readable.

- **Self-Referential Structure**: A structure that contains a pointer to another structure of the same type, used for building linked data structures like linked lists.

- **Dynamic Memory Allocation**: Using malloc(), calloc(), or free() to allocate and deallocate memory for structures at runtime rather than compile time.

## Important Formulas and Theorems

- Structure pointer arithmetic: `ptr + n` advances the pointer by n × sizeof(struct StructureName) bytes

- Arrow operator equivalence: `ptr->member` ≡ `(*ptr).member`

- Memory allocation: `ptr = (struct Type *)malloc(sizeof(struct Type));`

## Key Points

- Always use the arrow operator (->) when working with structure pointers for cleaner, error-free code

- Passing structures by pointer is more efficient than pass-by-value, especially for large structures

- Dynamic allocation is essential for creating data structures that can grow and shrink during execution

- Self-referential structures form the foundation for linked lists, trees, and graphs

- Never dereference an uninitialized or NULL pointer—always check allocation success

- Remember to free() dynamically allocated memory to prevent memory leaks

- Structure pointers enable functions to modify the original structure data

- Arrays of structures can be traversed efficiently using pointer arithmetic

## Common Mistakes to Avoid

- Using dot operator without parentheses when dereferencing: always use (*ptr).member or ptr->member

- Forgetting to check for NULL after malloc() and attempting to use the pointer

- Not initializing the next pointer to NULL in self-referential structures, causing infinite loops

- Confusing the structure tag name with the typedef name when declaring pointers

- Attempting to access members through a pointer that doesn't point to valid memory

## Revision Tips

- Practice writing code that creates, manipulates, and frees structure pointers manually

- Trace through linked list examples step-by-step to understand pointer manipulation

- Remember: arrow operator = pointer to structure accessing member (no dereference needed)

- Understand why pass-by-pointer enables modification while pass-by-value does not

- Review the relationship between array names and pointers in the context of structure arrays