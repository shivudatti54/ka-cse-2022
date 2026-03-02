# Method Overriding in Java


## Table of Contents

- [Method Overriding in Java](#method-overriding-in-java)
- [Introduction](#introduction)
- [What is Method Overriding?](#what-is-method-overriding)
- [Rules of Method Overriding](#rules-of-method-overriding)
- [Example of Method Overriding](#example-of-method-overriding)
- [@Override Annotation](#override-annotation)
- [Runtime Polymorphism](#runtime-polymorphism)
- [Benefits of Method Overriding](#benefits-of-method-overriding)
- [Comparison of Method Overriding and Method Overloading](#comparison-of-method-overriding-and-method-overloading)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

## Introduction

Method overriding is a fundamental concept in object-oriented programming (OOP) that allows a subclass to provide its own implementation of a method already defined in its superclass. This feature enables runtime polymorphism, which is the ability of an object to take on multiple forms at runtime. In this chapter, we will explore the concept of method overriding in Java, its rules, benefits, and applications.

## What is Method Overriding?

Method overriding occurs when a subclass provides its own implementation of a method already defined in its superclass. The method in the subclass must have the same name, return type (or covariant), and parameter list as the method in the superclass.

## Rules of Method Overriding

To override a method in Java, the following rules must be followed:

1. **Same method signature**: The method in the subclass must have the same name and parameter list as the method in the superclass.
2. **Return type**: The return type of the method in the subclass must be the same or a subtype (covariant) of the return type of the method in the superclass.
3. **Access modifier**: The access modifier of the method in the subclass cannot be more restrictive than the access modifier of the method in the superclass.
4. **Cannot override final, static, or private methods**: Methods declared as final, static, or private in the superclass cannot be overridden in the subclass.

## Example of Method Overriding

```java
class Animal {
 void speak() {
 System.out.println("Animal speaks");
 }
}

class Dog extends Animal {
 @Override
 void speak() {
 System.out.println("Dog barks");
 }
}

public class Main {
 public static void main(String[] args) {
 Animal a = new Dog();
 a.speak(); // Output: Dog barks (runtime polymorphism)
 }
}
```

In this example, the `Dog` class overrides the `speak()` method of the `Animal` class. The `speak()` method in the `Dog` class has the same signature as the `speak()` method in the `Animal` class, but it provides its own implementation.

## @Override Annotation

The `@Override` annotation is optional but recommended. It tells the compiler to verify that the method actually overrides a superclass method. If the method does not override a superclass method, the compiler will throw an error.

## Runtime Polymorphism

When a superclass reference points to a subclass object, the overridden method in the subclass is called at runtime. This is known as runtime polymorphism.

## Benefits of Method Overriding

Method overriding provides several benefits, including:

- **Increased flexibility**: Method overriding allows subclasses to provide their own implementation of methods, making the code more flexible and reusable.
- **Improved modularity**: Method overriding enables modular programming, where each module can be developed and tested independently.
- **Easier maintenance**: Method overriding makes it easier to modify or extend the behavior of a class without affecting other parts of the code.

## Comparison of Method Overriding and Method Overloading

|                      | Method Overriding                                                                 | Method Overloading                                                                     |
| -------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Method signature** | Same method signature as superclass method                                        | Different method signature than superclass method                                      |
| **Return type**      | Same or covariant return type as superclass method                                | Can have different return type than superclass method                                  |
| **Access modifier**  | Cannot be more restrictive than superclass method                                 | Can be more restrictive than superclass method                                         |
| **Purpose**          | Provides a specific implementation for a method already defined in the superclass | Provides multiple definitions for a method with the same name but different parameters |

## Exam Tips

- Focus on the method signature, return type, and access modifiers when overriding a method.
- Understand runtime polymorphism and its relation to method overriding.
- Be prepared to identify correct and incorrect method overriding examples.

## Key Takeaways

- Method overriding is a feature in Java that allows a subclass to provide its own implementation of a method already defined in its superclass.
- The method in the subclass must have the same name, return type (or covariant), and parameter list as the method in the superclass.
- Method overriding enables runtime polymorphism, which is the ability of an object to take on multiple forms at runtime.
- The `@Override` annotation is optional but recommended to verify that the method actually overrides a superclass method.
