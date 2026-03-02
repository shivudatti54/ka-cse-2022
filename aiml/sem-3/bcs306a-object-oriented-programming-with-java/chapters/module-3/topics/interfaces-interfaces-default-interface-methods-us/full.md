# Interfaces in Java

=====================================================

## Introduction

---

In Java, an interface is a abstract class that can't be instantiated on its own and is used to define a contract that must be implemented by any class that implements it. Interfaces are a way to define a common set of methods that must be implemented by any class that implements the interface. In this topic, we will cover the basics of interfaces, default interface methods, using static methods in an interface, and private interface methods.

## Historical Context

---

The concept of interfaces dates back to the early days of object-oriented programming. The first interfaces were introduced in the Smalltalk programming language in the 1970s. Java's interfaces were inspired by Smalltalk's interfaces and were introduced in the Java Language Specification (JLS) in 1995.

## Basic Syntax of Interfaces

---

An interface in Java is defined using the `interface` keyword followed by the name of the interface. The interface can contain a set of methods, constants, and fields.

```java
public interface MyInterface {
    void myMethod();
}
```

## Abstract Classes vs Interfaces

---

While both abstract classes and interfaces are used to define blueprints for classes, they serve different purposes.

- An abstract class can have both abstract and non-abstract methods and fields.
- An interface can only have abstract methods and fields.

```java
public abstract class AbstractClass {
    public abstract void myMethod();
}

public interface Interface {
    void myMethod();
}
```

## Implementing Interfaces

---

To implement an interface, a class must use the `implements` keyword followed by the name of the interface.

```java
public class MyClass implements MyInterface {
    public void myMethod() {
        System.out.println("Implementing myMethod");
    }
}
```

## Default Interface Methods

---

Java 8 introduced default interface methods, which allow interfaces to provide default implementations for certain methods.

```java
public interface MyInterface {
    default void myMethod() {
        System.out.println("Default implementation of myMethod");
    }
}
```

In this example, the `myMethod()` method in the `MyInterface` interface has a default implementation.

## Static Methods in Interfaces

---

Java 8 also introduced static methods in interfaces, which can be used to provide utility methods that can be used by any class that implements the interface.

```java
public interface MyInterface {
    static void myStaticMethod() {
        System.out.println("My static method");
    }
}
```

In this example, the `myStaticMethod()` method in the `MyInterface` interface is a static method.

## Private Interface Methods

---

Java does not support private interface methods. However, you can use the `package-private` access modifier to make a method in an interface accessible only within the same package.

```java
public interface MyInterface {
    package-private void myPrivateMethod();
}
```

In this example, the `myPrivateMethod()` method in the `MyInterface` interface is package-private.

## Multilevel Hierarchy with Interfaces

---

Interfaces can be used to create a multilevel hierarchy of classes. A class can implement multiple interfaces.

```java
public interface MyInterface1 {
    void myMethod1();
}

public interface MyInterface2 extends MyInterface1 {
    void myMethod2();
}

public class MyClass implements MyInterface2 {
    public void myMethod1() {
        System.out.println("Implementing myMethod1");
    }

    public void myMethod2() {
        System.out.println("Implementing myMethod2");
    }
}
```

In this example, the `MyClass` class implements the `MyInterface2` interface, which in turn implements the `MyInterface1` interface.

## Example Use Case

---

Here is an example of using interfaces to define a contract for a payment gateway.

```java
public interface PaymentGateway {
    void processPayment(double amount);
}

public class PayPal implements PaymentGateway {
    public void processPayment(double amount) {
        System.out.println("Processing payment using PayPal");
    }
}

public class Stripe implements PaymentGateway {
    public void processPayment(double amount) {
        System.out.println("Processing payment using Stripe");
    }
}

public class PaymentProcessor {
    public void processPayment(PaymentGateway gateway, double amount) {
        gateway.processPayment(amount);
    }
}

public class Main {
    public static void main(String[] args) {
        PaymentProcessor processor = new PaymentProcessor();
        processor.processPayment(new PayPal(), 100.0);
        processor.processPayment(new Stripe(), 50.0);
    }
}
```

In this example, the `PaymentGateway` interface defines the contract for payment processing. The `PayPal` and `Stripe` classes implement the `PaymentGateway` interface to provide their own implementation of payment processing. The `PaymentProcessor` class uses the `PaymentGateway` interface to process payments using any of the implementing classes.

## Further Reading

---

- [Java API Documentation](https://docs.oracle.com/javase/8/docs/api/java/lang/Interface.html)
- [Java Tutorials: Interfaces](https://docs.oracle.com/javase/tutorial/java/concepts/index.html)
- [Java 8 In Action: Interfaces](https://www.baeldung.com/java-8-interfaces)
- [Interface vs Abstract Class in Java](https://www.geeksforgeeks.org/interface-vs-abstract-class-in-java/)
