# Inheritance Basics

======================

## What is Inheritance?

---

Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows one class to inherit the properties and behavior of another class. The class that is being inherited from is called the **superclass** or **parent class**, while the class that does the inheriting is called the **subclass** or **child class**.

## Benefits of Inheritance

---

- **Code Reusability**: Inheritance allows us to reuse code from the superclass in the subclass, reducing code duplication.
- **Easier Maintenance**: Changes to the superclass are automatically reflected in the subclass, making maintenance easier.
- **Improved Readability**: Inheritance helps to organize code into a hierarchical structure, making it easier to understand and navigate.

## Using the `super` Keyword

---

The `super` keyword is used to access the members (methods and variables) of the superclass from a subclass. There are two types of `super` keywords:

- **Upcasting**: `super` is used to access the members of the superclass from a subclass. This is done using the `super` keyword followed by the member name.
- **Downcasting**: `super` is used to access the members of the superclass from a subclass. This is done using the `super` keyword followed by the member name and then the class name.

### Example:

```java
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound.");
    }
}

public class Dog extends Animal {
    public void sound() {
        System.out.println("The dog barks.");
        super.sound(); // Upcasting
    }
}
```

## Creating a Multilevel Hierarchy

---

A multilevel hierarchy is a class hierarchy where a subclass is a subclass of another subclass. This creates a nested hierarchy of classes.

### Example:

```java
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound.");
    }
}

public class Mammal extends Animal {
    public void feedMe() {
        System.out.println("I am a mammal and I need food.");
    }
}

public class Dog extends Mammal {
    public void bark() {
        System.out.println("I am a dog and I bark.");
    }
}
```

## Constructors in Inheritance

---

When a subclass inherits a constructor from the superclass, it should be called using the `super` keyword. If a subclass does not explicitly call the superclass constructor, the compiler automatically calls it.

### Example:

```java
public class Animal {
    public Animal() {
        System.out.println("Animal constructor called.");
    }
}

public class Dog extends Animal {
    public Dog() {
        System.out.println("Dog constructor called.");
    }
}
```

In this example, the `Dog` class calls both its own constructor and the `Animal` constructor using the `super` keyword.
