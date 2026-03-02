# Interfaces in Java

## Overview

An interface in Java is a reference type that defines a contract of methods that implementing classes must provide. Interfaces are declared with the `interface` keyword and implemented using `implements`. They are used to define a blueprint for classes that includes a set of methods that must be implemented.

## Key Points

- Interfaces are declared with `interface` and implemented with `implements`.
- Methods in an interface are implicitly `public abstract`.
- Variables in an interface are implicitly `public static final`.
- A class can implement multiple interfaces.
- Interfaces define contracts without implementation.
- Java supports default and static methods in interfaces since Java 8.
- Interfaces cannot have constructors.

## Important Definitions

- **Interface**: A reference type that defines a contract of methods that implementing classes must provide.
- **Implement**: To provide an implementation for the methods defined in an interface.

## Key Syntax

- `interface InterfaceName { ... }`
- `class ClassName implements InterfaceName { ... }`
- `public abstract returnType methodName();` (method declaration in an interface)

## Comparisons

| Feature     | Interface                   | Abstract Class      |
| ----------- | --------------------------- | ------------------- |
| Methods     | Abstract (+ default/static) | Abstract + concrete |
| Variables   | public static final only    | Any type            |
| Inheritance | Multiple                    | Single              |
| Constructor | No                          | Yes                 |

## Exam Tips

- Focus on the differences between interfaces and abstract classes.
- Understand how to declare and implement interfaces.
- Be prepared to explain the use of interfaces in defining contracts and promoting multiple inheritance.
