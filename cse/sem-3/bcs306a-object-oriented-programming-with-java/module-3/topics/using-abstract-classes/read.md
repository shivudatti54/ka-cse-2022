# Using Abstract Classes in Java

## Table of Contents

- [Using Abstract Classes in Java](#using-abstract-classes-in-java)
- [Introduction](#introduction)
- [What is an Abstract Class?](#what-is-an-abstract-class)
- [Declaring Abstract Classes](#declaring-abstract-classes)
- [Characteristics of Abstract Classes](#characteristics-of-abstract-classes)
- [Extending Abstract Classes](#extending-abstract-classes)
- [Rules for Abstract Classes](#rules-for-abstract-classes)
- [When to Use Abstract Classes](#when-to-use-abstract-classes)
- [Comparison with Interfaces](#comparison-with-interfaces)
- [Real-World Example](#real-world-example)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

## Introduction

Abstract classes in Java are a fundamental concept in object-oriented programming (OOP) that enables code reuse and facilitates the creation of a hierarchy of related classes. An abstract class is declared with the `abstract` keyword and serves as a base for subclasses, providing a mix of abstract and concrete methods. In this chapter, we will delve into the world of abstract classes, exploring their purpose, characteristics, and usage.

## What is an Abstract Class?

An abstract class is a class that cannot be instantiated directly and is intended to be inherited by other classes. It provides a common base with shared implementation while forcing subclasses to implement specific methods. Abstract classes are useful when you want to define a blueprint for a group of related classes that share some common attributes and methods.

## Declaring Abstract Classes

To declare an abstract class, you use the `abstract` keyword followed by the `class` keyword and the name of the class. Here is an example:

```java
abstract class Shape {
 String color;
 abstract double area(); // no body, must be overridden
 void displayColor() { // concrete method
 System.out.println("Color: " + color);
 }
}
```

In this example, `Shape` is an abstract class that has an abstract method `area()` and a concrete method `displayColor()`.

## Characteristics of Abstract Classes

Here are the key characteristics of abstract classes:

- **Cannot be instantiated directly**: You cannot create an instance of an abstract class using the `new` keyword.
- **Can have abstract and concrete methods**: Abstract classes can have both abstract methods (no body) and concrete methods (with body).
- **Must be inherited**: Abstract classes are intended to be inherited by other classes.
- **Can have constructors, fields, and concrete methods**: Abstract classes can have constructors, fields, and concrete methods, just like regular classes.

## Extending Abstract Classes

To extend an abstract class, you use the `extends` keyword followed by the name of the abstract class. Here is an example:

```java
class Circle extends Shape {
 double radius;
 Circle(double r, String c) {
 radius = r;
 color = c;
 }
 @Override
 double area() {
 return Math.PI * radius * radius;
 }
}
```

In this example, `Circle` is a concrete class that extends the `Shape` abstract class and implements the `area()` method.

## Rules for Abstract Classes

Here are the rules for abstract classes:

- **Cannot instantiate an abstract class**: You cannot create an instance of an abstract class using the `new` keyword.
- **Abstract methods have no body**: Abstract methods must be overridden by subclasses and have no body.
- **A class with any abstract method must be declared abstract**: If a class has an abstract method, it must be declared as an abstract class.
- **Concrete subclass must implement all abstract methods**: A concrete subclass must implement all abstract methods of its abstract superclass.
- **Abstract classes can have constructors, fields, and concrete methods**: Abstract classes can have constructors, fields, and concrete methods, just like regular classes.

## When to Use Abstract Classes

Use abstract classes when you want to:

- **Provide a common base with shared implementation**: Abstract classes can provide a common base with shared implementation for a group of related classes.
- **Force subclasses to implement specific methods**: Abstract classes can force subclasses to implement specific methods, ensuring that they provide their own implementation.

## Comparison with Interfaces

Here is a comparison between abstract classes and interfaces:

|                             | Abstract Classes                                                                                                         | Interfaces                                                                                           |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| **Instantiation**           | Cannot be instantiated directly                                                                                          | Cannot be instantiated directly                                                                      |
| **Methods**                 | Can have abstract and concrete methods                                                                                   | Can only have abstract methods (Java 7 and earlier) or default and static methods (Java 8 and later) |
| **Inheritance**             | Can be inherited by a single class                                                                                       | Can be implemented by multiple classes                                                               |
| **Constructors and Fields** | Can have constructors and fields                                                                                         | Cannot have constructors and fields                                                                  |
| **Use**                     | Use when you want to provide a common base with shared implementation and force subclasses to implement specific methods | Use when you want to define a contract that must be implemented by classes                           |

## Real-World Example

The Java Collections framework uses abstract classes to provide a common base for various collection classes. For example, the `AbstractList` class is an abstract class that provides a common base for list classes, such as `ArrayList` and `LinkedList`.

## Exam Tips

- Be prepared to identify and explain the use of abstract classes and methods.
- Understand the rules governing abstract classes, including instantiation and method implementation.
- Focus on the benefits of using abstract classes, such as providing a common base with shared implementation.

## Key Takeaways

- Abstract classes are declared with the `abstract` keyword and serve as a base for subclasses.
- Abstract classes can have abstract and concrete methods.
- Abstract classes cannot be instantiated directly and must be inherited by other classes.
- Use abstract classes when you want to provide a common base with shared implementation and force subclasses to implement specific methods.
