# Structure Initialization

## Overview

Structure initialization assigns values to member variables either at declaration or later. Multiple initialization methods exist, from simple braced lists to designated initializers, enabling flexible setup of complex data types and data structure nodes.

## Key Points

- **Declaration-Time Initialization**: Using braces `struct Student s = {101, "John", 85.5};` sets all members
- **Designated Initializers**: C99 feature `.member = value` allows explicit member specification
- **Partial Initialization**: Unspecified members automatically set to zero for numeric types
- **Zero Initialization**: `struct Student s = {0};` sets all members to zero/NULL
- **Separate Assignment**: Can assign members individually using dot operator after declaration
- **Array of Structures**: Initialize multiple structure instances using nested braces
- **Nested Structures**: Initialize hierarchically with multiple levels of braces

## Important Concepts

- Order matters in non-designated initialization matching member declaration order
- typedef simplifies syntax by removing need for struct keyword
- Dynamic structures initialized after malloc using individual member assignment
- Self-referential structures require proper pointer initialization to NULL
- Common pattern: initialization function creates and returns pointer to new structure
- Best practice: always initialize pointers to NULL to avoid dangling pointers

## Notes

- Practice all initialization methods for exam preparation
- Understand difference between initialization at declaration vs assignment
- Remember uninitialized members default to zero in global/static context
- Know when to use designated initializers for clarity and flexibility
- Be able to write initialization code for linked list nodes and tree nodes
