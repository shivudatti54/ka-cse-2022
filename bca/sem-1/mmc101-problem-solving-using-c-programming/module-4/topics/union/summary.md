# Union in C Programming - Summary

## Key Definitions and Concepts

- UNION: A user-defined data type that allows storing different data types in the same memory location, where all members share the same memory space
- MEMORY SHARING: All union members occupy the same memory location; writing to one member overwrites others
- TYPE PUNNING: The technique of accessing the same memory location through different member types

## Important Formulas and Theorems

- SIZE OF UNION = SIZE OF LARGEST MEMBER (plus any padding added by compiler)
- Memory address of all union members is the same
- Only one member can contain a valid value at any given time

## Key Points

- Unions use the `union` keyword, similar to `struct` syntax
- All union members share the same memory starting at the same address
- The compiler allocates memory equal to the largest member's size
- Only the first member can be traditionally initialized; use designated initializers (C99) for others
- Unions are ideal for memory-efficient storage of mutually exclusive data
- Common applications include byte extraction, hardware register mapping, and variant data types
- Anonymous unions (C11) allow direct member access without union name when declared inside structures
- Access union members using dot (.) operator for variables and arrow (->) operator for pointers

## Common Mistakes to Avoid

- Accessing a different union member after storing a value leads to garbage values
- Assuming union size equals sum of all member sizes
- Forgetting that writing to any member invalidates other members' values
- Not using the correct access operator (dot vs arrow) based on variable type

## Revision Tips

- MEMORIZE: Union size equals largest member size, not the sum
- PRACTICE: Write programs to extract bytes from integers using unions
- COMPARE: Always contrast unions with structures to understand the fundamental difference
- REMEMBER: Unions share memory; structures allocate separate memory
- UNDERSTAND: Only one union member holds valid data at a time; use a tag/flag to track which member is active