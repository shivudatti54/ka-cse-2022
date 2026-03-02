# Generic Functions in C++ - Summary

## Key Definitions and Concepts

- **Generic Function (Function Template)**: A family of functions defined with template parameters that the compiler instantiates for specific types at compile-time

- **Template Parameter**: A placeholder (using `typename` or `class`) in a template definition that represents a data type

- **Template Instantiation**: The process where the compiler generates a specific function from a function template for a particular type

- **Explicit Specialization**: Providing a specific implementation for a particular type using `template<>`

- **Template Argument Deduction**: The compiler's process of determining template arguments from function call arguments

## Important Formulas and Theorems

The general syntax for a function template is:

```cpp
template<typename T1, typename T2, ...>
return_type function_name(parameters) {
    // function body
}
```

For explicit specification: `function_name<explicit_type>(arguments)`

## Key Points

- Generic functions provide compile-time polymorphism without runtime overhead
- The `typename` and `class` keywords are interchangeable in template declarations
- Template arguments can be explicitly specified when automatic deduction is not possible
- Function templates support overloading with regular functions and other templates
- Explicit specialization uses `template<>` syntax with fully specified types
- Non-type template parameters allow passing compile-time constants as arguments
- Operations used within templates must be defined for the template type

## Common Mistakes to Avoid

- Using uninitialized variables of template type (always initialize with `T()`)
- Assuming all operators work with any type—comparison and arithmetic operators must be defined
- Confusing function template overloading with partial specialization (function templates don't support partial specialization)
- Forgetting that template code is compiled twice: once for template syntax, once during instantiation

## Revision Tips

1. Practice writing simple generic functions (swap, maximum, minimum) until syntax becomes automatic

2. Remember the order of function resolution: exact match → template deduction → conversions

3. Focus on understanding when explicit template argument specification is necessary

4. Review how STL algorithms utilize generic functions as preparation for the next module

5. Solve previous year university exam questions on templates to understand the expected answer format
