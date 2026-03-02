# Using Super

## Overview

The `super` keyword in Java is used to refer to the superclass of the current class, allowing access to its members and constructors. It is essential for initializing superclass members and invoking superclass methods. This concept is crucial in object-oriented programming, especially when dealing with inheritance.

## Key Points

- The `super` keyword is used to call the superclass constructor from a subclass constructor.
- It must be the first statement in a subclass constructor.
- `super` can also be used to access superclass members (methods and variables) when they are overridden in the subclass.
- If a subclass constructor does not explicitly call a superclass constructor using `super`, the compiler will insert a call to the superclass's no-arg constructor.
- The `super` keyword can only be used within the subclass.

## Important Definitions

- **Superclass**: The class from which a subclass inherits its properties and behavior.
- **Subclass**: A class that inherits properties and behavior from a superclass.

## Key Syntax

- `super(parameterList)`: Calls the superclass constructor with the specified parameters.
- `super.memberName`: Accesses a superclass member (method or variable).

## Exam Tips

- Be prepared to identify and explain the purpose of `super` in a given code snippet.
- Understand the implications of not using `super` to call a superclass constructor in a subclass constructor.
