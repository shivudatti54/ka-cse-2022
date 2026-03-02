# Variables in Java

## Table of Contents

- [Variables in Java](#variables-in-java)
- [Introduction to Variables](#introduction-to-variables)
- [Types of Variables](#types-of-variables)
  - [Primitive Types](#primitive-types)
  - [Reference Types](#reference-types)
  - [Local Variables](#local-variables)
  - [Instance Variables](#instance-variables)
  - [Static Variables](#static-variables)
- [Declaring and Initializing Variables](#declaring-and-initializing-variables)
  - [Declaring Variables](#declaring-variables)
  - [Initializing Variables](#initializing-variables)
- [Type Conversion and Casting](#type-conversion-and-casting)
  - [Automatic Type Promotion](#automatic-type-promotion)
  - [Explicit Casting](#explicit-casting)
- [Exam Tips and Key Takeaways](#exam-tips-and-key-takeaways)

=====================================================

## Introduction to Variables

---

In Java, a variable is a name given to a memory location that stores a value. Variables are used to store and manipulate data in a program. In this chapter, we will explore the different types of variables, how to declare and initialize them, and how to use them in Java programs.

## Types of Variables

---

### Primitive Types

Java has eight primitive types:

| Type    | Description                                      | Example           |
| ------- | ------------------------------------------------ | ----------------- |
| byte    | 8-bit signed integer                             | byte x = 10;      |
| short   | 16-bit signed integer                            | short x = 10;     |
| int     | 32-bit signed integer                            | int x = 10;       |
| long    | 64-bit signed integer                            | long x = 10L;     |
| float   | 32-bit floating-point number                     | float x = 10.5f;  |
| double  | 64-bit floating-point number                     | double x = 10.5;  |
| char    | 16-bit unsigned integer representing a character | char x = 'A';     |
| boolean | true or false value                              | boolean x = true; |

### Reference Types

Reference types are objects that are instances of classes, interfaces, or arrays. They are stored in memory and can be accessed through a reference variable.

### Local Variables

Local variables are declared inside a method or block and are only accessible within that scope.

### Instance Variables

Instance variables are declared inside a class and are associated with an instance of that class.

### Static Variables

Static variables are declared inside a class and are shared by all instances of that class.

## Declaring and Initializing Variables

---

### Declaring Variables

Variables can be declared using the following syntax:

```java
type variableName;
```

For example:

```java
int x;
```

### Initializing Variables

Variables can be initialized using the following syntax:

```java
type variableName = value;
```

For example:

```java
int x = 10;
```

## Type Conversion and Casting

---

### Automatic Type Promotion

Java automatically promotes a smaller type to a larger type when necessary. For example:

```java
int x = 10;
double y = x; // x is automatically promoted to double
```

### Explicit Casting

Explicit casting is used to convert a larger type to a smaller type. For example:

```java
double x = 10.5;
int y = (int) x; // x is explicitly cast to int
```

## Exam Tips and Key Takeaways

---

- Variables are used to store and manipulate data in a program.
- Java has eight primitive types: byte, short, int, long, float, double, char, and boolean.
- Reference types are objects that are instances of classes, interfaces, or arrays.
- Local variables are declared inside a method or block and are only accessible within that scope.
- Instance variables are declared inside a class and are associated with an instance of that class.
- Static variables are declared inside a class and are shared by all instances of that class.
- Variables can be declared and initialized using the `type variableName` and `type variableName = value` syntax.
- Java automatically promotes a smaller type to a larger type when necessary.
- Explicit casting is used to convert a larger type to a smaller type.
