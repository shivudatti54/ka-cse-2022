# Variables in Java

## Introduction

Variables are fundamental building blocks in any programming language, and Java is no exception. A variable in Java represents a named storage location in memory that holds a value which can be modified during program execution. Understanding variables is essential for any Java programmer, as they form the foundation upon which data manipulation and program logic are built.

In the context of the University of Delhi's Computer Science curriculum, variables represent one of the first practical concepts students encounter when learning Java programming. This topic builds upon the theoretical knowledge of data types and prepares students for more complex topics like object-oriented programming, where variables serve as instance fields, static members, and local storage containers. The proper understanding of variable declaration, initialization, scope, and lifetime is crucial for writing efficient and bug-free Java code.

This chapter explores the concept of variables in Java comprehensively, covering variable types, naming conventions, memory allocation, and practical examples that demonstrate their usage in real-world Java applications. The knowledge gained here will be repeatedly applied throughout your Java programming journey, making it essential to master these concepts thoroughly.

## Key Concepts

### What is a Variable?

A variable is a container that holds data values which can be changed during the execution of a program. In Java, every variable has three essential properties: a type, a name, and a value. The type defines what kind of data the variable can hold, the name (also called identifier) is used to reference the variable in the code, and the value is the actual data stored in the variable's memory location.

Java is a statically typed language, meaning that the type of a variable must be declared at compile time. This is different from dynamically typed languages where variable types are determined at runtime. The static typing in Java provides type safety and helps catch errors early in the development process.

### Variable Declaration and Initialization

Before using a variable in Java, it must be declared. The declaration tells the compiler the variable's name and its data type. The basic syntax for declaring a variable is:

```java
dataType variableName;
```

For example:
```java
int age;
double salary;
String name;
```

Initialization is the process of assigning a value to a variable for the first time. In Java, you can declare and initialize a variable in a single statement:

```java
int age = 25;
double salary = 50000.50;
String name = "Amit Kumar";
```

It is important to note that using an uninitialized variable in Java will result in a compilation error. The compiler ensures that all variables are initialized before they are used, which prevents many common programming mistakes.

### Types of Variables in Java

Java defines four types of variables, each with different purposes, scopes, and lifetimes:

**Instance Variables (Non-Static Fields):**

Instance variables are declared inside a class but outside any method, constructor, or block. They are associated with objects (instances) of the class. Each object gets its own copy of instance variables. These variables are initialized to default values if not explicitly initialized. For numeric types, the default is 0; for boolean, it is false; and for object references, it is null.

```java
public class Student {
    String name;      // instance variable
    int rollNumber;   // instance variable
    double marks;     // instance variable
    
    public void display() {
        System.out.println("Name: " + name);
    }
}
```

**Static Variables (Class Variables):**

Static variables are declared using the static keyword. They belong to the class rather than to any specific object. Only one copy of a static variable exists regardless of how many objects are created. Static variables are initialized when the class is loaded into memory.

```java
public class University {
    static String universityName = "University of Delhi";  // static variable
    static int studentCount = 0;                            // static variable
    
    public University() {
        studentCount++;
    }
}
```

**Local Variables:**

Local variables are declared inside a method, constructor, or block. They exist only within the scope of that method or block and are not accessible outside it. Local variables do not have default values and must be initialized before use. They are stored on the stack memory.

```java
public void calculateSum() {
    int a = 10;  // local variable
    int b = 20;  // local variable
    int sum = a + b;  // local variable
    System.out.println("Sum: " + sum);
}
```

**Parameters:**

Parameters are variables that receive values passed to methods. They are considered local variables of the method. When a method is called, the parameters are initialized with the passed arguments.

```java
public void setAge(int age) {  // parameter
    this.age = age;
}
```

### Variable Naming Rules and Conventions

Java has strict rules for naming variables:

**Rules (Must Follow):**

- Variable names can contain letters, digits, underscores, and dollar signs ($).
- The first character cannot be a digit.
- Variable names are case-sensitive (age and Age are different).
- Cannot use Java keywords as variable names.
- Cannot have spaces in variable names.

**Conventions (Should Follow):**

- Use camelCase for variable names (e.g., firstName, totalAmount).
- Use meaningful and descriptive names.
- Start with a lowercase letter.
- For constants (final variables), use UPPERCASE with underscores (e.g., MAX_VALUE).
- Avoid single-letter names except for loop counters.

### Scope and Lifetime of Variables

The scope of a variable determines where in the program the variable can be accessed. In Java, scope is determined by the block in which the variable is declared:

- **Class Scope:** Instance and static variables are accessible throughout the class.
- **Method Scope:** Local variables and parameters are accessible only within the method.
- **Block Scope:** Variables declared inside a block (e.g., inside an if statement or for loop) are accessible only within that block.

The lifetime of a variable refers to how long the variable exists in memory:

- Instance variables exist as long as the object exists.
- Static variables exist for the entire duration of the program.
- Local variables exist only during the execution of the method or block.
- Parameters exist only during the execution of the method.

