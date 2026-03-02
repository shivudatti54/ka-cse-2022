# **Chapter 9: Packages, Packages and Member Access, Importing Packages**

## **Introduction**

In Java, a package is a collection of related classes, interfaces, and other types that can be used together in a program. In this chapter, we will learn about packages, package access, member access, and importing packages.

## **What is a Package?**

A package is a way to organize related classes, interfaces, and other types in Java. It is a way to group related types together to make them easier to use and to avoid naming conflicts.

### Benefits of Packages

- Organizes related types together
- Avoids naming conflicts
- Makes types easier to use
- Allows us to create a namespace

## **Declaring a Package**

To declare a package in Java, we use the `package` keyword followed by the name of the package.

```java
package com.example.mypackage;
```

### Example

```java
// MyClass.java
package com.example.mypackage;

public class MyClass {
    // Class definition
}
```

## **Importing Packages**

To use a type from a package, we need to import it. We use the `import` keyword followed by the package name and the type we want to use.

### Example

```java
// Main.java
import com.example.mypackage.MyClass;

public class Main {
    public static void main(String[] args) {
        MyClass obj = new MyClass();
    }
}
```

## **Member Access**

Member access refers to the access level of a class member (method or variable). There are four levels of member access:

- **Public**: Can be accessed from anywhere
- **Protected**: Can be accessed from anywhere in the same class and its subclasses
- **Default**: Can be accessed from anywhere in the same package
- **Private**: Can only be accessed from within the same class

### Example

```java
// MyClass.java
package com.example.mypackage;

public class MyClass {
    // Public member
    public int x = 10;

    // Protected member
    protected int y = 20;

    // Default member
    int z = 30;

    // Private member
    private int w = 40;
}
```

```java
// Main.java
import com.example.mypackage.MyClass;

public class Main {
    public static void main(String[] args) {
        MyClass obj = new MyClass();
        System.out.println(obj.x); // Public member
        System.out.println(obj.y); // Protected member
        System.out.println(obj.z); // Default member
        obj.w = 50; // Can modify private member
        System.out.println(obj.w); // Can access private member
    }
}
```

## **Access Modifiers**

Access modifiers are used to define the access level of a class member. The four access modifiers are:

- **public**: Can be accessed from anywhere
- **protected**: Can be accessed from anywhere in the same class and its subclasses
- **default**: Can be accessed from anywhere in the same package
- **private**: Can only be accessed from within the same class

### Example

```java
// MyClass.java
package com.example.mypackage;

public class MyClass {
    // Public member
    public int x = 10;

    // Protected member
    protected int y = 20;

    // Default member
    int z = 30;

    // Private member
    private int w = 40;
}
```

```java
// Main.java
import com.example.mypackage.MyClass;

public class Main {
    public static void main(String[] args) {
        MyClass obj = new MyClass();
        System.out.println(obj.x); // Public member
        System.out.println(obj.y); // Protected member
        obj.z = 50; // Can modify default member
        obj.w = 60; // Can modify private member
        System.out.println(obj.x); // Can access public member
        System.out.println(obj.y); // Can access protected member
        System.out.println(obj.z); // Can access default member
        System.out.println(obj.w); // Can access private member
    }
}
```

## **Best Practices**

- Use access modifiers to define the access level of class members
- Use packages to organize related types together
- Avoid naming conflicts by using unique names for types
- Use import statements to use types from other packages
- Follow the single responsibility principle when designing classes
- Use inheritance to create a hierarchy of classes
