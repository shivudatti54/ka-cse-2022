# Abstraction in Java


## Table of Contents

- [Abstraction in Java](#abstraction-in-java)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Abstract Classes](#abstract-classes)
  - [Abstract Methods](#abstract-methods)
  - [Interfaces](#interfaces)
  - [Abstract Class vs Interface](#abstract-class-vs-interface)
- [Examples](#examples)
  - [Example 1: Abstract Class with Abstract Methods](#example-1-abstract-class-with-abstract-methods)
  - [Example 2: Interface for Multiple Inheritance](#example-2-interface-for-multiple-inheritance)
  - [Example 3: Abstract Class Implementing Interface](#example-3-abstract-class-implementing-interface)
- [Exam Tips](#exam-tips)

## Introduction

Abstraction is one of the fundamental pillars of Object-Oriented Programming (OOP), alongside encapsulation, inheritance, and polymorphism. In the context of Java programming, abstraction refers to the process of hiding complex implementation details and showing only the essential features of an object to the outside world. This concept allows programmers to manage complexity by focusing on what an object does rather than how it achieves its functionality.

In real-world software development, abstraction plays a crucial role in building maintainable, scalable, and extensible applications. When you use a smartphone, you interact with simple interfaces like touch screens and buttons without understanding the intricate electronics and programming behind them. Similarly, abstraction in Java enables developers to create reusable components that can be used without worrying about their internal workings. The the syllabus emphasizes understanding abstraction through abstract classes and interfaces, which are the primary mechanisms Java provides for achieving abstraction.

Abstraction differs from encapsulation in a subtle but important way. While encapsulation bundles data and methods together and restricts access to components, abstraction focuses on hiding implementation details and exposing only the necessary interface. Both concepts work together to achieve data hiding and modularity in Java applications. As you prepare for your university examinations, remember that abstraction is about "what" rather than "how" - it answers the question of functionality without delving into the mechanism.

## Key Concepts

### Abstract Classes

An abstract class in Java is a class that cannot be instantiated directly and may contain both abstract methods (methods without implementation) and concrete methods (methods with implementation). Abstract classes are declared using the `abstract` keyword and serve as blueprints for other classes. They can have constructors, which are called when a subclass is instantiated, and they can also have instance variables, static methods, and final methods.

The syntax for declaring an abstract class is straightforward: `abstract class ClassName { // body }`. Abstract classes can extend other classes and implement interfaces, providing a mechanism for code reuse and establishing IS-A relationships between classes. For example, if you have an abstract class `Animal`, you cannot create an object of type `Animal` directly, but you can create instances of its subclasses like `Dog` or `Cat` that extend `Animal`.

Abstract classes are used when you want to create a common base class with some shared functionality while forcing subclasses to provide specific implementations. They are particularly useful in scenarios where you have related classes that share common behavior but also require unique implementations for certain methods. The abstract class can define abstract methods that must be overridden by all non-abstract subclasses, ensuring a contract is maintained throughout the inheritance hierarchy.

### Abstract Methods

An abstract method is a method declared without an implementation - it has only a signature and does not contain a method body. The syntax for an abstract method is `abstract return_type method_name(parameter_list);`. Abstract methods must be overridden by any concrete subclass that extends an abstract class. If a subclass fails to implement all abstract methods from its parent class, it must also be declared as abstract.

Abstract methods define a contract that subclasses must fulfill, ensuring that all derived classes provide their own implementation for specific behaviors. This is particularly useful when you want to define a general structure or template for a group of related classes while allowing each subclass to define its own specific implementation. For instance, an abstract class `Shape` might have an abstract method `draw()`, and each subclass like `Circle`, `Rectangle`, or `Triangle` would provide its own implementation of how to draw that particular shape.

It is important to note that abstract methods cannot be `static`, `final`, or `private` because they are meant to be overridden by subclasses. The combination of `private` and `abstract` is not allowed since private methods cannot be overridden, and abstract methods require overriding. Understanding these constraints is essential for writing correct Java code and avoiding compilation errors.

### Interfaces

An interface in Java is a reference type that can contain only constants, method signatures, default methods, static methods, and nested types. Interfaces cannot contain instance fields or constructors. Prior to Java 8, interfaces could only contain abstract methods, but Java 8 introduced default and static methods, and Java 9 introduced private methods. Interfaces are declared using the `interface` keyword and are implemented by classes using the `implements` keyword.

Interfaces achieve full abstraction since all methods in an interface are by default abstract (unless they are default or static methods). A class can implement multiple interfaces, which allows Java to achieve multiple inheritance in a controlled manner. This is particularly valuable because Java does not support multiple inheritance through classes due to the diamond problem, but interfaces provide a way to achieve similar functionality.

The key difference between abstract classes and interfaces lies in their purpose and capabilities. Abstract classes can provide partial implementation and have state through instance variables, while interfaces cannot have instance state (only constants). Abstract classes are used when you want to share code and state among closely related classes, while interfaces are used to define capabilities or contracts that unrelated classes can implement. For your university exam, remember that interfaces represent "can-do" relationships, while abstract classes represent "is-a" relationships.

### Abstract Class vs Interface

Understanding when to use an abstract class versus an interface is a crucial skill in Java programming. Use an abstract class when you want to share code and state among related classes that share a common ancestor. Abstract classes are ideal when you have a clear IS-A relationship and want to provide some common implementation while forcing subclasses to provide specific behaviors. For example, a `Vehicle` abstract class might provide common functionality for all vehicles while requiring subclasses to implement `start()` and `stop()` methods.

Use an interface when you want to define a contract or capability that unrelated classes can implement. Interfaces are perfect for defining shared behavior across different class hierarchies. For instance, the `Comparable` interface can be implemented by any class that needs to compare its instances, regardless of what that class represents. A class can implement multiple interfaces but can extend only one class, making interfaces the preferred choice when you need to combine behaviors from multiple sources.

In modern Java development, the trend is to prefer interfaces over abstract classes for defining types, using abstract classes primarily when you need to share implementation code. With the addition of default methods in Java 8, interfaces can now provide default implementations, making them even more powerful and reducing the need for abstract classes in many scenarios.

## Examples

### Example 1: Abstract Class with Abstract Methods

Consider a scenario where we are building a banking system. We have different types of bank accounts like Savings Account and Current Account. While both account types share common properties like account number, balance, and owner name, they have different interest calculation methods.

```java
abstract class BankAccount {
 protected String accountNumber;
 protected String ownerName;
 protected double balance;

 public BankAccount(String accountNumber, String ownerName, double initialBalance) {
 this.accountNumber = accountNumber;
 this.ownerName = ownerName;
 this.balance = initialBalance;
 }

 // Abstract method - no implementation
 abstract double calculateInterest();

 // Concrete method - has implementation
 public void deposit(double amount) {
 if (amount > 0) {
 balance += amount;
 System.out.println("Deposited: " + amount);
 }
 }

 public void withdraw(double amount) {
 if (amount > 0 && amount <= balance) {
 balance -= amount;
 System.out.println("Withdrawn: " + amount);
 }
 }

 public void displayBalance() {
 System.out.println("Current Balance: " + balance);
 }
}

class SavingsAccount extends BankAccount {
 private double interestRate = 0.04;

 public SavingsAccount(String accountNumber, String ownerName, double initialBalance) {
 super(accountNumber, ownerName, initialBalance);
 }

 @Override
 double calculateInterest() {
 return balance * interestRate;
 }
}

class CurrentAccount extends BankAccount {
 private double interestRate = 0.02;

 public CurrentAccount(String accountNumber, String ownerName, double initialBalance) {
 super(accountNumber, ownerName, initialBalance);
 }

 @Override
 double calculateInterest() {
 return balance * interestRate;
 }
}

public class Main {
 public static void main(String[] args) {
 BankAccount savings = new SavingsAccount("SAV001", "John", 50000);
 savings.deposit(10000);
 System.out.println("Interest: " + savings.calculateInterest());
 savings.displayBalance();
 }
}
```

In this example, `BankAccount` is an abstract class that cannot be instantiated directly. The `calculateInterest()` method is abstract, forcing each subclass to provide its own implementation. The `deposit()` and `withdraw()` methods are concrete, providing shared functionality.

### Example 2: Interface for Multiple Inheritance

Java does not support multiple inheritance through classes to avoid ambiguity. However, interfaces provide a way to achieve multiple inheritance. Consider a class that needs to be both `Comparable` and `Serializable`.

```java
interface Drawable {
 void draw();
 default void display() {
 System.out.println("Displaying shape");
 }
}

interface Movable {
 void move();
}

class Circle implements Drawable, Movable {
 private double radius;

 public Circle(double radius) {
 this.radius = radius;
 }

 @Override
 public void draw() {
 System.out.println("Drawing a circle with radius: " + radius);
 }

 @Override
 public void move() {
 System.out.println("Moving the circle");
 }

 public double getRadius() {
 return radius;
 }
}

public class InterfaceDemo {
 public static void main(String[] args) {
 Circle circle = new Circle(5.0);
 circle.draw();
 circle.move();
 circle.display(); // Default method from interface

 // Using interface reference
 Drawable d = new Circle(3.0);
 d.draw();
 // d.move(); // Not accessible - compile error
 }
}
```

This example demonstrates how a class can implement multiple interfaces, achieving multiple inheritance of type. The `Circle` class implements both `Drawable` and `Movable` interfaces, inheriting behavior from both. Interface references can hold objects of implementing classes, providing flexibility in designing systems.

### Example 3: Abstract Class Implementing Interface

An abstract class can implement an interface without providing implementations for all methods, leaving the implementation to concrete subclasses.

```java
interface Player {
 void play();
 void pause();
 void stop();
}

abstract class MediaPlayer implements Player {
 protected String currentMedia;

 public MediaPlayer(String media) {
 this.currentMedia = media;
 }

 @Override
 public void play() {
 System.out.println("Playing: " + currentMedia);
 }

 // pause() and stop() left unimplemented - abstract class need not implement all
}

class AudioPlayer extends MediaPlayer {
 public AudioPlayer(String audioFile) {
 super(audioFile);
 }

 @Override
 public void pause() {
 System.out.println("Audio paused");
 }

 @Override
 public void stop() {
 System.out.println("Audio stopped");
 }
}

class VideoPlayer extends MediaPlayer {
 public VideoPlayer(String videoFile) {
 super(videoFile);
 }

 @Override
 public void pause() {
 System.out.println("Video paused");
 }

 @Override
 public void stop() {
 System.out.println("Video stopped");
 }
}
```

This example shows that an abstract class implementing an interface does not need to provide implementations for all interface methods. The concrete subclasses `AudioPlayer` and `VideoPlayer` must implement the remaining methods.

## Exam Tips

1. **Remember the syntax**: Abstract classes use the `abstract` keyword, and interfaces are declared with the `interface` keyword. For your university exam, always write correct syntax in code-based questions.

2. **Key differences between abstract classes and interfaces**: Abstract classes can have constructors and instance variables; interfaces cannot. A class can implement multiple interfaces but can extend only one class.

3. **Abstract methods cannot be**: `final`, `static`, `private`, or `synchronized` because they must be overridden by subclasses.

4. **Interface default methods**: Since Java 8, interfaces can have default methods with implementation using the `default` keyword. These methods can be overridden by implementing classes.

5. **Interface static methods**: Interfaces can have static methods that belong to the interface itself, not to implementing classes. They are called using `InterfaceName.methodName()`.

6. **Multiple inheritance through interfaces**: A class can implement multiple interfaces, achieving a form of multiple inheritance. This is a common exam question.

7. **Abstract class instantiation**: Remember that you cannot create an instance of an abstract class directly, but you can have a reference variable of abstract type pointing to concrete subclass objects.

8. **Interface variables**: All variables in an interface are implicitly `public`, `static`, and `final` (constants). You cannot have instance variables in an interface.

9. **Abstract class with constructors**: Even though abstract classes cannot be instantiated, they can have constructors that are called when subclass objects are created.

10. **Real-world analogy**: In the exam, if asked to explain abstraction, use real-world analogies like a car (you press accelerator without knowing engine internals) or ATM (you see screen without knowing database operations).
