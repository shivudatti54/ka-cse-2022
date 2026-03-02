# Constructors in Java

## Table of Contents

- [Constructors in Java](#constructors-in-java)
- [Introduction](#introduction)
- [Default Constructor](#default-constructor)
- [Parameterized Constructor](#parameterized-constructor)
- [Constructor Overloading](#constructor-overloading)
- [Constructor Chaining with this()](#constructor-chaining-with-this)
- [Key Points](#key-points)
- [Comparison of Constructors and Methods](#comparison-of-constructors-and-methods)
- [Exam Tips](#exam-tips)

## Introduction

A constructor is a special method in Java that is called automatically when an object is created using the `new` keyword. Its primary purpose is to initialize the newly created object with a valid state. A constructor has two key characteristics: it has the **same name as the class**, and it has **no return type**, not even `void`.

## Default Constructor

If a class does not define any constructor, Java provides a default constructor automatically. This default constructor is a no-argument constructor that does nothing. For example:

```java
class Box {
 double width, height, depth;
 // Java provides: Box() { } implicitly
}
```

However, as soon as you define any constructor, the default constructor is no longer provided. If you want to have a no-argument constructor along with other constructors, you must define it explicitly.

## Parameterized Constructor

A parameterized constructor is used to initialize objects with specific values. For example:

```java
class Box {
 double width, height, depth;
 Box(double w, double h, double d) {
 width = w;
 height = h;
 depth = d;
 }
}
Box myBox = new Box(10, 20, 15);
```

## Constructor Overloading

Constructor overloading is a technique in Java that allows you to define multiple constructors with different parameter lists. This is useful when you want to provide different ways to initialize an object. For example:

```java
class Box {
 double width, height, depth;
 Box() {
 width = height = depth = 0;
 }
 Box(double side) {
 width = height = depth = side;
 }
 Box(double w, double h, double d) {
 width = w;
 height = h;
 depth = d;
 }
}
```

## Constructor Chaining with this()

Constructor chaining is a technique in Java that allows you to call one constructor from another constructor using the `this()` keyword. This is useful when you want to reduce code duplication and improve constructor organization. For example:

```java
class Box {
 double width, height, depth;
 Box() {
 this(0, 0, 0);
 }
 Box(double side) {
 this(side, side, side);
 }
 Box(double w, double h, double d) {
 width = w;
 height = h;
 depth = d;
 }
}
```

Note that `this()` must be the first statement in a constructor.

## Key Points

- A constructor has the same name as the class and no return type.
- A default constructor is provided only if no other constructor is defined.
- Constructor overloading allows multiple constructors with different parameter lists.
- `this()` is used for constructor chaining and must be the first statement.
- Java has no destructors; memory is handled by garbage collection.

## Comparison of Constructors and Methods

|             | Constructors                                | Methods              |
| ----------- | ------------------------------------------- | -------------------- |
| Purpose     | Initialize objects                          | Perform actions      |
| Name        | Same as class                               | Any valid name       |
| Return Type | No return type                              | May have return type |
| Call        | Called automatically when object is created | Called explicitly    |

## Exam Tips

- Focus on constructor overloading, chaining, and default constructors.
- Understand the use of `this()` in constructor chaining.
- Be prepared to identify and write constructors in code snippets.
- Practice creating classes with multiple constructors and chaining them using `this()`.
- Understand the importance of constructors in ensuring objects start in a valid state and their connection to other concepts, such as classes, inheritance, and garbage collection.
