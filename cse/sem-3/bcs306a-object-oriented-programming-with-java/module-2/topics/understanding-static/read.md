# Understanding Static

## Table of Contents

- [Understanding Static](#understanding-static)
- [Overview](#overview)
- [Static Variables](#static-variables)
  - [Declaration and Initialization](#declaration-and-initialization)
  - [Sharing Among Instances](#sharing-among-instances)
- [Static Methods](#static-methods)
  - [Declaration and Use](#declaration-and-use)
  - [Restrictions](#restrictions)
- [Comparison of Static and Instance Members](#comparison-of-static-and-instance-members)
- [Class Loading Process](#class-loading-process)
- [Implications of Using Static Members](#implications-of-using-static-members)
- [Exam Tips](#exam-tips)

## Overview

In Java, the `static` keyword is used to denote a variable, method, or block that belongs to the class itself, rather than an instance of the class. Static variables are shared among all instances of a class, while instance variables are unique to each instance.

## Static Variables

### Declaration and Initialization

A static variable is declared using the `static` keyword. It is loaded into memory only once, when the class is loaded.

```java
public class Employee {
 static String company = ""; // static variable
}
```

### Sharing Among Instances

Static variables are shared among all instances of a class. Changes to a static variable affect all instances of the class.

```java
public class Employee {
 static String company = ""; // static variable
 int id; // instance variable

 Employee(int id) {
 this.id = id;
 }

 void display() {
 System.out.println("ID: " + id + ", Company: " + company);
 }

 public static void main(String[] args) {
 Employee e1 = new Employee(101);
 Employee e2 = new Employee(102);
 e1.display(); // Output: ID: 101, Company:
 e2.display(); // Output: ID: 102, Company:

 // Changing static variable
 Employee.company = " Engineering";
 e1.display(); // Output: ID: 101, Company: Engineering
 e2.display(); // Output: ID: 102, Company: Engineering
 }
}
```

## Static Methods

### Declaration and Use

A static method is declared using the `static` keyword. It can access only static variables and can be called without creating an instance of the class.

```java
public class Employee {
 static String company = ""; // static variable

 static void displayCompany() {
 System.out.println("Company: " + company);
 }

 public static void main(String[] args) {
 Employee.displayCompany(); // Output: Company:
 }
}
```

### Restrictions

Static methods cannot directly access instance variables or methods.

```java
public class Employee {
 int id; // instance variable

 static void displayId() {
 // Error: cannot access instance variable from static method
 System.out.println("ID: " + id);
 }
}
```

## Comparison of Static and Instance Members

|                        | Static Members                       | Instance Members                        |
| ---------------------- | ------------------------------------ | --------------------------------------- |
| **Belongs to**         | Class itself                         | Instance of the class                   |
| **Loaded into memory** | Only once, when the class is loaded  | Every time an instance is created       |
| **Access**             | Can be accessed using the class name | Can be accessed using the instance name |
| **Sharing**            | Shared among all instances           | Unique to each instance                 |

## Class Loading Process

When a class is loaded into memory, its static variables are initialized. This process happens only once, when the class is first loaded.

## Implications of Using Static Members

Using static members can have implications on memory management and object creation. Since static variables are shared among all instances, changes to a static variable affect all instances. Additionally, static methods can be called without creating an instance of the class, which can be useful for utility methods.

## Exam Tips

- Be prepared to identify and explain the use of static variables in a given Java program.
- Understand how changes to a static variable affect all instances of a class.
- Focus on the differences between static and instance variables.
- Practice designing simple Java classes that effectively use static variables and methods to achieve a specific purpose.
