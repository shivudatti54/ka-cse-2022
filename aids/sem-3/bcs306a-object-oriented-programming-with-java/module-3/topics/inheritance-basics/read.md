# Inheritance Basics in Java


## Table of Contents

- [Inheritance Basics in Java](#inheritance-basics-in-java)
- [Introduction](#introduction)
- [Syntax](#syntax)
- [Member Access](#member-access)
- [Single Inheritance Only](#single-inheritance-only)
- [Benefits](#benefits)
- [Using super](#using-super)
- [Creating a Multilevel Hierarchy](#creating-a-multilevel-hierarchy)
- [When Constructors Are Executed](#when-constructors-are-executed)
- [Method Overriding](#method-overriding)
- [Dynamic Method Dispatch](#dynamic-method-dispatch)
- [Using Abstract Classes](#using-abstract-classes)
- [Using final with Inheritance](#using-final-with-inheritance)
- [Local Variable Type Inference and Inheritance](#local-variable-type-inference-and-inheritance)
- [The Object Class](#the-object-class)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

## Introduction

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (subclass) to acquire the properties and behaviors of an existing class (superclass). Java uses the `extends` keyword to implement inheritance, which represents the IS-A relationship between classes. In this chapter, we will explore the basics of inheritance in Java, including its syntax, member access, single inheritance, benefits, and key points.

## Syntax

The syntax for implementing inheritance in Java is as follows:

```java
class Subclass extends Superclass {
 // subclass members
}
```

For example:

```java
class Animal {
 void eat() {
 System.out.println("Eating...");
 }
}

class Dog extends Animal {
 void bark() {
 System.out.println("Barking...");
 }
}
```

In this example, the `Dog` class inherits the `eat()` method from the `Animal` class and adds a new method `bark()`.

## Member Access

A subclass inherits all non-private members of the superclass. Private members are not directly accessible in the subclass. However, the subclass can access the private members of the superclass through public or protected methods.

```java
class A {
 private int secret = 10;
 int visible = 20;

 public int getSecret() {
 return secret;
 }
}

class B extends A {
 void test() {
 // System.out.println(secret); // ERROR - private
 System.out.println(visible); // OK
 System.out.println(getSecret()); // OK
 }
}
```

## Single Inheritance Only

Java does not support multiple class inheritance. A class can extend only one superclass.

```java
// class C extends A, B { } // ERROR - not allowed
```

However, a class can implement multiple interfaces.

## Benefits

Inheritance provides several benefits, including:

- **Code Reuse**: A subclass inherits the functionality of the superclass, reducing code duplication.
- **Extensibility**: A subclass can add new features or override the ones inherited from the superclass.
- **Polymorphism**: Subclass objects can be treated as superclass type, allowing for more flexibility in programming.

## Using super

The `super` keyword is used to access the members of the superclass from the subclass. It can be used to:

- Call the superclass constructor
- Access superclass members
- Override superclass methods

```java
class Animal {
 void eat() {
 System.out.println("Eating...");
 }
}

class Dog extends Animal {
 void eat() {
 super.eat(); // calls Animal's eat() method
 System.out.println("Dog is eating...");
 }
}
```

## Creating a Multilevel Hierarchy

Inheritance can be used to create a multilevel hierarchy of classes.

```java
class Animal {
 void eat() {
 System.out.println("Eating...");
 }
}

class Mammal extends Animal {
 void walk() {
 System.out.println("Walking...");
 }
}

class Dog extends Mammal {
 void bark() {
 System.out.println("Barking...");
 }
}
```

In this example, the `Dog` class inherits the `eat()` method from the `Animal` class and the `walk()` method from the `Mammal` class.

## When Constructors Are Executed

When an object of a subclass is created, the constructors of the superclass are executed first, followed by the constructors of the subclass.

```java
class Animal {
 Animal() {
 System.out.println("Animal constructor");
 }
}

class Dog extends Animal {
 Dog() {
 System.out.println("Dog constructor");
 }
}

public class Main {
 public static void main(String[] args) {
 Dog dog = new Dog();
 }
}
```

In this example, the output will be:

```
Animal constructor
Dog constructor
```

## Method Overriding

Method overriding is a feature of inheritance that allows a subclass to provide a different implementation of a method that is already defined in the superclass.

```java
class Animal {
 void eat() {
 System.out.println("Eating...");
 }
}

class Dog extends Animal {
 void eat() {
 System.out.println("Dog is eating...");
 }
}
```

In this example, the `Dog` class overrides the `eat()` method of the `Animal` class.

## Dynamic Method Dispatch

Dynamic method dispatch is a feature of inheritance that allows the correct method to be called based on the type of object being referred to.

```java
class Animal {
 void eat() {
 System.out.println("Eating...");
 }
}

class Dog extends Animal {
 void eat() {
 System.out.println("Dog is eating...");
 }
}

public class Main {
 public static void main(String[] args) {
 Animal animal = new Dog();
 animal.eat();
 }
}
```

In this example, the output will be:

```
Dog is eating...
```

## Using Abstract Classes

Abstract classes are classes that cannot be instantiated and are used as a base class for other classes.

```java
abstract class Animal {
 abstract void eat();
}

class Dog extends Animal {
 void eat() {
 System.out.println("Dog is eating...");
 }
}
```

In this example, the `Animal` class is an abstract class that defines an abstract method `eat()`. The `Dog` class extends the `Animal` class and provides an implementation for the `eat()` method.

## Using final with Inheritance

The `final` keyword can be used to prevent a method from being overridden or a class from being subclassed.

```java
class Animal {
 final void eat() {
 System.out.println("Eating...");
 }
}

class Dog extends Animal {
 // void eat() { } // ERROR - cannot override final method
}
```

In this example, the `eat()` method of the `Animal` class is declared as `final` and cannot be overridden by the `Dog` class.

## Local Variable Type Inference and Inheritance

Local variable type inference is a feature of Java that allows the type of a local variable to be inferred by the compiler.

```java
class Animal {
 void eat() {
 System.out.println("Eating...");
 }
}

public class Main {
 public static void main(String[] args) {
 var animal = new Animal();
 animal.eat();
 }
}
```

In this example, the type of the `animal` variable is inferred by the compiler to be `Animal`.

## The Object Class

The `Object` class is the superclass of all classes in Java and provides several methods that can be overridden by subclasses.

```java
class Animal {
 @Override
 public String toString() {
 return "Animal";
 }
}

public class Main {
 public static void main(String[] args) {
 Animal animal = new Animal();
 System.out.println(animal.toString());
 }
}
```

In this example, the `Animal` class overrides the `toString()` method of the `Object` class.

## Exam Tips

- Understand the IS-A relationship and single class inheritance in Java.
- Be prepared to identify and explain the benefits of inheritance, including code reuse, extensibility, and polymorphism.
- Practice creating simple inheritance relationships using the `extends` keyword.
- Understand how to use the `super` keyword to access superclass members.
- Be familiar with method overriding and dynamic method dispatch.
- Understand how to use abstract classes and the `final` keyword with inheritance.

## Key Takeaways

- Inheritance is a mechanism where a new class (subclass) acquires the properties and behaviors of an existing class (superclass).
- Java uses the `extends` keyword to implement inheritance.
- A subclass inherits all non-private members of the superclass.
- Private members are not directly accessible in the subclass.
- Inheritance promotes code reuse, extensibility, and polymorphism.
- A subclass can add new features or override the ones inherited from the superclass.
- The `super` keyword is used to access superclass members.
- Method overriding allows a subclass to provide a different implementation of a method that is already defined in the superclass.
- Dynamic method dispatch allows the correct method to be called based on the type of object being referred to.
