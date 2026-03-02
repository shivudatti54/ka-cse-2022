# Constructors in Java

## Overview

A constructor is a special method called automatically when an object is created using `new`. It initializes the newly created object with the same name as the class and no return type. Java provides a default constructor if none is defined.

## Key Points

- A constructor has the same name as the class and no return type.
- Default constructor is provided only if none is defined.
- Constructor overloading allows multiple constructors with different parameters.
- `this()` is used for constructor chaining and must be the first statement.
- Java has no destructors; memory is handled by garbage collection.

## Important Definitions

- **Default Constructor**: A constructor provided by Java if none is defined.
- **Constructor Overloading**: Defining multiple constructors with different parameter lists.
- **Constructor Chaining**: Using `this()` to call another constructor from a constructor.

## Key Syntax

- `class Box { Box() { } }` : Default constructor
- `class Box { Box(double w, double h, double d) { } }` : Parameterized constructor
- `class Box { Box() { this(0, 0, 0); } }` : Constructor chaining with `this()`

## Exam Tips

- Focus on constructor overloading, chaining, and default constructors.
- Understand the use of `this()` in constructor chaining.
- Be prepared to identify and write constructors in code snippets.
