# Handling Derived Class Exceptions - Summary

## Key Definitions and Concepts

- **Exception**: An object thrown to indicate an error condition during program execution
- **Exception Hierarchy**: A class inheritance tree with `std::exception` as the root
- **Object Slicing**: Loss of derived class data when catching by value instead of reference
- **Stack Unwinding**: Process of destroying local objects as exceptions propagate up the call stack
- **Rethrowing**: Using `throw;` to propagate the original exception to an outer handler

## Important Formulas and Theorems

- Standard exception hierarchy: `std::exception` → `std::logic_error`, `std::runtime_error`
- Custom exception template: Derive from appropriate standard class and override `what()` method
- Correct catch signature: `catch(const BaseException& e)` - always by const reference

## Key Points

- Always catch exceptions by reference to preserve polymorphic behavior and avoid object slicing
- Order catch blocks from most specific (derived) to most general (base) types
- Virtual functions in caught exceptions exhibit polymorphic behavior
- Use `noexcept` for functions that should never throw exceptions
- Never throw exceptions from destructors - it leads to undefined behavior
- Custom exceptions should derive from the most appropriate standard exception class
- The `what()` method is virtual and returns derived class-specific messages
- Rethrow using `throw;` (no operand) to preserve original exception type

## Common Mistakes to Avoid

- Catching exceptions by value (causes object slicing)
- Placing catch blocks in wrong order (unreachable code)
- Throwing exceptions from destructors
- Using empty catch blocks that silently swallow errors
- Catching by pointer when reference is more appropriate

## Revision Tips

- Practice creating custom exception classes with proper inheritance
- Always visualize the exception hierarchy when designing error handling
- Remember the golden rule: catch by reference, not by value or pointer
- Review the standard exception hierarchy and when to use each type
- Write code with multiple try-catch blocks to understand exception propagation
