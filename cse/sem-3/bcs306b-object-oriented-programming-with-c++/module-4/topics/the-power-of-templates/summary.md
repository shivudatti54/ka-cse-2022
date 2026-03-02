# The Power of Templates - Summary

## Key Definitions and Concepts

- **Template**: A C++ language feature that enables generic programming by allowing code to be written without specifying exact data types.
- **Type Parameter**: A placeholder (typename T or class T) in template definitions that represents an arbitrary type.
- **Template Instantiation**: The process where the compiler generates specific code for a particular type from a template.
- **Template Specialization**: Providing a specific implementation for a particular type, overriding the generic template.
- **Variadic Templates**: Templates that accept a variable number of arguments using parameter packs.

## Important Formulas and Theorems

- **Template Declaration Syntax**: `template<typename T> return_type function_name(parameters)`
- **Multiple Type Parameters**: `template<typename T1, typename T2, typename T3>`
- **Non-type Parameters**: `template<typename T, int size>`
- **Default Template Arguments**: `template<typename T = int>`

## Key Points

1. Templates provide compile-time polymorphism, offering better performance than runtime polymorphism (virtual functions).

2. Both function templates and class templates support generic programming in C++.

3. The compiler performs type checking during template instantiation, ensuring type safety.

4. Template definitions must be visible at the point of instantiation (usually in headers).

5. Function templates support automatic type deduction, while class templates often require explicit type specification.

6. STL containers like vector, stack, queue, and algorithms are all template-based.

7. Partial specialization is only available for class templates, not function templates.

8. Templates enable writing highly reusable, maintainable, and efficient code.

## Common Mistakes to Avoid

1. Placing template implementation in a separate .cpp file instead of header file, causing linker errors.

2. Confusing typename and class keywords - they are interchangeable in template declarations but typename is preferred.

3. Forgetting that template specialization requires the `template<>` syntax with empty parameter list.

4. Using templates with incompatible operators (e.g., trying to compare user-defined types without operator overloading).

5. Not providing default constructors when templates require them for internal operations.

## Revision Tips

1. Write small template programs to reinforce syntax and compilation process.

2. Study STL container implementations to see practical template usage.

3. Compare template-based sorting with type-specific sorting to understand efficiency gains.

4. Practice creating class templates with multiple parameters and default arguments.

5. Review previous year university exam questions on templates for pattern understanding.
