# Creating a Multilevel Hierarchy

## Table of Contents

- [Creating a Multilevel Hierarchy](#creating-a-multilevel-hierarchy)
- [Overview of Multilevel Hierarchy](#overview-of-multilevel-hierarchy)
- [Components of a Multilevel Hierarchy](#components-of-a-multilevel-hierarchy)
  - [Example of a Multilevel Hierarchy](#example-of-a-multilevel-hierarchy)
- [Constructors in a Multilevel Hierarchy](#constructors-in-a-multilevel-hierarchy)
  - [Using `super()` to Call Superclass Constructors](#using-super-to-call-superclass-constructors)
- [Method Overriding in a Multilevel Hierarchy](#method-overriding-in-a-multilevel-hierarchy)
  - [Example of Method Overriding](#example-of-method-overriding)
- [Comparison of Single-Level Inheritance and Multilevel Inheritance](#comparison-of-single-level-inheritance-and-multilevel-inheritance)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

## Overview of Multilevel Hierarchy

A multilevel hierarchy in object-oriented programming is a structure where a subclass is also a superclass, creating multiple levels of inheritance. This allows for a more complex and nuanced representation of relationships between classes.

## Components of a Multilevel Hierarchy

A multilevel hierarchy consists of at least three classes:

- **Grandparent Class (Topmost Superclass)**: The grandparent class is the topmost superclass and has no parent class. It is the highest level in the hierarchy.
- **Parent Class (Subclass and Superclass)**: The parent class is both a subclass of the grandparent class and a superclass of the child class. It inherits properties and behavior from the grandparent class and passes them down to the child class.
- **Child Class (Bottommost Subclass)**: The child class is the bottommost subclass and has no subclass of its own. It inherits properties and behavior from both the parent class and the grandparent class.

### Example of a Multilevel Hierarchy

Suppose we have a hierarchy of vehicles:

- **Vehicle (Grandparent Class)**: The Vehicle class is the topmost superclass and has properties such as color and speed.
- **Car (Parent Class)**: The Car class is a subclass of Vehicle and adds properties such as number of doors and engine type. It is also a superclass of the SportsCar class.
- **SportsCar (Child Class)**: The SportsCar class is a subclass of Car and adds properties such as horsepower and turbocharger.

```java
// Grandparent Class
class Vehicle {
 private String color;
 private int speed;

 public Vehicle(String color, int speed) {
 this.color = color;
 this.speed = speed;
 }

 public void displayDetails() {
 System.out.println("Color: " + color);
 System.out.println("Speed: " + speed);
 }
}

// Parent Class
class Car extends Vehicle {
 private int numberOfDoors;
 private String engineType;

 public Car(String color, int speed, int numberOfDoors, String engineType) {
 super(color, speed);
 this.numberOfDoors = numberOfDoors;
 this.engineType = engineType;
 }

 public void displayCarDetails() {
 super.displayDetails();
 System.out.println("Number of Doors: " + numberOfDoors);
 System.out.println("Engine Type: " + engineType);
 }
}

// Child Class
class SportsCar extends Car {
 private int horsepower;
 private boolean turbocharger;

 public SportsCar(String color, int speed, int numberOfDoors, String engineType, int horsepower, boolean turbocharger) {
 super(color, speed, numberOfDoors, engineType);
 this.horsepower = horsepower;
 this.turbocharger = turbocharger;
 }

 public void displaySportsCarDetails() {
 super.displayCarDetails();
 System.out.println("Horsepower: " + horsepower);
 System.out.println("Turbocharger: " + turbocharger);
 }
}
```

## Constructors in a Multilevel Hierarchy

In a multilevel hierarchy, constructors are called in the following order:

1. The grandparent class constructor is called first.
2. The parent class constructor is called next.
3. The child class constructor is called last.

This order ensures that the properties and behavior of the superclasses are initialized before the subclass is initialized.

### Using `super()` to Call Superclass Constructors

The `super()` keyword is used to call the superclass constructor from a subclass constructor. This is necessary to ensure that the superclass properties are initialized before the subclass properties.

```java
// Parent Class
class Car extends Vehicle {
 private int numberOfDoors;
 private String engineType;

 public Car(String color, int speed, int numberOfDoors, String engineType) {
 super(color, speed); // Calls the Vehicle class constructor
 this.numberOfDoors = numberOfDoors;
 this.engineType = engineType;
 }
}
```

## Method Overriding in a Multilevel Hierarchy

Method overriding occurs when a subclass provides a different implementation of a method that is already defined in its superclass. In a multilevel hierarchy, method overriding can occur at multiple levels.

### Example of Method Overriding

Suppose we have a hierarchy of shapes:

- **Shape (Grandparent Class)**: The Shape class has a method called `area()` that calculates the area of the shape.
- **Rectangle (Parent Class)**: The Rectangle class overrides the `area()` method to calculate the area of a rectangle.
- **Square (Child Class)**: The Square class overrides the `area()` method to calculate the area of a square.

```java
// Grandparent Class
class Shape {
 public double area() {
 return 0;
 }
}

// Parent Class
class Rectangle extends Shape {
 private double length;
 private double width;

 public Rectangle(double length, double width) {
 this.length = length;
 this.width = width;
 }

 @Override
 public double area() {
 return length * width;
 }
}

// Child Class
class Square extends Rectangle {
 private double side;

 public Square(double side) {
 super(side, side);
 this.side = side;
 }

 @Override
 public double area() {
 return side * side;
 }
}
```

## Comparison of Single-Level Inheritance and Multilevel Inheritance

|                      | Single-Level Inheritance      | Multilevel Inheritance         |
| -------------------- | ----------------------------- | ------------------------------ |
| **Number of Levels** | Only one level of inheritance | Multiple levels of inheritance |
| **Complexity**       | Less complex                  | More complex                   |
| **Reusability**      | Limited reusability           | Higher reusability             |
| **Example**          | Animal -> Dog                 | Animal -> Mammal -> Dog        |

## Exam Tips

- Be able to identify and describe the relationships between classes in a multilevel hierarchy.
- Understand how inheritance works in a multilevel hierarchy and how subclasses can add new properties and behavior or override those inherited from their superclasses.
- Be able to explain the order in which constructors are called in a multilevel hierarchy.
- Understand how method overriding works in a multilevel hierarchy and be able to provide examples.

## Key Takeaways

- A multilevel hierarchy is a structure where a subclass is also a superclass, creating multiple levels of inheritance.
- The grandparent class is the topmost superclass, the parent class is both a subclass and a superclass, and the child class is the bottommost subclass.
- Constructors are called in the order of grandparent class, parent class, and child class.
- Method overriding can occur at multiple levels in a multilevel hierarchy.
