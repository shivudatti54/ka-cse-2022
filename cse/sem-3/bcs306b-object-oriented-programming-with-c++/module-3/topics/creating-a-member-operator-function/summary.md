# Creating a Member Operator Function - Summary

## Key Definitions and Concepts

- **Operator Overloading**: Redefining existing operators to work with user-defined data types.
- **Member Operator Function**: An operator function defined as a member of a class, where the left operand is the calling object.
- **Operator Function**: A special function using the `operator` keyword followed by the operator symbol.

## Important Formulas and Theorems

- **Binary Operator Syntax**: `return_type operator+(const ClassName& obj)` - takes one argument
- **Unary Operator Syntax**: `return_type operator--()` - takes no arguments
- **Post-increment Syntax**: `return_type operator++(int)` - dummy int parameter distinguishes from pre-increment

## Key Points

- When an operator is overloaded as a member function, the left operand is the object (`this` pointer) through which it's called.
- Binary operators require one explicit argument; unary operators require no arguments.
- Operators that should be member functions: `=`, `[]`, `()`, `->`.
- Cannot overload: `::`, `.*`, `.`, `?:`, `sizeof`.
- Always check for self-assignment when overloading assignment operator.
- Return `*this` from assignment operator for chaining.
- Use const qualifier for operators that don't modify the object.

## Common Mistakes to Avoid

1. Forgetting the dummy `int` parameter in post-increment/decrement, causing compilation errors.
2. Not checking for self-assignment in assignment operator overload.
3. Using member function when friend function is needed (left operand not class object).
4. Not returning appropriate type for chaining operations.

## Revision Tips

1. Practice writing operator overloading code for at least 3-4 different classes.
2. Remember: member function for binary operators = 1 argument; friend function = 2 arguments.
3. Draw memory diagrams to understand how `this` pointer works in operator functions.
4. Focus on pre/post increment, assignment operator, and arithmetic operators as these are most frequently asked in university exams.
5. Review previous year university questions on operator overloading to understand the pattern.
