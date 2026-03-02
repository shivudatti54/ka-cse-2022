# **Chapter 2: Object-Oriented Programming with JAVA**

## **2.1 Introduction to Object-Oriented Programming (OOP)**

Object-Oriented Programming (OOP) is a programming paradigm that revolves around the concept of objects and classes. It is a way of designing and organizing code that simulates real-world objects and systems.

### Key Concepts:

- **Object**: An object is an instance of a class that has its own set of attributes (data) and methods (functions).
- **Class**: A class is a blueprint or a template that defines the characteristics and behavior of an object.
- **Inheritance**: Inheritance is a mechanism that allows one class to inherit the properties and behavior of another class.
- **Polymorphism**: Polymorphism is the ability of an object to take on multiple forms, depending on the context in which it is used.

### Benefits of OOP:

- **Modularity**: OOP allows for the creation of modular code that is easy to maintain and modify.
- **Reusability**: OOP enables the reuse of code, reducing the amount of code that needs to be written and maintained.
- **Abstraction**: OOP provides abstraction, which allows developers to focus on the essential features of an object or system, rather than its implementation details.

### Types of OOP Paradigms:

- **Classical OOP**: Classical OOP is the traditional approach to OOP, which emphasizes the use of classes and objects to design and implement software systems.
- **Object-Oriented OOP**: Object-Oriented OOP is a variant of classical OOP that emphasizes the use of objects and their interactions to design and implement software systems.

### Abstraction:

Abstraction is a fundamental concept in OOP that allows developers to focus on the essential features of an object or system, rather than its implementation details. Abstraction involves the exposure of only the necessary information to the outside world, while hiding the internal details.

### The Three OOP Principles:

The Three OOP Principles are:

- **Encapsulation**: Encapsulation is the concept of bundling data and methods that operate on that data within a single unit, called a class or object.
- **Abstraction**: Abstraction is the concept of exposing only the necessary information to the outside world, while hiding the internal details.
- **Inheritance**: Inheritance is the concept of creating a new class based on an existing class, which inherits the properties and behavior of the parent class.

### Benefits of the Three OOP Principles:

- **Modularity**: The Three OOP Principles enable the creation of modular code that is easy to maintain and modify.
- **Reusability**: The Three OOP Principles enable the reuse of code, reducing the amount of code that needs to be written and maintained.
- **Flexibility**: The Three OOP Principles enable developers to create flexible and adaptable software systems that can respond to changing requirements.

### Example:

```java
// Classical OOP Example

public class Employee {
    private String name;
    private int age;

    public Employee(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void displayDetails() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

public class Manager extends Employee {
    private String department;

    public Manager(String name, int age, String department) {
        super(name, age);
        this.department = department;
    }

    public void displayDetails() {
        super.displayDetails();
        System.out.println("Department: " + department);
    }
}

public class Main {
    public static void main(String[] args) {
        Employee employee = new Employee("John Doe", 30);
        Manager manager = new Manager("Jane Doe", 35, "Sales");

        employee.displayDetails();
        manager.displayDetails();
    }
}
```

In this example, we use classical OOP to define an `Employee` class and a `Manager` class that extends the `Employee` class. The `Manager` class inherits the properties and behavior of the `Employee` class and adds its own properties and behavior. The `displayDetails` method is overridden in the `Manager` class to include the department information.

### Polymorphism:

Polymorphism is the ability of an object to take on multiple forms, depending on the context in which it is used. In OOP, polymorphism is achieved through method overriding or method overloading.

### Example:

```java
// Polymorphism Example

class Animal {
    public void sound() {
        System.out.println("The animal makes a sound.");
    }
}

class Dog extends Animal {
    public void sound() {
        System.out.println("The dog barks.");
    }
}

class Cat extends Animal {
    public void sound() {
        System.out.println("The cat meows.");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal animal = new Dog();
        animal.sound(); // Output: The dog barks.

        animal = new Cat();
        animal.sound(); // Output: The cat meows.
    }
}
```

In this example, we define an `Animal` class with a `sound` method and two subclasses `Dog` and `Cat` that override the `sound` method. We create instances of the `Dog` and `Cat` classes and assign them to an `Animal` reference variable. When we call the `sound` method on the `Animal` reference variable, the correct implementation of the `sound` method is called based on the actual type of the object.
