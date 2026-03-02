# **Chapter 2: Object-Oriented Programming with Java**

## **2.1 Introduction to Object-Oriented Programming**

Object-Oriented Programming (OOP) is a programming paradigm that revolves around the concept of objects and classes. It provides a practical way to organize and structure code, making it easier to maintain and modify.

### Key Paradigms of OOP

- **Class-Based Paradigm (Traditional OOP):** This paradigm is based on the concept of classes and objects. It provides a blueprint for creating objects that have their own characteristics and behaviors.
- **Object-Based Paradigm:** This paradigm focuses on the objects that are created from classes. It provides a more flexible and dynamic way of programming.

### Abstraction

Abstraction is a fundamental concept in OOP that allows developers to show only the necessary information to the outside world while hiding the internal details. It is achieved through encapsulation, inheritance, and polymorphism.

#### Definition:

Abstraction is the process of showing only the necessary information to the outside world while hiding the internal details.

#### Example:

Consider a car. A car has internal components such as engine, transmission, and brakes, but when you interact with a car, you only see the external features such as wheels, steering wheel, and gearshift. Abstraction helps to hide the internal details and show only the necessary information.

### The Three OOP Concepts

The three core concepts of OOP are:

- **Encapsulation:** The process of bundling data and methods that operate on that data into a single unit, called a class or object.
- **Inheritance:** The process of creating a new class based on an existing class, inheriting its properties and behaviors.
- **Polymorphism:** The ability of an object to take on multiple forms, depending on the context in which it is used.

#### Definition:

Polymorphism is the ability of an object to take on multiple forms, depending on the context in which it is used.

#### Example:

Consider a shape class with subclasses such as rectangle, circle, and triangle. All shapes can be drawn using the draw method, but the actual drawing process may vary depending on the shape. This is an example of polymorphism.

### Benefits of OOP

- **Modularity:** OOP allows developers to create self-contained modules that can be easily maintained and modified.
- **Reusability:** OOP enables developers to reuse code by creating classes and objects that can be used in multiple contexts.
- **Flexibility:** OOP provides a flexible way of programming that allows developers to change the behavior of objects and classes at runtime.

```markdown
**Key Concepts:**

- **Abstraction:** The process of showing only the necessary information to the outside world while hiding the internal details.
- **Encapsulation:** The process of bundling data and methods that operate on that data into a single unit, called a class or object.
- **Inheritance:** The process of creating a new class based on an existing class, inheriting its properties and behaviors.
- **Polymorphism:** The ability of an object to take on multiple forms, depending on the context in which it is used.
```

# **2.2 OOP in Java**

Java is a programming language that supports object-oriented programming. It provides a wide range of features and tools to help developers create object-oriented programs.

### Key Features of Java OOP

- **Classes and Objects:** Java supports the creation of classes and objects that have their own characteristics and behaviors.
- **Inheritance:** Java supports inheritance, which allows developers to create new classes based on existing classes.
- **Polymorphism:** Java supports polymorphism, which allows developers to create objects that can take on multiple forms depending on the context in which they are used.
- **Encapsulation:** Java supports encapsulation, which allows developers to bundle data and methods that operate on that data into a single unit, called a class or object.

### Example of Java OOP

```java
public class Car {
    private String color;
    private int speed;

    public Car(String color, int speed) {
        this.color = color;
        this.speed = speed;
    }

    public void accelerate() {
        speed++;
    }

    public void brake() {
        speed--;
    }

    public String getColor() {
        return color;
    }

    public int getSpeed() {
        return speed;
    }
}

public class ElectricCar extends Car {
    public ElectricCar(String color, int speed) {
        super(color, speed);
    }

    public void charge() {
        speed += 10;
    }
}
```

In this example, we have a `Car` class that has properties such as `color` and `speed`, and methods such as `accelerate` and `brake`. We also have an `ElectricCar` class that extends the `Car` class and adds a new method called `charge`. This is an example of inheritance and polymorphism in Java.
