# The this Keyword

## Overview

The `this` keyword in Java is used to refer to the current object of the class. It is often used to distinguish between instance variables and method or constructor parameters with the same name. This helps to avoid variable shadowing and ensures that the correct variables are being accessed.

## Key Points

- The `this` keyword is used to refer to the current object of the class.
- It is used to distinguish between instance variables and method or constructor parameters with the same name.
- `this` is often used in constructors to initialize instance variables.
- It can also be used in setter methods to update instance variables.
- The `this` keyword helps to avoid variable shadowing.

## Important Definitions

- **Variable Shadowing**: When a method or constructor parameter has the same name as an instance variable, hiding the instance variable.
- **Instance Variable**: A variable that is defined inside a class but outside any method or constructor.

## Key Syntax

- `this.variableName` to refer to an instance variable
- Example: `this.name = name;`

## Exam Tips

- Pay attention to variable names in constructors and setter methods.
- Use `this` to avoid variable shadowing in Java code.
- Be prepared to identify and explain the purpose of `this` in a given Java code snippet.
