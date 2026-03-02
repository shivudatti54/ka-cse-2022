# Overloading Methods

## Overview

Method overloading allows multiple methods with the same name but different parameters in the same class, enabling compile-time polymorphism. The compiler determines which method to call based on the method signature. This feature improves code readability and facilitates performing the same operation on different data types.

## Key Points

- Methods must differ in number, type, or order of parameters.
- Return type alone is not sufficient for overloading.
- Method overloading enables compile-time polymorphism.
- Improves code readability by allowing same operation on different data types.
- Compiler determines which method to call based on method signature.

## Important Definitions

- **Method Overloading**: Multiple methods with the same name but different parameters in the same class.
- **Method Signature**: Combination of method name and parameter list.
- **Compile-time Polymorphism**: Ability of an object to take on multiple forms at compile-time.

## Key Formulas / Syntax

```java
public int add(int a, int b) { return a + b; }
public double add(double a, double b) { return a + b; }
```

## Exam Tips

- Focus on understanding method overloading rules and benefits.
- Practice identifying correct method calls based on method signatures.
- Be prepared to explain the concept of compile-time polymorphism.
