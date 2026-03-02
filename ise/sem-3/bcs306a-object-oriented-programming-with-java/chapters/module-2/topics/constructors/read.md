# Constructors in Java

## Introduction

Constructors are fundamental building blocks in object-oriented programming with Java that initialize newly created objects. When you create an object using the `new` keyword, a constructor is automatically invoked to set up the initial state of the object. Without constructors, objects would be created without any initial values, leading to unpredictable behavior and potential runtime errors. In the context of the University of Delhi's Computer Science curriculum, understanding constructors is essential for mastering class design and object instantiation—key concepts that appear frequently in both internal assessments and end semester examinations.

The Java constructor mechanism differs significantly from traditional procedural programming functions. Unlike methods, constructors have no return type (not even void) and share the same name as the class they initialize. This design choice by Java's creators emphasizes the special role constructors play in object lifecycle management. As you progress through your studies, you will discover that constructors are not merely initialization routines but powerful tools that enable encapsulation, provide validation, and support sophisticated object creation patterns used in real-world software development.

## Key Concepts

### What is a Constructor?

A constructor is a special method in a class that is called when an object of the class is instantiated. Its primary purpose is to initialize the object's state by assigning initial values to its instance variables. The constructor has the same name as the class and is distinguished from regular methods by the absence of a return type specification.

Consider the basic syntax:

```java
class Student {
    String name;
    int rollNumber;
    double marks;
    
    // This is a constructor
    Student(String n, int r, double m) {
        name = n;
        rollNumber = r;
        marks = m;
    }
}
```

When you create an object using `new Student("Aisha", 101, 95.5)`, the constructor automatically executes, initializing the Student object with the provided values.

### Types of Constructors

**Default Constructor (No-Arg Constructor)**

A default constructor is a constructor that takes no arguments. If you do not explicitly define any constructor in your class, the Java compiler automatically provides a default constructor that initializes all instance variables to their default values (0 for numeric types, null for reference types, false for boolean, '\u0000' for char).

```java
class BankAccount {
    String accountHolder;
    double balance;
    
    // Default constructor provided by compiler
}
```

However, once you define any constructor (with parameters), the compiler no longer provides the default constructor:

```java
class BankAccount {
    String accountHolder;
    double balance;
    
    // Parameterized constructor
    BankAccount(String holder, double initialBalance) {
        accountHolder = holder;
        balance = initialBalance;
    }
}

// This will cause a compilation error
BankAccount acc = new BankAccount(); // Error: No constructor
```

**Parameterized Constructor**

A parameterized constructor accepts one or more arguments, allowing you to initialize objects with specific values at the time of creation. This is the most commonly used constructor type in professional Java development:

```java
class Employee {
    int id;
    String name;
    String department;
    double salary;
    
    Employee(int empId, String empName, String dept, double empSalary) {
        id = empId;
        name = empName;
        department = dept;
        salary = empSalary;
    }
}
```

**Constructor Overloading**

Like methods, constructors can be overloaded—meaning a class can have multiple constructors with different parameter lists. The Java compiler distinguishes between overloaded constructors based on the number, type, and order of parameters:

```java
class Rectangle {
    int length;
    int breadth;
    
    // Constructor 1: No parameters (default values)
    Rectangle() {
        length = 0;
        breadth = 0;
    }
    
    // Constructor 2: One parameter (square)
    Rectangle(int side) {
        length = side;
        breadth = side;
    }
    
    // Constructor 3: Two parameters (rectangle)
    Rectangle(int l, int b) {
        length = l;
        breadth = b;
    }
}
```

### Constructor Chaining

Constructor chaining occurs when one constructor calls another constructor in the same class using the `this()` keyword. This approach reduces code duplication when multiple constructors share common initialization logic:

```java
class Customer {
    String name;
    String email;
    String phone;
    String address;
    
    // Primary constructor with all fields
    Customer(String name, String email, String phone, String address) {
        this.name = name;
        this.email = email;
        this.phone = phone;
        this.address = address;
    }
    
    // Secondary constructor calling primary constructor
    Customer(String name, String email) {
        this(name, email, "Not Provided", "Not Provided");
    }
    
    // Third constructor calling secondary constructor
    Customer(String name) {
        this(name, "Not Provided");
    }
}
```

### Copy Constructor

Unlike C++, Java does not provide a native copy constructor. However, you can implement one manually to create a new object as a copy of an existing object:

```java
class Book {
    String title;
    String author;
    int pages;
    
    Book(String title, String author, int pages) {
        this.title = title;
        this.author = author;
        this.pages = pages;
    }
    
    // Copy constructor
    Book(Book other) {
        this.title = other.title;
        this.author = other.author;
        this.pages = other.pages;
    }
}
```

### Constructor vs Methods

Understanding the distinction between constructors and regular methods is crucial for examination success:

| Feature | Constructor | Method |
|---------|-------------|--------|
| Return Type | None (not even void) | Required (void, int, etc.) |
| Name | Same as class name | Can be any valid identifier |
| Invocation | Automatic on object creation | Explicit method call |
| Inheritance | Not inherited | Can be inherited and overridden |
| this/super | Can use this() and super() | Cannot call as this() or super() |

## Examples

### Example 1: Bank Account System

