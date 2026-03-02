# Exception Handling in C++ - Summary

## Key Definitions and Concepts

- **Exception**: An abnormal condition or runtime error that disrupts the normal flow of program execution
- **Exception Handling**: A mechanism to detect and respond to runtime errors without terminating the program
- **Throw**: The keyword used to signal that an exceptional condition has occurred
- **Try Block**: A block of code that may throw exceptions and is followed by catch handlers
- **Catch Block**: Code that handles specific types of exceptions
- **Stack Unwinding**: Process of destroying local objects as exceptions propagate up the call stack
- **noexcept**: Specifier indicating a function will not throw exceptions

## Important Formulas and Theorems

Exception handling syntax follows this pattern:
```cpp
try {
    // Code that may throw
} catch (exception_type1) {
    // Handle exception_type1
} catch (exception_type2) {
    // Handle exception_type2
} catch (...) {
    // Handle any other exception
}
```

Custom exception class pattern:
```cpp
class CustomException : public std::exception {
    const char* what() const noexcept override {
        return "Custom error message";
    }
};
```

## Key Points

- Exception handling separates error detection from error handling, improving code organization
- Always catch exceptions by const reference to prevent object slicing
- Place more specific catch blocks before general ones; the catch-all `...` must be last
- Uncaught exceptions call `std::terminate()` which invokes `std::abort()`
- Throwing from destructors during stack unwinding calls `std::terminate()`
- Standard exception hierarchy: `std::exception` → `runtime_error`/`logic_error`
- Use `throw;` for rethrowing and `throw e;` for throwing new copies
- The `noexcept` specifier enables optimizations but violations terminate the program

## Common Mistakes to Avoid

1. Placing a semicolon after catch blocks (e.g., `catch (...) { };`)
2. Catching exceptions by value instead of by reference (causes object slicing)
3. Putting catch-all handler before specific handlers (compilation error)
4. Using exceptions for flow control instead of error handling
5. Throwing raw integers or char* instead of proper exception objects

## Revision Tips

1. Practice writing complete programs with nested try-catch blocks
2. Create custom exception classes and use them in realistic scenarios
3. Trace through code with exceptions to understand stack unwinding
4. Memorize the standard exception hierarchy and when to use each type
5. Review previous year question papers to understand exam patterns
6. Focus on the "throw by value, catch by reference" principle
7. Understand the difference between logic errors and runtime errors