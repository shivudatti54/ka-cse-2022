# Array of Structures - Summary

## Key Definitions and Concepts

- ARRAY OF STRUCTURES: A data structure that combines arrays and structures, allowing storage of multiple records where each record contains multiple fields of different data types

- STRUCTURE TEMPLATE: A user-defined data type created using the struct keyword that defines the layout of a record containing heterogeneous members

- MEMORY CONTIGUITY: Array of structures stores all elements sequentially in memory, providing efficient cache performance and sequential access

- STRUCTURE PADDING: Compiler-inserted bytes between members for memory alignment, affecting the actual size of structures

## Important Formulas and Theorems

- Total memory = sizeof(struct StructureName) × number of elements

- Array index access: array_name[index].member_name

- Pointer arithmetic: (ptr + i)->member is equivalent to ptr[i].member

- Structure assignment: structName var1, var2; var1 = var2; copies all members

## Key Points

- Array of structures combines the indexing capability of arrays with the record organization capability of structures

- C supports variable-length arrays (VLA) since C99, allowing runtime-sized arrays like struct Student class[n]

- Two methods of member access exist: dot operator (for structure variables) and arrow operator (for pointers to structures)

- When sorting array of structures, entire structure instances can be swapped using assignment operator—no need to swap members individually

- The arrow operator (->) combines dereferencing (*) and member access (.) into a single operation: ptr->member is equivalent to (*ptr).member

- Passing array of structures to functions is efficient when using pointers since no actual copying occurs

- Searching requires comparing target value against specific structure members, not the entire structure

## Common Mistakes to Avoid

- CONFUSING STRUCTURE SIZE WITH MEMBER SUM: Always use sizeof(struct) rather than summing individual member sizes, as padding affects actual size

- FORGETTING ARRAY INDEX STARTS FROM 0: The nth element is accessed using index n-1, a common source of off-by-one errors

- NOT USING AMPERSAND WITH scanf FOR STRUCTURE MEMBERS: When reading values, use &structure_var.member unless member is already an array (strings)

- INCORRECT POINTER ARITHMETIC: Adding 1 to a structure pointer moves by sizeof(struct), not 1 byte

## Revision Tips

- Practice declaring array of structures with different member types (int, float, char arrays)

- Write programs that implement linear search and sorting on array of structures

- Memorize the arrow operator syntax and understand its equivalence to dereference plus dot

- Review structure padding concepts as memory calculation questions are frequently asked in exams

- Solve at least 3-4 complete programs involving student or employee record management