Create a BankAccount class with constructors to initialize different types of accounts:

```java
class BankAccount {
    private String accountNumber;
    private String holderName;
    private double balance;
    private String accountType;
    
    // Default constructor
    BankAccount() {
        accountNumber = "Not Assigned";
        holderName = "Unknown";
        balance = 0.0;
        accountType = "Savings";
    }
    
    // Parameterized constructor for savings account
    BankAccount(String accNo, String name, double initialBalance) {
        accountNumber = accNo;
        holderName = name;
        balance = initialBalance;
        accountType = "Savings";
    }
    
    // Parameterized constructor for specific account type
    BankAccount(String accNo, String name, double initialBalance, String type) {
        accountNumber = accNo;
        holderName = name;
        balance = initialBalance;
        accountType = type;
    }
    
    void display() {
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Holder Name: " + holderName);
        System.out.println("Balance: Rs. " + balance);
        System.out.println("Account Type: " + accountType);
    }
}

public class TestBank {
    public static void main(String[] args) {
        BankAccount acc1 = new BankAccount();
        BankAccount acc2 = new BankAccount("SB12345", "Rahul Sharma", 5000);
        BankAccount acc3 = new BankAccount("CA98765", "Priya Singh", 25000, "Current");
        
        System.out.println("=== Account 1 (Default) ===");
        acc1.display();
        System.out.println("\n=== Account 2 (Savings) ===");
        acc2.display();
        System.out.println("\n=== Account 3 (Current) ===");
        acc3.display();
    }
}
```

**Output:**
```
=== Account 1 (Default) ===
Account Number: Not Assigned
Holder Name: Unknown
Balance: Rs. 0.0
Account Type: Savings

=== Account 2 (Savings) ===
Account Number: SB12345
Holder Name: Rahul Sharma
Balance: Rs. 5000.0
Account Type: Savings

=== Account 3 (Current) ===
Account Number: CA98765
Holder Name: Priya Singh
Balance: Rs. 25000.0
Account Type: Current
```

### Example 2: Constructor with Validation

Implement a constructor with validation to ensure data integrity:

```java
class Student {
    private String name;
    private int age;
    private double marks;
    
    // Constructor with validation
    Student(String name, int age, double marks) {
        // Validate name
        if (name == null || name.trim().isEmpty()) {
            this.name = "Unknown";
        } else {
            this.name = name;
        }
        
        // Validate age (reasonable range for student)
        if (age < 0 || age > 150) {
            this.age = 0;
        } else {
            this.age = age;
        }
        
        // Validate marks (0-100 range)
        if (marks < 0 || marks > 100) {
            this.marks = 0.0;
        } else {
            this.marks = marks;
        }
    }
    
    void showDetails() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Marks: " + marks);
    }
}

public class TestValidation {
    public static void main(String[] args) {
        Student s1 = new Student("Arjun", 20, 85.5);
        Student s2 = new Student("", -5, 150); // Invalid data
        
        System.out.println("=== Valid Student ===");
        s1.showDetails();
        System.out.println("\n=== Invalid Data (Validated) ===");
        s2.showDetails();
    }
}
```

### Example 3: Constructor Chaining with Employee Class

```java
class Employee {
    int id;
    String name;
    String department;
    double salary;
    
    // Primary constructor
    Employee(int id, String name, String department, double salary) {
        this.id = id;
        this.name = name;
        this.department = department;
        this.salary = salary;
    }
    
    // Secondary constructor: defaults department to "General"
    Employee(int id, String name, double salary) {
        this(id, name, "General", salary);
    }
    
    // Tertiary constructor: defaults department to "General" and salary to 0
    Employee(int id, String name) {
        this(id, name, "General", 0.0);
    }
    
    void display() {
        System.out.println("ID: " + id);
        System.out.println("Name: " + name);
        System.out.println("Department: " + department);
        System.out.println("Salary: " + salary);
    }
}

public class TestEmployee {
    public static void main(String[] args) {
        Employee e1 = new Employee(101, "Kavya", "IT", 55000);
        Employee e2 = new Employee(102, "Vikram", 40000);
        Employee e3 = new Employee(103, "Anjali");
        
        e1.display();
        System.out.println();
        e2.display();
        System.out.println();
        e3.display();
    }
}
```

## Exam Tips

1. **Remember the constructor signature**: Constructors have no return type, not even void. Writing `void ClassName()` creates a regular method, not a constructor.

2. **Default constructor disappears when you define any constructor**: If you define a parameterized constructor, the compiler no longer provides a free default constructor.

3. **Constructor overloading depends on parameter list**: The compiler distinguishes constructors by the number, type, and order of parameters—return type is not considered.

4. **Use this() for constructor chaining**: Remember that `this()` must be the first statement in a constructor to call another constructor in the same class.

5. **Constructors are not inherited**: Unlike methods, constructors cannot be overridden or inherited by subclasses.

6. **Access modifiers apply to constructors**: You can make constructors public, private, protected, or default to control object creation (private constructors implement the Singleton pattern).

7. **Constructors initialize instance variables**: Always initialize all instance variables in constructors to avoid working with default values (0, null, false).

8. **Superclass constructor**: If your class extends another class, the subclass constructor implicitly calls the superclass default constructor using `super()` before executing its own code.