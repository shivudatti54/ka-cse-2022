# Structures and Unions - Summary

## Overview

Structures (struct) and unions are user-defined data types in C that enable grouping of heterogeneous data elements. While structures allocate separate memory for each member, unions share memory among members. These constructs are fundamental for representing complex real-world entities and implementing dynamic data structures.

## Key Concepts

### Structure Fundamentals
- **Definition**: `struct tag { members; };` creates a composite type
- **Variable Declaration**: Can declare during or after definition
- **Member Access**: Dot operator (.) for variables, arrow operator (->) for pointers
- **Initialization**: Order-based or designated initializers (C99)

### Memory Considerations
- Structures allocate contiguous memory for all members
- Padding/alignment may increase actual size beyond simple sum
- `sizeof(struct)` returns total memory allocated
- `__attribute__((packed))` removes padding (GCC)

### Advanced Features
- **Nested Structures**: Structures containing other structures
- **Arrays of Structures**: Collection of structure instances
- **Self-Referential Structures**: Pointers to same type—basis for linked lists
- **typedef**: Simplifies syntax: `typedef struct { ... } Name;`

### Unions
- All members share the same memory address
- Size equals largest member's size
- Only one member should be accessed at a time
- Useful for: variant types, hardware registers, memory-efficient storage

## Important Formulas and Proofs

**Arrow Operator Equivalence:**
```
ptr->member ≡ (*ptr).member
```

**Union Size:**
```
sizeof(union) = sizeof(largest_member)
```

**Structure Size (with padding):**
```
Actual size ≥ Sum of all member sizes
Size determined by alignment requirements
```

## Common Operations

| Operation | Syntax |
|-----------|--------|
| Access member | `struct_var.member` |
| Access via pointer | `ptr->member` |
| Member of nested struct | `outer.inner.member` |
| Array element member | `array[i].member` |

## Notes

- Always use meaningful structure and member names
- Prefer designated initializers for clarity
- Remember that structure assignment copies all members
- Use unions when members are mutually exclusive
- Self-referential structures require pointers
- Typedef eliminates need for `struct` keyword in declarations
- Practice with real-world entity modeling (student, employee, point)