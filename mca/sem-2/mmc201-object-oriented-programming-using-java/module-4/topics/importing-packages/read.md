# Importing Packages


## Table of Contents

- [Importing Packages](#importing-packages)
- [Overview of Importing Packages](#overview-of-importing-packages)
- [Purpose of Importing Packages](#purpose-of-importing-packages)
- [Types of Import Statements](#types-of-import-statements)
  - [1. Specific Class Imports](#1-specific-class-imports)
  - [2. Wildcard Imports](#2-wildcard-imports)
  - [3. Static Imports](#3-static-imports)
- [Role of the Classpath in Resolving Class Names](#role-of-the-classpath-in-resolving-class-names)
- [Implicit and Explicit Imports](#implicit-and-explicit-imports)
- [Using Fully Qualified Names (FQNs) vs. Import Statements](#using-fully-qualified-names-fqns-vs-import-statements)
- [Justifying the Use of Import Statements](#justifying-the-use-of-import-statements)
- [Designing and Implementing a Simple Java Program](#designing-and-implementing-a-simple-java-program)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

=====================================

## Overview of Importing Packages

---

In Java, importing packages is a crucial concept that allows you to use classes and interfaces from other packages in your program without having to use their fully qualified names (FQN) every time. This makes your code more readable and easier to maintain. In this topic, we will explore the purpose of importing packages, different types of import statements, and how to use them effectively in your Java programs.

## Purpose of Importing Packages

---

Importing packages is essential in Java because it enables you to:

- Use classes and interfaces from other packages without having to specify their FQN every time.
- Write more readable and maintainable code.
- Avoid naming conflicts between classes with the same name in different packages.

## Types of Import Statements

---

Java provides two types of import statements:

### 1. Specific Class Imports

You can import a specific class from a package using the following syntax:

```java
import package_name.ClassName;
```

For example:

```java
import java.util.ArrayList;
```

This imports the `ArrayList` class from the `java.util` package.

### 2. Wildcard Imports

You can import all classes from a package using the wildcard character (\*):

```java
import package_name.*;
```

For example:

```java
import java.util.*;
```

This imports all classes from the `java.util` package.

### 3. Static Imports

You can import static members (methods and variables) from a class using the `static` keyword:

```java
import static package_name.ClassName.staticMember;
```

For example:

```java
import static java.lang.Math.PI;
```

This imports the `PI` constant from the `Math` class.

## Role of the Classpath in Resolving Class Names

---

The classpath is a list of directories and JAR files that the Java compiler and runtime environment use to find classes. When you import a class, the Java compiler searches for it in the following order:

1. The current package (if the class is in the same package as the importing class).
2. The imported packages (if the class is imported using an import statement).
3. The classpath (if the class is not found in the current package or imported packages).

## Implicit and Explicit Imports

---

Implicit imports are classes that are imported automatically by the Java compiler, such as classes in the `java.lang` package. Explicit imports are classes that are imported using an import statement.

For example:

```java
// Implicit import
String str = "Hello";

// Explicit import
import java.util.ArrayList;
ArrayList<String> list = new ArrayList<>();
```

## Using Fully Qualified Names (FQNs) vs. Import Statements

---

You can use FQNs to access classes and interfaces without importing their packages. However, this can make your code less readable and more prone to errors.

For example:

```java
// Using FQN
java.util.ArrayList<String> list = new java.util.ArrayList<>();

// Using import statement
import java.util.ArrayList;
ArrayList<String> list = new ArrayList<>();
```

## Justifying the Use of Import Statements

---

Import statements are essential in Java programming because they:

- Make your code more readable and maintainable.
- Avoid naming conflicts between classes with the same name in different packages.
- Enable you to use classes and interfaces from other packages without having to specify their FQN every time.

## Designing and Implementing a Simple Java Program

---

Here is an example of a simple Java program that demonstrates the use of import statements:

```java
import java.util.ArrayList;
import java.util.List;

public class MyClass {
 public static void main(String[] args) {
 List<String> list = new ArrayList<>();
 list.add("");
 System.out.println(list);
 }
}
```

This program imports the `ArrayList` and `List` classes from the `java.util` package and uses them to create a list of strings.

## Exam Tips

---

- Be prepared to identify and explain the use of import statements and FQNs in Java code.
- Understand how to import packages and classes correctly in Java.
- Practice designing and implementing simple Java programs that demonstrate the use of import statements.

## Key Takeaways

---

- Importing packages is essential in Java programming because it enables you to use classes and interfaces from other packages without having to specify their FQN every time.
- Java provides two types of import statements: specific class imports and wildcard imports.
- The classpath plays a crucial role in resolving class names in Java.
- Implicit imports are classes that are imported automatically by the Java compiler, while explicit imports are classes that are imported using an import statement.
- Using FQNs can make your code less readable and more prone to errors, while import statements make your code more readable and maintainable.
