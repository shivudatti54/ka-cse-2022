# Introduction to Data Structures - Summary

## Key Definitions and Concepts

- DATA STRUCTURE: A specialized format for organizing, processing, and storing data that enables efficient access and modification. It consists of data values, relationships among them, and operations that can be performed.

- PRIMITIVE DATA STRUCTURES: Basic building blocks provided by programming languages that represent single values including INTEGER, FLOAT, CHAR, BOOLEAN, and DOUBLE.

- NON-PRIMITIVE DATA STRUCTURES: Composite data structures constructed from primitive types, further classified into Linear (arrays, linked lists, stacks, queues) and Non-Linear (trees, graphs) structures.

- POINTER: A variable that stores the memory address of another variable, fundamental for implementing dynamic data structures.

- DYNAMIC MEMORY ALLOCATION: Runtime memory allocation from heap using functions like malloc(), calloc(), realloc(), and deallocation using free().

- ABSTRACT DATA TYPE (ADT): A data structure defined by its behavior (operations) rather than implementation details, providing abstraction between interface and actual code.

## Important Formulas and Theorems

- Time Complexity of Array Access: O(1) - constant time for index-based access

- Time Complexity of Linear Search: O(n) - worst case examines all elements

- Time Complexity of Binary Search: O(log n) - requires sorted data

- Time Complexity of Insertion at Beginning: O(n) - requires shifting all elements

- Time Complexity of Insertion at End: O(1) - if size is maintained

## Key Points

- Data structures enable efficient data organization and manipulation in computer programs

- Primitive data types (int, float, char, double, boolean) form the foundation for building complex structures

- Non-primitive data structures are classified into Linear (sequential arrangement) and Non-Linear (hierarchical/network relationships)

- Five fundamental operations exist across most data structures: traversal, insertion, deletion, searching, and sorting

- Pointers store memory addresses and enable dynamic memory management essential for flexible data structures

- Dynamic memory allocation allows programs to use memory efficiently based on runtime requirements

- ADTs separate what a data structure does (interface) from how it does it (implementation)

- Array elements are stored in contiguous memory locations enabling efficient index-based access

- The choice of data structure significantly impacts algorithm performance and resource utilization

## Common Mistakes to Avoid

- Confusing primitive data types with non-primitive data structures (integers are primitive, arrays are non-primitive)

- Forgetting to check for array bounds before insertion or deletion, leading to buffer overflow or underflow errors

- Not freeing dynamically allocated memory, causing memory leaks in programs

- Confusing the address-of operator (&) with the dereference operator (*) when working with pointers

- Assuming all operations on arrays take constant time; insertion and deletion at the beginning are O(n)

## Revision Tips

- Practice writing pointer declarations and understanding memory addresses through diagrams

- Memorize the classification tree of data structures and be able to draw it from memory

- Implement basic array operations (insert, delete, search, traverse) in C to reinforce concepts

- Review dynamic memory allocation examples and trace through code to understand memory flow

- Solve previous year examination questions to familiarize yourself with question patterns and important topics