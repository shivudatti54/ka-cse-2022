# Nested Try Blocks and User-Defined Exceptions - Summary

## Key Definitions and Concepts

- **Nested Try Blocks**: A try block contained within another try block, enabling hierarchical error handling at multiple levels
- **Rethrowing**: Using `throw;` (without operand) to propagate the currently caught exception to an outer handler
- **User-Defined Exceptions**: Custom exception classes created by inheriting from `std::exception` or other standard exception classes
- **Exception Propagation**: The mechanism by which thrown exceptions travel through nested try blocks until caught
- **Stack Unwinding**: The process of destroying local objects as exceptions propagate up the call stack
- **Exception Safety**: Guarantee that resources are properly released even when exceptions occur

## Important Formulas and Theorems

- **Exception Matching Rule**: Exceptions are matched by type; derived class exceptions must be caught before base class exceptions
- **Catch Block Order**: More specific (derived) exception types should be caught before more general (base) types
- **Rethrow Syntax**: `throw;` rethrows current exception; `throw e;` creates new exception (potential slicing)
- ** noexcept Specification**: Functions declared `noexcept` will call `std::terminate()` if they throw

## Key Points

- Nested try blocks allow exceptions to be handled at multiple levels with different strategies
- When an exception is thrown, the runtime searches catch blocks from inside-out
- Always catch exceptions by reference to avoid object slicing: `catch(const exception& e)`
- User-defined exceptions should override the `what()` virtual function
- Rethrowing with `throw;` preserves the original exception object's type and information
- If no matching catch block is found, `std::terminate()` is invoked
- The standard exception hierarchy provides a foundation for custom exceptions
- Stack unwinding ensures proper cleanup of local objects during exception propagation

## Common Mistakes to Avoid

1. **Catching by Value**: Using `catch(Exception e)` causes object slicing; always use references
2. **Wrong Catch Order**: Placing base class catch before derived class catches prevents derived exceptions from being caught properly
3. **Silent Exception Swallowing**: Catching exceptions without handling or rethrowing them
4. **Using `throw e;` Instead of `throw;`**: This creates a new exception object instead of rethrowing the original
5. **Not Providing `what()` Override**: Custom exceptions should override `what()` to return meaningful messages

## Revision Tips

1. **Practice Tracing**: Draw flow diagrams for nested try-catch programs to trace exception paths
2. **Code Examples**: Write and run programs with custom exceptions at different nesting levels
3. **Memory Visualization**: Visualize how stack unwinding works when exceptions propagate
4. **Compare Approaches**: Understand the difference between handling exceptions locally vs. propagating them
5. **Standard Hierarchy**: Memorize the standard exception class hierarchy for exam questions