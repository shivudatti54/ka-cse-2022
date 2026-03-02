# Object Oriented Programming with JAVA

## Module: Inheritance: Inheritance Basics, Using super, Creating a Multilevel Hierarchy, When Constructors Are Invoked

Inheritance is a fundamental concept in Object Oriented Programming (OOP) that allows one class to inherit the properties and behavior of another class. This study material will cover the basics of inheritance, using the `super` keyword, creating a multilevel hierarchy, and when constructors are invoked.

### What is Inheritance?

Inheritance is a mechanism that allows one class to inherit the attributes and methods of another class. The class that is being inherited from is called the parent or superclass, while the class that is doing the inheriting is called the child or subclass.

### Types of Inheritance

There are three types of inheritance:

- **Single Inheritance**: A child class inherits from a single parent class.
- **Multilevel Inheritance**: A child class inherits from a parent class that itself inherits from another parent class.
- **Hierarchical Inheritance**: Multiple child classes inherit from a single parent class.

### Using the `super` Keyword

The `super` keyword is used to access the parent class's members from a child class. The `super` keyword can be used in the following ways:

- To call a parent class's constructor: `super()`
- To access a parent class's member variable: `super.var_name`
- To call a parent class's member method: `super.method_name()`

### Creating a Multilevel Hierarchy

A multilevel hierarchy is created when a child class inherits from a parent class that itself inherits from another parent class. Here's an example:

```java
// Parent class
class Animal {
    void eat() {
        System.out.println("Eating...");
    }
}

// Parent class of Animal
class Mammal extends Animal {
    void walk() {
        System.out.println("Walking...");
    }
}

// Child class of Mammal
class Dog extends Mammal {
    void bark() {
        System.out.println("Barking...");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();  // Output: Eating...
        dog.walk(); // Output: Walking...
        dog.bark(); // Output: Barking...
    }
}
```

In this example, `Dog` is a child class of `Mammal`, which is a child class of `Animal`.

### When Constructors Are Invoked

Constructors are special methods that are called when an object is created. The constructor of the parent class is invoked before the constructor of the child class. Here's an example:

```java
// Parent class
class Animal {
    Animal() {
        System.out.println("Animal constructor invoked");
    }
}

// Child class
class Dog extends Animal {
    Dog() {
        System.out.println("Dog constructor invoked");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog();
    }
}
```

In this example, the `Animal` constructor is invoked before the `Dog` constructor.

### Key Concepts

- Inheritance is a mechanism that allows one class to inherit the properties and behavior of another class.
- The `super` keyword is used to access the parent class's members from a child class.
- A multilevel hierarchy is created when a child class inherits from a parent class that itself inherits from another parent class.
- Constructors are special methods that are called when an object is created, and the constructor of the parent class is invoked before the constructor of the child class.
