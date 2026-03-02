# Template Functions and Template Classes - Summary

## Key Definitions and Concepts

- **Template**: A blueprint that allows the compiler to generate type-specific code automatically
- **Generic Programming**: Writing code that works with multiple data types through templates
- **Template Parameter**: A placeholder (typename or class) that represents a type
- **Template Argument**: The actual type substituted when using the template
- **Template Specialization**: Providing a specific implementation for a particular type
- **Non-type Template Parameter**: A template parameter representing a constant value

## Important Formulas and Techniques

```cpp
// Function template syntax
template <typename T> return_type function_name(params);

// Class template syntax  
template <typename T>
class ClassName {
    // members
};

// Multiple parameters
template <typename T1, typename T2, int size>

// Specialization
template <>
class ClassName<specific_type> { };
```

## Key Points

- Templates provide compile-time polymorphism through code generation
- The `typename` keyword is preferred over `class` for template parameters
- Template instantiation happens at compile time, with no runtime overhead
- Class template member functions defined outside require separate `template` declaration
- Non-type parameters must be integral types or global pointers/references
- Function templates perform automatic type deduction; class templates require explicit arguments
- Template specialization allows custom behavior for specific types

## Common Mistakes to Avoid

1. Forgetting the `template <typename T>` declaration when defining member functions outside the class
2. Confusing template specialization with function overloading — they are different mechanisms
3. Attempting to use non-type parameters with floating-point types (not allowed)
4. Not providing angle brackets `<>` when using class templates with default arguments

## Revision Tips

1. Practice writing complete class templates with all member functions
2. Trace through what code the compiler generates for specific template instantiations
3. Review STL containers to see how templates are used in real-world code
4. Solve previous year examination questions on templates
5. Remember: templates are compile-time mechanisms — no runtime cost for type flexibility