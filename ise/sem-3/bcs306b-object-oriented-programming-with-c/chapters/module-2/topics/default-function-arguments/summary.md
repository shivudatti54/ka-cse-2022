# Default Function Arguments

### Overview

- A default argument in a function is an argument that is assigned a value when the function is called, and it can be used if the argument is not provided.
- The default value is specified after the argument name in the function declaration.
- In C++, default arguments can only be specified for function parameters, not for variables or return types.

### Key Points

- **Definition**: Default argument - an argument with a default value assigned when the function is called.
- **Syntax**: `function_name(argument_name = default_value)`
- **Example**: `int add(int a = 0, int b = 0) { return a + b; }`
- **Importance**: Reduces code duplication and makes functions more flexible.
- **Best Practices**:
  - Use default values for function parameters when they have a meaningful default value.
  - Document default values clearly in function documentation.
  - Avoid using default values for function parameters that are used in conditional statements.

### Important Formulas and Definitions

- **Arbitrary Arguments**: Functions that accept a variable number of arguments.
- **Variable Arguments**: Functions that accept a variable number of arguments using arrays or pointers.
- **Parameter Pack**: A feature that allows passing a list of values to a function.

### Theorems and Rules

- **Rule 1**: Default arguments can only be specified for function parameters, not for variables or return types.
- **Rule 2**: Default arguments must be assigned a value when the function is called.
- **Rule 3**: Default arguments cannot be used in conditional statements.

### Important C++ Concepts

- **Template Metaprogramming**: A technique for generating code at compile-time.
- **SFINAE**: A technique for enabling or disabling function overloading based on template parameters.
