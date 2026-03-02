# Exception Handling Options in C++ - Summary

## Key Definitions and Concepts

- **Exception**: An object or value that signals an error condition during program execution, disrupting the normal control flow.
- **Throw**: The keyword used to signal that an exceptional condition has occurred, creating an exception object and initiating exception handling.
- **Try Block**: A block of code that encloses statements which might throw exceptions and is followed by catch handlers.
- **Catch Block**: A handler that receives and processes exceptions of specific types thrown within the corresponding try block.
- **Exception Safety**: Guarantees regarding program state and resource management when exceptions occur during execution.

## Important Formulas and Theorems

- **Exception Matching Rules**: Catch blocks are evaluated top-to-bottom; first matching handler executes. Base class catch blocks must come after derived class catch blocks.
- **Exception Hierarchy**: std::exception → (std::logic_error, std::runtime_error) → Specific error types (invalid_argument, out_of_range, overflow_error, etc.)
- **noexcept Guarantee**: Functions marked noexcept that throw exceptions result in std::terminate being called.
- **RAII Principle**: Resources are acquired in constructors and released in destructors, ensuring cleanup even when exceptions are thrown.

## Key Points

1. C++ exception handling uses three keywords: try, catch, and throw, providing a cleaner alternative to traditional error handling.

2. Exceptions can be of any type in C++, including primitive types, but using classes (especially standard exception classes) provides more information.

3. The standard exception hierarchy provides a rich set of exception types in <stdexcept> header, with std::exception as the base class.

4. Custom exceptions should inherit from standard exceptions and override the what() method for meaningful error messages.

5. Catching exceptions by reference (preferably const reference) avoids object slicing and unnecessary copying.

6. The noexcept specifier indicates a function will not throw, enabling optimizations and providing guarantees to callers.

7. Exception safety is achieved primarily through RAII, using smart pointers and standard containers that manage resources automatically.

8. The ellipsis catch (catch(...)) catches all exceptions but should generally re-throw the exception after handling.

9. Unhandled exceptions propagate up the call stack and ultimately cause program termination via std::terminate.

10. Re-throwing an exception is done with throw; (without an exception object) in a catch block.

## Common Mistakes to Avoid

- Catching exceptions by value instead of by reference, causing object slicing
- Placing base class catch handlers before derived class handlers, preventing proper polymorphic handling
- Swallowing exceptions with empty catch blocks without any logging or handling
- Throwing raw pointers to dynamically allocated memory without proper ownership management
- Not marking functions that don't throw as noexcept when they could benefit from the guarantee
- Using exception handling for flow control instead of exceptional conditions

## Revision Tips

1. Practice writing try-catch blocks with multiple catch handlers to understand matching rules.

2. Review the standard exception class hierarchy and remember the purpose of each standard exception type.

3. Implement custom exception classes with inheritance to reinforce polymorphism concepts in exception handling.

4. Study RAII principles and how smart pointers provide automatic resource management with exceptions.

5. Remember that catch(...) exists but should typically be followed by re-throwing the exception.

6. Review the distinction between logic errors (detectable before execution) and runtime errors (detectable only during execution).
