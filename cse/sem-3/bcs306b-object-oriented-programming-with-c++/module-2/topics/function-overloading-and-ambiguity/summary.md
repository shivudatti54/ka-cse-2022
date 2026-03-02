# Function Overloading and Ambiguity - Summary

## Key Definitions and Concepts

- **Function Overloading**: Defining multiple functions with the same name but different parameter lists to perform similar operations on different data types
- **Compile-time Polymorphism**: Another name for function overloading, where the appropriate function is selected during compilation
- **Function Overload Resolution**: The process by which the C++ compiler determines which overloaded function to call based on the arguments provided
- **Ambiguity**: A compilation error that occurs when the compiler cannot uniquely determine which overloaded function to invoke

## Important Rules and Concepts

- Function overloading depends ONLY on parameter list differences (number, type, or order), NOT on return type
- Parameter promotion follows: char/short → int → long → float → double
- Exact matches are preferred, followed by promotion, then standard conversions, and finally user-defined conversions
- Reference parameters cannot accept rvalues (literals, temporaries), while value parameters can

## Key Points

1. Function overloading enables multiple functions with the same name but different parameters
2. The compiler resolves function calls by matching arguments to parameter types through a hierarchical process
3. Ambiguity occurs when multiple overloaded functions are equally good matches for a call
4. Type conversion ambiguity arises when arguments require conversion to multiple parameter types
5. Default arguments combined with overloading can cause ambiguity
6. Reference and value parameters of similar types can create ambiguity
7. Constructor overloading allows creating objects in multiple ways
8. Explicit type casting can resolve ambiguity by guiding the compiler

## Common Mistakes to Avoid

- Assuming that different return types make functions overloaded (this causes compilation error)
- Creating overloaded functions with identical parameter types in the same order
- Combining default arguments with overloaded functions without considering ambiguity
- Passing rvalues (literals) to functions expecting non-const reference parameters
- Confusing function overloading with function overriding (runtime polymorphism)

## Revision Tips

1. Practice identifying whether function calls will be ambiguous before compiling
2. Remember the function resolution hierarchy: exact match → promotion → conversion → user-defined
3. Draw parameter type comparison tables when analyzing ambiguous scenarios
4. Write small test programs to verify your understanding of overload resolution
5. Review previous year questions on this topic for pattern familiarity
