# Access Control in Java

## Introduction

Access control is a fundamental concept in object-oriented programming that determines the visibility and accessibility of classes, variables, methods, and constructors within a Java program. In Java, access modifiers are keywords that restrict access to the members of a class, enabling encapsulation—one of the four pillars of object-oriented programming. Encapsulation protects the internal state of an object from unauthorized modification and promotes data hiding, which is essential for building robust and maintainable software systems.

The concept of access control becomes particularly significant when working with classes in Java. When you declare a class, you control what parts of your code can access its members. This control ensures that the internal implementation details remain hidden from external code, allowing developers to change the internal workings of a class without affecting the code that uses it. For DU students preparing for semester examinations, understanding access modifiers is crucial because questions on this topic frequently appear in both theoretical and practical examinations.

In real-world software development, access control plays a vital role in large-scale applications. Consider a banking application where account balances should not be directly modified by external code. By making the balance variable private and providing controlled access through methods like deposit() and withdraw(), the application can enforce business rules and prevent invalid transactions. This chapter explores the four access modifiers in Java—public, private, protected, and default—and their appropriate usage in class design.

## Key Concepts

### Understanding Access Modifiers

Java provides four access modifiers that define the scope of accessibility for classes, variables, methods, and constructors. Each modifier determines which parts of the program can access a particular member. The choice of access modifier affects encapsulation, inheritance, and the overall structure of object-oriented code.

The four access modifiers in Java are:

1. **Public** - The member is accessible from any other class
2. **Private** - The member is accessible only within the same class
3. **Protected** - The member is accessible within the same package and from subclasses
4. **Default (Package-Private)** - The member is accessible only within the same package

### The Public Access Modifier

When a member is declared as public, it is accessible from any other class in the same package or different packages. Public members form the interface through which external code interacts with a class. The public modifier has the widest scope of all access modifiers.

A public class can be accessed by any other class, provided the class itself is not restricted by other factors. Public methods serve as the entry points to the functionality of a class. Consider the following example:

```java
public class Student {
    public String name;
    public int rollNumber;
    
    public void displayDetails() {
        System.out.println("Name: " + name);
        System.out.println("Roll Number: " + rollNumber);
    }
}

public class Main {
    public static void main(String[] args) {
        Student s = new Student();
        s.name = "Aisha Khan";
        s.rollNumber = 101;
        s.displayDetails();
    }
}
```

In this example, the name and rollNumber variables, along with the displayDetails() method, are all public. This means any class can access and modify these members directly, which may not always be desirable from an encapsulation standpoint.

### The Private Access Modifier

The private modifier restricts access to members within the same class only. Private members cannot be accessed from any other class, even in the same package. This is the most restrictive access modifier and is essential for achieving data hiding.

Private variables are typically accessed through public getter and setter methods, which provide controlled access to the internal state of an object. This pattern allows validation and ensures that objects maintain their integrity. The following demonstrates proper use of private access:

```java
public class BankAccount {
    private double balance;
    private String accountNumber;
    
    public BankAccount(String accountNumber, double initialBalance) {
        this.accountNumber = accountNumber;
        if (initialBalance >= 0) {
            this.balance = initialBalance;
        } else {
            this.balance = 0;
        }
    }
    
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposited: " + amount);
        } else {
            System.out.println("Invalid deposit amount");
        }
    }
    
    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println("Withdrawn: " + amount);
        } else {
            System.out.println("Insufficient funds or invalid amount");
        }
    }
    
    public double getBalance() {
        return balance;
    }
}
```

In this BankAccount class, the balance and accountNumber variables are private. External code cannot directly modify the balance, ensuring that business rules (like preventing negative balances) are always enforced through the deposit and withdraw methods.

### The Protected Access Modifier

The protected modifier allows access from within the same package and from subclasses in other packages. This is particularly useful when you want to provide controlled access to class members for inheritance purposes while still keeping them hidden from unrelated classes.

Protected members are often used for methods that subclasses might need to override or use. Consider a scenario where you have a base class representing different types of employees:

```java
package employee;
public class Employee {
    protected String name;
    protected double salary;
    
    protected void calculateBonus() {
        salary = salary + (salary * 0.10);
    }
}

package hr;
import employee.Employee;
public class Manager extends Employee {
    public void displayDetails() {
        name = "Rahul Verma";
        salary = 75000;
        calculateBonus();
        System.out.println("Manager: " + name + ", Salary: " + salary);
    }
}
```

In this example, the Manager class can access the protected members name, salary, and calculateBonus() from the Employee class because Manager is a subclass of Employee. However, a class that does not extend Employee cannot access these protected members.

### The Default Access Modifier (Package-Private)

When no access modifier is specified, Java uses default access, also known as package-private. Members with default access are accessible only within the same package. This modifier is commonly used for helper classes and methods that are intended for internal use within a package.

Default access is useful when you want to group related classes together and provide them with shared access to certain members while keeping them hidden from classes outside the package. The following illustrates default access:

