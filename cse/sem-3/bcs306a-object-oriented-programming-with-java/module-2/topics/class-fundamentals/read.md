# Class Fundamentals in Java

## Table of Contents

- [Class Fundamentals in Java](#class-fundamentals-in-java)
- [Introduction](#introduction)
- [Declaring Objects](#declaring-objects)
- [Assigning Object Reference Variables](#assigning-object-reference-variables)
- [Introducing Methods](#introducing-methods)
- [Constructors](#constructors)
- [The `this` Keyword](#the-this-keyword)
- [Garbage Collection](#garbage-collection)
- [Overloading Methods](#overloading-methods)
- [Objects as Parameters](#objects-as-parameters)
- [Argument Passing](#argument-passing)
- [Returning Objects](#returning-objects)
- [Recursion](#recursion)
- [Access Control](#access-control)
- [Understanding `static`](#understanding-static)
- [Introducing `final`](#introducing-final)
- [Introducing Nested and Inner Classes](#introducing-nested-and-inner-classes)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

## Introduction

A class is the foundational building block of Java, defining a new data type that can be used to create objects. It describes the state (fields) and behavior (methods) that objects will have. Classes are templates for objects. In this chapter, we will explore the basics of classes in Java, including declaring objects, assigning object reference variables, introducing methods, constructors, the `this` keyword, and garbage collection.

## Declaring Objects

An object is an instance of a class, and it has its own set of attributes (fields) and methods. To declare an object, you need to use the `new` keyword.

```java
Box myBox = new Box();
```

## Assigning Object Reference Variables

When you assign one object reference variable to another, you are not creating a new copy of the object. Instead, you are creating a new reference to the same object.

```java
Box myBox1 = new Box();
Box myBox2 = myBox1;
```

## Introducing Methods

Methods are used to perform operations on objects. They can take parameters and return values.

```java
class Box {
 double width, height, depth;
 double volume() {
 return width * height * depth;
 }
}
```

## Constructors

Constructors are special methods that are used to initialize objects when they are created. They have the same name as the class and do not have a return type.

```java
class Box {
 double width, height, depth;
 Box(double w, double h, double d) {
 width = w;
 height = h;
 depth = d;
 }
}
```

## The `this` Keyword

The `this` keyword is used to refer to the current object. It can be used to access the members of the current object.

```java
class Box {
 double width, height, depth;
 Box(double w, double h, double d) {
 this.width = w;
 this.height = h;
 this.depth = d;
 }
}
```

## Garbage Collection

Garbage collection is the process of automatically freeing up memory occupied by objects that are no longer in use. Java has a built-in garbage collector that periodically frees up memory.

## Overloading Methods

Method overloading is the process of defining multiple methods with the same name but different parameters.

```java
class Box {
 double width, height, depth;
 void setSize(double w, double h, double d) {
 width = w;
 height = h;
 depth = d;
 }
 void setSize(double size) {
 width = size;
 height = size;
 depth = size;
 }
}
```

## Objects as Parameters

Objects can be passed as parameters to methods.

```java
class Box {
 double width, height, depth;
 void setSize(Box b) {
 width = b.width;
 height = b.height;
 depth = b.depth;
 }
}
```

## Argument Passing

Arguments can be passed to methods using the pass-by-value mechanism.

```java
class Box {
 double width, height, depth;
 void setSize(double w, double h, double d) {
 width = w;
 height = h;
 depth = d;
 }
}
```

## Returning Objects

Methods can return objects.

```java
class Box {
 double width, height, depth;
 Box createBox(double w, double h, double d) {
 Box b = new Box();
 b.width = w;
 b.height = h;
 b.depth = d;
 return b;
 }
}
```

## Recursion

Recursion is the process of a method calling itself.

```java
class Box {
 double width, height, depth;
 double volume() {
 return width * height * depth;
 }
 double volume(int n) {
 if (n == 0) {
 return volume();
 } else {
 return volume(n-1) * 2;
 }
 }
}
```

## Access Control

Access control is used to restrict access to the members of a class.

```java
public class Box {
 private double width, height, depth;
 public void setSize(double w, double h, double d) {
 width = w;
 height = h;
 depth = d;
 }
}
```

## Understanding `static`

The `static` keyword is used to declare members that belong to the class rather than instances of the class.

```java
public class Box {
 static int count = 0;
 public Box() {
 count++;
 }
}
```

## Introducing `final`

The `final` keyword is used to declare members that cannot be overridden or changed.

```java
public class Box {
 final double PI = 3.14;
}
```

## Introducing Nested and Inner Classes

Nested classes are classes that are defined inside another class. Inner classes are classes that are defined inside another class and have access to the members of the outer class.

```java
public class Box {
 class InnerBox {
 double width, height, depth;
 }
}
```

## Exam Tips

- Be prepared to define classes and create objects in Java.
- Understand how to access and modify class members using the dot operator.
- Focus on the basics of class structure, including fields and methods.
- Practice creating and using classes and objects in Java.

## Key Takeaways

- A class defines a type; an object is an instance.
- Classes contain fields and methods.
- Objects are created using the `new` keyword.
- Members are accessed via the dot operator.
- Each object has its own instance variables.
- Methods can be added to classes to perform operations on objects.
