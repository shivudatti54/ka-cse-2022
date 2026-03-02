# Functions and Type Casting - Summary

## Key Definitions and Concepts

- **Function:** A self-contained block of code that performs a specific task and can be called from other parts of a program.

- **Function Declaration:** A prototype that tells the compiler about the function name, return type, and parameters.

- **Function Overloading:** Creating multiple functions with the same name but different parameter lists (different number or types of parameters).

- **Recursion:** A programming technique where a function calls itself to solve a problem by breaking it into smaller subproblems.

- **Type Casting:** Converting a value from one data type to another, either implicitly by the compiler or explicitly by the programmer.

## Important Formulas and Theorems

- **Function Signature:** Function name + Parameter types (not return type)
- **Type Promotion Hierarchy:** `bool → char → short → int → long → float → double`
- **static_cast<new_type>(expression):** Compile-time checked explicit conversion
- **dynamic_cast<new_type>(expression):** Runtime-safe downcasting in polymorphic hierarchies

## Key Points

1. Functions promote code reusability, modularity, and cleaner organization of programs.

2. Pass-by-value creates a copy (original unchanged), pass-by-reference uses an alias (original modifiable), pass-by-pointer uses addresses (original modifiable via dereferencing).

3. Function overloading resolves calls at compile-time based on argument types matching parameter types.

4. Default arguments must be specified from right to left and typically appear in the function declaration.

5. Recursive functions require a base case to terminate; without it, infinite recursion occurs.

6. Implicit conversions happen automatically but may cause data loss; explicit casts make programmer intentions clear.

7. C-style casts like `(int)x` perform multiple conversions at once and are less safe than C++ casts.

8. Use `static_cast` for numeric conversions, `const_cast` for const removal, `reinterpret_cast` for unsafe reinterpreting, and `dynamic_cast` for polymorphic downcasting.

## Common Mistakes to Avoid

- Forgetting the base case in recursive functions, leading to stack overflow
- Casting after integer division instead of before: `static_cast<double>(a/b)` vs `static_cast<double>(a)/b`
- Using C-style casts for potentially unsafe conversions that should use static_cast
- Confusing pass-by-reference with pass-by-value—remember references are aliases, not copies
- Specifying default arguments in both declaration and definition, causing compilation errors

## Revision Tips

1. Practice writing function prototypes and definitions repeatedly until comfortable with syntax.

2. Trace through recursive function calls manually using a call stack diagram to understand execution flow.

3. Remember the thumb rule: cast only one operand to double when performing floating-point division with integers to get accurate results.

4. For exams, memorize which cast operator to use in each scenario: static_cast for numeric/conversions, dynamic_cast for polymorphism, const_cast for const removal.

5. Review previous years' DU question papers to understand the pattern and difficulty level of function and casting questions.