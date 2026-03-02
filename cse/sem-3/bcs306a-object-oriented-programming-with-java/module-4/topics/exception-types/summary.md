# Exception Types in Java

## Overview

Exception types in Java are categorized under the `Throwable` class, branching into `Error` and `Exception`. Understanding the hierarchy and types of exceptions is crucial for effective error handling. Java differentiates between checked and unchecked exceptions, impacting how they are handled and declared.

## Key Points

- The `Throwable` class is the root of the exception hierarchy.
- `Error` represents JVM-level problems and should generally not be caught.
- `Exception` is checked unless it's a `RuntimeException`, which is unchecked.
- Checked exceptions (e.g., `IOException`, `SQLException`) must be handled or declared.
- Unchecked exceptions (e.g., `NullPointerException`, `ArithmeticException`) are usually programming bugs.
- The compiler enforces handling or declaration of checked exceptions but not unchecked ones.

## Important Definitions

- **Checked Exceptions**: Must be handled (try-catch) or declared (throws).
- **Unchecked Exceptions**: Not enforced by the compiler; usually programming errors.
- **Throwable**: The root class of the exception hierarchy.

## Key Syntax

```java
try {
    // Code that may throw an exception
} catch (ExceptionType e) {
    // Handle the exception
}
```

## Comparisons

| Feature              | Checked Exceptions          | Unchecked Exceptions                      |
| -------------------- | --------------------------- | ----------------------------------------- |
| Compiler Enforcement | Yes                         | No                                        |
| Handling/Declaration | Must be handled or declared | Not required                              |
| Examples             | IOException, SQLException   | NullPointerException, ArithmeticException |

## Exam Tips

- Focus on understanding the hierarchy of exceptions and the difference between checked and unchecked exceptions.
- Be prepared to identify and handle checked exceptions, and recognize common unchecked exceptions as programming errors.
