# Default Interface Methods

## Table of Contents

- [Default Interface Methods](#default-interface-methods)
- [Introduction](#introduction)
- [What are Default Interface Methods?](#what-are-default-interface-methods)
  - [Example: Vehicle Interface with Default Method](#example-vehicle-interface-with-default-method)
- [Syntax for Declaring Default Methods](#syntax-for-declaring-default-methods)
  - [Example: Default Method with Parameters](#example-default-method-with-parameters)
- [Resolving Conflicts with Multiple Interfaces](#resolving-conflicts-with-multiple-interfaces)
  - [Example: Resolving Conflicts with Multiple Interfaces](#example-resolving-conflicts-with-multiple-interfaces)
- [Comparison with Abstract Classes](#comparison-with-abstract-classes)
  - [Example: Using Abstract Classes](#example-using-abstract-classes)
- [Real-World Applications](#real-world-applications)
  - [Example: Java Collections Framework](#example-java-collections-framework)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

================================

## Introduction

---

Java 8 introduced a significant feature in interface design: default interface methods. This feature allows interfaces to have methods with an implementation, enabling more flexibility in interface design. In this chapter, we will explore the concept of default interface methods, their significance, syntax, and application in real-world scenarios.

## What are Default Interface Methods?

---

Default interface methods are non-abstract methods in an interface with an implementation. They are used to provide a basic implementation for a method that can be inherited or overridden by implementing classes. This feature is useful for adding new functionality to existing interfaces without breaking backward compatibility.

### Example: Vehicle Interface with Default Method

```java
public interface Vehicle {
 // Traditional abstract method
 void start();

 // Default method with an implementation
 default void honk() {
 System.out.println("Beep Beep!");
 }

 // Another abstract method
 void stop();
}
```

In this example, the `Vehicle` interface has two abstract methods (`start()` and `stop()`) and one default method (`honk()`). Any class implementing the `Vehicle` interface can use the `honk()` method without providing an implementation.

## Syntax for Declaring Default Methods

---

The syntax for declaring a default method within an interface is as follows:

```java
default returnType methodName() {
 // implementation
}
```

### Example: Default Method with Parameters

```java
public interface Calculator {
 default int add(int a, int b) {
 return a + b;
 }
}
```

In this example, the `Calculator` interface has a default method `add()` that takes two parameters and returns their sum.

## Resolving Conflicts with Multiple Interfaces

---

When a class implements multiple interfaces with the same default method, conflicts can arise. To resolve such conflicts, the class can override the default method and provide its own implementation.

### Example: Resolving Conflicts with Multiple Interfaces

```java
public interface Interface1 {
 default void method() {
 System.out.println("Interface 1");
 }
}

public interface Interface2 {
 default void method() {
 System.out.println("Interface 2");
 }
}

public class MyClass implements Interface1, Interface2 {
 @Override
 public void method() {
 System.out.println("My Class");
 }
}
```

In this example, the `MyClass` class implements both `Interface1` and `Interface2`, which have the same default method `method()`. To resolve the conflict, the `MyClass` class overrides the `method()` and provides its own implementation.

## Comparison with Abstract Classes

---

Default methods in interfaces are similar to methods in abstract classes. However, there are key differences between the two.

|                          | Default Methods in Interfaces | Methods in Abstract Classes |
| ------------------------ | ----------------------------- | --------------------------- |
| **Multiple Inheritance** | Supported                     | Not supported               |
| **State**                | No state                      | Can have state              |
| **Constructors**         | No constructors               | Can have constructors       |

### Example: Using Abstract Classes

```java
public abstract class Animal {
 public abstract void sound();

 public void eat() {
 System.out.println("Eating...");
 }
}

public class Dog extends Animal {
 @Override
 public void sound() {
 System.out.println("Barking...");
 }
}
```

In this example, the `Animal` abstract class has an abstract method `sound()` and a non-abstract method `eat()`. The `Dog` class extends the `Animal` class and provides an implementation for the `sound()` method.

## Real-World Applications

---

Default interface methods have numerous applications in real-world scenarios, such as the Java Collections Framework.

### Example: Java Collections Framework

```java
public interface Collection<E> {
 // ...

 default boolean isEmpty() {
 return size() == 0;
 }

 // ...
}
```

In this example, the `Collection` interface has a default method `isEmpty()` that returns `true` if the collection is empty.

## Exam Tips

---

- Focus on understanding the purpose and usage of default methods in interfaces.
- Be prepared to identify and explain the differences between abstract and default methods in interfaces.
- Understand how to resolve conflicts when a class implements multiple interfaces with the same default method.

## Key Takeaways

---

- Default interface methods are non-abstract methods in an interface with an implementation.
- Default methods are used to provide a basic implementation for a method that can be inherited or overridden by implementing classes.
- Default methods are useful for adding new functionality to existing interfaces without breaking backward compatibility.
- Understand the syntax for declaring default methods and how to resolve conflicts with multiple interfaces.
