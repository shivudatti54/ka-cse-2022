# Object-Oriented Programming

## Table of Contents

- [Object-Oriented Programming](#object-oriented-programming)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Classes and Objects](#classes-and-objects)
  - [Encapsulation](#encapsulation)
  - [Inheritance](#inheritance)
  - [Polymorphism](#polymorphism)
  - [Abstraction](#abstraction)
  - [Constructors](#constructors)
- [Examples](#examples)
  - [Example 1: Implementing Encapsulation with a Student Class](#example-1-implementing-encapsulation-with-a-student-class)
  - [Example 2: Demonstrating Inheritance and Method Overriding](#example-2-demonstrating-inheritance-and-method-overriding)
  - [Example 3: Demonstrating Polymorphism](#example-3-demonstrating-polymorphism)
- [Exam Tips](#exam-tips)

## Introduction

Object-Oriented Programming (OOP) is a fundamental programming paradigm that revolutionized software development by providing a more intuitive and modular approach to organizing code. Unlike procedural programming, which focuses on procedures and functions operating on data, OOP centers around objects that combine both data (attributes) and behavior (methods) into a single unit. This approach closely models real-world entities, making it easier to conceptualize, design, and maintain complex software systems.

Java, developed by Sun Microsystems in 1995, is one of the most prominent pure object-oriented programming languages. Every piece of code in Java is written within a class, and every variable represents an object reference. This strict adherence to OOP principles makes Java an ideal language for learning object-oriented concepts. The four pillars of OOP—Encapsulation, Inheritance, Polymorphism, and Abstraction—form the foundation upon which robust, scalable, and maintainable applications are built.

Understanding OOP is essential for any computer science engineer, as it forms the basis for modern software development frameworks, enterprise applications, and mobile app development. This topic covers the fundamental concepts of OOP using Java as the implementation language, aligning with the the syllabus for BCS306A-Object-Oriented-Programming-with-Java.

## Key Concepts

### Classes and Objects

A **class** is a blueprint or template that defines the structure and behavior of objects. It serves as a logical construct that encapsulates data (fields) and operations (methods). In Java, classes are declared using the `class` keyword followed by the class name.

**Syntax for defining a class:**

```java
class ClassName {
 // Fields (data members)
 data_type variable1;
 data_type variable2;

 // Constructors
 ClassName() {
 // initialization code
 }

 // Methods (behavior)
 return_type methodName(parameters) {
 // method body
 }
}
```

An **object** is an instance of a class. It occupies memory in the heap and represents a real-world entity. Objects are created using the `new` keyword, which allocates memory and invokes the constructor.

**Creating objects:**

```java
ClassName objectName = new ClassName();
```

The relationship between classes and objects can be understood as the distinction between a blueprint (class) and the actual product built from that blueprint (object). For example, `Car` is a class, while a specific car like "Toyota Innova" is an object of that class.

### Encapsulation

**Encapsulation** is the mechanism of bundling data (variables) and methods (functions) together into a single unit (class) while restricting direct access to some of the object's components. This is achieved through **access modifiers** in Java:

- **private**: Accessible only within the same class
- **default (package-private)**: Accessible within the same package
- **protected**: Accessible within the same package and subclasses
- **public**: Accessible from anywhere

The primary purpose of encapsulation is to protect data from unauthorized access and modification. Private fields are accessed and modified through public getter and setter methods, providing controlled access.

**Example demonstrating encapsulation:**

```java
class BankAccount {
 private double balance; // Private data member

 // Public getter method
 public double getBalance() {
 return balance;
 }

 // Public setter method with validation
 public void deposit(double amount) {
 if(amount > 0) {
 balance += amount;
 }
 }

 public void withdraw(double amount) {
 if(amount > 0 && amount <= balance) {
 balance -= amount;
 }
 }
}
```

In this example, the `balance` field is hidden from outside access, preventing direct manipulation. All modifications go through methods that can include validation logic.

### Inheritance

**Inheritance** is the OOP mechanism that allows a class to inherit properties and behaviors from another class. The class that inherits is called a **subclass** (or derived class), and the class being inherited from is called a **superclass** (or parent class). Inheritance promotes code reusability and establishes a natural hierarchy.

In Java, inheritance is implemented using the `extends` keyword:

```java
class ParentClass {
 // Parent class members
}

class ChildClass extends ParentClass {
 // Child class members
}
```

**Key points about inheritance:**

- A class can extend only one class (single inheritance in Java)
- A subclass inherits all public and protected members of the superclass
- Private members are not directly accessible in subclasses
- Constructors are not inherited but can be called using `super()`

**Example of inheritance:**

```java
// Superclass
class Animal {
 String name;

 public void eat() {
 System.out.println(name + " is eating");
 }
}

// Subclass
class Dog extends Animal {
 public void bark() {
 System.out.println(name + " is barking");
 }
}

// Main class
public class Main {
 public static void main(String[] args) {
 Dog dog = new Dog();
 dog.name = "Buddy";
 dog.eat(); // Inherited method
 dog.bark(); // Subclass method
 }
}
```

### Polymorphism

**Polymorphism** allows objects to take many forms. The term derives from Greek words "poly" (many) and "morph" (forms). In Java, polymorphism is primarily of two types:

1. **Compile-time Polymorphism (Method Overloading)**: Multiple methods with the same name but different parameters within the same class.

2. **Runtime Polymorphism (Method Overriding)**: A subclass provides a specific implementation of a method already defined in its superclass.

**Method Overloading Example:**

```java
class Calculator {
 // Overloaded methods with different parameters
 public int add(int a, int b) {
 return a + b;
 }

 public double add(double a, double b) {
 return a + b;
 }

 public int add(int a, int b, int c) {
 return a + b + c;
 }
}
```

**Method Overriding Example:**

```java
class Vehicle {
 public void run() {
 System.out.println("Vehicle is running");
 }
}

class Car extends Vehicle {
 @Override
 public void run() {
 System.out.println("Car is running");
 }
}

public class Main {
 public static void main(String[] args) {
 Vehicle v = new Car(); // Runtime polymorphism
 v.run(); // Outputs: Car is running
 }
}
```

### Abstraction

**Abstraction** is the process of hiding complex implementation details and showing only the essential features of an object. It helps in reducing programming complexity and effort. In Java, abstraction is achieved through **abstract classes** and **interfaces**.

An **abstract class** is a class that cannot be instantiated and may contain abstract methods (methods without implementation). Concrete subclasses must provide implementations for all abstract methods.

```java
abstract class Shape {
 abstract double area(); // Abstract method

 public void display() {
 System.out.println("Displaying shape");
 }
}

class Circle extends Shape {
 double radius;

 Circle(double r) {
 radius = r;
 }

 @Override
 double area() {
 return Math.PI * radius * radius;
 }
}
```

An **interface** is a blueprint of a class that contains only abstract methods (until Java 7). From Java 8, interfaces can have default and static methods. A class implements an interface using the `implements` keyword.

```java
interface Drawable {
 void draw(); // Abstract method

 default void display() {
 System.out.println("Displaying drawable");
 }
}

class Rectangle implements Drawable {
 @Override
 public void draw() {
 System.out.println("Drawing rectangle");
 }
}
```

### Constructors

A **constructor** is a special method called when an object is created. It initializes the object. Key characteristics:

- Constructor name must match the class name
- No return type (not even void)
- Called automatically when object is created using `new`

**Types of constructors:**

1. **Default Constructor**: Provided by Java if no constructor is defined
2. **Parameterized Constructor**: Accepts parameters for initialization
3. **Copy Constructor**: Creates object by copying another object's values

```java
class Student {
 String name;
 int age;

 // Parameterized constructor
 Student(String n, int a) {
 name = n;
 age = a;
 }

 // Copy constructor
 Student(Student s) {
 name = s.name;
 age = s.age;
 }
}
```

## Examples

### Example 1: Implementing Encapsulation with a Student Class

**Problem**: Create a Student class with proper encapsulation for roll number and marks.

**Solution:**

```java
class Student {
 // Private data members (encapsulation)
 private int rollNo;
 private String name;
 private double marks;

 // Getter for roll number
 public int getRollNo() {
 return rollNo;
 }

 // Setter for roll number with validation
 public void setRollNo(int rollNo) {
 if(rollNo > 0) {
 this.rollNo = rollNo;
 } else {
 System.out.println("Invalid roll number");
 }
 }

 // Getter for name
 public String getName() {
 return name;
 }

 // Setter for name
 public void setName(String name) {
 this.name = name;
 }

 // Getter for marks
 public double getMarks() {
 return marks;
 }

 // Setter for marks with validation
 public void setMarks(double marks) {
 if(marks >= 0 && marks <= 100) {
 this.marks = marks;
 } else {
 System.out.println("Marks should be between 0 and 100");
 }
 }

 // Method to display student details
 public void display() {
 System.out.println("Roll No: " + rollNo);
 System.out.println("Name: " + name);
 System.out.println("Marks: " + marks);
 }
}

public class Main {
 public static void main(String[] args) {
 Student s1 = new Student();
 s1.setRollNo(101);
 s1.setName("John");
 s1.setMarks(85.5);
 s1.display();

 // Trying invalid marks
 s1.setMarks(150); // Will show error message
 }
}
```

### Example 2: Demonstrating Inheritance and Method Overriding

**Problem**: Create a hierarchy of Employee and Manager classes demonstrating inheritance.

**Solution:**

```java
// Base class
class Employee {
 protected String name;
 protected double salary;

 public Employee(String name, double salary) {
 this.name = name;
 this.salary = salary;
 }

 public void display() {
 System.out.println("Name: " + name);
 System.out.println("Salary: " + salary);
 }

 public double calculateBonus() {
 return salary * 0.10; // 10% bonus
 }
}

// Derived class
class Manager extends Employee {
 private double incentive;

 public Manager(String name, double salary, double incentive) {
 super(name, salary); // Call parent constructor
 this.incentive = incentive;
 }

 // Method overriding
 @Override
 public double calculateBonus() {
 return (salary * 0.10) + incentive;
 }

 @Override
 public void display() {
 super.display(); // Call parent display
 System.out.println("Incentive: " + incentive);
 }
}

public class Main {
 public static void main(String[] args) {
 Employee emp = new Employee("Alice", 50000);
 Manager mgr = new Manager("Bob", 80000, 10000);

 System.out.println("Employee Bonus: " + emp.calculateBonus());
 System.out.println("Manager Bonus: " + mgr.calculateBonus());

 emp.display();
 System.out.println("---");
 mgr.display();
 }
}
```

### Example 3: Demonstrating Polymorphism

**Problem**: Create a program showing runtime polymorphism with shapes.

**Solution:**

```java
abstract class Shape {
 abstract double area();
 abstract double perimeter();
}

class Rectangle extends Shape {
 double length, width;

 Rectangle(double l, double w) {
 length = l;
 width = w;
 }

 @Override
 double area() {
 return length * width;
 }

 @Override
 double perimeter() {
 return 2 * (length + width);
 }
}

class Circle extends Shape {
 double radius;

 Circle(double r) {
 radius = r;
 }

 @Override
 double area() {
 return Math.PI * radius * radius;
 }

 @Override
 double perimeter() {
 return 2 * Math.PI * radius;
 }
}

public class Main {
 public static void main(String[] args) {
 // Runtime polymorphism - parent reference holding child object
 Shape s1 = new Rectangle(10, 5);
 Shape s2 = new Circle(7);

 System.out.println("Rectangle Area: " + s1.area());
 System.out.println("Rectangle Perimeter: " + s1.perimeter());
 System.out.println("Circle Area: " + s2.area());
 System.out.println("Circle Perimeter: " + s2.perimeter());
 }
}
```

## Exam Tips

1. **Remember the four pillars**: For university exams, always remember and explain all four OOP pillars—Encapsulation, Inheritance, Polymorphism, and Abstraction—as they form the foundation.

2. **Access modifiers priority**: The order of accessibility from most restrictive to least restrictive is: private → default → protected → public.

3. **Constructors vs Methods**: Remember constructors have the same name as the class and no return type, while methods have a return type (even if void).

4. **Key Java OOP keywords**: Know the purpose of `extends` (for inheritance), `implements` (for interfaces), `super` (to access parent class members), and `this` (to refer to current object).

5. **Method overloading vs overriding**: Method overloading (compile-time) involves same method name with different parameters in the same class, while method overriding (runtime) involves same method signature in a subclass.

6. **Abstract classes vs interfaces**: Abstract classes can have constructors and both abstract and non-abstract methods, while interfaces (pre-Java 8) could only have abstract methods. Know this distinction clearly.

7. **Real-world examples**: Be prepared to give real-world examples for each OOP concept—for example, TV remote as abstraction, bank account as encapsulation, and vehicle inheritance hierarchy.
