# Inline Functions in C++ - Summary

## Key Definitions and Concepts

- **Inline Function**: A function defined with the `inline` keyword that suggests the compiler replace function calls with the function body at the point of invocation.
- **Inlining**: The compiler optimization technique of substituting function call sites with the actual function code.
- **Code Bloat**: Potential downside of excessive inlining where code size increases significantly.

## Important Formulas and Theorems

There are no specific formulas for inline functions. The concept is based on the principle of **Call Overhead Reduction**: by eliminating function call mechanics (stack operations, jumps, register saving), execution time decreases for frequently called small functions.

## Key Points

- The `inline` keyword is a request to the compiler, not a command; the compiler decides whether to inline.
- Inline functions must be defined in header files for compilation in every translation unit.
- Class member functions defined inside the class are implicitly inline.
- Inline functions provide type safety, unlike preprocessor macros.
- Recursive functions and virtual functions (with dynamic binding) typically cannot be inlined.
- Inline functions are ideal for small, simple functions like getters, setters, and utility functions.
- The compiler ignores inline requests for large functions, functions with static variables, and functions with complex control flow.
- Modern compilers often perform automatic inlining even without the `inline` keyword through whole-program optimization.

## Common Mistakes to Avoid

1. **Defining inline functions in .cpp files**: Inline functions must be in headers so all calling compilation units can see the definition.

2. **Assuming all small functions are automatically inlined**: While modern compilers optimize aggressively, explicit `inline` keyword provides a hint and documents programmer intent.

3. **Using inline for large functions**: This can cause code bloat and may still be rejected by the compiler.

4. **Forgetting that inline is a request**: The compiler may ignore the inline request based on optimization strategies.

## Revision Tips

1. Remember: **Inline = Request, Not Command** — compiler has final say.

2. Recall the key advantage over macros: **Type Safety** — inline functions perform type checking while macros do not.

3. Know where to place inline functions: **Header Files** — required for the compiler to see the definition at each call site.

4. Review when not to inline: **Recursion, Virtual Functions (dynamic), Large Functions, Static Variables**.

5. Practice writing simple inline functions and predicting compiler behavior in exam scenarios.
