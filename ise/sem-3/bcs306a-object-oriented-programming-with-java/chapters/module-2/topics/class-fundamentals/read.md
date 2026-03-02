# Class Fundamentals

## Introduction

In object-oriented programming, a CLASS serves as the fundamental building block that defines the blueprint or template for creating objects. When studying Java as part of the University of Delhi Computer Science curriculum, understanding class fundamentals becomes essential for mastering object-oriented programming concepts. A class encapsulates data (in the form of fields or variables) and behavior (in the form of methods), providing a mechanism to model real-world entities in software design.

The concept of classes forms the cornerstone of OOP because it enables programmers to create custom data types that extend beyond the primitive types provided by Java. Every object in Java is an instance of a class, and the class definition determines what attributes an object will have and what operations it can perform. This abstraction allows developers to model complex systems by breaking them down into manageable, reusable components. For instance, a "Student" class can define properties like name, roll number, and marks, along with methods to calculate grades or display information.

In the context of DU's Computer Science program, class fundamentals are not just theoretical concepts but practical skills tested extensively in both internal assessments and end-semester examinations. Students must understand how to define classes, declare objects, and implement methods to write effective Java programs. This topic connects directly with other concepts in the module, including constructors, method overloading, and access control, making it a foundational topic for the entire OOP paradigm.

## Key Concepts

### Definition and Structure of a Class

A CLASS in Java is a user-defined data type that acts as a blueprint for creating objects. The general syntax for defining a class is:

```java
[access_modifier] class ClassName {
    // fields (instance variables)
    // constructors
    // methods
}
```

The class body is enclosed within curly braces and contains three major components: FIELDS (also called instance variables or attributes), CONSTRUCTORS (special methods for initializing objects), and METHODS (functions that define behavior). Each of these components plays a distinct role in defining the structure and functionality of objects created from the class.

### Instance Variables and Class Variables

INSTANCE VARIABLES are declared inside a class but outside any method. Each object created from the class has its own copy of instance variables, meaning their values can differ from one object to another. These variables represent the state or attributes of an object. For example, in a BankAccount class, each account object would have its own balance and account number.

CLASS VARIABLES (declared using the static keyword) are shared among all instances of a class. There is only one copy of a static variable per class, regardless of how many objects are created. Static variables are useful for storing constants or values that should be common to all objects, such as the total number of BankAccount objects created.

### Methods in Classes

METHODS are blocks of code that perform specific tasks and can be invoked on objects. A method consists of a method signature (name and parameters) and a method body (the actual code). Methods can return a value or return void if they do not return anything. The general structure includes:

```java
return_type method_name(parameter_list) {
    // method body
    // return statement (if return_type is not void)
}
```

Methods provide the behavioral aspect of a class. They can access and modify instance variables, call other methods, and perform computations. Methods can also be classified as instance methods (operating on instance variables) or static methods (belonging to the class rather than any instance).

### Access Modifiers and Encapsulation

ACCESS MODIFIERS control the visibility and accessibility of class members. Java provides four access levels: public (accessible from anywhere), protected (accessible within the same package and subclasses), default or package-private (accessible within the same package only), and private (accessible only within the same class). The use of private access modifier for instance variables with public getter and setter methods exemplifies ENCAPSULATION, a fundamental OOP principle that restricts direct access to some components and prevents unintended interference.

Encapsulation protects the internal state of an object from accidental modification and allows the class to enforce its own invariants. By making instance variables private and providing public methods to access and modify them (getters and setters), programmers can validate input, maintain data integrity, and change internal implementation without affecting code that uses the class.

### Object Declaration and Initialization

OBJECTS are instances of a class created using the `new` keyword, which allocates memory for the object and calls a constructor to initialize it. The process involves two steps: declaring a reference variable and creating the actual object. For example:

```java
Student student1;              // Declaration
student1 = new Student();     // Creation and initialization
```

The `new` operator dynamically allocates memory on the heap and returns a reference to the newly created object. This reference is stored in the reference variable, which can then be used to access the object's fields and methods.

## Examples

### Example 1: Defining a Simple Class

Consider a class to represent a Rectangle in a geometric application.

```java
public class Rectangle {
    // Instance variables (fields)
    private double length;
    private double width;
    
    // Constructor
    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }
    
    // Getter methods
    public double getLength() {
        return length;
    }
    
    public double getWidth() {
        return width;
    }
    
    // Method to calculate area
    public double calculateArea() {
        return length * width;
    }
    
    // Method to calculate perimeter
    public double calculatePerimeter() {
        return 2 * (length + width);
    }
}
```

