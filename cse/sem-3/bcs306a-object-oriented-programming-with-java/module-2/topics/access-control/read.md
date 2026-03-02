# Access Control in Java

## Table of Contents

- [Access Control in Java](#access-control-in-java)
- [Introduction](#introduction)
- [Importance of Access Control](#importance-of-access-control)
- [The Four Access Levels](#the-four-access-levels)
  - [1. public](#1-public)
  - [2. private](#2-private)
  - [3. protected](#3-protected)
  - [4. Default (Package-Private)](#4-default-package-private)
- [Access Level Summary](#access-level-summary)
- [Encapsulation](#encapsulation)
- [Key Points](#key-points)
- [Comparison of Access Levels](#comparison-of-access-levels)
- [Exam Tips](#exam-tips)

## Introduction

Access control in Java is a mechanism that restricts the visibility of classes, methods, and variables, implementing **encapsulation** through four access levels: public, protected, default, and private. Proper use of access control ensures data hiding and code security. Access levels are defined using access modifiers.

## Importance of Access Control

Access control is crucial in object-oriented programming as it allows developers to hide internal implementation details and expose only necessary information. This helps prevent unauthorized modifications and ensures code security.

## The Four Access Levels

Java provides four access levels through three access modifiers — `public`, `private`, and `protected` — plus a default (package-private) level.

### 1. public

Accessible from **any class** in any package. Public members are the least restrictive and can be accessed from anywhere.

```java
public class Calculator {
 public int add(int a, int b) {
 return a + b;
 }
}
```

### 2. private

Accessible **only within its own class**. Private members are the most restrictive and are used to hide internal implementation details.

```java
class BankAccount {
 private double balance;
 public double getBalance() {
 return balance;
 }
}
```

### 3. protected

Accessible within **same package** and by **subclasses** in other packages. Protected members are used to provide a level of access that is more restrictive than public but less restrictive than private.

```java
class Animal {
 protected String name;
 protected void eat() {
 System.out.println(name + " is eating");
 }
}
```

### 4. Default (Package-Private)

No modifier — accessible only within **same package**. Default members are used when no access modifier is specified.

```java
class Helper {
 int count; // default access
 void increment() {
 count++;
 }
}
```

## Access Level Summary

| Modifier  | Same Class | Same Package | Subclass (diff pkg) | Other Packages |
| --------- | ---------- | ------------ | ------------------- | -------------- |
| public    | Yes        | Yes          | Yes                 | Yes            |
| protected | Yes        | Yes          | Yes                 | No             |
| default   | Yes        | Yes          | No                  | No             |
| private   | Yes        | No           | No                  | No             |

## Encapsulation

Encapsulation is the concept of hiding internal implementation details and exposing only necessary information. In Java, encapsulation is achieved through the use of private fields and public getters/setters.

```java
class Employee {
 private String name;
 private int age;
 public String getName() {
 return name;
 }
 public void setName(String name) {
 this.name = name;
 }
 public int getAge() {
 return age;
 }
 public void setAge(int age) {
 this.age = age;
 }
}
```

## Key Points

- Four access levels: public, protected, default, private.
- private is most restrictive; public has no restriction.
- Encapsulation: private fields + public getters/setters.
- No modifier means package-private access.

## Comparison of Access Levels

|                   | public            | protected                            | default                         | private                              |
| ----------------- | ----------------- | ------------------------------------ | ------------------------------- | ------------------------------------ |
| **Accessibility** | Any class         | Same package and subclasses          | Same package                    | Only within its own class            |
| **Restriction**   | Least restrictive | Less restrictive than private        | More restrictive than public    | Most restrictive                     |
| **Usage**         | Expose API        | Hide internal implementation details | Package-specific implementation | Hide internal implementation details |

## Exam Tips

- Focus on understanding the four access levels and their usage.
- Remember that no modifier means default (package-private) access.
- Encapsulation is a key concept in object-oriented programming; know how to implement it using access control.
- Practice designing classes that demonstrate proper use of access control to implement encapsulation.
