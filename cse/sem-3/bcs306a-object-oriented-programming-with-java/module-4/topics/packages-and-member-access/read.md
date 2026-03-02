# Packages and Member Access in Java

## Table of Contents

- [Packages and Member Access in Java](#packages-and-member-access-in-java)
- [Introduction](#introduction)
- [What are Packages?](#what-are-packages)
  - [Declaring a Package](#declaring-a-package)
- [Member Access Modifiers](#member-access-modifiers)
  - [Public Access Modifier](#public-access-modifier)
  - [Private Access Modifier](#private-access-modifier)
  - [Protected Access Modifier](#protected-access-modifier)
  - [Default (Package-Private) Access Modifier](#default-package-private-access-modifier)
- [Importing Packages](#importing-packages)
  - [Static Import](#static-import)
- [Encapsulation](#encapsulation)
- [Access Control](#access-control)
  - [Comparing Access Modifiers](#comparing-access-modifiers)
  - [Example](#example)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

=====================================================

## Introduction

---

In Java, packages are used to organize related classes and interfaces into logical groups. Member access modifiers are used to control the visibility of variables, methods, and constructors within a class. These features are fundamental for encapsulation and proper class design in Java programs.

## What are Packages?

---

A package is a namespace that groups related classes and interfaces. It is essentially a directory structure that stores related classes and interfaces. Packages are used to:

- Organize large-scale applications into logical groups
- Avoid naming conflicts between classes
- Control access to classes and members

### Declaring a Package

---

A package declaration must be the first statement in a Java file. The syntax for declaring a package is:

```java
package packagename;
```

For example:

```java
package com..mypackage;
```

## Member Access Modifiers

---

Member access modifiers are used to control the visibility of variables, methods, and constructors within a class. There are four access modifiers in Java:

- `public`
- `private`
- `protected`
- default (package-private)

### Public Access Modifier

---

The `public` access modifier makes a member accessible from any class in any package. It is the least restrictive access modifier.

### Private Access Modifier

---

The `private` access modifier makes a member accessible only within the same class. It is the most restrictive access modifier.

### Protected Access Modifier

---

The `protected` access modifier makes a member accessible within the same package and subclasses in different packages.

### Default (Package-Private) Access Modifier

---

The default (package-private) access modifier makes a member accessible only within the same package.

## Importing Packages

---

Classes can be imported using the `import` statement. There are two types of imports:

- Single class import: `import packagename.ClassName;`
- Wildcard import: `import packagename.*;`

For example:

```java
import java.util.Scanner; // Single class import
import java.util.*; // Wildcard import
```

### Static Import

---

Static import is used to import static members of a class. The syntax for static import is:

```java
import static packagename.ClassName.MEMBER;
```

## Encapsulation

---

Encapsulation is the concept of bundling data and methods while restricting direct access to some components. It is used to hide the implementation details of a class from the outside world.

## Access Control

---

Access control is used to control the visibility of classes, methods, and variables within a package hierarchy. It is used to enforce encapsulation and define clear APIs in a class design.

### Comparing Access Modifiers

---

The following table compares the access modifiers in Java:

| Modifier  | Same Class | Same Package | Subclass (diff pkg) | Different Package |
| --------- | ---------- | ------------ | ------------------- | ----------------- |
| public    |            |              |                     |                   |
| protected |            |              |                     |                   |
| default   |            |              |                     |                   |
| private   |            |              |                     |                   |

### Example

---

Consider the following example:

```java
package com..mypackage;

public class MyClass {
 public int a; // public access
 private int b; // private access
 protected int c; // protected access
 int d; // default/package-private access
}
```

In this example:

- `a` is accessible from any class in any package.
- `b` is accessible only within the same class.
- `c` is accessible within the same package and subclasses in different packages.
- `d` is accessible only within the same package.

## Exam Tips

---

- Remember the visibility hierarchy: private < default < protected < public
- Predict output or identify compilation errors based on access modifier usage.
- Note that top-level classes can only have public or default access.
- Protected members are accessible in subclasses even if in different package.
- Focus on understanding when to use each modifier for encapsulation.

## Key Takeaways

---

- Packages are used to organize related classes and interfaces into logical groups.
- Member access modifiers are used to control the visibility of variables, methods, and constructors within a class.
- There are four access modifiers in Java: public, private, protected, and default (package-private).
- Encapsulation is the concept of bundling data and methods while restricting direct access to some components.
- Access control is used to control the visibility of classes, methods, and variables within a package hierarchy.
