# Giving Values to Members

## Overview

Assigning values to structure members can be done using the dot operator for regular structure variables or the arrow operator for structure pointers. Understanding member access is essential for manipulating data within structures and implementing data structure operations.

## Key Points

- **Dot Operator Syntax**: `structure_variable.member_name = value;` for direct structure access
- **Arrow Operator Syntax**: `structure_pointer->member_name = value;` for pointer-based access
- **Individual Assignment**: Each member assigned separately using member name
- **Member Access**: Dot operator for stack-allocated structures, arrow for heap-allocated
- **Initialization vs Assignment**: Initialization at declaration uses braces, assignment uses operators
- **String Members**: Use strcpy for character array members, not direct assignment
- **Pointer Equivalence**: `ptr->member` is shorthand for `(*ptr).member`

## Important Concepts

- Dot operator used when working with structure variable directly
- Arrow operator simplifies syntax when working with structure pointers
- Cannot assign entire structure with single statement after declaration
- String member assignment requires string manipulation functions
- Common in dynamic data structures where nodes allocated with malloc
- Arrow operator more common in data structure implementations

## Notes

- Practice using both dot and arrow operators correctly
- Remember strcpy needed for string member assignment, not =
- Understand equivalence between ptr->member and (\*ptr).member
- Know when to use each operator based on whether variable is pointer
- Be able to identify syntax errors in structure member access code
