# The throw Statement in Java - Summary

## Key Definitions

- **throw**: A Java keyword used to explicitly throw an exception object from within a method or code block, transferring control to the nearest exception handler.

- **throws**: A method modifier that declares which checked exceptions a method might propagate to its calling methods, forming part of the method signature.

- **Unchecked Exception**: Exceptions that extend `RuntimeException` or `Error`; the compiler does not require handling or declaration of these exceptions.

- **Checked Exception**: Exceptions that extend `Exception` but not `RuntimeException`; the compiler enforces handling or declaration of these exceptions.

- **Exception Propagation**: The process by which an uncaught exception moves up the call stack from the throwing method to its callers until a handler is found.

- **Exception Chaining**: The practice of wrapping one exception within another to preserve the full context of an error while transforming it for higher-level handling.

## Important Formulas

```java
// Basic throw syntax
throw new ExceptionClass("error message");

// Throwing with exception chaining
throw new NewException("message", originalException);

// Method declaration with throws
public returnType methodName(parameters) throws ExceptionType1, ExceptionType2 {
    // method body
}
```

## Key Points

1. The `throw` keyword must be followed by a valid exception object created using the `new` operator.

2. Only objects that are instances of `Throwable` or its subclasses can be thrown.

3. Once a `throw` statement executes, no subsequent statements in the same block will execute unless the exception is caught.

4. Unchecked exceptions (RuntimeException subclasses) do not require declaration in the `throws` clause.

5. Checked exceptions must either be caught with try-catch or declared in the method's `throws` clause.

6. Custom exceptions are created by extending `Exception` (for checked) or `RuntimeException` (for unchecked).

7. The `throw` statement differs fundamentally from `throws`: `throw` is an action that throws, while `throws` is a declaration about what might be thrown.

8. Rethrowing an exception preserves the original stack trace information.

9. Multiple exceptions can be thrown sequentially if each is caught and handled before the next throw executes.

## Common Mistakes

1. **Throwing non-exception objects**: Students sometimes attempt to throw primitive values or non-Throwable objects, which causes compilation errors. Remember: only Throwable instances can be thrown.

2. **Confusing throw and throws**: Using `throw` in place of `throws` in method declarations or vice versa results in compilation errors. `throw` is a statement, `throws` is a clause.

3. **Forgetting to declare checked exceptions**: Throwing a checked exception without catching it or declaring it in `throws` causes a compilation error.

4. **Unreachable code after throw**: Placing statements immediately after a `throw` statement without proper try-catch block results in unreachable code warnings or errors.

5. **Throwing generic Exception**: While valid, throwing the generic `Exception` class is considered poor practice; more specific exception types provide better error handling and debugging information.