# Inheritance Basics in Java

## Overview

Inheritance is a mechanism where a new class (subclass) acquires the properties and behaviors of an existing class (superclass) using the `extends` keyword, implementing the IS-A relationship. Java supports single class inheritance only.

## Key Points

- `extends` keyword creates inheritance relationship.
- Subclass inherits all non-private members of the superclass.
- Java supports single class inheritance only.
- Private members of superclass are not directly accessible in subclass.
- Inheritance promotes code reuse, extensibility, and polymorphism.
- A subclass can add new features or override the ones inherited from the superclass.

## Important Definitions

- **Superclass**: The existing class from which a new class inherits properties and behaviors.
- **Subclass**: The new class that inherits properties and behaviors from an existing class.
- **IS-A relationship**: A relationship where a subclass is a specialized version of the superclass.

## Key Syntax

- `class Subclass extends Superclass { ... }`
- ```java
  class A {
      int x;
      void showX() { System.out.println("x: " + x); }
  }
  class B extends A {
      int y;
      void showY() { System.out.println("y: " + y); }
  }
  ```

```

## Exam Tips
- Focus on understanding the IS-A relationship and single class inheritance in Java.
- Be prepared to identify and explain the benefits of inheritance, including code reuse, extensibility, and polymorphism.
- Practice creating simple inheritance relationships using the `extends` keyword.
```
