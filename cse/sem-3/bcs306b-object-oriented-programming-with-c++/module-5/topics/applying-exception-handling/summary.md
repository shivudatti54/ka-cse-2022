# Applying Exception Handling in C++ - Summary

## Key Definitions and Concepts

- **Exception**: An abnormal condition or error that occurs during program execution, disrupting the normal flow of instructions.
- **Throw**: The keyword used to signal that an exceptional condition has been detected and transfer control to an appropriate exception handler.
- **Try block**: A block of code that contains statements which might throw exceptions.
- **Catch block**: A handler that processes exceptions of a specific type thrown from the corresponding try block.
- **Stack unwinding**: The process of destroying local objects and popping function call stack when an exception propagates.
- **Exception safety**: Guarantees about the state of a program and its objects when an exception is thrown.

## Important Formulas and Theorems

Exception handling follows these key principles:

- **Exception propagation**: When an exception is thrown, the runtime searches catch handlers in order, moving up the call stack until a matching handler is found.
- **Exception matching rules**: A handler matches an exception if the exception type is the same as or derived from the handler's parameter type. Reference and pointer catches can handle derived exceptions without object slicing.
- **Best-match semantics**: The first catch block that can handle the exception type is executed; ordering matters.

## Key Points

- The three essential keywords for exception handling are try, catch, and throw.
- Always catch exceptions by const reference to prevent object slicing.
- Order catch blocks from most specific (derived classes) to most general (base classes).
- Use catch(...) as a last resort handler to catch any unhandled exception.
- User-defined exceptions should derive from std::exception for standard compatibility.
- The noexcept specifier indicates a function will not throw; if it does, std::terminate is called.
- Stack unwinding destroys local objects but not objects allocated on the heap.
- Destructors should never throw exceptions; wrap potential throws in try-catch within destructors.
- Use RAII principles (smart pointers, lock guards) to ensure exception safety.

## Common Mistakes to Avoid

1. **Catching by value instead of reference**: Causes object slicing, losing derived class information.
2. **Wrong catch block ordering**: Placing base class handlers before derived class handlers prevents derived class handlers from executing.
3. **Swallowing exceptions**: Empty catch blocks that silently absorb exceptions without logging or handling.
4. **Throwing raw pointers instead of objects**: Leads to memory management issues; throw by value or use smart pointers.
5. **Throwing exceptions in destructors**: Can cause std::terminate during stack unwinding when another exception is active.

## Revision Tips

1. Practice writing programs with various exception scenarios: division by zero, file operations, out-of-bounds access, and custom exceptions.

2. Draw the call stack and trace exception propagation to understand stack unwinding thoroughly.

3. Memorize the standard exception hierarchy: std::exception → std::logic_error → std::runtime_error.

4. Review previous university question papers to understand the typical exam pattern for exception handling questions.

5. Implement a complete program with custom exception classes to reinforce the concept of user-defined exceptions.
