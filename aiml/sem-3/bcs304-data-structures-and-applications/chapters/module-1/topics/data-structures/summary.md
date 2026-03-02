# Data Structures - Summary

## Key Definitions and Concepts

- DATA STRUCTURE: A specialized way of organizing, storing, and managing data in a computer to enable efficient access and modification

- PRIMITIVE DATA STRUCTURES: Basic data types provided by programming languages (int, float, char, double)

- NON-PRIMITIVE DATA STRUCTURES: Complex structures derived from primitive types, further classified into linear (arrays, linked lists, stacks, queues) and non-linear (trees, graphs) categories

- POINTER: A variable that stores the memory address of another variable, essential for dynamic data structures

- DYNAMIC MEMORY ALLOCATION: Allocating memory at runtime using functions like malloc(), calloc(), and realloc()

## Important Formulas and Theorems

- Array element address calculation: ADDRESS(arr[i]) = BASE_ADDRESS + (i × SIZE_OF_ELEMENT)

- Time complexity of array access: O(1) constant time

- Time complexity of linear search: O(n) linear time

- Time complexity of insertion at beginning: O(n) due to element shifting

- Memory for dynamic allocation: total_bytes = number_of_elements × sizeof(data_type)

## Key Points

- Data structures directly impact algorithm efficiency and program performance

- Linear data structures arrange elements sequentially (one-dimensional arrangement)

- Non-linear data structures arrange elements in hierarchical or networked patterns

- Static data structures have fixed sizes determined at compile time, while dynamic data structures can grow and shrink during execution

- Pointers provide the mechanism for creating dynamic data structures and referencing scattered memory blocks

- The choice of data structure depends on the types of operations required and their frequency

- Arrays offer O(1) access time but O(n) insertion/deletion time

- Linked structures offer O(1) insertion/deletion time (at known positions) but O(n) access time

## Common Mistakes to Avoid

- Confusing primitive data types with primitive data structures—data structures are more complex organizational forms

- Forgetting to free dynamically allocated memory, leading to memory leaks

- Assuming arrays are always superior; the "best" structure depends on specific requirements

- Neglecting to consider space complexity alongside time complexity when evaluating data structures

- Misunderstanding pointer arithmetic, especially in multi-dimensional arrays

## Revision Tips

- Practice drawing memory layouts for arrays and pointer chains to build visual understanding

- Memorize the time complexities of basic operations on arrays and linked lists

- Write small C programs to implement dynamic memory allocation and pointer operations

- Create comparison tables listing characteristics of different data structure types

- Solve previous year question papers to understand the examination pattern and important topics