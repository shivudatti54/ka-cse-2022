# Objects as Parameters

## Overview

In Java, objects can be passed as parameters to methods. When an object is passed, its reference is copied and passed to the method, allowing the method to modify the original object's state. This is in contrast to primitive types, which are passed by value.

## Key Points

- Objects are passed by reference, not by value.
- When an object is passed to a method, its reference is copied and passed.
- The method can modify the original object's state.
- Changes made to the object's state are reflected outside the method.
- Primitive types are passed by value, not by reference.

## Important Definitions

- **Pass by Reference**: Passing an object's reference to a method, allowing the method to modify the original object's state.
- **Pass by Value**: Passing a copy of a primitive type's value to a method, preventing the method from modifying the original value.

## Key Code Snippet

```java
public static void doubleValue(NumberBox box) {
    box.value = box.value * 2; // Modifies the original object's state
}
```

## Exam Tips

- Be aware of the difference between pass by reference and pass by value.
- Understand how objects are passed to methods and how their state can be modified.
- Focus on how changes made to an object's state within a method affect the original object outside the method.
