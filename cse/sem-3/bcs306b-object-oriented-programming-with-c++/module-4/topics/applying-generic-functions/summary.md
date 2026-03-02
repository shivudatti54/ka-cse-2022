# Applying Generic Functions - Summary

## Key Definitions and Concepts

- **Function Template**: A blueprint for creating functions that operate with different data types while maintaining the same logic.
- **Template Parameter**: A placeholder type (represented by `typename T` or `class T`) that the compiler replaces with actual types during instantiation.
- **Template Instantiation**: The process where the compiler generates actual function code from a template for specific types.
- **Template Argument Deduction**: Automatic determination of template arguments based on function call arguments.

## Important Formulas and Syntax

```cpp
template<typename T> return_type function_name(parameters)
// or
template<class T> return_type function_name(parameters)
```

- Multiple parameters: `template<typename T1, typename T2>`
- Default template arguments: `template<typename T = int>`
- Explicit specification: `function_name<int>(args)`

## Key Points

1. Function templates enable writing type-safe, reusable code without code duplication.

2. The compiler performs type checking at the point of template instantiation, catching errors early.

3. Both `typename` and `class` keywords are interchangeable in template declarations.

4. Template functions support overloading with regular functions - regular functions have higher precedence.

5. Non-type template parameters allow passing compile-time constant values to templates.

6. Template definitions must be visible to the compiler at the point of instantiation (typically in headers).

7. Generic functions work seamlessly with primitive types and user-defined types that support the required operations.

## Common Mistakes to Avoid

1. Using operations in template code that aren't supported by all potential types (e.g., `<` operator for comparison).

2. Forgetting that templates do not compile until instantiated - syntax errors appear only when called.

3. Not providing appropriate default values when template arguments might be ambiguous.

4. Placing template definitions in separate .cpp files instead of header files, causing linking errors.

## Revision Tips

1. Practice writing simple function templates for operations like swap, maximum, minimum, and sorting.

2. Remember the template declaration syntax: `template<typename T>` comes before the function.

3. Understand the difference between explicit and implicit template argument specification.

4. Review how the compiler resolves between multiple function template overloads.

5. Focus on the concept of "write once, use for multiple types" as the core idea of generic functions.
