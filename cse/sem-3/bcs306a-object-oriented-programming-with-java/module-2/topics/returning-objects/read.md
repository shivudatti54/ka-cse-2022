# Returning Objects

## Table of Contents

- [Returning Objects](#returning-objects)
- [Introduction](#introduction)
- [Returning Object References](#returning-object-references)
- [Difference between Returning Primitive Data Types and Objects](#difference-between-returning-primitive-data-types-and-objects)
- [Scenarios for Returning Objects](#scenarios-for-returning-objects)
- [Implementing Object-Returning Methods](#implementing-object-returning-methods)
- [Comparing Returning Objects with Passing Objects as Parameters](#comparing-returning-objects-with-passing-objects-as-parameters)
- [Real-World Applications](#real-world-applications)
- [Designing and Implementing the Factory Method Pattern](#designing-and-implementing-the-factory-method-pattern)
- [Critique of Using Object-Returning Methods for Chaining Operations](#critique-of-using-object-returning-methods-for-chaining-operations)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

=====================================================

## Introduction

---

In Java, methods can return objects, allowing for more complex data to be passed between methods and classes. This is achieved by returning the reference to the object. Returning objects is a fundamental concept in object-oriented programming.

## Returning Object References

---

When a method returns an object, it actually returns the reference to the object. The return type of the method must match the type of the object being returned.

```java
public class MyClass {
 public MyClass getMyObject() {
 MyClass obj = new MyClass();
 return obj; // Return the reference to the object
 }
}
```

## Difference between Returning Primitive Data Types and Objects

---

When a method returns a primitive data type, the value is passed by value. However, when a method returns an object, the reference to the object is passed by value.

|                               | Primitive Data Types        | Objects                        |
| ----------------------------- | --------------------------- | ------------------------------ |
| **Passing Mechanism**         | Passed by value             | Passed by reference            |
| **Changes to Original Value** | No effect on original value | Changes affect original object |

## Scenarios for Returning Objects

---

Returning objects from methods is beneficial in the following scenarios:

- Creating new objects
- Retrieving specific objects from a database
- Implementing the Factory Method pattern
- Chaining operations in fluent interfaces

## Implementing Object-Returning Methods

---

Methods can return new or existing object references. The returned object can be used immediately.

```java
public class MyClass {
 public MyClass getNewObject() {
 return new MyClass(); // Return a new object
 }

 public MyClass getExistingObject(MyClass obj) {
 return obj; // Return an existing object
 }
}
```

## Comparing Returning Objects with Passing Objects as Parameters

---

Returning objects from methods is different from passing objects as method parameters. When an object is passed as a parameter, the method can modify the object. However, when an object is returned from a method, the method cannot modify the original object.

```java
public class MyClass {
 public void modifyObject(MyClass obj) {
 obj.setValue("New Value"); // Modifies the original object
 }

 public MyClass getModifiedObject(MyClass obj) {
 MyClass newObj = new MyClass();
 newObj.setValue("New Value"); // Does not modify the original object
 return newObj;
 }
}
```

## Real-World Applications

---

Object-returning methods have various real-world applications, such as:

- Creating new objects in a database
- Retrieving specific objects from a database
- Implementing the Factory Method pattern
- Chaining operations in fluent interfaces

## Designing and Implementing the Factory Method Pattern

---

The Factory Method pattern is a creational design pattern that provides a way to create objects without specifying the exact class of object that will be created.

```java
public abstract class Animal {
 public abstract Animal createAnimal();
}

public class Dog extends Animal {
 @Override
 public Animal createAnimal() {
 return new Dog();
 }
}

public class Cat extends Animal {
 @Override
 public Animal createAnimal() {
 return new Cat();
 }
}
```

## Critique of Using Object-Returning Methods for Chaining Operations

---

Using object-returning methods for chaining operations can make the code more readable and maintainable. However, it can also lead to tight coupling between objects.

```java
public class MyClass {
 public MyClass setValue(String value) {
 this.value = value;
 return this; // Return the current object for chaining
 }

 public MyClass printValue() {
 System.out.println(value);
 return this; // Return the current object for chaining
 }
}
```

## Exam Tips

---

- Pay attention to the return type of the method and ensure it matches the type of the object being returned.
- Understand that objects are passed by reference, and changes made to the object in the method will affect the original object.

## Key Takeaways

---

- Methods can return object references, not the objects themselves.
- The return type of the method must match the type of the object being returned.
- Returning objects allows for data encapsulation and reuse.
- Objects are passed by reference, not by value.
