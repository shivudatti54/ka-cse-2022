# Operator Overloading - Summary

## Key Definitions and Concepts

- **Operator Overloading**: Redefining the functionality of existing operators when applied to user-defined data types (classes)
- **Unary Operators**: Operators working on single operand (++, --, -, !)
- **Binary Operators**: Operators working on two operands (+, -, \*, /, ==, <, etc.)
- **Friend Function**: A non-member function with special access to private members, often used for operator overloading

## Important Formulas and Theorems

- **Syntax**: `return_type operator op(arguments)`
- **Complex Multiplication**: (a+bi)(c+di) = (ac-bd) + (ad+bc)i
- **Complex Division**: (a+bi)/(c+di) = ((ac+bd) + (bc-ad)i)/(c²+d²)

## Key Points

- Four operators cannot be overloaded: `::`, `.*`, `.`, `?:`
- At least one operand must be user-defined type
- Precedence and associativity cannot be changed
- Prefix ++ returns reference, postfix ++ returns by value (with dummy int parameter)
- Stream operators (<<, >>) must be friend functions
- Assignment operator needs overloading for classes with dynamic memory
- Arithmetic operators typically return class object by value

## Common Mistakes to Avoid

- Forgetting to return appropriate type (not returning \*this for assignment operators)
- Confusing prefix and postfix increment implementations
- Not handling self-assignment in assignment operator (not checking `this != &obj`)
- Attempting to overload operators for built-in types only
- Creating new operators that don't exist in C++

## Revision Tips

- Practice writing complete classes with multiple overloaded operators
- Memorize the four unoverloadable operators for exam
- Understand when to use friend functions vs member functions
- Remember: left operand is implicit object for member functions
- Review examples of complex numbers and string classes for pattern
