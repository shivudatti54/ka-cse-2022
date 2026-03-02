# Overloading Methods

## Table of Contents

- [Overloading Methods](#overloading-methods)
- [Introduction](#introduction)
- [Rules for Overloading Methods](#rules-for-overloading-methods)
  - [Method Signature](#method-signature)
- [Example](#example)
- [Benefits](#benefits)
- [Comparison with Method Overriding](#comparison-with-method-overriding)
- [Real-World Applications](#real-world-applications)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

## Introduction

Method overloading is a fundamental concept in object-oriented programming (OOP) that allows multiple methods with the same name but different parameters in the same class. This feature enables compile-time polymorphism, where the compiler determines which method to call based on the method signature. In this chapter, we will explore the rules, benefits, and applications of method overloading in Java.

## Rules for Overloading Methods

To overload methods in Java, the following rules must be followed:

- Methods must differ in:
- Number of parameters
- Type of parameters
- Order of parameter types
- Return type alone is NOT sufficient for overloading.

### Method Signature

A method signature is the combination of a method's name and parameter list. The method signature is used by the compiler to determine which method to call.

## Example

```java
class Calculator {
 // Overloaded add methods
 public int add(int a, int b) {
 return a + b;
 }

 public double add(double a, double b) {
 return a + b;
 }

 public int add(int a, int b, int c) {
 return a + b + c;
 }

 public String add(String a, String b) {
 return a + b;
 }
}

public class Main {
 public static void main(String[] args) {
 Calculator calc = new Calculator();
 System.out.println(calc.add(5, 10)); // Calls add(int, int)
 System.out.println(calc.add(5.5, 10.5)); // Calls add(double, double)
 System.out.println(calc.add(1, 2, 3)); // Calls add(int, int, int)
 System.out.println(calc.add("Hello", "World")); // Calls add(String, String)
 }
}
```

## Benefits

Method overloading offers several benefits, including:

- **Code Readability**: Method overloading allows for more readable code by enabling the same operation to be performed on different data types.
- **Polymorphism**: Method overloading enables compile-time polymorphism, where the compiler determines which method to call based on the method signature.
- **Flexibility**: Method overloading allows for more flexibility in programming by enabling the same method name to be used for different operations.

## Comparison with Method Overriding

Method overloading is often confused with method overriding. However, there are key differences between the two concepts:

|                             | Method Overloading                                    | Method Overriding                                   |
| --------------------------- | ----------------------------------------------------- | --------------------------------------------------- |
| **Method Name**             | Same method name, different parameters                | Same method name, same parameters                   |
| **Method Signature**        | Different method signatures                           | Same method signature                               |
| **Compile-time vs Runtime** | Compile-time polymorphism                             | Runtime polymorphism                                |
| **Purpose**                 | To perform the same operation on different data types | To provide a specific implementation for a subclass |

## Real-World Applications

Method overloading is widely used in Java's standard libraries and custom class APIs. For example, the `String` class has multiple overloaded methods for concatenating strings, such as `concat(String)` and `concat(CharSequence)`.

## Exam Tips

- Focus on understanding the rules and benefits of method overloading.
- Practice identifying correct method calls based on method signatures.
- Be prepared to explain the concept of compile-time polymorphism and its differences with runtime polymorphism.

## Key Takeaways

- Method overloading allows multiple methods with the same name but different parameters in the same class.
- The compiler determines which method to call based on the method signature.
- Method overloading enables compile-time polymorphism and improves code readability.
- Method overloading is different from method overriding, which is used to provide a specific implementation for a subclass.
