# When Constructors Are Executed

## Overview

Constructors are special methods in Java classes that are executed when an object of the class is created. The order of constructor execution is crucial in understanding how objects are initialized. This topic explains the sequence of constructor execution in Java.

## Key Points

- The order of constructor execution is determined by the inheritance hierarchy of the classes.
- The constructor of the parent class is executed before the constructor of the child class.
- Instance variable initializers are executed before the constructor of the class.
- Instance initialization blocks are executed before the constructor of the class.
- The implicit `super()` call is made by the compiler if not specified explicitly.
- The order of execution is: Grandparent constructor, Parent constructor, Child instance block, Child constructor.

## Important Definitions

- **Implicit `super()` call**: A call to the parent class constructor made by the compiler if not specified explicitly.
- **Instance variable initializer**: A statement that initializes an instance variable when an object is created.
- **Instance initialization block**: A block of code that is executed when an object is created.

## Key Formulas / Syntax

```java
class Child extends Parent {
 // implicit super() call to Parent()
 Child() {
 // ...
 }
}
```

## Exam Tips

- Focus on the order of constructor execution in the context of inheritance.
- Understand the role of instance variable initializers and instance initialization blocks in object initialization.
- Be prepared to answer questions on implicit `super()` calls and their significance in constructor execution.