### Memory Allocation

Java manages memory automatically through its garbage collection mechanism. However, understanding memory allocation helps in writing efficient code:

- **Stack Memory:** Stores local variables and method call information.
- **Heap Memory:** Stores objects and instance variables.
- **Method Area:** Stores class-level information including static variables.

When you create an object using the new keyword, the object is stored in heap memory, and the reference variable points to that memory location. Primitive variables are stored directly in the stack if they are local, or in the heap if they are instance variables of an object.

## Examples

### Example 1: Demonstrating Variable Declaration and Initialization

```java
public class VariableDemo {
    // Instance variables
    String studentName;
    int studentAge;
    double studentGrade;
    
    public static void main(String[] args) {
        // Local variables - must be initialized before use
        String courseName = "Computer Science";
        int semester = 1;
        float fee = 15000.50f;
        
        // Display local variables
        System.out.println("Course: " + courseName);
        System.out.println("Semester: " + semester);
        System.out.println("Fee: " + fee);
        
        // Creating object to access instance variables
        VariableDemo demo = new VariableDemo();
        demo.studentName = "Priya Sharma";
        demo.studentAge = 19;
        demo.studentGrade = 85.5;
        
        System.out.println("Student Name: " + demo.studentName);
        System.out.println("Student Age: " + demo.studentAge);
        System.out.println("Student Grade: " + demo.studentGrade);
    }
}
```

**Output:**
```
Course: Computer Science
Semester: 1
Fee: 15000.5
Student Name: Priya Sharma
Student Age: 19
Student Grade: 85.5
```

### Example 2: Static vs Instance Variables

```java
public class Library {
    // Static variable - shared by all objects
    static String libraryName = "Central Library";
    static int totalBooks = 0;
    
    // Instance variable - unique to each object
    String bookTitle;
    String author;
    int bookId;
    
    Library(String title, String author) {
        this.bookTitle = title;
        this.author = author;
        bookId = ++totalBooks;  // Increment static counter
    }
    
    public void display() {
        System.out.println("Book ID: " + bookId);
        System.out.println("Title: " + bookTitle);
        System.out.println("Author: " + author);
        System.out.println("Library: " + libraryName);
        System.out.println("Total Books: " + totalBooks);
    }
    
    public static void main(String[] args) {
        Library book1 = new Library("Data Structures", "Cormen");
        Library book2 = new Library("Database Systems", "Silberschatz");
        
        System.out.println("=== Book 1 Details ===");
        book1.display();
        
        System.out.println("\n=== Book 2 Details ===");
        book2.display();
    }
}
```

**Output:**
```
=== Book 1 Details ===
Book ID: 1
Title: Data Structures
Author: Cormen
Library: Central Library
Total Books: 1

=== Book 2 Details ===
Book ID: 2
Title: Database Systems
Author: Silberschatz
Library: Central Library
Total Books: 2
```

### Example 3: Local Variable Scope

```java
public class ScopeDemo {
    int instanceVar = 10;  // Instance variable
    
    public void demonstrateScope() {
        int localVar = 20;  // Local variable
        
        System.out.println("Instance Variable: " + instanceVar);
        System.out.println("Local Variable: " + localVar);
        
        if (localVar > 15) {
            int blockVar = 30;  // Block-scoped variable
            System.out.println("Block Variable: " + blockVar);
            System.out.println("Can access localVar here: " + localVar);
        }
        
        // System.out.println(blockVar);  // ERROR - blockVar not accessible here
        
        for (int i = 0; i < 3; i++) {
            System.out.println("Loop counter i: " + i);
        }
        // System.out.println(i);  // ERROR - i not accessible here
    }
    
    public static void main(String[] args) {
        ScopeDemo demo = new ScopeDemo();
        demo.demonstrateScope();
        
        // System.out.println(localVar);  // ERROR - localVar not accessible here
    }
}
```

## Exam Tips

1. **Remember the Four Types:** Be clear about instance variables, static variables, local variables, and parameters. Know their default values and scope rules.

2. **Default Values Matter:** Instance and static variables get default values (0, false, null), but local variables do not and must be initialized before use.

3. **Static vs Instance:** In exam questions, remember that static variables are shared across all objects and belong to the class, while instance variables are unique to each object.

4. **Variable Naming:** Know the difference between rules (mandatory) and conventions (recommended). Keywords cannot be used as variable names.

5. **Scope Determines Accessibility:** Understand that inner blocks can access outer variables, but outer blocks cannot access variables declared inside inner blocks.

6. **Memory Concept:** Remember that local variables are stored in stack memory, while objects (and their instance variables) are stored in heap memory.

7. **Initialization is Mandatory:** Always initialize local variables before use. Uninitialized local variables cause compilation errors, not runtime errors.

8. **Practice Code Analysis:** Be prepared to analyze code snippets and determine what values variables will hold at different points in program execution.