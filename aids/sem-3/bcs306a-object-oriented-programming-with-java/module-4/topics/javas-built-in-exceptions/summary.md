# Java's Built-in Exceptions

## Overview

Java provides a hierarchy of built-in exception classes to handle various error conditions, divided into checked and unchecked exceptions. Understanding these exceptions is crucial for effective error handling in Java programming. This topic covers the most common built-in exceptions and their characteristics.

## Key Points

- Java's exception hierarchy is rooted in the `Throwable` class, which has two main subclasses: `Error` and `Exception`.
- Unchecked exceptions are instances of `RuntimeException` or its subclasses, and are typically not handled by the programmer.
- Checked exceptions are instances of `Exception` (excluding `RuntimeException`) and must be handled or declared.
- Common unchecked exceptions include `ArithmeticException`, `NullPointerException`, `ArrayIndexOutOfBoundsException`, `NumberFormatException`, and `ClassCastException`.
- Common checked exceptions include `IOException`, `SQLException`, and `ClassNotFoundException`.

## Important Definitions

- **Checked Exception**: An exception that must be handled or declared in the code.
- **Unchecked Exception**: An exception that is not required to be handled or declared in the code.
- **RuntimeException**: The base class for all unchecked exceptions.

## Key Syntax

```java
try {
 // Code that may throw an exception
} catch (ExceptionType e) {
 // Handle the exception
}
```

## Comparisons

| Feature    | Checked Exceptions          | Unchecked Exceptions                      |
| ---------- | --------------------------- | ----------------------------------------- |
| Handling   | Must be handled or declared | Optional handling                         |
| Check Time | Compile-time                | Runtime                                   |
| Examples   | IOException, SQLException   | NullPointerException, ArithmeticException |

## Exam Tips

- Be familiar with the hierarchy of Java's built-in exceptions and their characteristics.
- Understand the difference between checked and unchecked exceptions, and how to handle them in your code.
- Focus on recognizing and handling common exceptions such as `NullPointerException`, `ArithmeticException`, and `IOException`.
