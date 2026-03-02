# Argument Passing in Java

## Overview

In Java, when a method is called, arguments can be passed to it. The way these arguments are passed depends on their type, and this affects how changes made within the method impact the original values. Understanding argument passing is crucial for predicting the behavior of Java programs.

## Key Points

- Primitive types (like int, double, boolean) are passed by value, meaning a copy of the original value is passed to the method.
- Changes made to primitive types within a method do not affect the original value outside the method.
- Reference types (like objects and arrays) are passed by reference, but the reference itself is passed by value.
- Modifying the state of an object within a method affects the original object because both the original reference and the method's copy of the reference point to the same object in memory.
- However, if a method changes the reference itself (points it to a new object), this change does not affect the original reference outside the method.

## Important Definitions

- **Pass by Value**: A method of passing arguments where a copy of the original value is passed to the method.
- **Pass by Reference**: A method of passing arguments where a reference to the original value is passed to the method.

## Key Code Snippet

```java
public static void modifyValue(int x) {
    x = x + 10; // Modifying the copy
}
```

## Exam Tips

- Be prepared to identify whether a given argument passing scenario in Java involves primitive or reference types and predict the outcome accordingly.
- Understand that changes to primitive types within a method do not affect the original values, but changes to the state of objects can affect the originals if the method modifies the object's state rather than reassigning the reference.
