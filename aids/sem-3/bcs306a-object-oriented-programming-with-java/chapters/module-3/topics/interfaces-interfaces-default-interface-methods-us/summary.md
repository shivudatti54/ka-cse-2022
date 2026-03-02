# Interfaces in Java

=====================================

## Overview

---

- An interface in Java is a abstract class that cannot be instantiated.
- It is used to achieve multiple inheritance.
- Interfaces are used when a class wants to inherit multiple classes.

## Interface Basics

---

- A interface is declared using the `interface` keyword.
- An interface can have multiple methods and variables.
- A interface is abstract by default.
- An interface can extend another interface using the `extends` keyword.

## Default Interface Methods

---

- Java 8 introduced default methods in interfaces.
- Default methods are methods with a body.
- Default methods can be overridden by classes implementing the interface.

## Static Methods in an Interface

---

- Java does not support static methods in interfaces.
- However, we can use static methods in classes implementing the interface.

## Private Interface Methods

---

- Java does not support private methods in interfaces.
- However, we can use private methods in classes implementing the interface.

## Important Formulas/Definitions/Theorems

---

- The Interface Segregation Principle (ISP): Clients should not be forced to depend on interfaces they do not use.
- The Open-Closed Principle (OCP): Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.