To use this class:

```java
public class RectangleDemo {
    public static void main(String[] args) {
        Rectangle rect1 = new Rectangle(10.5, 5.5);
        Rectangle rect2 = new Rectangle(7.0, 3.0);
        
        System.out.println("Rectangle 1:");
        System.out.println("Length: " + rect1.getLength());
        System.out.println("Width: " + rect1.getWidth());
        System.out.println("Area: " + rect1.calculateArea());
        System.out.println("Perimeter: " + rect1.calculatePerimeter());
        
        System.out.println("\nRectangle 2:");
        System.out.println("Area: " + rect2.calculateArea());
    }
}
```

This example demonstrates encapsulation (private fields with public methods), constructors for initialization, and methods that operate on instance data.

### Example 2: Class with Static Variable

A class to track the number of employees in a company:

```java
public class Employee {
    // Instance variable (unique to each employee)
    private int empId;
    private String name;
    private String department;
    
    // Class variable (shared among all employees)
    private static int employeeCount = 0;
    
    // Constructor
    public Employee(String name, String department) {
        employeeCount++;
        this.empId = employeeCount;
        this.name = name;
        this.department = department;
    }
    
    // Static method to get employee count
    public static int getEmployeeCount() {
        return employeeCount;
    }
    
    // Instance methods
    public void displayInfo() {
        System.out.println("Employee ID: " + empId);
        System.out.println("Name: " + name);
        System.out.println("Department: " + department);
    }
}

public class EmployeeDemo {
    public static void main(String[] args) {
        Employee emp1 = new Employee("Aisha", "Computer Science");
        Employee emp2 = new Employee("Raj", "Mathematics");
        Employee emp3 = new Student("Priya", "Physics");
        
        emp1.displayInfo();
        System.out.println();
        emp2.displayInfo();
        System.out.println();
        
        // Accessing static variable via class name
        System.out.println("Total Employees: " + Employee.getEmployeeCount());
    }
}
```

This example illustrates the use of static variables to maintain shared state across all instances and demonstrates how static methods can be called using the class name without creating any object.

### Example 3: Parameterized Constructor and this Keyword

```java
public class Book {
    private String title;
    private String author;
    private double price;
    
    // Parameterized constructor
    public Book(String title, String author, double price) {
        this.title = title;
        this.author = author;
        this.price = price;
    }
    
    // Copy constructor
    public Book(Book other) {
        this.title = other.title;
        this.author = other.author;
        this.price = other.price;
    }
    
    // Display method
    public void display() {
        System.out.println("Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("Price: Rs. " + price);
    }
    
    public static void main(String[] args) {
        Book b1 = new Book("Let Us C", "Yashavant Kanetkar", 450.00);
        Book b2 = new Book(b1);  // Using copy constructor
        
        System.out.println("Book 1:");
        b1.display();
        System.out.println("\nBook 2 (Copy):");
        b2.display();
    }
}
```

The `this` keyword is used to distinguish between instance variables and parameters with the same name. This example also demonstrates a copy constructor that creates a new object with the same values as an existing object.

## Exam Tips

For the DU semester examinations, keep the following points in mind when answering questions on Class Fundamentals:

1. MEMORY ALLOCATION: Remember that when an object is created using `new`, memory is allocated on the heap, and the constructor is automatically invoked. The reference variable stores the memory address (reference) to the object.

2. DEFAULT VALUES: Instance variables get default values (0 for numeric, false for boolean, null for reference types) even if not explicitly initialized, but local variables must be explicitly initialized before use.

3. STATIC VS INSTANCE: In exam questions, carefully identify whether a variable or method should be static based on whether it needs to access instance-specific data. Static methods cannot access instance variables directly.

4. ENCAPSULATION BENEFITS: When explaining encapsulation, mention data hiding, easier maintenance, reusability, and the ability to validate input before modifying instance variables.

5. CONSTRUCTOR OVERLOADING: Multiple constructors can exist in a class with different parameter lists. This is an example of compile-time polymorphism.

6. THIS KEYWORD: The `this` keyword always refers to the current object and can be used to resolve naming conflicts between instance variables and parameters, or to call one constructor from another using `this(arguments)`.

7. EXAM CODING PATTERNS: Practice writing complete class definitions with appropriate access modifiers, constructors, getters, setters, and business logic methods. Most exam questions require complete, compilable code.

8. COMMON ERRORS: Avoid confusing class variables with instance variables, forgetting to initialize objects before use, or attempting to access non-static members from static contexts (like the main method).