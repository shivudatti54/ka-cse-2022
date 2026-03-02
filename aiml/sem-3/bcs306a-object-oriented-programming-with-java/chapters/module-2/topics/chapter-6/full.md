# Object Oriented Programming with JAVA

## Chapter 6: Introducing Classes

In this chapter, we will delve into the fundamentals of classes in object-oriented programming (OOP) with Java. Classes are the building blocks of OOP, and understanding them is crucial for any aspiring Java developer.

### Historical Context

The concept of classes has its roots in the 1930s, when the first OOP language, Simula, was developed. However, it was not until the publication of the book "Object-Oriented Programming: An Introduction" by Douglas T. Ross in 1987 that the concept of classes became widely accepted.

In Java, classes were introduced in the first version of the language, Java 1.0, in 1995. Since then, classes have become a fundamental part of the Java language.

### Class Fundamentals

A class is a blueprint or a template that defines the properties and behavior of an object. It is essentially a design pattern or a template that defines the characteristics of an object.

A class typically consists of the following elements:

#### 1. Class Name

The class name is a unique identifier that distinguishes one class from another. It is usually written in uppercase letters and is followed by a colon (:).

#### 2. Class Body

The class body is the group of statements that define the properties and behavior of the class. It is enclosed in curly brackets ({}) and is usually written in the following format:

```java
public class ClassName {
    // class body
}
```

#### 3. Properties (Data Members)

Properties, also known as data members, are the variables that are associated with a class. They are used to store data that is specific to the class. Properties can be accessed and modified using getter and setter methods.

#### 4. Methods (Behavior)

Methods are the functions that are defined within a class. They are used to perform actions that can be performed on the data stored in the properties. Methods can take arguments and return values.

#### 5. Constructors

Constructors are special methods that are used to initialize objects when they are created. They are called when an object is instantiated, and they are used to set the initial values of the properties.

### Declaring Objects

An object is an instance of a class. It is a concrete entity that has its own set of properties and behavior. To declare an object, we need to create an instance of the class using the `new` keyword.

```java
public class Person {
    private String name;
    private int age;
}

public class Main {
    public static void main(String[] args) {
        // declare an object of the Person class
        Person person = new Person();
    }
}
```

### Assigning Object Reference Variables

An object reference variable is a variable that holds the memory address of an object. It is a pointer that points to the object in memory. Object reference variables are used to refer to objects that have been declared.

```java
public class Person {
    private String name;
    private int age;
}

public class Main {
    public static void main(String[] args) {
        // declare an object reference variable
        Person personRef = new Person();
    }
}
```

### UML Diagrams

UML (Unified Modeling Language) diagrams are used to model the structure and behavior of a system. There are several types of UML diagrams that can be used to model a class, including:

#### 1. Class Diagram

A class diagram is a type of UML diagram that is used to model the structure of a class. It typically consists of a rectangle that represents the class, and it may contain attributes (data members) and methods (behavior).

```markdown
+---------------+
| Person |
+---------------+
| - name |
| - age |
+---------------+
| - getName() |
| - setAge(int) |
+---------------+
```

#### 2. Object Diagram

An object diagram is a type of UML diagram that is used to model the structure of an object. It typically consists of one or more objects that are instances of a class.

```markdown
+---------------+
| Person1 |
| - name: John |
| - age: 25 |
+---------------+
+---------------+
| Person2 |
| - name: Jane |
| - age: 30 |
+---------------+
```

### Case Study

Suppose we want to create a program that allows us to store and retrieve information about employees. We can define a `Employee` class that has properties for `name`, `age`, and `salary`, and methods for `getName()`, `setAge(int)`, `getSalary()`, and `setSalary(double)`.

```java
public class Employee {
    private String name;
    private int age;
    private double salary;

    public Employee(String name, int age, double salary) {
        this.name = name;
        this.age = age;
        this.salary = salary;
    }

    public String getName() {
        return name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }
}

public class Main {
    public static void main(String[] args) {
        // declare an object reference variable
        Employee employeeRef = new Employee("John", 25, 50000.0);

        // access and modify properties
        System.out.println("Name: " + employeeRef.getName());
        employeeRef.setAge(26);
        System.out.println("Age: " + employeeRef.getAge());
    }
}
```

### Applications

Classes have a wide range of applications in various fields, including:

#### 1. Software Development

Classes are used to model real-world objects and systems in software development. They allow developers to create reusable code and improve code organization.

#### 2. Database Management

Classes are used to model database tables and relationships in database management. They allow developers to create complex database structures and improve data integrity.

#### 3. Scientific Computing

Classes are used to model complex systems and phenomena in scientific computing. They allow developers to create realistic simulations and improve computational efficiency.

### Further Reading

- "Head First Java" by Kathy Sierra and Bert Bates
- "Java: A Beginner's Guide" by Herbert Schildt
- "Thinking in Java" by Bruce Eckel
- "Object-Oriented Programming in Java" by Keith D. Cooper and Sunil T. Gokhale
- "UML for Java Programmers" by Scott Ambler and Mark Richards

## Conclusion

In this chapter, we have learned about the fundamentals of classes in object-oriented programming with Java. We have covered the definition of a class, the different types of classes, and the various elements that make up a class. We have also discussed the declaration of objects, assigning object reference variables, and the use of UML diagrams to model classes.
