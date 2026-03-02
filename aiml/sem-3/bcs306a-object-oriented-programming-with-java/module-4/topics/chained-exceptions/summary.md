# Chained Exceptions in Java - Summary

## Key Definitions and Concepts

- **Chained Exception**: A mechanism that links one exception to another, preserving the complete error history from the original cause to the final exception thrown to the caller.

- **Exception Chaining**: The process of catching a low-level exception and throwing a higher-level exception while preserving the original exception as the cause.

- **Root Cause**: The original exception that initiated the chain of exceptions in a program.

## Important Formulas and Methods

- **`initCause(Throwable cause)`**: Sets the cause of the invoking exception; can only be called once and returns a reference to the exception.

- **`getCause()`**: Returns the cause of the exception, or null if the cause has not been set.

- **Chained Constructors**: `Exception(String message, Throwable cause)` - preferred method for creating chained exceptions in a single step.

- **`printStackTrace()`**: Automatically prints the complete exception chain including all causes.

## Key Points

- Exception chaining preserves debugging information across multiple layers of an application.

- The `initCause()` method works with any Throwable object and allows setting cause after object creation.

- Chained exception constructors (like `new Exception(msg, cause)`) are the recommended approach in modern Java.

- Each exception in the chain can have its own stack trace showing where that specific exception occurred.

- Exception chaining is particularly useful in servlet-JSP-EJB-database layered architectures.

- Custom exceptions should provide constructors accepting a Throwable cause parameter.

- The cause chain can be traversed using a while loop with `getCause()` until null is returned.

## Common Mistakes to Avoid

- Forgetting to chain exceptions when catching and re-throwing, losing the original error information.

- Calling `initCause()` on an exception that already has a cause set, which throws `IllegalStateException`.

- Not providing a way to set the cause in custom exception classes, limiting their usefulness.

- Over-chaining exceptions where simple handling would suffice, making code unnecessarily complex.

## Revision Tips

- Remember: Use `initCause()` when you need to set cause after exception creation; use chained constructors for new exception creation.

- Practice tracing exception chains by hand: identify the original cause, the intermediate exceptions, and the final thrown exception.

- Review the concept with the stack trace output - notice how each exception shows its own stack trace and "Caused by" sections.

- Focus on the difference between checked and unchecked exceptions when implementing chaining.
