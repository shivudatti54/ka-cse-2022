# **Interfaces: Interfaces, Default Interface Methods, Use static Methods in an Interface, Private Interface Methods**

## **Introduction**

In Object Oriented Programming (OOP) with Java, an interface is a abstract concept that defines a contract between classes. It provides a blueprint for implementing a set of methods, which must be implemented by any class that implements the interface. In this study material, we will explore the different aspects of interfaces in Java, including default interface methods, static methods in an interface, and private interface methods.

## **What is an Interface?**

An interface is a abstract class that cannot be instantiated and provides a set of methods that must be implemented by any class that implements the interface.

### Characteristics of an Interface

- An interface cannot be instantiated.
- An interface cannot have a constructor.
- An interface cannot have a private constructor.
- An interface cannot have a private method or variable.
- An interface does not have a body.
- An interface can have a default method (introduced in Java 8).

## **Default Interface Methods**

Java 8 introduced default methods in interfaces, which allows interfaces to provide default implementations for methods. These methods can be overridden by classes that implement the interface.

### Characteristics of Default Interface Methods

- A default method is a method declared in an interface.
- A default method can be overridden by a class that implements the interface.
- A default method can be called without creating an instance of the interface.

**Example of a Default Interface Method**

```java
public interface Animal {
    void sound(); // default method

    default void makeSound() {
        System.out.println("The animal makes a sound.");
    }
}

class Dog implements Animal {
    @Override
    public void sound() {
        System.out.println("The dog barks.");
    }

    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.sound(); // Output: The dog barks.
        dog.makeSound(); // Output: The animal makes a sound.
    }
}
```

## **Use static Methods in an Interface**

In Java, an interface can have static methods, which can be called without creating an instance of the interface.

### Characteristics of Static Methods in an Interface

- A static method is a method declared in an interface.
- A static method belongs to the interface itself, not to any class.
- A static method can be called without creating an instance of the interface.

**Example of a Static Method in an Interface**

```java
public interface MathOperations {
    int add(int a, int b); // default method
    static int multiply(int a, int b) {
        return a * b;
    }
}

public class Main {
    public static void main(String[] args) {
        MathOperations ops = new MathOperations() {
            @Override
            public int add(int a, int b) {
                return a + b;
            }
        };
        System.out.println(ops.add(2, 3)); // Output: 5
        System.out.println(MathOperations.multiply(2, 3)); // Output: 6
    }
}
```

## **Private Interface Methods**

Java does not support private methods in interfaces. Any method declared in an interface is implicitly public.

### Characteristics of Private Interface Methods

- Java does not support private methods in interfaces.
- Any method declared in an interface is implicitly public.

## **Conclusion**

In conclusion, interfaces in Java provide a way to define a contract between classes. They can have default methods, static methods, and cannot have a private constructor or variable. Understanding the characteristics of interfaces and their methods is essential for writing effective and efficient code in Java.
