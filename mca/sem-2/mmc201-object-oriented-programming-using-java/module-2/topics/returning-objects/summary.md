# Returning Objects

## Overview

In Java, methods can return objects, allowing for more complex data to be passed between methods and classes. This is achieved by returning the reference to the object. Returning objects is a fundamental concept in object-oriented programming.

## Key Points

- Methods can return object references, not the objects themselves.
- The return type of the method must match the type of the object being returned.
- The returned object can be a new object or an existing one.
- Returning objects allows for data encapsulation and reuse.
- Objects are passed by reference, not by value.

## Important Definitions

- **Returning Objects**: The process of passing an object reference from a method back to the caller.
- **Object Reference**: A variable that holds the memory address of an object.

## Key Syntax

- `public ClassName methodName() { return objectReference; }`

## Exam Tips

- Pay attention to the return type of the method and ensure it matches the type of the object being returned.
- Understand that objects are passed by reference, and changes made to the object in the method will affect the original object.
