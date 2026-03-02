# Declaring Objects


## Table of Contents

- [Declaring Objects](#declaring-objects)
- [Introduction](#introduction)
- [Basic Syntax](#basic-syntax)
  - [Example](#example)
- [Declaring vs. Creating Objects](#declaring-vs-creating-objects)
  - [Example](#example)
- [Instantiating Objects](#instantiating-objects)
  - [Example](#example)
- [Importance of Declaring Objects](#importance-of-declaring-objects)
  - [Example](#example)
- [Comparison of Reference Variables and Objects](#comparison-of-reference-variables-and-objects)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

=====================================================

## Introduction

---

In Java, objects are the foundation of Object-Oriented Programming (OOP). Declaring objects is a crucial step in creating instances of classes that can be used in a Java program. In this topic, we will explore the purpose of declaring objects, the basic syntax, and the difference between declaring a reference variable and creating an object.

## Basic Syntax

---

The basic syntax for declaring an object in Java is:

```java
ClassName referenceVariable;
```

Here, `ClassName` is the name of the class, and `referenceVariable` is the name given to the object.

### Example

```java
public class Car {
 // class members
}

Car myCar;
```

In this example, `Car` is the class name, and `myCar` is the reference variable.

## Declaring vs. Creating Objects

---

Declaring an object does not create an object in memory. It only declares a reference variable that can hold the memory address of an object. To create an object, you need to use the `new` keyword and a class constructor.

### Example

```java
public class Car {
 public Car() {
 System.out.println("Car object created");
 }
}

Car myCar; // declaring an object
myCar = new Car(); // creating an object
```

In this example, `myCar` is declared as a reference variable, and then an object is created using the `new` keyword and the `Car` class constructor.

## Instantiating Objects

---

Instantiating an object means creating a new instance of a class. This can be done using the `new` keyword and a class constructor.

### Example

```java
public class Car {
 public Car(String color) {
 System.out.println("Car object created with color " + color);
 }
}

Car myCar = new Car("Red");
```

In this example, an object of the `Car` class is created with the color "Red" using the `new` keyword and the `Car` class constructor.

## Importance of Declaring Objects

---

Declaring objects is essential in OOP because it allows you to create instances of classes that can be used in a Java program. Without declaring objects, you cannot access the members of a class.

### Example

```java
public class Car {
 public void startEngine() {
 System.out.println("Engine started");
 }
}

Car myCar = new Car();
myCar.startEngine(); // accessing the startEngine() method
```

In this example, an object of the `Car` class is created, and the `startEngine()` method is accessed using the `myCar` reference variable.

## Comparison of Reference Variables and Objects

---

|                       | Reference Variable             | Object                                          |
| --------------------- | ------------------------------ | ----------------------------------------------- |
| **Declaration**       | `ClassName referenceVariable;` | `referenceVariable = new ClassName();`          |
| **Memory Allocation** | No memory allocated            | Memory allocated for the object                 |
| **Accessing Members** | Cannot access members directly | Can access members using the reference variable |

## Exam Tips

---

- Pay attention to the syntax used for declaring objects in Java.
- Understand the difference between object declaration and object creation.
- Make sure to declare objects before using them in a Java program.

## Key Takeaways

---

- Declaring objects is essential in OOP.
- The basic syntax for declaring an object is `ClassName referenceVariable;`.
- Declaring an object does not create an object in memory.
- Instantiating an object means creating a new instance of a class.
- Declaring objects allows you to access the members of a class.
