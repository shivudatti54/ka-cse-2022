# Packages in Java


## Table of Contents

- [Packages in Java](#packages-in-java)
- [Introduction to Packages](#introduction-to-packages)
- [Package Declaration](#package-declaration)
- [Package Components](#package-components)
- [Importing Packages](#importing-packages)
- [Built-in Packages](#built-in-packages)
- [Default Package](#default-package)
- [Package Naming Conventions](#package-naming-conventions)
- [Fully Qualified Name](#fully-qualified-name)
- [Advantages of Packages](#advantages-of-packages)
- [Creating a User-Defined Package](#creating-a-user-defined-package)
- [Example Program](#example-program)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

=====================================================

## Introduction to Packages

---

In Java, a package is a logical grouping of related classes, interfaces, and sub-packages. It provides a way to organize large-scale applications, prevent naming conflicts, and control access through encapsulation. In this topic, we will explore the concept of packages in Java, their importance, and how to implement them in Java code.

## Package Declaration

---

A package is declared using the `package` keyword followed by the package name. The package name must match the directory/folder structure. For example, if the package name is `com..mypackage`, the folder structure should be `com//mypackage`.

```java
// Package declaration (must be first line)
package com..mypackage;
```

## Package Components

---

A package can contain the following components:

- Classes
- Interfaces
- Sub-packages
- Enumerations

All source files in a package must have the same package declaration.

## Importing Packages

---

The `import` keyword is used to access classes from other packages. There are two types of import statements:

- **Specific Import**: Imports a specific class from a package.
- **Wildcard Import**: Imports all classes from a package.

```java
// Specific import
import com..mypackage.MyClass;

// Wildcard import
import java.util.*;
```

## Built-in Packages

---

Java provides several built-in packages, including:

- `java.lang`: Contains fundamental classes such as `String`, `Integer`, and `Math`.
- `java.util`: Contains utility classes such as `ArrayList`, `LinkedList`, and `HashMap`.
- `java.io`: Contains classes for input/output operations such as `File`, `InputStream`, and `OutputStream`.
- `java.awt`: Contains classes for graphics and GUI programming such as `Graphics`, `JFrame`, and `JButton`.
- `java.net`: Contains classes for networking such as `Socket`, `ServerSocket`, and `URL`.

## Default Package

---

A class without a package declaration belongs to the default package. The default package is unnamed and is not recommended for use in large-scale applications.

## Package Naming Conventions

---

Package names follow the reverse domain naming convention. For example, if a company's domain name is `.com`, the package name could be `com..project`.

## Fully Qualified Name

---

The fully qualified name of a class includes the package name. For example, if a class `MyClass` is in package `com..mypackage`, the fully qualified name is `com..mypackage.MyClass`.

## Advantages of Packages

---

Packages provide several advantages, including:

- **Namespace Management**: Packages help to avoid naming conflicts between classes.
- **Access Control**: Packages provide a way to control access to classes and their members.
- **Modularization**: Packages help to modularize code and promote maintainability.

## Creating a User-Defined Package

---

To create a user-defined package, follow these steps:

1. Create a new folder with the package name (e.g., `com//mypackage`).
2. Create a new Java source file inside the package folder (e.g., `MyClass.java`).
3. Declare the package name at the top of the source file using the `package` keyword.
4. Compile the source file using the `javac` command.

## Example Program

---

Here is an example program that demonstrates how to create and use a user-defined package:

```java
// Package declaration (must be first line)
package com..mypackage;

// Class declaration
public class MyClass {
 public static void main(String[] args) {
 System.out.println("Hello, World!");
 }
}
```

To compile and run this program, follow these steps:

1. Save the source file `MyClass.java` in the package folder `com//mypackage`.
2. Compile the source file using the `javac` command: `javac com//mypackage/MyClass.java`
3. Run the program using the `java` command: `java com..mypackage.MyClass`

## Exam Tips

---

- Remember that the package declaration must be the first executable statement in the file.
- Make sure to include the root directory containing the package folders in the classpath.
- Be prepared to answer questions about the purpose of packages and how to create a user-defined package.
- Don't confuse `import` with C++ `#include` — import only makes classes accessible, doesn't copy code.

## Key Takeaways

---

- Packages are a logical grouping of related classes, interfaces, and sub-packages.
- Packages provide namespace management, access control, and help avoid naming conflicts between classes.
- The `package` keyword is used to declare a package, and the `import` keyword is used to access classes from other packages.
- Java provides several built-in packages, and you can create your own user-defined packages.
- Packages help to modularize code and promote maintainability.