```java
package college;
class InternalHelper {
    void displayMessage() {
        System.out.println("This is internal to the college package");
    }
}

public class Department {
    void useHelper() {
        InternalHelper helper = new InternalHelper();
        helper.displayMessage();
    }
}
```

Here, InternalHelper has default (package-private) access. It can be used by other classes within the college package but would not be accessible from outside the package.

### Access Control and Inheritance

When a subclass inherits from a parent class, the access modifiers of the inherited members affect their visibility in the subclass. A subclass cannot weaken the access control of inherited methods—it can only maintain or widen the access scope. For example, a protected method in the parent class can be made public in the subclass, but cannot be made private.

Understanding this rule is essential for proper class design and for passing examinations. The hierarchy of access levels from most restrictive to least restrictive is: private, default (package-private), protected, and public.

## Examples

### Example 1: Demonstrating All Access Modifiers

```java
package mystorage;

public class Storage {
    public String publicVar = "Public - accessible everywhere";
    private String privateVar = "Private - accessible only in Storage";
    protected String protectedVar = "Protected - accessible in package and subclasses";
    String defaultVar = "Default - accessible only in mystorage package";
    
    public void publicMethod() {
        System.out.println("Public method");
    }
    
    private void privateMethod() {
        System.out.println("Private method");
    }
    
    protected void protectedMethod() {
        System.out.println("Protected method");
    }
    
    void defaultMethod() {
        System.out.println("Default method");
    }
    
    public void accessAll() {
        System.out.println(privateVar);
        privateMethod();
    }
}
```

```java
package mystorage;

public class AccessDemo {
    public static void main(String[] args) {
        Storage s = new Storage();
        
        System.out.println(s.publicVar);
        System.out.println(s.protectedVar);
        System.out.println(s.defaultVar);
        
        s.publicMethod();
        s.protectedMethod();
        s.defaultMethod();
        s.accessAll();
    }
}
```

In this example, all members are accessible from within the same package. However, the private members can only be accessed through the public method accessAll().

### Example 2: Access Control with Inheritance Across Packages

```java
package vehicle;

public class Vehicle {
    protected int speed;
    public String model;
    
    protected void accelerate() {
        speed += 10;
    }
}

package car;
import vehicle.Vehicle;

public class Car extends Vehicle {
    public void displaySpeed() {
        model = "Sedan";
        accelerate();
        System.out.println("Car Model: " + model + ", Speed: " + speed);
    }
}
```

Here, the Car class extends Vehicle and can access the protected members speed and accelerate(). If a non-subclass in the car package tried to access these members, it would result in a compilation error.

### Example 3: Practical Encapsulation Example

```java
public class Rectangle {
    private double length;
    private double breadth;
    
    public Rectangle(double length, double breadth) {
        if (length > 0 && breadth > 0) {
            this.length = length;
            this.breadth = breadth;
        } else {
            this.length = 1;
            this.breadth = 1;
        }
    }
    
    public double calculateArea() {
        return length * breadth;
    }
    
    public double calculatePerimeter() {
        return 2 * (length + breadth);
    }
    
    public double getLength() {
        return length;
    }
    
    public double getBreadth() {
        return breadth;
    }
}

public class Main {
    public static void main(String[] args) {
        Rectangle r = new Rectangle(5, 3);
        System.out.println("Area: " + r.calculateArea());
        System.out.println("Perimeter: " + r.calculatePerimeter());
        
        Rectangle r2 = new Rectangle(-5, 3);
        System.out.println("Default Area: " + r2.calculateArea());
    }
}
```

This example demonstrates how private variables with public methods create a controlled interface. The constructor validates input, ensuring that invalid dimensions are replaced with defaults. External code cannot create rectangles with negative dimensions.

## Exam Tips

For DU semester examinations, keep the following points in mind when answering questions on access control:

1. **Memorize the hierarchy**: Remember that access levels from most restrictive to least restrictive are PRIVATE, DEFAULT (package-private), PROTECTED, and PUBLIC. This hierarchy is frequently tested in multiple-choice questions.

2. **Default vs. package-private**: Understand that when no access modifier is specified, Java applies default access, which is equivalent to package-private. This is often confused with protected but is actually more restrictive.

3. **Protected access**: Remember that protected members are accessible within the same package AND in subclasses even if the subclass is in a different package. This dual accessibility is a common exam topic.

4. **Private members and inheritance**: Private members are NOT directly accessible in subclasses. Subclasses inherit private members but cannot access them directly—they must use public or protected methods provided by the parent class.

5. **Access in same package**: Within the same package, public, protected, and default members are all accessible. Only private members are restricted within the same package.

6. **Subclass accessibility rule**: A subclass cannot make inherited members MORE restrictive. If a parent has a protected method, the subclass can make it public but cannot make it private or default.

7. **Constructor access**: Constructors can also have access modifiers. A private constructor prevents direct instantiation from outside the class (singleton pattern), while protected constructors allow subclass instantiation.

8. **Real-world analogy**: In exams, questions often ask you to identify which code will produce a compilation error. Always trace the relationship between the accessing class and the class whose member is being accessed.