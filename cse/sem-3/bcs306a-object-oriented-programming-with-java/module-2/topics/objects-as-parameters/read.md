# Objects as Parameters

## Table of Contents

- [Objects as Parameters](#objects-as-parameters)
- [Introduction](#introduction)
- [Passing Primitive Types vs. Objects](#passing-primitive-types-vs-objects)
  - [Example: Passing Primitive Types](#example-passing-primitive-types)
  - [Example: Passing Objects](#example-passing-objects)
- [How Objects are Passed by Reference](#how-objects-are-passed-by-reference)
  - [Example: Modifying Object State](#example-modifying-object-state)
- [Returning Objects from Methods](#returning-objects-from-methods)
  - [Example: Returning Objects](#example-returning-objects)
- [Comparison of Pass by Reference and Pass by Value](#comparison-of-pass-by-reference-and-pass-by-value)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

=====================================================

## Introduction

---

In Java, objects can be passed as parameters to methods. This is a fundamental concept in object-oriented programming that allows for code reusability, modularity, and encapsulation. In this topic, we will explore the concept of passing objects as parameters to methods in Java, including the difference between passing primitive types and objects, how objects are passed by reference, and the implications for modifying object state within a method.

## Passing Primitive Types vs. Objects

---

When passing primitive types (such as `int`, `double`, etc.) to a method, a copy of the value is passed. This is known as **pass by value**. Any changes made to the primitive type within the method do not affect the original value outside the method.

On the other hand, when passing objects to a method, a copy of the object's reference is passed. This is known as **pass by reference**. Any changes made to the object's state within the method affect the original object outside the method.

### Example: Passing Primitive Types

```java
public class PrimitiveExample {
 public static void changeValue(int x) {
 x = x * 2; // Does not affect the original value
 System.out.println("Inside method: " + x);
 }

 public static void main(String[] args) {
 int myValue = 5;
 System.out.println("Before method call: " + myValue);
 changeValue(myValue); // Pass the primitive type value
 System.out.println("After method call: " + myValue);
 }
}
```

### Example: Passing Objects

```java
public class ObjectExample {
 public static void changeValue(NumberBox box) {
 box.value = box.value * 2; // Modifies the original object's state
 System.out.println("Inside method: " + box.value);
 }

 public static void main(String[] args) {
 NumberBox myBox = new NumberBox(5);
 System.out.println("Before method call: " + myBox.value);
 changeValue(myBox); // Pass the object reference
 System.out.println("After method call: " + myBox.value);
 }
}
```

## How Objects are Passed by Reference

---

When an object is passed to a method, a copy of the object's reference is passed. This means that both the original object and the method's parameter refer to the same object in memory. Any changes made to the object's state within the method affect the original object outside the method.

### Example: Modifying Object State

```java
public class ModifyObjectExample {
 public static void modifyObject(NumberBox box) {
 box.value = box.value * 2; // Modifies the original object's state
 System.out.println("Inside method: " + box.value);
 }

 public static void main(String[] args) {
 NumberBox myBox = new NumberBox(5);
 System.out.println("Before method call: " + myBox.value);
 modifyObject(myBox); // Pass the object reference
 System.out.println("After method call: " + myBox.value);
 }
}
```

## Returning Objects from Methods

---

Methods can also return objects as their return type. This allows for the creation and return of new objects within a method.

### Example: Returning Objects

```java
public class ReturnObjectExample {
 public static NumberBox createObject(int value) {
 NumberBox box = new NumberBox(value); // Creates a new object
 return box; // Returns the new object
 }

 public static void main(String[] args) {
 NumberBox myBox = createObject(5); // Receives the returned object
 System.out.println("Received object: " + myBox.value);
 }
}
```

## Comparison of Pass by Reference and Pass by Value

---

|                             | Pass by Reference                | Pass by Value                        |
| --------------------------- | -------------------------------- | ------------------------------------ |
| **What is passed**          | A copy of the object's reference | A copy of the primitive type's value |
| **Changes affect original** | Yes                              | No                                   |
| **Example**                 | Passing objects to methods       | Passing primitive types to methods   |

## Exam Tips

---

- Be aware of the difference between pass by reference and pass by value.
- Understand how objects are passed to methods and how their state can be modified.
- Focus on how changes made to an object's state within a method affect the original object outside the method.

## Key Takeaways

---

- Objects are passed by reference in Java, allowing methods to modify their state.
- Primitive types are passed by value, preventing methods from modifying their original value.
- Methods can return objects as their return type, allowing for the creation and return of new objects.
- Understanding the difference between pass by reference and pass by value is crucial for effective programming in Java.
