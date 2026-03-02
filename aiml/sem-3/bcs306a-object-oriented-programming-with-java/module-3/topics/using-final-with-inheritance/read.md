# Using final with Inheritance


## Table of Contents

- [Using final with Inheritance](#using-final-with-inheritance)
- [Introduction](#introduction)
- [1. Final Classes](#1-final-classes)
- [2. Final Methods](#2-final-methods)
- [3. Final Variables](#3-final-variables)
- [Comparison of Final Classes, Methods, and Variables](#comparison-of-final-classes-methods-and-variables)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

## Introduction

In Java, the `final` keyword is used to restrict modifications to classes, methods, and variables. It plays a crucial role in ensuring security, maintaining method behavior, and creating constants. In this topic, we will explore the three main applications of the `final` keyword: final classes, final methods, and final variables.

## 1. Final Classes

A final class is a class that cannot be extended (inherited) by any subclass. This means that no other class can inherit its properties and behavior. Final classes are used to prevent inheritance for security purposes.

```java
final class ImmutableClass {
 // This class cannot be subclassed
}

// class SubClass extends ImmutableClass { } // ERROR: Cannot extend final class
```

**Example:** The `String` class in Java is final. This ensures that its behavior cannot be modified by any subclass.

```java
// Attempting to extend the String class will result in a compile-time error
// class CustomString extends String { } // ERROR: Cannot extend final class
```

## 2. Final Methods

A final method is a method that cannot be overridden by any subclass. This means that once a method is declared as final, its behavior cannot be changed by any subclass.

```java
class Parent {
 public final void display() {
 System.out.println("This method cannot be overridden");
 }
}

class Child extends Parent {
 // public void display() { } // ERROR: Cannot override final method
}
```

**Example:** Suppose we have a `BankAccount` class with a final method `getBalance()`. This ensures that the balance calculation logic cannot be modified by any subclass.

```java
class BankAccount {
 private double balance;

 public final double getBalance() {
 return balance;
 }
}

class SavingsAccount extends BankAccount {
 // Attempting to override the getBalance() method will result in a compile-time error
 // public double getBalance() { } // ERROR: Cannot override final method
}
```

## 3. Final Variables

A final variable is a variable that becomes a constant and cannot be reassigned. Final variables are used to create constants that do not change throughout the program.

```java
class Constants {
 public static final double PI = 3.14159;
 public static final int MAX_VALUE = 100;
}
```

**Example:** Suppose we have a `MathUtils` class with a final variable `PI`. This ensures that the value of PI remains constant throughout the program.

```java
class MathUtils {
 public static final double PI = 3.14159;

 public static double calculateArea(double radius) {
 return PI * radius * radius;
 }
}
```

## Comparison of Final Classes, Methods, and Variables

|         | Final Class                 | Final Method                         | Final Variable                                       |
| ------- | --------------------------- | ------------------------------------ | ---------------------------------------------------- |
| Purpose | Prevent inheritance         | Prevent method overriding            | Create constants                                     |
| Syntax  | `final class ClassName { }` | `public final void methodName() { }` | `public static final dataType variableName = value;` |
| Example | `String` class              | `getBalance()` method                | `PI` constant                                        |

## Exam Tips

- Focus on the use cases of final classes, methods, and variables.
- Understand the security benefits of using final classes and methods.
- Practice identifying scenarios where final variables are necessary.
- Be prepared to explain the implications of using the `final` keyword in inheritance.

## Key Takeaways

- The `final` keyword is used to restrict modifications to classes, methods, and variables.
- Final classes prevent inheritance, final methods prevent method overriding, and final variables create constants.
- The `final` keyword is essential for ensuring security, maintaining method behavior, and creating constants.
- Understand the syntax and use cases of final classes, methods, and variables to write secure and maintainable code.
