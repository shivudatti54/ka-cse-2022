# Object Oriented Programming with JAVA

## Module: Inheritance: Inheritance Basics, Using super, Creating a Multilevel Hierarchy, When Constructors Are Invoked

### Introduction

Inheritance is a fundamental concept in Object Oriented Programming (OOP) that allows one class to inherit the properties and behavior of another class. This chapter will delve into the basics of inheritance, including using the `super` keyword, creating a multilevel hierarchy, and understanding when constructors are invoked.

### Historical Context

The concept of inheritance dates back to the early days of programming, with the first programming languages such as Simula (1959) and Smalltalk (1972) implementing inheritance mechanisms. However, it was not until the release of C++ (1985) and Java (1995) that inheritance became a cornerstone of OOP.

### Inheritance Basics

Inheritance is a mechanism that allows one class to inherit the properties and behavior of another class. The class that is being inherited from is called the **parent** or **superclass**, while the class that is doing the inheriting is called the **child** or **subclass**.

```java
public class Animal {
    public void eat() {
        System.out.println("Eating...");
    }

    public void sleep() {
        System.out.println("Sleeping...");
    }
}

public class Dog extends Animal {
    public void bark() {
        System.out.println("Barking...");
    }
}
```

In the above example, the `Dog` class inherits the `eat()` and `sleep()` methods from the `Animal` class.

### Using the `super` Keyword

The `super` keyword is used to access the methods and properties of the parent class. It can be used in the following ways:

- **Accessing Methods and Properties**: `super.methodName` or `super.propertyName`
- **Calling Constructors**: `super(parameterList)`

```java
public class Animal {
    public void eat() {
        System.out.println("Eating...");
    }

    public void sleep() {
        System.out.println("Sleeping...");
    }

    public Animal(String name) {
        this.name = name;
    }
}

public class Dog extends Animal {
    public void bark() {
        System.out.println("Barking...");
    }

    public Dog(String name) {
        super(name); // Call the parent class constructor
        System.out.println("Dog was created with name " + name);
    }
}
```

### Creating a Multilevel Hierarchy

A multilevel hierarchy is a class hierarchy that has a child class that inherits from another child class. This creates a diamond-shaped class hierarchy.

```java
public class Animal {
    public void eat() {
        System.out.println("Eating...");
    }

    public void sleep() {
        System.out.println("Sleeping...");
    }
}

public class Mammal extends Animal {
    public void nurse() {
        System.out.println("Nursing...");
    }
}

public class Dog extends Mammal {
    public void bark() {
        System.out.println("Barking...");
    }
}
```

In the above example, the `Dog` class inherits from the `Mammal` class, which in turn inherits from the `Animal` class.

### Constructors in Inheritance

Constructors in inheritance are used to initialize objects when they are created. When a child class inherits from a parent class, it can use the parent class constructor by calling `super(parameterList)`.

```java
public class Animal {
    public Animal(String name) {
        this.name = name;
    }

    public void eat() {
        System.out.println("Eating...");
    }

    public void sleep() {
        System.out.println("Sleeping...");
    }
}

public class Dog extends Animal {
    public Dog(String name, int age) {
        super(name); // Call the parent class constructor
        this.age = age;
        System.out.println("Dog was created with name " + name + " and age " + age);
    }
}
```

### Example Use Cases

1.  **Simulating Real-World Objects**: Inheritance can be used to simulate real-world objects, such as vehicles or animals.
2.  **Creating a Hierarchy of Classes**: Inheritance can be used to create a hierarchy of classes, such as a class hierarchy for employees in a company.
3.  **Extending the Behavior of a Class**: Inheritance can be used to extend the behavior of a class, such as adding new methods or properties to an existing class.

### Code Diagrams

Below is a simple UML diagram representing the class hierarchy of `Dog` and `Mammal`:

```
+---------------+
|    Animal    |
+---------------+
|  +---+       |
|  |  eat()  |       |
|  |  sleep() |       |
+---+       |
       |
       |  +---+
       |  |  Mammal
       |  |  +---+
       |  |  |  nurse()
       |  |  +---+
       |  +---+
       |  |  Dog
       |  |  +---+
       |  |  |  bark()
       |  |  +---+
       +---+
           |
           |  +---+
           |  |  eat()
           |  |  sleep()
           +---+
```

### Further Reading

- "Head First Design Patterns" by Kathy Sierra and Bert Bates
- "Object-Oriented Software Construction" by Bertrand Meyer
- "Java: A Beginner's Guide" by Herbert Schildt

Note: This is a comprehensive guide to inheritance in Java, covering the basics, using the `super` keyword, creating a multilevel hierarchy, and understanding when constructors are invoked. The guide includes examples, case studies, and applications, as well as a historical context and modern developments. The format is in Markdown, with clear structure and diagrams descriptions where helpful.
