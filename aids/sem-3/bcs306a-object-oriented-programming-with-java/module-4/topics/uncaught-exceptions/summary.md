# Uncaught Exceptions - Summary

## Key Definitions

- **Uncaught Exception**: An exception thrown during program execution that is not handled by any catch block in the call chain, causing the JVM's default exception handler to terminate the program.

- **Exception Propagation**: The process by which an exception moves up the call stack from the throwing method to calling methods until either caught or reaching the JVM.

- **Default Exception Handler**: The JVM's built-in handler that executes when an exception propagates uncaught, printing the stack trace and terminating the program.

- **Checked Exceptions**: Exceptions that must be handled at compile time through try-catch or declared with throws; failures result in compilation errors.

- **Unchecked Exceptions**: Runtime exceptions and errors that can propagate without declaration; uncaught ones cause runtime failures.

## Important Formulas

There are no specific formulas for this topic, but understanding the exception handling syntax is essential:

```java
try {
 // code that may throw exception
} catch (ExceptionType e) {
 // handler code
}
```

## Key Points

- When an exception is thrown and no catch block matches, it propagates up the call stack to calling methods.

- If no handler is found in the entire call chain, the JVM's default handler terminates the program and prints the stack trace.

- Uncaught checked exceptions cause compilation errors, while unchecked exceptions cause runtime failures.

- The throws keyword only declares that a method may throw exceptions; it does not handle them.

- Exception propagation follows the LIFO (Last In First Out) order of method calls in the stack.

- The stack trace shows the complete path of method calls from main() to the throwing method.

- Even with uncaught exceptions, finally blocks execute before the exception propagates further.

## Common Mistakes

1. **Confusing throws with catch**: Students often think that adding `throws` in the method signature handles the exception, but it only propagates it.

2. **Forgetting checked exception requirements**: Failing to handle or declare checked exceptions results in compilation errors, not runtime issues.

3. **Catching exceptions in wrong order**: Placing a general Exception catch before specific ones prevents the specific handlers from executing.

4. **Assuming all exceptions are caught**: Not every exception is caught—unchecked exceptions without proper handlers become uncaught.

5. **Ignoring exception propagation**: Not considering that exceptions thrown in called methods must be handled either in those methods or in calling methods.
