# When Constructors Are Executed


## Table of Contents

- [When Constructors Are Executed](#when-constructors-are-executed)
- [Introduction](#introduction)
- [Constructor Execution Order](#constructor-execution-order)
  - [Implicit `super()` Call](#implicit-super-call)
  - [Instance Variable Initializers](#instance-variable-initializers)
  - [Instance Initialization Blocks](#instance-initialization-blocks)
  - [Execution Order](#execution-order)
- [Multilevel Inheritance Hierarchy](#multilevel-inheritance-hierarchy)
- [Example Use Case](#example-use-case)
- [Comparison Table](#comparison-table)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

=====================================================

## Introduction

---

Constructors are special methods in Java classes that are executed when an object of the class is created. The order of constructor execution is crucial in understanding how objects are initialized. In this topic, we will explore the sequence of constructor execution in Java, including the role of instance variable initializers, instance initialization blocks, and the implicit `super()` call.

## Constructor Execution Order

---

The order of constructor execution is determined by the inheritance hierarchy of the classes. The constructor of the parent class is executed before the constructor of the child class. This ensures that the parent class is fully initialized before the child class is initialized.

### Implicit `super()` Call

When a child class constructor is called, the compiler makes an implicit call to the parent class constructor using the `super()` method. This call is made before the child class constructor is executed. If the parent class has multiple constructors, the compiler will call the no-arg constructor by default.

```java
class Child extends Parent {
 Child() {
 // implicit super() call to Parent()
 }
}
```

### Instance Variable Initializers

Instance variable initializers are statements that initialize instance variables when an object is created. These initializers are executed before the constructor of the class.

```java
class Child {
 private String name = "Initialized"; // Instance variable initializer
}
```

### Instance Initialization Blocks

Instance initialization blocks are blocks of code that are executed when an object is created. These blocks are executed before the constructor of the class.

```java
class Child {
 {
 System.out.println("Child Instance Block");
 }
}
```

### Execution Order

The order of execution is as follows:

1. Grandparent constructor
2. Parent constructor
3. Child instance block
4. Child constructor

## Multilevel Inheritance Hierarchy

---

In a multilevel inheritance hierarchy, the constructor execution order follows the same pattern. The constructor of the grandparent class is executed first, followed by the constructor of the parent class, and finally the constructor of the child class.

```java
class Grandparent {
 Grandparent() {
 System.out.println("Grandparent Constructor Executed");
 }
}

class Parent extends Grandparent {
 Parent() {
 // implicit super() call to Grandparent()
 System.out.println("Parent Constructor Executed");
 }
}

class Child extends Parent {
 Child() {
 // implicit super() call to Parent()
 System.out.println("Child Constructor Executed");
 }
}
```

## Example Use Case

---

Here is an example use case that demonstrates the constructor execution order:

```java
public class ConstructorOrderDemo {
 public static void main(String[] args) {
 System.out.println("Creating Child object...");
 new Child();
 }
}

class Grandparent {
 Grandparent() {
 System.out.println("Grandparent Constructor Executed");
 }
}

class Parent extends Grandparent {
 Parent() {
 // implicit super() call to Grandparent()
 System.out.println("Parent Constructor Executed");
 }
}

class Child extends Parent {
 private String name = "Initialized"; // Instance variable initializer

 {
 System.out.println("Child Instance Block: name = " + name);
 }

 Child() {
 // implicit super() call to Parent()
 System.out.println("Child Constructor Executed");
 }
}
```

Output:

```
Creating Child object...
Grandparent Constructor Executed
Parent Constructor Executed
Child Instance Block: name = Initialized
Child Constructor Executed
```

## Comparison Table

---

|                                | Grandparent | Parent | Child              |
| ------------------------------ | ----------- | ------ | ------------------ |
| Constructor Execution Order    | 1st         | 2nd    | 3rd                |
| Instance Variable Initializers | -           | -      | Before constructor |
| Instance Initialization Blocks | -           | -      | Before constructor |

## Exam Tips

---

- Focus on the order of constructor execution in the context of inheritance.
- Understand the role of instance variable initializers and instance initialization blocks in object initialization.
- Be prepared to answer questions on implicit `super()` calls and their significance in constructor execution.

## Key Takeaways

---

- The constructor execution order is determined by the inheritance hierarchy of the classes.
- The constructor of the parent class is executed before the constructor of the child class.
- Instance variable initializers and instance initialization blocks are executed before the constructor of the class.
- The implicit `super()` call is made by the compiler if not specified explicitly.
