# Exception Handling Fundamentals - Summary

## Key Definitions

- **Exception**: An event that disrupts the normal flow of program execution during runtime
- **Exception Handling**: A mechanism to handle runtime errors gracefully without terminating the program
- **Checked Exceptions**: Exceptions that must be declared in method signature or caught explicitly (subclasses of Exception but not RuntimeException)
- **Unchecked Exceptions**: Runtime exceptions that do not require declaration or explicit handling (RuntimeException and its subclasses)
- **Throwable**: The root class of all exceptions and errors in Java
- **Exception Propagation**: The process by which an uncaught exception moves up the call stack

## Important Formulas

- **Exception Hierarchy**: Throwable → {Error, Exception} → RuntimeException → {NullPointerException, ArrayIndexOutOfBoundsException, etc.}
- **Try-Catch Structure**: `try { } catch(ExceptionType e) { } finally { }`

## Key Points

1. Java exception handling uses five keywords: try, catch, throw, throws, and finally

2. The Throwable class is the root of all exceptions, with Error for JVM errors and Exception for application-level issues

3. Checked exceptions must be caught or declared with throws; unchecked exceptions (RuntimeException) do not require either

4. A try block must be followed by at least one catch or finally block

5. Multiple catch blocks should be ordered from most specific to most general exception types

6. The finally block always executes regardless of whether an exception occurs

7. The throw keyword creates and throws an exception object; throws declares exceptions a method might throw

8. If an exception is not caught, it propagates up the call stack until handled or program terminates

9. Best practice is to catch specific exceptions rather than using a generic Exception or Throwable catch

10. Never swallow exceptions silently—always log or handle them appropriately

## Common Mistakes

1. Placing more general exception catch blocks before specific ones (causes compilation error)

2. Forgetting that finally always executes, even after a return statement in try block

3. Using exceptions for flow control instead of handling actual error conditions

4. Catching Exception or Throwable when more specific exception types would be more appropriate

5. Not understanding the difference between throw (action) and throws (declaration)