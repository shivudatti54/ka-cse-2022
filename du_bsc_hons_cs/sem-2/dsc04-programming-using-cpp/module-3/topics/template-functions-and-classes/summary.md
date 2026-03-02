# Template Functions and Classes - Summary

## Key Definitions and Concepts

- **Template:** A C++ feature enabling generic programming by writing code that works with multiple data types without duplication.
- **Generic Programming:** Writing reusable, type-agnostic code where the same logic applies to different data types.
- **Template Function:** A family of functions defined with template parameters, allowing the same function to operate on different types.
- **Template Class:** A generic class definition where type is parameterized, enabling creation of type-safe containers.
- **Template Specialization:** Providing custom implementation for specific types when the generic version doesn't suit.
- **Template Argument Deduction:** Compiler's automatic inference of template types from function arguments.

## Important Formulas and Theorems

- **Function Template Syntax:** `template <typename T> return_type func_name(params);`
- **Class Template Syntax:** `template <typename T> class ClassName { };`
- **Non-type Parameter:** `template <typename T, int N>` (must be compile-time constant)
- **Default Template Argument:** `template <typename T = int>`
- **Full Specialization:** `template <> class ClassName<SpecificType> { };`

## Key Points

1. Templates provide compile-time polymorphism, generating type-specific code during compilation.

2. Both `typename` and `class` are equivalent for declaring type template parameters.

3. Class templates require explicit type specification during instantiation (e.g., `Stack<int>`), while function templates can deduce types automatically.

4. Non-type template parameters must be integral types, pointers, or references—never floating-point values.

5. Default template arguments can be specified for both type and non-type parameters.

6. Template specialization allows customized behavior for specific types while keeping the generic implementation for others.

7. All template code must be visible to the compiler at the point of instantiation—typically placed in header files.

8. Templates have zero runtime overhead compared to runtime polymorphism mechanisms.

## Common Mistakes to Avoid

- Forgetting to specify template parameters when instantiating class templates.
- Attempting to use non-const variables as non-type template parameters.
- Placing template definitions in separate .cpp files instead of header files.
- Confusing partial specialization (class templates only) with full specialization.

## Revision Tips

1. Practice writing template functions for common operations: swap, maximum, minimum, sorting.

2. Implement at least one generic data structure (stack, queue, or linked list) from scratch.

3. Review STL containers to understand real-world template applications.

4. Memorize the syntax pattern: `template <typename T>` comes before every template declaration.

5. Solve previous year DU exam questions on templates to understand the question pattern and marking scheme.