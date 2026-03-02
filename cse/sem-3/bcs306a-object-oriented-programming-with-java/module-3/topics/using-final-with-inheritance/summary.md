# Using final with Inheritance

## Overview

The `final` keyword in Java restricts modifications to classes, methods, and variables. It can be used to prevent inheritance, method overriding, and variable reassignment. This concept is crucial for ensuring security, maintaining method behavior, and creating constants.

## Key Points

- A final class cannot be extended (inherited) by any subclass.
- A final method cannot be overridden by any subclass.
- A final variable becomes a constant and cannot be reassigned.
- Final classes are used to prevent inheritance for security purposes.
- Final methods ensure that method behavior is not changed.
- Final variables are used to create constants.
- The `final` keyword is used with classes like String and Integer to prevent inheritance.

## Important Definitions

- **Final Class**: A class that cannot be extended by any subclass.
- **Final Method**: A method that cannot be overridden by any subclass.
- **Final Variable**: A variable that becomes a constant and cannot be reassigned.

## Key Syntax

- `final class ClassName { }` declares a final class.
- `public final void methodName() { }` declares a final method.
- `public static final dataType variableName = value;` declares a final variable.

## Exam Tips

- Focus on the use cases of final classes, methods, and variables.
- Understand the security benefits of using final classes and methods.
- Practice identifying scenarios where final variables are necessary.
- Be prepared to explain the implications of using the `final` keyword in inheritance.
