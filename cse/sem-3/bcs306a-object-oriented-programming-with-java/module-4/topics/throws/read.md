# throws Clause in Java

## Table of Contents

- [throws Clause in Java](#throws-clause-in-java)
- [Overview](#overview)
- [Purpose of throws](#purpose-of-throws)
- [Types of Exceptions](#types-of-exceptions)
  - [Checked Exceptions](#checked-exceptions)
  - [Unchecked Exceptions](#unchecked-exceptions)
- [Using throws](#using-throws)
  - [Syntax](#syntax)
  - [Example](#example)
- [Difference between throw and throws](#difference-between-throw-and-throws)
  - [Example](#example)
- [Method Overriding and throws](#method-overriding-and-throws)
  - [Example](#example)
- [Real-World Applications](#real-world-applications)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

=====================================================

## Overview

---

The `throws` clause in Java is used to declare the exceptions that a method might throw, allowing the caller to handle them. It is an essential part of Java's exception handling mechanism, which enables robust and maintainable code.

## Purpose of throws

---

The primary purpose of the `throws` keyword is to declare the exceptions that a method may throw. This declaration is mandatory for **checked exceptions**, which are exceptions that inherit from the `Exception` class but not from the `RuntimeException` class. On the other hand, declaring **unchecked exceptions**, which are exceptions that inherit from the `RuntimeException` class, is optional.

## Types of Exceptions

---

There are two types of exceptions in Java: checked and unchecked.

### Checked Exceptions

Checked exceptions are exceptions that must be declared or caught. They inherit from the `Exception` class but not from the `RuntimeException` class. Examples of checked exceptions include:

- `IOException`
- `SQLException`
- `FileNotFoundException`

### Unchecked Exceptions

Unchecked exceptions are exceptions that do not require declaration. They inherit from the `RuntimeException` class. Examples of unchecked exceptions include:

- `NullPointerException`
- `ArrayIndexOutOfBoundsException`
- `ClassCastException`

## Using throws

---

The `throws` clause is used in method declaration to indicate potential exceptions. It declares exceptions without actually throwing them.

### Syntax

```java
return_type method_name(parameters) throws ExceptionType1, ExceptionType2 {
 // method body
}
```

### Example

```java
public void readFile() throws IOException, FileNotFoundException {
 // method body
}
```

In this example, the `readFile` method declares that it may throw `IOException` and `FileNotFoundException`.

## Difference between throw and throws

---

| Aspect  | throw                          | throws                            |
| ------- | ------------------------------ | --------------------------------- |
| Purpose | Actually throws an exception   | Declares exceptions to be thrown  |
| Usage   | Inside method body             | In method declaration             |
| Object  | Followed by exception instance | Followed by exception class names |
| Count   | Single exception               | Multiple exceptions possible      |

### Example

```java
public void readFile() throws IOException {
 throw new IOException("File not found");
}
```

In this example, the `throw` keyword is used to actually throw an `IOException`, while the `throws` keyword is used to declare that the method may throw an `IOException`.

## Method Overriding and throws

---

When overriding a method, the `throws` clause must be compatible with the superclass. This means that the subclass method cannot throw any checked exceptions that are not declared in the superclass method.

### Example

```java
class SuperClass {
 public void readFile() throws IOException {
 // method body
 }
}

class SubClass extends SuperClass {
 @Override
 public void readFile() throws IOException, FileNotFoundException {
 // method body
 }
}
```

In this example, the `SubClass` method `readFile` declares that it may throw `IOException` and `FileNotFoundException`, which is compatible with the superclass method.

## Real-World Applications

---

The `throws` clause is essential in real-world applications, as it allows developers to handle exceptions in a robust and maintainable way. By declaring potential exceptions, developers can ensure that their code is reliable and error-free.

## Exam Tips

---

- Remember: `throw` = verb (action), `throws` = noun (declaration)
- Always declare checked exceptions; unchecked exceptions are optional
- If overriding a method, the `throws` clause must be compatible with the superclass
- Common question: "Explain the difference between throw and throws with examples"

## Key Takeaways

---

- The `throws` clause is used to declare potential exceptions in a method
- Checked exceptions must be declared, while unchecked exceptions are optional
- The `throws` clause is essential in method overriding and real-world applications
- Understanding the difference between `throw` and `throws` is crucial for robust and maintainable code.
