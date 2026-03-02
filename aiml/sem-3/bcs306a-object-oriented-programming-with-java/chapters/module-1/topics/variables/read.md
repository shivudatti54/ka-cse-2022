# Variables in Java

## Introduction

Variables are fundamental building blocks in any programming language, and Java is no exception. A variable in Java represents a named storage location in memory that holds a value which can be modified during program execution. Understanding variables is crucial for any Java programmer, as all data manipulation, computation, and data storage in Java programs occur through variables. In the context of object-oriented programming, variables serve as the state that objects maintain, making them essential for representing the attributes of classes and the data processed by methods.

In Java, variables must be declared before they can be used, and this declaration specifies the type of data the variable will hold. This strong typing system distinguishes Java from loosely typed languages and provides compile-time type checking, reducing runtime errors. The concept of variables in Java extends beyond simple storage containers to include different types based on their scope, lifetime, and usage context. Mastering variables is the first step toward writing effective Java programs, as they form the foundation upon which more complex data structures and algorithms are built.

## Key Concepts

### Variable Declaration and Initialization

In Java, a variable must be declared before it can be used. The basic syntax for declaring a variable is:

```
dataType variableName;
```

For example:
```java
int age;
double salary;
String name;
char grade;
boolean isActive;
```

A variable can be initialized at the time of declaration or later in the code:

```java
int age = 25;              // Declaration with initialization
int height;                // Declaration only
height = 170;              // Initialization later
```

The data type determines what kind of values the variable can hold and how much memory is allocated for it.

### Types of Variables in Java

Java defines four types of variables based on their location and usage:

**1. Instance Variables (Non-static Variables)**
Instance variables are declared inside a class but outside any method, constructor, or block. They are created when an object of the class is instantiated and destroyed when the object is destroyed. Each object has its own copy of instance variables.

```java
public class Student {
    String name;           // Instance variable
    int rollNumber;        // Instance variable
    double marks;          // Instance variable
    
    public void display() {
        System.out.println(name);
    }
}
```

**2. Class Variables (Static Variables)**
Static variables are declared using the `static` keyword within a class but outside any method. They are shared among all objects of the class and belong to the class rather than to any specific instance. Memory for static variables is allocated only once when the class is loaded.

```java
public class Company {
    static String companyName;  // Static variable
    static int employeeCount;   // Static variable
}
```

**3. Local Variables**
Local variables are declared inside a method, constructor, or block. They exist only within the scope of that method or block and must be initialized before use. They do not have default values, and the compiler will generate an error if an uninitialized local variable is accessed.

```java
public void calculate() {
    int a = 10;          // Local variable
    int b = 20;          // Local variable
    int sum = a + b;     // Local variable
    System.out.println(sum);
}
```

**4. Parameters (Formal Parameters)**
Parameters are variables declared in method definitions that receive values when the method is called. They act as local variables within the method scope.

```java
public void setAge(int age) {  // Parameter
    this.age = age;
}
```

### The `final` Keyword

Variables declared with the `final` keyword become constants and cannot be reassigned after initialization. Conventionally, final variable names are written in UPPERCASE with underscores separating words.

```java
final double PI = 3.14159;
final int MAX_SIZE = 100;
final String APP_NAME = "StudentPortal";
```

Attempting to modify a final variable results in a compile-time error.

### Type Inference with `var` (Java 10+)

Java 10 introduced local variable type inference, allowing the compiler to infer the type of a variable from its initializer:

```java
var name = "Alice";           // Compiler infers String
var count = 100;              // Compiler infers int
var price = 99.99;            // Compiler infers double
var list = new ArrayList<>(); // Compiler infers ArrayList
```

The `var` keyword can only be used for local variables with initializers, not for instance variables or method parameters.

### Variable Naming Conventions

Java follows specific rules and conventions for naming variables:

**Rules (Mandatory):**
- Variable names can contain letters, digits, underscores, and dollar signs ($)
- Must begin with a letter, underscore, or dollar sign
- Cannot use Java keywords as variable names
- Are case-sensitive (age, Age, and AGE are three different variables)

**Conventions (Recommended):**
- Use camelCase for variable names (first word lowercase, subsequent words uppercase)
- Choose meaningful, descriptive names
- Avoid single-letter names except for loop counters
- Do not start with underscore or dollar sign in normal coding

