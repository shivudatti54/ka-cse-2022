# Dynamic Method Dispatch

## Table of Contents

- [Dynamic Method Dispatch](#dynamic-method-dispatch)
- [Introduction](#introduction)
- [What is Dynamic Method Dispatch?](#what-is-dynamic-method-dispatch)
- [Method Overriding](#method-overriding)
  - [Example of Method Overriding](#example-of-method-overriding)
- [Dynamic Method Dispatch in Action](#dynamic-method-dispatch-in-action)
  - [Example of Dynamic Method Dispatch](#example-of-dynamic-method-dispatch)
- [Comparison with Static Method Binding](#comparison-with-static-method-binding)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

=====================================================

## Introduction

---

Dynamic method dispatch is a fundamental concept in object-oriented programming (OOP) that allows for more flexibility and polymorphism in programming. It is a technique where the method to be invoked is determined at runtime, rather than at compile time. In Java, this is achieved through method overriding. In this chapter, we will explore the concept of dynamic method dispatch, its significance in OOP, and how it is implemented in Java.

## What is Dynamic Method Dispatch?

---

Dynamic method dispatch is a technique where the method to be invoked is determined at runtime, rather than at compile time. This allows for more flexibility and polymorphism in programming. In Java, this is achieved through method overriding, where a subclass provides a different implementation of a method that is already defined in its superclass.

## Method Overriding

---

Method overriding is a technique in Java where a subclass provides a different implementation of a method that is already defined in its superclass. The method in the subclass has the same name, return type, and parameter list as the method in the superclass, but it can have a different implementation. Method overriding is used to achieve polymorphism, where objects of different classes can be treated as objects of a common superclass.

### Example of Method Overriding

```java
// Superclass
class Animal {
 void sound() {
 System.out.println("The animal makes a sound.");
 }
}

// Subclass
class Dog extends Animal {
 @Override
 void sound() {
 System.out.println("The dog barks.");
 }
}

public class Test {
 public static void main(String[] args) {
 Animal myAnimal = new Dog();
 myAnimal.sound(); // Output: "The dog barks."
 }
}
```

## Dynamic Method Dispatch in Action

---

Dynamic method dispatch is used to invoke the overridden method in a subclass. The method to be invoked is determined by the type of object being referred to, not by the type of reference variable.

### Example of Dynamic Method Dispatch

```java
// Superclass
class Vehicle {
 void move() {
 System.out.println("Vehicles can move.");
 }
}

// Subclass 1
class Car extends Vehicle {
 @Override
 void move() {
 System.out.println("Car is driving on the road.");
 }
}

// Subclass 2
class Boat extends Vehicle {
 @Override
 void move() {
 System.out.println("Boat is sailing on the water.");
 }
}

public class TestDispatch {
 public static void main(String[] args) {
 // Dynamic Method Dispatch in action
 Vehicle myVehicle; // Reference of type Vehicle
 myVehicle = new Car(); // Object of type Car
 myVehicle.move(); // Output: "Car is driving on the road."
 myVehicle = new Boat(); // Object of type Boat
 myVehicle.move(); // Output: "Boat is sailing on the water."
 myVehicle = new Vehicle(); // Object of type Vehicle
 myVehicle.move(); // Output: "Vehicles can move."
 }
}
```

## Comparison with Static Method Binding

---

|                       | Static Method Binding      | Dynamic Method Dispatch |
| --------------------- | -------------------------- | ----------------------- |
| **Method invocation** | Determined at compile time | Determined at runtime   |
| **Method overriding** | Not allowed                | Allowed                 |
| **Polymorphism**      | Not supported              | Supported               |

## Exam Tips

---

- Be prepared to explain the concept of dynamic method dispatch and its advantages.
- Understand how to use method overriding to achieve polymorphism in Java.
- Practice writing code that demonstrates dynamic method dispatch.
- Remember that the method to be invoked is determined by the type of object being referred to, not by the type of reference variable.

## Key Takeaways

---

- Dynamic method dispatch is a technique where the method to be invoked is determined at runtime, rather than at compile time.
- Method overriding is used to achieve polymorphism, where objects of different classes can be treated as objects of a common superclass.
- The method to be invoked is determined by the type of object being referred to, not by the type of reference variable.
- Dynamic method dispatch is used to invoke the overridden method in a subclass.
