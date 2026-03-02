# **Introducing Methods, Constructors, The `this` Keyword, Garbage Collection**

## **Table of Contents**

1. [Introduction to Methods](#introduction-to-methods)
2. [Constructors](#constructors)
3. [The `this` Keyword](#the-this-keyword)
4. [Garbage Collection](#garbage-collection)

### Introduction to Methods

---

A method is a block of code that performs a specific task within a class. It is a block of code that can be executed multiple times from different parts of a program.

#### Key Concepts:

- **Method Signature**: A method signature is the combination of return type and method name.
- **Method Body**: The method body contains the code that is executed when the method is called.

### Constructors

---

A constructor is a special method that is used to initialize objects when they are created. It has the same name as the class and does not have a return type.

#### Key Points:

- **Constructor Signature**: A constructor signature is similar to a method signature but does not have a return type.
- **Default Constructor**: A default constructor is a special constructor that does not take any arguments and is used to initialize objects with default values.

### The `this` Keyword

---

The `this` keyword is used to refer to the current object of a class. It is used in methods to refer to the object that the method is currently being executed on.

#### Key Concepts:

- **This Keyword**: The `this` keyword is used to refer to the current object of a class.
- **This Keyword in Constructors**: The `this` keyword is used in constructors to refer to the object being created.
- **This Keyword in Methods**: The `this` keyword is used in methods to refer to the object that the method is currently being executed on.

### Garbage Collection

---

Garbage collection is a process that automatically frees memory occupied by objects that are no longer in use. It is used to prevent memory leaks in programming languages.

#### Key Points:

- **Garbage Collection**: Garbage collection is a process that automatically frees memory occupied by objects that are no longer in use.
- **Garbage Collection in Java**: Java uses a garbage collection algorithm called generational garbage collection to free memory occupied by objects that are no longer in use.

### Example Code

---

```java
public class Person {
    private String name;
    private int age;

    // Constructor
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Method
    public void displayDetails() {
        System.out.println("Name: " + this.name);
        System.out.println("Age: " + this.age);
    }
}

public class Main {
    public static void main(String[] args) {
        // Create a new object of the Person class
        Person person = new Person("John Doe", 30);

        // Call the displayDetails method on the person object
        person.displayDetails();
    }
}
```

In this example, the `Person` class has a constructor that takes two arguments: `name` and `age`. The `this` keyword is used in the constructor to refer to the object being created. The `displayDetails` method is used to display the details of the person object. The `this` keyword is used in the method to refer to the object that the method is currently being executed on.
