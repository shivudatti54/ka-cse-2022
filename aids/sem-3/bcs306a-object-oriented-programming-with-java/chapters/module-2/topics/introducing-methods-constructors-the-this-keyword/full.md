# **Object Oriented Programming with JAVA**

## **Module: Introducing Classes: Class Fundamentals, Declaring Objects, Assigning Object Reference Variables**

### Introduction

In this module, we will delve into the fundamental concepts of Java Object Oriented Programming (OOP). We will explore the basics of classes, objects, methods, constructors, the `this` keyword, and garbage collection. These concepts form the foundation of Java programming and are essential for any aspiring developer.

### Historical Context

Object Oriented Programming was first introduced by Alan Kay in 1968. The idea was to create a programming paradigm that allowed for the creation of reusable, modular, and maintainable code. The concept of objects and classes was further developed by Larry Wall, who created the Perl programming language.

In Java, the Object Oriented Programming model was implemented by James Gosling and his team at Sun Microsystems in the mid-1990s. Java's OOP features were designed to be platform-independent, allowing Java programs to run on any device that could execute Java bytecode.

### Class Fundamentals

A class in Java is a blueprint or a template that defines the properties and behavior of an object. It is essentially a design pattern or a template that is used to create objects.

**Class Declaration**

A class is declared in Java using the `class` keyword followed by the name of the class.

```java
public class MyClass {
    // class members
}
```

The `public` access modifier means that the class can be accessed from any part of the program.

**Class Members**

Class members are data and methods that are defined within a class. There are two types of class members:

- **Instance Variables**: These are also known as data members or attributes. They are associated with each object that is created from the class.
- **Methods**: These are functions that belong to a class and are used to perform specific tasks.

**Constructors**

A constructor is a special method that is used to initialize an object when it is created. It has the same name as the class and does not have a return type.

```java
public class MyClass {
    private String name;

    public MyClass(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}
```

In this example, the `MyClass` constructor takes a `name` parameter and assigns it to the `name` instance variable.

**The `this` Keyword**

The `this` keyword is used to refer to the current object. It is used to access class members, methods, and fields from within a constructor or method.

```java
public class MyClass {
    private String name;

    public MyClass(String name) {
        this.name = name;
    }

    public void printName() {
        System.out.println(this.name);
    }
}
```

In this example, the `printName()` method uses the `this` keyword to access the `name` instance variable.

### Methods

Methods are functions that belong to a class and are used to perform specific tasks. They can take arguments and return values.

**Method Declaration**

A method is declared in Java using the `public` access modifier, the return type, the method name, and the parameter list.

```java
public class MyClass {
    public void printName(String name) {
        System.out.println(name);
    }
}
```

In this example, the `printName()` method takes a `name` parameter and prints it to the console.

### Garbage Collection

Garbage collection is a mechanism that automatically frees up memory occupied by objects that are no longer in use. It is an essential feature of Java because it prevents memory leaks and reduces the risk of application crashes.

**How Garbage Collection Works**

Garbage collection works by identifying objects that are no longer referenced and freeing up their memory. Here's a step-by-step overview of the garbage collection process:

1.  **Object Creation**: An object is created and assigned to a reference variable.
2.  **Object Usage**: The object is used and its memory is allocated.
3.  **Object Reference Removal**: The object reference is removed from the code.
4.  **Garbage Collection Trigger**: The Java Virtual Machine (JVM) triggers garbage collection when the object is no longer referenced.
5.  **Memory Deallocation**: The JVM frees up the memory occupied by the object.

### Example Use Case

Here's an example use case that demonstrates the concepts we've covered so far:

```java
public class MyClass {
    private String name;

    public MyClass(String name) {
        this.name = name;
    }

    public void printName() {
        System.out.println(this.name);
    }

    public static void main(String[] args) {
        MyClass obj = new MyClass("John");
        obj.printName(); // prints "John"
        obj = null; // removes the reference to the object
        System.gc(); // triggers garbage collection
        // obj is no longer referenced, garbage collection will free up its memory
    }
}
```

In this example, we create an object `obj` and assign it a reference. We use the object and print its name. We then remove the reference to the object and trigger garbage collection. The JVM will free up the memory occupied by the object.

### Further Reading

- "Head First Java" by Kathy Sierra and Bert Bates
- "Java: A Beginner's Guide" by Herbert Schildt
- "Java Programming: From Problem Analysis" by Marvin J. Harrell Jr.
- Oracle's Java Documentation: Class and Method Declarations
- Oracle's Java Documentation: Garbage Collection

### Diagrams

Here's a diagram that illustrates the concept of garbage collection:

```
+---------------+
|  Object Creation  |
+---------------+
          |
          |
          v
+---------------+
|  Object Usage  |
+---------------+
          |
          |
          v
+---------------+
|  Object Reference  |
|  Removal         |
+---------------+
          |
          |
          v
+---------------+
|  Garbage Collection  |
|  Triggered          |
+---------------+
          |
          |
          v
+---------------+
|  Memory Deallocation  |
+---------------+
```

This diagram shows the object creation, usage, reference removal, and garbage collection process.
