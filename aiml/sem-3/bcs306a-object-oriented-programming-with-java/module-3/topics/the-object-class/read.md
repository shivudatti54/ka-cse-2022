# The Object Class


## Table of Contents

- [The Object Class](#the-object-class)
- [Introduction](#introduction)
- [Common Methods of Object Class](#common-methods-of-object-class)
  - [1. toString()](#1-tostring)
  - [2. equals(Object obj)](#2-equalsobject-obj)
  - [3. hashCode()](#3-hashcode)
  - [4. getClass()](#4-getclass)
  - [5. clone()](#5-clone)
  - [6. finalize()](#6-finalize)
- [Importance of Overriding equals() and hashCode() Methods](#importance-of-overriding-equals-and-hashcode-methods)
- [Comparison of getClass() and instanceof Operator](#comparison-of-getclass-and-instanceof-operator)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

## Introduction

The Object class is the root of the Java class hierarchy, providing fundamental methods available to all Java objects. Every class in Java directly or indirectly inherits from the Object class. It serves as the foundation for object-oriented programming in Java.

## Common Methods of Object Class

The Object class provides several common methods that can be overridden by subclasses to achieve desired behavior. These methods include:

### 1. toString()

Returns a string representation of the object. By default, it returns the class name and the hash code of the object.

```java
class Student {
 String name;
 int rollNo;

 @Override
 public String toString() {
 return "Student[name=" + name + ", rollNo=" + rollNo + "]";
 }
}
```

### 2. equals(Object obj)

Compares two objects for equality. By default, it checks if the two objects are the same instance.

```java
@Override
public boolean equals(Object obj) {
 if (this == obj) return true;
 if (obj == null || getClass() != obj.getClass()) return false;
 Student student = (Student) obj;
 return rollNo == student.rollNo;
}
```

### 3. hashCode()

Returns a hash code value for the object. By default, it returns a unique hash code for each object.

```java
@Override
public int hashCode() {
 return rollNo;
}
```

### 4. getClass()

Returns the runtime class of the object.

```java
Object obj = new String("Hello");
Class c = obj.getClass();
System.out.println(c.getName()); // java.lang.String
```

### 5. clone()

Creates and returns a copy of the object. Note that this method is protected, so it can only be accessed within the same class or its subclasses.

```java
class Student implements Cloneable {
 String name;
 int rollNo;

 @Override
 protected Object clone() throws CloneNotSupportedException {
 return super.clone();
 }
}
```

### 6. finalize()

Called by the garbage collector before the object is destroyed. Note that this method is deprecated since Java 9 and should not be used.

## Importance of Overriding equals() and hashCode() Methods

When using Java's Collections Framework, it's essential to override the equals() and hashCode() methods in custom classes to ensure correct behavior. For example, when using a HashSet to store custom objects, the equals() and hashCode() methods are used to determine whether two objects are equal.

## Comparison of getClass() and instanceof Operator

| Method     | Description                                              | Example                  |
| ---------- | -------------------------------------------------------- | ------------------------ |
| getClass() | Returns the runtime class of the object                  | `obj.getClass()`         |
| instanceof | Checks if an object is an instance of a particular class | `obj instanceof Student` |

## Exam Tips

- Be prepared to explain the purpose of the Object class and its methods.
- Understand how to override common methods like toString(), equals(), and hashCode().
- Familiarize yourself with the getClass() and clone() methods.
- Review object-oriented programming concepts and their relation to the Object class.

## Key Takeaways

- The Object class is the root of the Java class hierarchy.
- The Object class provides common methods that can be overridden by subclasses.
- Overriding the equals() and hashCode() methods is crucial when using Java's Collections Framework.
- The getClass() method returns the runtime class of the object.
- The clone() method creates and returns a copy of the object.
