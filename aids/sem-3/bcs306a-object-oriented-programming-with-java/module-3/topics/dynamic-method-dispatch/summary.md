# Dynamic Method Dispatch

## Overview

Dynamic method dispatch is a technique in object-oriented programming where the method to be invoked is determined at runtime, rather than at compile time. This allows for more flexibility and polymorphism in programming. In Java, this is achieved through method overriding.

## Key Points

- Dynamic method dispatch is used to resolve method calls at runtime.
- It is achieved through method overriding in Java.
- The method to be invoked is determined by the type of object being referred to, not by the type of reference variable.
- It allows for polymorphism, where objects of different classes can be treated as objects of a common superclass.
- It is useful for writing more generic and reusable code.
- The actual method to be invoked is determined at runtime, based on the type of object being referred to.

## Important Definitions

- **Polymorphism**: The ability of an object to take on multiple forms, depending on the context in which it is used.
- **Method Overriding**: A technique in Java where a subclass provides a different implementation of a method that is already defined in its superclass.

## Key Syntax

- `@Override` annotation is used to indicate that a method is being overridden.

## Exam Tips

- Be prepared to explain the concept of dynamic method dispatch and its advantages.
- Understand how to use method overriding to achieve polymorphism in Java.
- Practice writing code that demonstrates dynamic method dispatch.
