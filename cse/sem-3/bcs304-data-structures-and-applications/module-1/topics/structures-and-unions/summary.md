# Structures and Unions

## Overview

Structures in C allow grouping variables of different types under a single name, while unions enable storing different types of data in the same memory location. Understanding these concepts is crucial for building complex data structures like linked lists, trees, and graphs. Structures are the foundation for organizing related data items into a single unit, and unions are used for conserving memory by storing one of several possible types.

## Key Points

- Structures are declared using the `struct` keyword and can contain members of different data types.
- Each structure variable has its own copy of all members, and members are accessed using the dot operator (.) or arrow operator (->) for pointers.
- `typedef` can be used to create an alias for a structure type, simplifying declarations.
- Nested structures are allowed, where a structure can contain another structure as a member.
- Arrays of structures can be used to store collections of records.
- Self-referential structures contain a pointer to their own type, forming the basis for linked lists, trees, and graphs.
- Unions are declared using the `union` keyword and allow storing different types of data in the same memory location, with all members sharing the same memory.

## Important Definitions

- **Structure**: A user-defined type that groups variables of different types into one unit.
- **Union**: A user-defined type where all members share the same memory location.
- **Self-referential structure**: A structure that contains a pointer to its own type.
- **Padding**: The compiler inserts unused bytes between structure members to align them to memory boundaries for faster access.

## Key Formulas / Syntax

- `struct StructureName { type member1; type member2; };`
- `union UnionName { type member1; type member2; };`
- `typedef struct { type member1; type member2; } AliasName;`

## Comparisons

| Feature | Structure                              | Union                             |
| ------- | -------------------------------------- | --------------------------------- |
| Memory  | Each member has its own memory         | All members share the same memory |
| Size    | Sum of all members (+ padding)         | Size of the largest member        |
| Access  | All members can be used simultaneously | Only one member at a time         |

## Exam Tips

- Focus on structure declaration syntax, including the semicolon after the closing brace.
- Understand the difference between dot (.) and arrow (->) operators for accessing structure members.
- Be prepared to calculate the size of structures and unions, considering padding effects.
- Explain the concept of self-referential structures and their connection to linked lists.
- Compare structures and unions, highlighting their differences in memory allocation and access.
- Practice passing structures to functions by value and by reference, and understand the efficiency implications.
