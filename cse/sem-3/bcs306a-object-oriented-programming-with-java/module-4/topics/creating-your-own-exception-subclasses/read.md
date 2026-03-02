# Creating Your Own Exception Subclasses

## Table of Contents

- [Creating Your Own Exception Subclasses](#creating-your-own-exception-subclasses)
- [Introduction](#introduction)
- [Why Create Custom Exceptions?](#why-create-custom-exceptions)
- [Steps to Create a Custom Exception](#steps-to-create-a-custom-exception)
- [Example: Creating a Custom Checked Exception](#example-creating-a-custom-checked-exception)
- [Difference Between Checked and Unchecked Custom Exceptions](#difference-between-checked-and-unchecked-custom-exceptions)
- [Benefits of Using Custom Exceptions](#benefits-of-using-custom-exceptions)
- [Comparison with Java's Built-in Exceptions](#comparison-with-javas-built-in-exceptions)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

=====================================================

## Introduction

---

In Java, exceptions are used to handle runtime errors. While Java provides a range of built-in exceptions, there are cases where you may want to create your own custom exceptions. Custom exceptions allow you to provide more specific and meaningful error messages, making it easier to diagnose and fix problems. In this topic, we will explore how to create your own exception subclasses in Java.

## Why Create Custom Exceptions?

---

Custom exceptions are useful when you want to:

- Provide more specific error messages that are relevant to your application.
- Handle specific error scenarios that are not covered by Java's built-in exceptions.
- Improve code readability and maintainability by providing clear and concise error messages.

## Steps to Create a Custom Exception

---

To create a custom exception, follow these steps:

1. **Extend the Exception Class**: Create a new class that extends the `Exception` class.
2. **Write Constructors**: Write constructors that call the parent class constructor using `super(message)`.
3. **Throw the Exception**: Use the `throw` keyword to throw the custom exception.
4. **Catch the Exception**: Use a `try-catch` block to catch the custom exception.

## Example: Creating a Custom Checked Exception

---

Here's an example of creating a custom checked exception:

```java
// Custom Checked Exception class
public class InvalidAgeException extends Exception {
 // Constructor with a custom message
 public InvalidAgeException(String message) {
 super(message);
 }
}

public class StudentRegistration {
 public void registerStudent(int age) throws InvalidAgeException {
 if (age < 18) {
 // Throw our specific custom exception
 throw new InvalidAgeException("Student age must be 18 or older. Provided: " + age);
 }
 // Proceed with registration
 System.out.println("Student registered successfully.");
 }

 public static void main(String[] args) {
 StudentRegistration registration = new StudentRegistration();
 try {
 registration.registerStudent(16); // This will throw the exception
 } catch (InvalidAgeException e) {
 System.err.println("Registration failed: " + e.getMessage());
 }
 }
}
```

## Difference Between Checked and Unchecked Custom Exceptions

---

|                | Checked Exceptions          | Unchecked Exceptions        |
| -------------- | --------------------------- | --------------------------- |
| **Definition** | Checked at compile-time     | Not checked at compile-time |
| **Usage**      | Used for recoverable errors | Used for programming errors |
| **Example**    | `InvalidAgeException`       | `NullPointerException`      |

## Benefits of Using Custom Exceptions

---

Custom exceptions provide several benefits, including:

- **Improved Error Handling**: Custom exceptions allow you to provide more specific and meaningful error messages.
- **Improved Code Readability**: Custom exceptions make it easier to understand the code and diagnose problems.
- **Improved Code Maintainability**: Custom exceptions make it easier to modify and extend the code.

## Comparison with Java's Built-in Exceptions

---

Custom exceptions are similar to Java's built-in exceptions, but they provide more specific and meaningful error messages. Here's a comparison:

|                    | Custom Exceptions                 | Java's Built-in Exceptions       |
| ------------------ | --------------------------------- | -------------------------------- |
| **Specificity**    | More specific                     | Less specific                    |
| **Error Messages** | More meaningful                   | Less meaningful                  |
| **Usage**          | Used for specific error scenarios | Used for general error scenarios |

## Exam Tips

---

- Be prepared to create a custom exception class and demonstrate its usage in a `try-catch` block.
- Focus on understanding the benefits of using custom exceptions, such as improved code readability and maintainability.
- Make sure to understand the difference between checked and unchecked custom exceptions.

## Key Takeaways

---

- Custom exceptions are created by extending the `Exception` class.
- Custom exceptions provide more specific and meaningful error messages.
- Custom exceptions are used to represent specific error scenarios in an application.
- Using custom exceptions improves code readability and maintainability.
