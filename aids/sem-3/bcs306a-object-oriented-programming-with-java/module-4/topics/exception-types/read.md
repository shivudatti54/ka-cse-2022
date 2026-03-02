# Exception Types in Java


## Table of Contents

- [Exception Types in Java](#exception-types-in-java)
- [Introduction](#introduction)
- [Hierarchy of Exceptions](#hierarchy-of-exceptions)
- [Error Class](#error-class)
- [Exception Class](#exception-class)
  - [Checked Exceptions](#checked-exceptions)
  - [Unchecked Exceptions (RuntimeException)](#unchecked-exceptions-runtimeexception)
- [Key Points](#key-points)
- [Comparison of Checked and Unchecked Exceptions](#comparison-of-checked-and-unchecked-exceptions)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

## Introduction

In Java, exceptions are events that occur during the execution of a program, disrupting the normal flow of instructions. Understanding exception types is crucial for effective error handling and robust programming. All exceptions in Java inherit from `java.lang.Throwable`, which has two main branches: `Error` and `Exception`. In this topic, we will explore the hierarchy of exceptions, the difference between checked and unchecked exceptions, and how to handle them.

## Hierarchy of Exceptions

The `Throwable` class is the root of the exception hierarchy. It has two main branches: `Error` and `Exception`.

```java
Throwable
+-- Error (unchecked - JVM problems)
| +-- OutOfMemoryError
| +-- StackOverflowError
+-- Exception (checked unless RuntimeException)
 +-- IOException
 +-- SQLException
 +-- ClassNotFoundException
 +-- RuntimeException (unchecked)
 +-- NullPointerException
 +-- ArithmeticException
 +-- ArrayIndexOutOfBoundsException
 +-- ClassCastException
 +-- NumberFormatException
```

## Error Class

The `Error` class represents JVM-level problems, such as running out of memory or stack overflow. These errors are usually unrecoverable and should generally not be caught.

```java
// StackOverflowError from infinite recursion
void infinite() {
 infinite();
}
```

## Exception Class

The `Exception` class is the base class for all exceptions that can be thrown by a Java program. It has two main subclasses: `IOException` and `RuntimeException`.

### Checked Exceptions

Checked exceptions are exceptions that are checked by the compiler. They must be either handled (try-catch) or declared (throws). Examples of checked exceptions include `IOException`, `SQLException`, and `ClassNotFoundException`.

```java
// Handling a checked exception
try {
 // Code that may throw an IOException
 File file = new File("example.txt");
 FileInputStream fis = new FileInputStream(file);
} catch (IOException e) {
 // Handle the exception
 System.out.println("Error reading file: " + e.getMessage());
}
```

### Unchecked Exceptions (RuntimeException)

Unchecked exceptions are exceptions that are not checked by the compiler. They are usually programming bugs and should be avoided. Examples of unchecked exceptions include `NullPointerException`, `ArithmeticException`, and `ArrayIndexOutOfBoundsException`.

```java
// Unchecked exception: NullPointerException
String s = null;
s.length(); // NullPointerException

// Unchecked exception: ArrayIndexOutOfBoundsException
int[] a = {1, 2};
a[5] = 10; // ArrayIndexOutOfBoundsException

// Unchecked exception: ArithmeticException
int x = 10 / 0; // ArithmeticException
```

## Key Points

- `Throwable` is the root class of the exception hierarchy.
- `Error` represents JVM-level problems and should generally not be caught.
- `Exception` is checked unless it's a `RuntimeException`, which is unchecked.
- Checked exceptions must be handled (try-catch) or declared (throws).
- Unchecked exceptions are usually programming bugs and should be avoided.

## Comparison of Checked and Unchecked Exceptions

| Feature              | Checked Exceptions          | Unchecked Exceptions                      |
| -------------------- | --------------------------- | ----------------------------------------- |
| Compiler Enforcement | Yes                         | No                                        |
| Handling/Declaration | Must be handled or declared | Not required                              |
| Examples             | IOException, SQLException   | NullPointerException, ArithmeticException |

## Exam Tips

- Focus on understanding the hierarchy of exceptions and the difference between checked and unchecked exceptions.
- Be prepared to identify and handle checked exceptions, and recognize common unchecked exceptions as programming errors.
- Understand how to use try-catch blocks and the throws keyword to handle checked exceptions.

## Key Takeaways

- Understanding exception types is crucial for effective error handling and robust programming.
- The `Throwable` class is the root of the exception hierarchy.
- Checked exceptions must be handled (try-catch) or declared (throws).
- Unchecked exceptions are usually programming bugs and should be avoided.
- The compiler enforces handling or declaration of checked exceptions but not unchecked ones.