Valid examples: `studentName`, `totalAmount`, `isActive`, `calculateSum`
Invalid examples: `123abc`, `my-variable`, `class`

## Examples

### Example 1: Demonstrating Different Variable Types

```java
public class VariableDemo {
    // Instance variables
    String studentName;
    int studentId;
    
    // Static variable
    static String universityName = "University of Delhi";
    
    public void demonstrateLocalVariables(int marks) {
        // Local variable
        String grade;
        
        if (marks >= 90) {
            grade = "A+";
        } else if (marks >= 80) {
            grade = "A";
        } else if (marks >= 70) {
            grade = "B+";
        } else {
            grade = "Pass";
        }
        
        System.out.println("Grade: " + grade);
    }
    
    public static void main(String[] args) {
        VariableDemo demo = new VariableDemo();
        demo.studentName = "Priya Sharma";
        demo.studentId = 2024001;
        
        System.out.println("Student: " + demo.studentName);
        System.out.println("ID: " + demo.studentId);
        System.out.println("University: " + universityName);
        
        demo.demonstrateLocalVariables(85);
    }
}
```

Output:
```
Student: Priya Sharma
ID: 2024001
University: University of Delhi
Grade: A
```

### Example 2: Using `var` for Type Inference

```java
import java.util.ArrayList;
import java.util.HashMap;

public class VarDemo {
    public static void main(String[] args) {
        // Type inference with var
        var message = "Welcome to Java Programming";
        var number = 42;
        var decimal = 3.14;
        var isEligible = true;
        
        // var with collections
        var list = new ArrayList<String>();
        list.add("Computer Science");
        list.add("Mathematics");
        
        var map = new HashMap<String, Integer>();
        map.put("Physics", 85);
        map.put("Chemistry", 90);
        
        // Displaying values
        System.out.println("Message: " + message);
        System.out.println("Number: " + number);
        System.out.println("Decimal: " + decimal);
        System.out.println("Eligible: " + isEligible);
        System.out.println("List: " + list);
        System.out.println("Map: " + map);
        
        // Demonstrating that types are inferred at compile-time
        // The following would cause compile error:
        // message = 100;  // Cannot assign int to String variable
    }
}
```

### Example 3: Final Variables as Constants

```java
public class ConstantsDemo {
    // Final variables (constants) - should be UPPERCASE
    public static final double PI = 3.14159265359;
    public static final int MAX_ATTEMPTS = 3;
    public static final String DEFAULT_ROLE = "STUDENT";
    
    public static void main(String[] args) {
        double radius = 7.5;
        double area = PI * radius * radius;
        
        System.out.println("Circle Area: " + area);
        System.out.println("Max Attempts: " + MAX_ATTEMPTS);
        System.out.println("Default Role: " + DEFAULT_ROLE);
        
        // The following would cause compile error:
        // PI = 3.14;  // Cannot assign to final variable
    }
}
```

## Exam Tips

1. **Remember the four types of variables**: Instance variables, static variables, local variables, and parameters. Know where each is declared and its scope.

2. **Local variables must be initialized**: Unlike instance and static variables which get default values, local variables must be explicitly initialized before use. This is a common source of compile-time errors.

3. **Default values matter**: Instance and static variables receive default values (0 for numeric types, false for boolean, null for reference types), but local variables do not.

4. **Static vs instance**: Static variables are shared across all objects and belong to the class, while instance variables belong to individual objects. This distinction is frequently tested in exams.

5. **Variable scope**: The scope of a variable is the region of code where it can be accessed. Local variables have block scope, instance variables have class scope, and parameters have method scope.

6. **`var` limitations**: Remember that `var` can only be used for local variables with initializers, not for method parameters, return types, or instance variables.

7. **Naming conventions**: Follow camelCase for regular variables and UPPERCASE with underscores for constants (final variables). This shows professional coding practice and may be tested in coding style questions.

8. **Memory allocation**: Static variables are allocated in static memory area, instance variables in heap memory with objects, and local variables in stack memory.

9. **Shadowing**: When a local variable has the same name as an instance variable, it shadows the instance variable. This concept may appear in tricky exam questions.

10. **Reference vs primitive**: Remember that variables of class types store references to objects, not the objects themselves. Changes to such variables affect the object they reference.