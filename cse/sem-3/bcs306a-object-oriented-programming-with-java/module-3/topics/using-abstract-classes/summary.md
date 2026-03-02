# Using Abstract Classes

## Overview

Abstract classes in Java are declared with the `abstract` keyword and serve as a base for subclasses, providing a mix of abstract and concrete methods. They cannot be instantiated directly. Abstract classes are used to provide a common base with shared implementation while forcing subclasses to implement specific methods.

## Key Points

- Abstract classes are declared with the `abstract` keyword.
- Abstract classes cannot be instantiated directly.
- Abstract classes can contain both abstract methods (no body) and concrete methods (with body).
- A class with any abstract method must be declared abstract.
- Concrete subclasses must implement all abstract methods.
- Abstract classes can have constructors, fields, and concrete methods.

## Important Definitions

- **Abstract Class**: A class declared with the `abstract` keyword that cannot be instantiated directly.
- **Abstract Method**: A method declared with the `abstract` keyword that has no body and must be overridden.
- **Concrete Method**: A method with a body that provides a shared implementation.

## Key Syntax

```java
abstract class ClassName {
    abstract returnType methodName(); // abstract method
    void concreteMethod() { /* implementation */ } // concrete method
}
```

## Exam Tips

- Be prepared to identify and explain the use of abstract classes and methods.
- Understand the rules governing abstract classes, including instantiation and method implementation.
- Focus on the benefits of using abstract classes, such as providing a common base with shared implementation.
