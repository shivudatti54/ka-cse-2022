# Interfaces in Java

======================================================

## Introduction

---

In Java, an interface is a abstract class that can't be instantiated on its own and is used to achieve abstraction. It provides a blueprint for implementing classes to follow. In this topic, we will explore the key concepts of interfaces, default interface methods, use of static methods in an interface, and private interface methods.

## Definition and Characteristics

---

- An interface is a keyword used in Java to define a contract that must be implemented by any class that implements it.
- An interface is an abstract class and can't be instantiated.
- An interface can have multiple inheritance.
- An interface can have multiple methods and variables.
- A class can implement multiple interfaces.

### Key Characteristics of Interfaces

- Abstraction
- Multiple Inheritance
- Multiple Methods and Variables
- Can't be instantiated
- Can't have constructors

## Default Interface Methods

---

In Java 8 and later versions, default interface methods were introduced. These methods can be implemented in interfaces.

### Example

```java
public interface Shape {
    default void draw() {
        System.out.println("Drawing shape...");
    }

    void displayDetails();
}

public class Circle implements Shape {
    @Override
    public void displayDetails() {
        System.out.println("This is a circle.");
    }

    public static void main(String[] args) {
        Circle circle = new Circle();
        circle.draw(); // Output: Drawing shape...
        circle.displayDetails(); // Output: This is a circle.
    }
}
```

In the above example, the `draw()` method is a default interface method. This method is implemented in the `Shape` interface and can be overridden by any class implementing the `Shape` interface.

## Use of Static Methods in an Interface

---

In Java, static methods can be declared in interfaces. These methods can be static or non-static.

### Example

```java
public interface MathOperations {
    int add(int a, int b);
    int multiply(int a, int b);
}

public class MathCalculator implements MathOperations {
    @Override
    public int add(int a, int b) {
        return a + b;
    }

    @Override
    public int multiply(int a, int b) {
        return a * b;
    }

    public static void main(String[] args) {
        MathOperations mathOperations = new MathCalculator();
        System.out.println(mathOperations.add(10, 20)); // Output: 30
        System.out.println(mathOperations.multiply(10, 20)); // Output: 200
    }
}
```

In the above example, the `add()` and `multiply()` methods are static methods in the `MathOperations` interface. These methods can be called without creating an instance of the interface.

## Private Interface Methods

---

Java does not support private methods in interfaces. However, you can declare methods as private in the implementing class.

### Example

```java
public interface Shape {
    void displayDetails();
}

public class Circle implements Shape {
    private void printCircleDetails() {
        System.out.println("This is a circle.");
    }

    @Override
    public void displayDetails() {
        printCircleDetails();
    }

    public static void main(String[] args) {
        Circle circle = new Circle();
        circle.displayDetails(); // Output: This is a circle.
    }
}
```

In the above example, the `printCircleDetails()` method is a private method in the `Circle` class. This method is called in the `displayDetails()` method, which is an interface method.

### Best Practice

- Use default interface methods to provide a default implementation for methods.
- Use static methods in interfaces to provide utility methods that can be called without creating an instance.
- Avoid using private methods in interfaces. Instead, use private methods in the implementing classes.
