# Generic Classes in C++ (Templates) - Summary

## Key Definitions and Concepts

- **Class Template**: A blueprint for creating classes where types are specified as parameters, enabling generic programming in C++.

- **Template Parameter**: A placeholder (type or non-type) specified in a template declaration that gets replaced with actual values during instantiation.

- **Template Instantiation**: The process where the compiler generates a concrete class from a template by substituting template arguments.

- **Template Specialization**: Providing a specific implementation of a template for particular types, either full (complete replacement) or partial (selective replacement).

- **Non-Type Template Parameter**: A template parameter that represents a value (typically integral) rather than a type.

## Important Formulas and Theorems

- **Template Declaration Syntax**: `template <class T>` or `template <typename T>`

- **Multiple Parameters**: `template <class T1, class T2, ...>`

- **Default Template Arguments**: `template <class T = int, int SIZE = 100>`

- **Non-Type Parameters**: `template <class T, int N>`

- **Full Specialization**: `template <> class ClassName<SpecificType> { }`

- **Partial Specialization**: `template <class T> class ClassName<T*> { }`

## Key Points

- Class templates enable compile-time polymorphism without runtime overhead, unlike virtual function-based polymorphism.

- Both `class` and `typename` keywords are interchangeable for declaring type template parameters.

- Each unique combination of template arguments creates a distinct class type in the program.

- Member functions of class templates are themselves templates and are instantiated only when called.

- Template specialization allows optimized implementations for specific types (e.g., char pointers).

- Non-type template parameters must be compile-time constants of integral types, pointers, or references.

- The Standard Template Library (STL) extensively uses class templates for containers, iterators, and algorithms.

## Common Mistakes to Avoid

1. **Forgetting template keyword**: When defining member functions outside the class template, always include the `template` prefix.

2. **Incorrect specialization syntax**: Using `template <class T>` instead of `template <>` for full specialization.

3. **Non-type parameter restrictions**: Attempting to use floating-point types as non-type template parameters (not allowed in C++).

4. **Default argument ordering**: Placing default arguments before non-default parameters in template parameter list.

5. **Separation of template files**: Templates typically require inclusion of implementation in header files since instantiation happens at compile-time.

## Revision Tips

1. Practice writing simple class templates first (like Stack, Queue) before moving to complex examples.

2. Memorize the syntax for both full and partial specialization - this is frequently tested in university exams.

3. Understand how the compiler instantiates templates - focus on the "on-demand" compilation concept.

4. Review STL container implementations to see practical applications of class templates.

5. Solve previous year university exam questions on templates to familiarize with question patterns.
