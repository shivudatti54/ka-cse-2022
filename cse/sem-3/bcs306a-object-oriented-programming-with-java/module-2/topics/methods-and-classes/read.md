# Methods and Classes in Java

## Table of Contents

- [Methods and Classes in Java](#methods-and-classes-in-java)
- [Introduction](#introduction)
- [Method Declaration](#method-declaration)
- [Return Types](#return-types)
- [Parameters and Pass-by-Value](#parameters-and-pass-by-value)
- [Static vs Instance Methods](#static-vs-instance-methods)
- [Constructors](#constructors)
- [The `this` Keyword](#the-this-keyword)
- [Garbage Collection](#garbage-collection)
- [Overloading Methods](#overloading-methods)
- [Objects as Parameters](#objects-as-parameters)
- [Argument Passing](#argument-passing)
- [Returning Objects](#returning-objects)
- [Recursion](#recursion)
- [Access Control](#access-control)
- [Understanding `static`](#understanding-static)
- [Introducing `final`](#introducing-final)
- [Introducing Nested and Inner Classes](#introducing-nested-and-inner-classes)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

## Introduction

In Java, methods define behaviors that objects can perform, while classes group data (fields) and methods together. Understanding methods and classes is crucial for designing and implementing object-oriented programs in Java. In this chapter, we will explore the fundamentals of methods and classes, including method declarations, return types, parameters, and the differences between static and instance methods.

## Method Declaration

A method declaration in Java consists of a return type, method name, and parameter list. The general syntax for a method declaration is:

```java
returnType methodName(parameterList) {
 // body
 return value;
}
```

For example:

```java
class Calculator {
 double divide(double a, double b) {
 return a / b;
 }

 void displayResult(double r) {
 System.out.println("Result: " + r);
 }
}
```

## Return Types

In Java, a method can return a value or be declared as `void` to return no value. The return type of a method is specified in the method declaration. For example:

```java
class Calculator {
 double divide(double a, double b) {
 return a / b; // returns a double value
 }

 void displayResult(double r) {
 System.out.println("Result: " + r); // returns no value
 }
}
```

## Parameters and Pass-by-Value

Java uses a pass-by-value mechanism for passing parameters to methods. This means that a copy of the actual parameter is passed to the method. For primitive types, such as `int` and `double`, a copy of the value is passed. For objects, the reference value is copied.

For example:

```java
void changeValue(int x) {
 x = 100; // only changes local copy
}

int originalValue = 50;
changeValue(originalValue);
System.out.println(originalValue); // prints 50
```

## Static vs Instance Methods

In Java, methods can be declared as static or instance methods. Static methods belong to the class and can be called without creating an instance of the class. Instance methods, on the other hand, belong to an object and require an instance to be called.

For example:

```java
class Counter {
 int count = 0; // instance variable
 static int total = 0; // static variable

 void increment() { // instance method
 count++;
 total++;
 }

 static int getTotal() { // static method
 return total; // cannot access count here
 }
}
```

## Constructors

A constructor is a special method that is used to initialize objects when they are created. Constructors have the same name as the class and do not have a return type.

For example:

```java
class Person {
 String name;
 int age;

 Person(String name, int age) {
 this.name = name;
 this.age = age;
 }
}
```

## The `this` Keyword

The `this` keyword is used to refer to the current object. It is often used in constructors and instance methods to access instance variables.

For example:

```java
class Person {
 String name;
 int age;

 Person(String name, int age) {
 this.name = name;
 this.age = age;
 }

 void displayInfo() {
 System.out.println("Name: " + this.name);
 System.out.println("Age: " + this.age);
 }
}
```

## Garbage Collection

Garbage collection is the process of automatically freeing up memory occupied by objects that are no longer in use. Java has a built-in garbage collector that periodically frees up memory.

## Overloading Methods

Method overloading is the process of declaring multiple methods with the same name but different parameter lists.

For example:

```java
class Calculator {
 int add(int a, int b) {
 return a + b;
 }

 double add(double a, double b) {
 return a + b;
 }
}
```

## Objects as Parameters

Objects can be passed as parameters to methods.

For example:

```java
class Person {
 String name;
 int age;

 Person(String name, int age) {
 this.name = name;
 this.age = age;
 }

 void displayInfo() {
 System.out.println("Name: " + this.name);
 System.out.println("Age: " + this.age);
 }
}

class Printer {
 void printPerson(Person person) {
 person.displayInfo();
 }
}
```

## Argument Passing

Arguments can be passed to methods using the pass-by-value mechanism.

For example:

```java
void printMessage(String message) {
 System.out.println(message);
}

printMessage("Hello, World!"); // passes a copy of the string
```

## Returning Objects

Methods can return objects.

For example:

```java
class Person {
 String name;
 int age;

 Person(String name, int age) {
 this.name = name;
 this.age = age;
 }

 Person getPerson() {
 return this;
 }
}
```

## Recursion

Recursion is the process of a method calling itself.

For example:

```java
int factorial(int n) {
 if (n == 0) {
 return 1;
 } else {
 return n * factorial(n - 1);
 }
}
```

## Access Control

Access control is used to restrict access to methods and variables.

For example:

```java
public class Person {
 private String name;
 private int age;

 public Person(String name, int age) {
 this.name = name;
 this.age = age;
 }

 public void displayInfo() {
 System.out.println("Name: " + this.name);
 System.out.println("Age: " + this.age);
 }
}
```

## Understanding `static`

The `static` keyword is used to declare methods and variables that belong to the class.

For example:

```java
class Counter {
 static int total = 0;

 static void increment() {
 total++;
 }

 static int getTotal() {
 return total;
 }
}
```

## Introducing `final`

The `final` keyword is used to declare methods and variables that cannot be overridden or changed.

For example:

```java
class Person {
 final String name;
 final int age;

 Person(String name, int age) {
 this.name = name;
 this.age = age;
 }

 final void displayInfo() {
 System.out.println("Name: " + this.name);
 System.out.println("Age: " + this.age);
 }
}
```

## Introducing Nested and Inner Classes

Nested classes are classes that are declared inside another class. Inner classes are classes that are declared inside another class and have access to the outer class's variables and methods.

For example:

```java
class OuterClass {
 int x = 10;

 class InnerClass {
 int y = 20;

 void displayInfo() {
 System.out.println("x: " + x);
 System.out.println("y: " + y);
 }
 }
}
```

## Exam Tips

- Be prepared to identify and explain the differences between static and instance methods.
- Understand how pass-by-value works in Java and its implications for method parameters.
- Focus on method signatures and how they are used to identify unique methods in a class.
- Practice creating and using methods, including overloaded methods and methods that return objects.
- Understand how to use access control to restrict access to methods and variables.

## Key Takeaways

- Methods define behaviors that objects can perform.
- Classes group data and methods together.
- Java uses pass-by-value for all parameters, including primitives and objects.
- Static methods belong to the class, while instance methods belong to objects.
- Method signatures consist of the method name and parameter types, excluding the return type.
- Methods can return values or be declared as `void` to return no value.
