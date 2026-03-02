# Using Super

## Table of Contents

- [Using Super](#using-super)
- [Introduction](#introduction)
- [What is Super?](#what-is-super)
  - [Example: Using Super to Call Superclass Constructor](#example-using-super-to-call-superclass-constructor)
  - [Example: Using Super to Access Superclass Members](#example-using-super-to-access-superclass-members)
- [Benefits of Using Super](#benefits-of-using-super)
  - [Comparison of Using Super vs. Not Using Super](#comparison-of-using-super-vs-not-using-super)
- [Important Definitions](#important-definitions)
- [Key Syntax](#key-syntax)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

=====================================

## Introduction

---

In Java, the `super` keyword is used to refer to the superclass of the current class, allowing access to its members and constructors. It is essential for initializing superclass members and invoking superclass methods. This concept is crucial in object-oriented programming, especially when dealing with inheritance.

## What is Super?

---

The `super` keyword is used to call the superclass constructor from a subclass constructor. It must be the first statement in a subclass constructor. `super` can also be used to access superclass members (methods and variables) when they are overridden in the subclass.

### Example: Using Super to Call Superclass Constructor

```java
class Vehicle {
 int maxSpeed;

 // Parameterized constructor in superclass
 Vehicle(int maxSpeed) {
 this.maxSpeed = maxSpeed;
 System.out.println("Vehicle constructor called.");
 }
}

class Car extends Vehicle {
 String fuelType;

 // Subclass constructor
 Car(int maxSpeed, String fuelType) {
 super(maxSpeed); // Calling superclass constructor. MUST be first.
 this.fuelType = fuelType;
 System.out.println("Car constructor called.");
 }
}

public class Test {
 public static void main(String[] args) {
 Car myCar = new Car(180, "Petrol");
 System.out.println("Max Speed: " + myCar.maxSpeed + ", Fuel: " + myCar.fuelType);
 }
}
```

### Example: Using Super to Access Superclass Members

```java
class Animal {
 void eat() {
 System.out.println("Eating...");
 }
}

class Dog extends Animal {
 void eat() {
 System.out.println("Dog is eating...");
 }

 void bark() {
 super.eat(); // Accessing superclass member
 System.out.println("Barking...");
 }
}

public class Test {
 public static void main(String[] args) {
 Dog myDog = new Dog();
 myDog.bark();
 }
}
```

## Benefits of Using Super

---

Using `super` to call a superclass constructor ensures that the superclass members are initialized properly. It also helps to prevent code duplication by allowing the subclass to reuse the superclass constructor.

### Comparison of Using Super vs. Not Using Super

|                                      | Using Super                                         | Not Using Super                                |
| ------------------------------------ | --------------------------------------------------- | ---------------------------------------------- |
| **Superclass Constructor Call**      | Explicitly calls superclass constructor             | Implicitly calls superclass no-arg constructor |
| **Superclass Member Initialization** | Ensures proper initialization of superclass members | May not initialize superclass members properly |
| **Code Duplication**                 | Helps to prevent code duplication                   | May lead to code duplication                   |

## Important Definitions

---

- **Superclass**: The class from which a subclass inherits its properties and behavior.
- **Subclass**: A class that inherits properties and behavior from a superclass.

## Key Syntax

---

- `super(parameterList)`: Calls the superclass constructor with the specified parameters.
- `super.memberName`: Accesses a superclass member (method or variable).

## Exam Tips

---

- Be prepared to identify and explain the purpose of `super` in a given code snippet.
- Understand the implications of not using `super` to call a superclass constructor in a subclass constructor.
- Practice designing class hierarchies that utilize the `super` keyword to demonstrate its practical application in Java programming.

## Key Takeaways

---

- The `super` keyword is used to refer to the superclass of the current class.
- `super` is used to call the superclass constructor from a subclass constructor.
- `super` can also be used to access superclass members (methods and variables) when they are overridden in the subclass.
- Using `super` ensures proper initialization of superclass members and helps to prevent code duplication.
