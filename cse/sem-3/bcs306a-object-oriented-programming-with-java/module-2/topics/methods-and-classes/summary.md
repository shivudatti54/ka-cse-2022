# Methods and Classes in Java

## Overview

Methods in Java define behaviors that objects can perform, while classes group data and methods together. Understanding methods and classes is crucial for designing and implementing object-oriented programs in Java. Methods can be static or instance-based, and Java uses a pass-by-value mechanism for passing parameters.

## Key Points

- Methods define behavior, while classes group data and methods together.
- Java uses **pass-by-value** for all parameters, including primitives and objects.
- **Static methods** belong to the class, while **instance methods** belong to objects.
- A method's signature consists of its name and parameter types, excluding the return type.
- Methods can return values or be declared as **void** to return no value.

## Important Definitions

- **Pass-by-value**: A mechanism where a copy of the actual parameter is passed to the method.
- **Method signature**: The combination of a method's name and parameter types.
- **Static method**: A method that belongs to the class and can be called without creating an instance.
- **Instance method**: A method that belongs to an object and requires an instance to be called.

## Key Formulas / Syntax

```java
returnType methodName(parameterList) {
    // body
    return value;
}
```

## Exam Tips

- Be prepared to identify and explain the differences between static and instance methods.
- Understand how pass-by-value works in Java and its implications for method parameters.
- Focus on method signatures and how they are used to identify unique methods in a class.
