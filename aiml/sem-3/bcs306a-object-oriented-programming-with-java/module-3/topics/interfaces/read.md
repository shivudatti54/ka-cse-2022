# Interfaces in Java


## Table of Contents

- [Interfaces in Java](#interfaces-in-java)
- [Introduction](#introduction)
- [Declaring an Interface](#declaring-an-interface)
- [Implementing an Interface](#implementing-an-interface)
- [Multiple Interface Implementation](#multiple-interface-implementation)
- [Interface Variables](#interface-variables)
- [Default Interface Methods](#default-interface-methods)
- [Static Interface Methods](#static-interface-methods)
- [Private Interface Methods](#private-interface-methods)
- [Interface vs Abstract Class](#interface-vs-abstract-class)
- [Key Points](#key-points)
- [Exam Tips](#exam-tips)

## Introduction

An interface in Java is a reference type that defines a contract of methods that implementing classes must provide. Interfaces are declared with the `interface` keyword and implemented using `implements`. They are used to achieve full abstraction and define a blueprint for classes that includes a set of methods that must be implemented.

## Declaring an Interface

```java
interface Drawable {
 void draw(); // implicitly public abstract
 double getArea(); // implicitly public abstract
}
```

In the above example, `Drawable` is an interface that declares two methods: `draw()` and `getArea()`. These methods are implicitly `public abstract`, meaning they must be implemented by any class that implements the `Drawable` interface.

## Implementing an Interface

```java
class Circle implements Drawable {
 double radius;
 Circle(double r) {
 radius = r;
 }
 @Override
 public void draw() {
 System.out.println("Drawing circle");
 }
 @Override
 public double getArea() {
 return Math.PI * radius * radius;
 }
}
```

In the above example, `Circle` is a class that implements the `Drawable` interface. It provides an implementation for the `draw()` and `getArea()` methods.

## Multiple Interface Implementation

Java supports implementing multiple interfaces:

```java
interface Printable {
 void print();
}
interface Showable {
 void show();
}
class Document implements Printable, Showable {
 public void print() {
 System.out.println("Printing");
 }
 public void show() {
 System.out.println("Showing");
 }
}
```

In the above example, `Document` is a class that implements both the `Printable` and `Showable` interfaces.

## Interface Variables

All variables in an interface are implicitly `public static final` (constants):

```java
interface Config {
 int MAX_SIZE = 100; // public static final
}
```

In the above example, `MAX_SIZE` is a constant variable declared in the `Config` interface.

## Default Interface Methods

Java 8 introduced default methods in interfaces, which allow interfaces to provide a default implementation for methods:

```java
interface MathOperations {
 default int add(int a, int b) {
 return a + b;
 }
 default int subtract(int a, int b) {
 return a - b;
 }
}
```

In the above example, `MathOperations` is an interface that declares two default methods: `add()` and `subtract()`.

## Static Interface Methods

Java 8 also introduced static methods in interfaces, which allow interfaces to provide static methods:

```java
interface MathOperations {
 static int multiply(int a, int b) {
 return a * b;
 }
}
```

In the above example, `MathOperations` is an interface that declares a static method: `multiply()`.

## Private Interface Methods

Java 9 introduced private methods in interfaces, which allow interfaces to encapsulate implementation details:

```java
interface MathOperations {
 default int add(int a, int b) {
 return addInternal(a, b);
 }
 private int addInternal(int a, int b) {
 return a + b;
 }
}
```

In the above example, `MathOperations` is an interface that declares a default method `add()` and a private method `addInternal()`.

## Interface vs Abstract Class

| Feature     | Interface                                | Abstract Class      |
| ----------- | ---------------------------------------- | ------------------- |
| Methods     | Abstract (+ default/static since Java 8) | Abstract + concrete |
| Variables   | public static final only                 | Any type            |
| Inheritance | Multiple                                 | Single              |
| Constructor | No                                       | Yes                 |

## Key Points

- Declared with `interface`, implemented with `implements`.
- Methods are implicitly public abstract.
- Variables are implicitly public static final.
- A class can implement multiple interfaces.
- Interfaces define contracts without implementation.
- Java supports default and static methods in interfaces since Java 8.
- Interfaces cannot have constructors.

## Exam Tips

- Focus on the differences between interfaces and abstract classes.
- Understand how to declare and implement interfaces.
- Be prepared to explain the use of interfaces in defining contracts and promoting multiple inheritance.
- Understand the use of default and static methods in interfaces.
- Be prepared to explain the benefits of using interfaces in software design.
