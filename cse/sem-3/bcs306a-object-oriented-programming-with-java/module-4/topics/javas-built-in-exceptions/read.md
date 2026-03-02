# Java's Built-in Exceptions

## Table of Contents

- [Java's Built-in Exceptions](#javas-built-in-exceptions)
- [Introduction](#introduction)
- [Exception Hierarchy](#exception-hierarchy)
- [Common Unchecked Exceptions (RuntimeException)](#common-unchecked-exceptions-runtimeexception)
  - [ArithmeticException](#arithmeticexception)
  - [NullPointerException](#nullpointerexception)
  - [ArrayIndexOutOfBoundsException](#arrayindexoutofboundsexception)
  - [NumberFormatException](#numberformatexception)
  - [ClassCastException](#classcastexception)
- [Common Checked Exceptions](#common-checked-exceptions)
  - [IOException](#ioexception)
  - [SQLException](#sqlexception)
  - [ClassNotFoundException](#classnotfoundexception)
- [Checked vs. Unchecked](#checked-vs-unchecked)
- [Using try-catch-finally Blocks](#using-try-catch-finally-blocks)
- [Using the throws Keyword](#using-the-throws-keyword)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

## Introduction

Java provides a rich hierarchy of built-in exception classes to handle various error conditions. These exceptions are divided into checked and unchecked exceptions. Understanding these exceptions is crucial for effective error handling in Java programming.

## Exception Hierarchy

```java
Throwable
├── Error (Unchecked)
└── Exception
 ├── RuntimeException (Unchecked)
 └── Other Exceptions (Checked)
```

The `Throwable` class is the root of the exception hierarchy in Java. It has two main subclasses: `Error` and `Exception`. The `Error` class represents unchecked exceptions that are typically not handled by the programmer, while the `Exception` class represents checked exceptions that must be handled or declared.

## Common Unchecked Exceptions (RuntimeException)

Unchecked exceptions are instances of `RuntimeException` or its subclasses. They are typically not handled by the programmer and are checked at runtime.

### ArithmeticException

```java
int result = 10 / 0; // Division by zero
```

An `ArithmeticException` is thrown when an arithmetic operation is attempted with an invalid operand, such as dividing by zero.

### NullPointerException

```java
String str = null;
int length = str.length(); // Accessing null object
```

A `NullPointerException` is thrown when an application attempts to use an object reference that has a null value.

### ArrayIndexOutOfBoundsException

```java
int[] arr = new int[5];
int value = arr[10]; // Invalid index
```

An `ArrayIndexOutOfBoundsException` is thrown when an application attempts to access an array element with an index that is outside the bounds of the array.

### NumberFormatException

```java
int num = Integer.parseInt("abc"); // Invalid number format
```

A `NumberFormatException` is thrown when an application attempts to parse a string that is not a valid number.

### ClassCastException

```java
Object obj = new String("Hello");
Integer num = (Integer) obj; // Invalid cast
```

A `ClassCastException` is thrown when an application attempts to cast an object to a class that is not its actual class.

## Common Checked Exceptions

Checked exceptions are instances of `Exception` (excluding `RuntimeException`) and must be handled or declared.

### IOException

```java
import java.io.*;
FileReader file = new FileReader("file.txt"); // Must handle or declare
```

An `IOException` is thrown when an I/O operation fails, such as reading from a file that does not exist.

### SQLException

```java
import java.sql.*;
Connection conn = DriverManager.getConnection(url); // Must handle
```

An `SQLException` is thrown when a database operation fails, such as connecting to a database with an invalid URL.

### ClassNotFoundException

```java
Class.forName("com.example.MyClass"); // Must handle
```

A `ClassNotFoundException` is thrown when an application attempts to load a class that does not exist.

## Checked vs. Unchecked

| Feature    | Checked Exceptions          | Unchecked Exceptions                      |
| ---------- | --------------------------- | ----------------------------------------- |
| Handling   | Must be handled or declared | Optional handling                         |
| Check Time | Compile-time                | Runtime                                   |
| Examples   | IOException, SQLException   | NullPointerException, ArithmeticException |

## Using try-catch-finally Blocks

```java
try {
 // Code that may throw an exception
} catch (ExceptionType e) {
 // Handle the exception
} finally {
 // Code that must be executed regardless of whether an exception is thrown
}
```

## Using the throws Keyword

```java
public void readFile(String filename) throws IOException {
 // Code that may throw an IOException
}
```

## Exam Tips

- Be familiar with the hierarchy of Java's built-in exceptions and their characteristics.
- Understand the difference between checked and unchecked exceptions, and how to handle them in your code.
- Focus on recognizing and handling common exceptions such as `NullPointerException`, `ArithmeticException`, and `IOException`.
- Practice using try-catch-finally blocks and the throws keyword to manage predefined exceptions effectively.

## Key Takeaways

- Java provides a rich hierarchy of built-in exception classes to handle various error conditions.
- Understanding the difference between checked and unchecked exceptions is crucial for effective error handling in Java programming.
- Using try-catch-finally blocks and the throws keyword can help manage predefined exceptions effectively.
- Recognizing and handling common exceptions can improve program stability, security, and user experience.
