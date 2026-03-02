# Declaring Structures

## Overview

Structure declaration defines a new user-defined data type by specifying the member variables and their types. Proper declaration is the foundation for creating complex data types and implementing data structure nodes in C programming.

## Key Points

- **Basic Syntax**: `struct structure_name { data_type member1; data_type member2; };` defines structure template
- **Variable Declaration**: Structure variables declared as `struct structure_name variable_name;`
- **typedef Shortcut**: `typedef struct { members } TypeName;` eliminates need for struct keyword
- **Tag Name**: Optional structure tag identifies the structure type for later use
- **Member Types**: Can include any valid data type including other structures
- **Self-Referential**: Can contain pointer to same structure type (not direct instance)
- **No Memory Allocation**: Declaration only creates template, no memory allocated until variable created
- **Memory Alignment**: Compiler may insert padding, affecting total structure size

## Important Concepts

- Structure acts as blueprint or template for creating variables
- Multiple variables of same structure type can be declared
- Anonymous structures (without tag) possible when using typedef
- Structure definition typically placed before main or in header files
- Memory allocated only when structure variable is instantiated
- Semicolon required after closing brace of structure definition
- Access members using dot operator (.) or arrow operator (->) for pointers

## Notes

- Understand difference between structure definition and variable declaration
- Practice both traditional and typedef declaration methods
- Remember structure tag is optional but useful for later references
- Know that self-referential structures require pointer members, not direct instances
- Be able to declare structures with various member types including arrays and pointers