# Argument Passing in Java

## Table of Contents

- [Argument Passing in Java](#argument-passing-in-java)
- [Introduction](#introduction)
- [Types of Argument Passing](#types-of-argument-passing)
  - [Pass by Value](#pass-by-value)
  - [Pass by Reference](#pass-by-reference)
- [Passing Primitive Types](#passing-primitive-types)
- [Passing Reference Types](#passing-reference-types)
- [Comparison of Primitive and Reference Types](#comparison-of-primitive-and-reference-types)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

=====================================================

## Introduction

---

In Java, when a method is called, arguments can be passed to it. The way these arguments are passed depends on their type, and this affects how changes made within the method impact the original values. Understanding argument passing is crucial for predicting the behavior of Java programs.

## Types of Argument Passing

---

### Pass by Value

In pass by value, a copy of the original value is passed to the method. This means that any changes made to the argument within the method do not affect the original value outside the method.

### Pass by Reference

In pass by reference, a reference to the original value is passed to the method. However, in Java, even reference types are passed by value, meaning that a copy of the reference is passed to the method. This subtlety is crucial in understanding how changes to objects within a method affect the original objects.

## Passing Primitive Types

---

Primitive types, such as `int`, `double`, and `boolean`, are passed by value in Java. This means that any changes made to the argument within the method do not affect the original value outside the method.

```java
public class PrimitivePassing {
 public static void modifyValue(int x) {
 x = x + 10; // Modifying the copy
 System.out.println("Value inside method: " + x); // Output: 20
 }

 public static void main(String[] args) {
 int originalValue = 10;
 System.out.println("Value before method call: " + originalValue); // Output: 10
 modifyValue(originalValue); // Passes a copy of the value 10
 System.out.println("Value after method call: " + originalValue); // Output: 10 (unchanged)
 }
}
```

## Passing Reference Types

---

Reference types, such as objects and arrays, are also passed by value in Java, but the value is a reference to the original object. This means that any changes made to the state of the object within the method affect the original object, but changes to the reference itself do not affect the original reference.

```java
public class ReferencePassing {
 public static void modifyObject(StringBuilder sb) {
 sb.append(" World!"); // Modifying the original object
 System.out.println("Value inside method: " + sb.toString()); // Output: Hello World!
 }

 public static void main(String[] args) {
 StringBuilder originalObject = new StringBuilder("Hello");
 System.out.println("Value before method call: " + originalObject.toString()); // Output: Hello
 modifyObject(originalObject); // Passes a copy of the reference to the original object
 System.out.println("Value after method call: " + originalObject.toString()); // Output: Hello World!
 }
}
```

## Comparison of Primitive and Reference Types

---

|                         | Primitive Types              | Reference Types                                                              |
| ----------------------- | ---------------------------- | ---------------------------------------------------------------------------- |
| **Passing Mechanism**   | Pass by Value                | Pass by Value (of reference)                                                 |
| **Changes to Argument** | Do not affect original value | Affect original object if state is modified, but not if reference is changed |

## Exam Tips

---

- Be prepared to identify whether a given argument passing scenario in Java involves primitive or reference types and predict the outcome accordingly.
- Understand that changes to primitive types within a method do not affect the original values, but changes to the state of objects can affect the originals if the method modifies the object's state rather than reassigning the reference.

## Key Takeaways

---

- Primitive types are passed by value in Java, meaning changes to the argument within a method do not affect the original value.
- Reference types are passed by value in Java, but the value is a reference to the original object, meaning changes to the state of the object within a method affect the original object.
- Understanding argument passing is crucial for predicting the behavior of Java programs.
