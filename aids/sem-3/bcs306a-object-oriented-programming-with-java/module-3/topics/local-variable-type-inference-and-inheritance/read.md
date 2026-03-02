# Local Variable Type Inference and Inheritance


## Table of Contents

- [Local Variable Type Inference and Inheritance](#local-variable-type-inference-and-inheritance)
- [Introduction](#introduction)
- [What is Local Variable Type Inference?](#what-is-local-variable-type-inference)
  - [Example](#example)
- [Benefits of Local Variable Type Inference](#benefits-of-local-variable-type-inference)
- [Limitations of Local Variable Type Inference](#limitations-of-local-variable-type-inference)
- [How Type Inference Works with Polymorphic Assignments and Method Calls](#how-type-inference-works-with-polymorphic-assignments-and-method-calls)
  - [Example](#example)
- [How Local Variable Type Inference Affects Method Resolution](#how-local-variable-type-inference-affects-method-resolution)
  - [Example](#example)
- [Using Local Variable Type Inference with Inheritance](#using-local-variable-type-inference-with-inheritance)
  - [Example](#example)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

## Introduction

Local variable type inference is a feature in Java that allows developers to declare local variables without specifying their type, using the `var` keyword instead. This feature simplifies code and improves readability. Inheritance is also an important concept in Java that allows one class to inherit properties and behavior from another class. In this topic, we will explore how local variable type inference works with inheritance and polymorphism.

## What is Local Variable Type Inference?

Local variable type inference is a feature in Java that allows developers to declare local variables without specifying their type. The type of the variable is inferred from the assigned value. This feature is only applicable to local variables, not to instance or static variables.

### Example

```java
// Without var
String message = "Hello, World!";
ArrayList<Integer> list = new ArrayList<>();

// With var
var message = "Hello, World!"; // Inferred as String
var list = new ArrayList<Integer>(); // Inferred as ArrayList<Integer>
```

## Benefits of Local Variable Type Inference

The benefits of using local variable type inference include:

- Simplified code: By not having to specify the type of the variable, the code becomes more concise and easier to read.
- Improved readability: The type of the variable is inferred from the assigned value, making it clear what type of data the variable holds.

## Limitations of Local Variable Type Inference

The limitations of local variable type inference include:

- Only applicable to local variables: Local variable type inference is only applicable to local variables, not to instance or static variables.
- Type must be inferrable: The type of the variable must be inferrable from the assigned value. If the type is not inferrable, the compiler will throw an error.

## How Type Inference Works with Polymorphic Assignments and Method Calls

When using local variable type inference with polymorphic assignments and method calls, the type of the variable is inferred from the assigned value. If the assigned value is a subclass of the declared type, the type of the variable is inferred to be the subclass.

### Example

```java
class Animal {
 void sound() {
 System.out.println("Animal makes a sound");
 }
}

class Dog extends Animal {
 void sound() {
 System.out.println("Dog barks");
 }
}

public class Main {
 public static void main(String[] args) {
 var animal = new Dog(); // Inferred as Dog
 animal.sound(); // Prints "Dog barks"
 }
}
```

## How Local Variable Type Inference Affects Method Resolution

Local variable type inference can affect method resolution in the context of inheritance and polymorphism. If the type of the variable is inferred to be a subclass of the declared type, the subclass's method is called instead of the superclass's method.

### Example

```java
class Animal {
 void sound() {
 System.out.println("Animal makes a sound");
 }
}

class Dog extends Animal {
 void sound() {
 System.out.println("Dog barks");
 }
}

public class Main {
 public static void main(String[] args) {
 var animal = new Dog(); // Inferred as Dog
 animal.sound(); // Prints "Dog barks"
 }
}
```

## Using Local Variable Type Inference with Inheritance

Local variable type inference can be used with inheritance to simplify code and improve readability. By using the `var` keyword, the type of the variable is inferred from the assigned value, making it clear what type of data the variable holds.

### Example

```java
class Animal {
 void sound() {
 System.out.println("Animal makes a sound");
 }
}

class Dog extends Animal {
 void sound() {
 System.out.println("Dog barks");
 }
}

public class Main {
 public static void main(String[] args) {
 var animal = new Dog(); // Inferred as Dog
 animal.sound(); // Prints "Dog barks"
 }
}
```

## Exam Tips

- Focus on the use of `var` keyword for local variable type inference.
- Understand the limitations of local variable type inference, such as its applicability only to local variables.
- Practice using local variable type inference in code examples to improve understanding.
- Make sure to understand how local variable type inference affects method resolution in the context of inheritance and polymorphism.

## Key Takeaways

- Local variable type inference is a feature in Java that allows developers to declare local variables without specifying their type.
- The type of the variable is inferred from the assigned value.
- Local variable type inference is only applicable to local variables, not to instance or static variables.
- Local variable type inference can simplify code and improve readability.
- Local variable type inference can affect method resolution in the context of inheritance and polymorphism.
