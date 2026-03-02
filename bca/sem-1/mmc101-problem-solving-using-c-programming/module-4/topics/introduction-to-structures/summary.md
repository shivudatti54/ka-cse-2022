# Introduction To Structures - Summary

## Key Definitions and Concepts

- **Structure**: A user-defined data type that groups together data items of different types under a single name
- **Structure Member**: Individual data items within a structure, each having a name and data type
- **Structure Tag**: The name given to a structure type (e.g., `struct Student`)
- **Structure Variable**: A variable declared of a structure type that holds actual data
- **Structure Padding**: Bytes added by the compiler between members for memory alignment

## Important Formulas and Theorems

- **Structure Definition Syntax**:
```c
struct tag_name {
    type member1;
    type member2;
};
```

- **Member Access**: `variable_name.member_name`

- **Structure Size**: May be greater than sum of member sizes due to padding; use `sizeof(struct tag_name)` to find actual size

## Key Points

- Structures combine different data types while arrays combine same data types
- The `struct` keyword is used to define a structure
- Members are accessed using the dot (.) operator for regular variables and arrow (->) operator for pointers
- Structures can be initialized using curly braces: `struct Point p = {10, 20}`
- C99 supports designated initializers: `struct Point p = {.x = 10, .y = 20}`
- Structure padding is done for efficient memory access by the CPU
- `typedef` is commonly used to create aliases for structure types
- Structures can be passed to functions either by value or by reference

## Common Mistakes to Avoid

- Forgetting to declare structure variables after defining the structure template
- Using array syntax instead of dot operator for accessing structure members
- Assuming structure size equals sum of member sizes (ignoring padding)
- Trying to compare two structures directly using == operator (not supported in C)
- Confusing structure tag names with variable names

## Revision Tips

1. Practice writing structure definitions for common real-world entities (student, employee, date, complex number)

2. Write programs to input and output structure data to become comfortable with member access

3. Remember that structure members are stored in contiguous memory locations sequentially

4. Review the difference between `struct Student s;` (declares variable) and `struct Student` (refers to type)

5. Solve previous year DU exam questions on structures to understand the exam pattern and difficulty level