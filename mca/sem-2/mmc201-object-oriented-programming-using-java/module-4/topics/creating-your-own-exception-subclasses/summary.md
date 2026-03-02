# Creating Your Own Exception Subclasses

## Overview

Creating custom exception subclasses in Java allows for more specific and meaningful error handling. By extending the Exception class, developers can create tailored exceptions that better represent the errors in their application. This approach enhances code readability and maintainability.

## Key Points

- Custom exceptions are created by extending the Exception class.
- A custom exception class should have a constructor that calls the superclass constructor using `super(message)`.
- Custom exceptions can be thrown using the `throw` keyword.
- Custom exceptions are caught using a `try-catch` block, just like built-in exceptions.
- The `getMessage()` method can be used to retrieve the error message associated with the custom exception.
- Custom exceptions should be used to represent specific error scenarios in an application.
- Using custom exceptions improves code readability and maintainability.

## Important Definitions

- **Custom Exception**: A user-defined exception class that extends the Exception class.
- **Checked Exception**: An exception that is checked at compile-time, typically used for recoverable errors.

## Key Formulas / Syntax

- `public class CustomException extends Exception { ... }`
- `throw new CustomException("Error message");`
- `try { ... } catch (CustomException e) { ... }`

## Exam Tips

- Be prepared to create a custom exception class and demonstrate its usage in a `try-catch` block.
- Focus on understanding the benefits of using custom exceptions, such as improved code readability and maintainability.
