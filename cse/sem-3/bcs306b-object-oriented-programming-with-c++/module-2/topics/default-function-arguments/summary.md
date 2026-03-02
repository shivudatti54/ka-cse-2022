# Default Function Arguments - Summary

## Key Definitions and Concepts

- **Default Function Argument**: A value specified in a function declaration that is automatically used when the caller omits the corresponding argument.
- **Right-to-Left Rule**: Default values must be assigned starting from the rightmost parameter toward the left; skipping is not allowed.
- **Ambiguity**: A situation where the compiler cannot distinguish between an overloaded function and a function with default arguments.

## Important Formulas and Theorems

- No mathematical formulas, but key syntax pattern:
  ```
  return_type function_name(type1 param1, type2 param2 = value2, type3 param3 = value3);
  ```
- Defaults are specified in the **declaration** (prototype), not repeated in the **definition**.
- Default values can be constants, global variables, or function call expressions.

## Key Points

- Default arguments allow functions to be called with fewer arguments than defined
- Defaults must follow right-to-left order (no gaps allowed)
- Specify defaults in the declaration, not in the definition when both exist
- Default arguments reduce the need for multiple overloaded functions
- A constructor with all default arguments can act as a default constructor
- Default values are evaluated at each function call, not at declaration time
- Combining default arguments with function overloading may cause ambiguity
- Default arguments were introduced in C++ and are not available in C
- Expressions and function calls can serve as default values
- Cannot skip a middle argument — arguments are matched left to right

## Common Mistakes to Avoid

- **Assigning defaults left-to-right**: `void f(int a = 5, int b)` is INVALID; always go right-to-left
- **Repeating defaults in both declaration and definition**: This causes a compilation error
- **Creating ambiguous overloads**: `void f(int a, int b = 10)` and `void f(int a)` cause ambiguity when called as `f(5)`
- **Trying to skip middle arguments**: `f(5, , 15)` is NOT valid C++ syntax

## Revision Tips

- Practice writing function prototypes with 3-4 parameters and varying default values
- Write a class with a constructor using default arguments and create objects with different numbers of arguments
- Create a comparison table: Default Arguments vs Function Overloading
- Always trace through function calls and write the output manually before compiling
