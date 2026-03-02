# **Object Oriented Programming with JAVA**

## **Module: Introducing Classes**

### Class Fundamentals

In object-oriented programming, a class is a blueprint or a template that defines the characteristics and behaviors of an object. In Java, a class is essentially a collection of related data and methods that operate on that data.

#### Characteristics of a Class

- A class can have attributes (data) and methods (functions).
- Attributes are used to store the data of an object, while methods are used to perform actions on that data.
- A class can have constructors, which are special methods used to initialize objects.

#### Declaring Classes

In Java, classes are declared using the `class` keyword followed by the name of the class. Here's an example of a simple class:

```java
public class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void introduce() {
        System.out.println("Hello, my name is " + name + " and I am " + age + " years old.");
    }
}
```

#### Creating Objects

To create an object from a class, you need to use the `new` keyword followed by the class name. Here's an example:

```java
public class Main {
    public static void main(String[] args) {
        Person person = new Person("John Doe", 30);
        person.introduce();
    }
}
```

### Introducing Methods

Methods are functions that operate on the data of an object. They can take arguments (input values) and return values (output values).

#### Types of Methods

- **Instance Methods**: These methods belong to a class and operate on the data of an object. They are called on an object and do not belong to the class itself.
- **Static Methods**: These methods belong to a class and do not operate on the data of an object. They are called on the class itself and do not require an object to be created.

#### Method Parameters

Method parameters are the values passed to a method when it is called. Here's an example:

```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
}
```

#### Returning Values from Methods

Methods can return values using the `return` keyword. Here's an example:

```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
}
```

### Constructors

Constructors are special methods that are used to initialize objects when they are created. They have the same name as the class and do not have a return type.

#### Constructor Syntax

The constructor syntax is as follows:

```java
public class ClassName {
    public ClassName(parameterList) {
        // constructor code
    }
}
```

#### Constructor Parameters

Constructor parameters are the values passed to the constructor when the object is created.

#### Access Modifiers

The access modifier of a constructor determines the scope of the constructor. Here are the access modifiers used for constructors:

- **public**: Accessible from anywhere.
- **private**: Accessible only within the class itself.
- **protected**: Accessible within the class itself and its subclasses.

#### Default Constructor

A default constructor is a constructor without any parameters. Here's an example:

```java
public class Person {
    public Person() {
        System.out.println("Default constructor called.");
    }
}
```

#### Parameterized Constructor

A parameterized constructor is a constructor that takes parameters. Here's an example:

```java
public class Person {
    public Person(String name, int age) {
        System.out.println("Parameterized constructor called.");
    }
}
```

### The `this` Keyword

The `this` keyword is used to refer to the current object.

#### Using `this` Keyword

The `this` keyword can be used in various ways, including:

- **Reference to the current object**: `this.name`
- **Reference to the current constructor**: `this()` (overloading)
- **Accessing members of the superclass**: `super`

#### Example

```java
public class Animal {
    private String name;

    public Animal(String name) {
        this.name = name;
    }

    public void speak() {
        System.out.println("The animal makes a sound.");
    }
}

public class Dog extends Animal {
    public Dog(String name) {
        super(name); // using `this` to refer to the superclass
    }

    public void bark() {
        System.out.println("The dog barks.");
    }
}
```

### Garbage Collection

Garbage collection is a process that automatically manages memory in Java. It frees the memory occupied by objects that are no longer in use.

#### Garbage Collection Process

The garbage collection process involves the following steps:

1.  **Marking**: The garbage collector identifies the objects that are currently in use.
2.  **Sweeping**: The garbage collector identifies the objects that are not in use and frees their memory.

#### Types of Garbage Collection

There are two types of garbage collection:

- **Generational Garbage Collection**: This type of garbage collection divides objects into generations based on their lifetimes.
- **Concurrent Garbage Collection**: This type of garbage collection runs in parallel with the application.

#### Example

```java
public class Main {
    public static void main(String[] args) {
        Object obj = new Object();
        obj = null; // no longer in use
    }
}
```

In this example, the `obj` object is no longer in use, so it is eligible for garbage collection.

**Further Reading**

- [The Java Programming Language](https://docs.oracle.com/javase/tutorial/java/index.html)
- [Java Object-Oriented Programming](https://docs.oracle.com/javase/tutorial/java/concepts/index.html)
- [Garbage Collection in Java](https://docs.oracle.com/javase/8/docs/technotes/guides/clr/concepts-gc.html)

**Diagram Description**

Here's a diagram describing the garbage collection process:

```
                                      +---------------+
                                      |  Marking      |
                                      |  (Identify   |
                                      |   objects in |
                                      |   use)        |
                                      +---------------+
                                             |
                                             |
                                             v
                                      +---------------+
                                      |  Sweeping     |
                                      |  (Free memory |
                                      |   occupied by |
                                      |   not-in-use  |
                                      |   objects)     |
                                      +---------------+
                                             |
                                             |
                                             v
                                      +---------------+
                                      |  Garbage     |
                                      |  Collection  |
                                      |  (Free memory |
                                      |   occupied by|
                                      |   objects that|
                                      |   are no longer|
                                      |   in use)     |
                                      +---------------+
```
