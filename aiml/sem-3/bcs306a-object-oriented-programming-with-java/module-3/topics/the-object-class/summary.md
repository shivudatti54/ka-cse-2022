# The Object Class

## Overview

The Object class is the root of the Java class hierarchy, providing fundamental methods available to all Java objects. Every class in Java directly or indirectly inherits from the Object class. It serves as the foundation for object-oriented programming in Java.

## Key Points

- The Object class is the superclass of all Java classes.
- It provides common methods that can be overridden by subclasses.
- Methods like `toString()`, `equals()`, and `hashCode()` are commonly overridden.
- `getClass()` returns the runtime class of an object.
- `clone()` creates a copy of an object, while `finalize()` is called before object destruction.
- Understanding the Object class is crucial for mastering object-oriented programming in Java.

## Important Definitions

- **toString()**: Returns a string representation of an object.
- **equals()**: Compares two objects for equality.
- **hashCode()**: Returns a hash code value for an object.
- **getClass()**: Returns the runtime class of an object.
- **clone()**: Creates and returns a copy of an object.

## Key Formulas / Syntax

```java
@Override
public String toString() {
 // implementation
}

@Override
public boolean equals(Object obj) {
 // implementation
}

@Override
public int hashCode() {
 // implementation
}
```

## Exam Tips

- Be prepared to explain the purpose of the Object class and its methods.
- Understand how to override common methods like `toString()`, `equals()`, and `hashCode()`.
- Familiarize yourself with the `getClass()` and `clone()` methods.
- Review object-oriented programming concepts and their relation to the Object class.
