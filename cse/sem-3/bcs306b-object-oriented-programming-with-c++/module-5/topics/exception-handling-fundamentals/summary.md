# Exception Handling Fundamentals - Summary

## Key Definitions and Concepts

- **Exception**: An object thrown to signal an error condition during program execution
- **Throw**: Keyword used to signal that an exceptional condition has occurred
- **Try block**: Code block that contains potentially risky operations to monitor for exceptions
- **Catch block**: Handler that processes specific types of exceptions
- **Stack unwinding**: Process of destroying local objects as exceptions propagate up the call stack
- **Rethrowing**: Propagating a caught exception to an outer handler using `throw;`

## Important Formulas and Theorems

- Exception hierarchy: `std::exception` → `std::runtime_error`, `std::logic_error`
- Custom exception creation: `class MyException : public runtime_error { public: MyException(const string& msg) : runtime_error(msg) {} }`

## Key Points

- Exception handling separates error detection from error handling, improving code organization
- The `try-catch` block structure allows graceful error recovery without program termination
- Catch blocks are examined sequentially; first matching handler executes
- Always catch exceptions by reference to avoid object slicing
- Standard exceptions like `runtime_error`, `logic_error`, `out_of_range`, and `invalid_argument` cover common error scenarios
- Stack unwinding ensures destructors of local objects are called, maintaining RAII principles
- The `catch(...)` handler catches all exceptions not matched by specific handlers
- The `what()` virtual method provides error description strings for debugging
- Functions marked `noexcept` will call `std::terminate` if they throw

## Common Mistakes to Avoid

- Placing more general catch handlers before specific ones, causing unreachable code
- Catching exceptions by value instead of by reference, leading to object slicing
- Forgetting that throwing destroys the current execution context before catch is found
- Using old-style dynamic exception specifications (deprecated in modern C++)
- Swallowing exceptions silently without logging or rethrowing when appropriate

## Revision Tips

1. Practice writing try-catch blocks with multiple catch handlers in different orders
2. Memorize the standard exception class hierarchy and their purposes
3. Understand the sequence: throw → stack unwinding → catch handler search → execution
4. Review how exceptions interact with constructors and destructors
5. Solve previous year university exam questions on exception handling to understand the expected answer pattern
