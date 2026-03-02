# Exception Handling in C++ - Summary

## Key Definitions and Concepts

- **Exception**: An unexpected event or error condition during program execution that disrupts normal flow
- **try block**: Code region that monitors for exceptions; must be followed by at least one catch block
- **throw statement**: Creates and transfers an exception object to the exception handling mechanism
- **catch block**: Exception handler that catches specific exception types thrown within corresponding try block
- **Exception hierarchy**: Standard exceptions rooted in `std::exception`, with `std::logic_error` and `std::runtime_error` as major branches
- **noexcept**: Specifier indicating a function will not throw exceptions; violations call `std::terminate()`

## Important Formulas and Theorems

- Exception matching follows "most derived first" rule in catch block order
- If no catch block matches, `std::unexpected()` is called (or program terminates in C++11+)
- Custom exceptions inherit from `std::exception` and override `what()` method
- `catch(...)` catches all exceptions regardless of type

## Key Points

- Exception handling separates error-handling code from normal program logic
- try-catch-throw provides structured error management compared to traditional error codes
- Standard exceptions include: `invalid_argument`, `out_of_range`, `runtime_error`, `overflow_error`, `bad_alloc`
- Catch blocks must be ordered from most specific to most general type
- The ellipsis catch `catch(...)` catches all exception types
- Use `throw;` (rethrow) to propagate caught exceptions further up the call stack
- noexcept guarantees help compiler optimization but require careful design

## Common Mistakes to Avoid

- Placing catch blocks in wrong order (catching base class before derived)
- Using exceptions for flow control instead of error handling
- Forgetting that throw transfers control immediately (no further statements in try execute)
- Not handling all possible exceptions leading to uncaught exceptions
- Catching by value instead of by reference (especially for polymorphic types)

## Revision Tips

1. Practice writing try-catch blocks with multiple catch handlers to understand exception matching
2. Create custom exception classes to understand inheritance relationships
3. Review the standard exception hierarchy diagram regularly
4. Remember: always catch by reference (`const reference` preferred) to avoid object slicing
5. Focus on understanding when to throw, what to throw, and where to catch